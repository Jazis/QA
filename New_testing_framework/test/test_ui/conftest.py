import os
import uuid
from typing import List, Generator

import pytest

from playwright.sync_api import Page, sync_playwright, Playwright, Browser, BrowserContext


from models.user import User
from pages.pages import Pages
from steps.steps import Steps
from utils.consts import AUTH_URL, WAIT_TIME_MSEC, ATTACHMENTS_DIR, VIEWPORT

from widgets.element import Element


class SessionConfig:
    """
    Класс для хранения конфигурации тестовой сессии
    browser - параметр для управления запускаемым браузером (chromium или firefox)
    headless - запускать ли браузер в headless-режиме
    """
    def __init__(self, request) -> None:
        self.browser = request.config.getoption("--browser")
        self.device = request.config.getoption("--device")
        # self.headless = request.config.getoption("--headless")

def pytest_addoption(parser):
    """Добавление опций для запуска тестов"""
    parser.addoption("--browser", action="store", default="chromium")
    parser.addoption("--device", action="store_true", default="iPhone 13")
    # parser.addoption("--headless", action="store_false")
    # parser.addoption("--slowmo 300")

def pytest_generate_tests(metafunc):
    """
    Генерация тестов на основе тегов с конфигурациями (пользователи, настройки приложения и т.д.)
    Каждый аргумент в теге - это новая фикстура
    В данном случае, идет поиск тегов с именем "conf*"
    """
    idlist = []
    argvalues = []
    for mark in metafunc.definition.iter_markers():
        if not mark.name.startswith("conf"):
            continue
        idlist.append(mark.name)
        argnames = list(mark.kwargs.keys())
        argvalues.append(list(mark.kwargs.values()))
    if idlist:
        metafunc.parametrize(argnames, argvalues, ids=idlist, scope="class")

def pytest_make_parametrize_id(config, val):
    """Создание идентификаторов для параметризации"""
    if isinstance(val, str) or isinstance(val, int) or isinstance(val, float):
        return val.__class__.__name__

@pytest.fixture(scope="session", autouse=True)
def session_config(request) -> SessionConfig:
    """Фикстура для хранения конфигурации тестовой сессии"""
    return SessionConfig(request)


@pytest.fixture(scope="session")
def playwright() -> Playwright:  # type: ignore
    """Фикстура для запуска Playwright. Один раз на всю тестовую сессию"""
    with sync_playwright() as pw:
        yield pw

@pytest.fixture(scope="session")
def browser(playwright: Playwright, session_config: SessionConfig) -> Browser:  # type: ignore
    """
    Фикстура для запуска браузера. Один раз на всю тестовую сессию
    https://playwright.dev/python/docs/browsers
    """
    browsers = {
        "chromium": playwright.chromium,
        "firefox": playwright.firefox,
        "webkit": playwright.webkit,
    }
    browser = browsers.get(session_config.browser).launch(
        # headless=False,
        # headless=session_config.headless,
        args=["--use-fake-device-for-media-stream", "--use-fake-ui-for-media-stream"],
        firefox_user_prefs={
            "permissions.default.microphone": 1,
            "permissions.default.camera": 1,
            "browser.cache.disk.enable": False,
            "browser.cache.disk.capacity": 0,
            "browser.cache.disk.smart_size.enabled": False,
            "media.navigator.streams.fake": True,
            "media.navigator.permission.disabled": True,
            "device.storage.enabled": False,
            "media.gstreamer.enabled": False,
        },

    )
    yield browser
    browser.close()

@pytest.fixture(scope="session")
def browser_permissions(session_config: SessionConfig) -> List[str]:
    """
    Фикстура для получения разрешений браузера на основе запущенного браузера
    chromium = ["clipboard-write", "clipboard-read"]
    firefox = []
    """
    permissions = []
    if session_config.browser == "chromium":
        permissions += ["clipboard-write", "clipboard-read", "microphone"]
    return permissions


@pytest.fixture(autouse=True)
def trace_path():
    """Фикстура для получения пути к файлу трассировки"""
    trace_path = os.path.join(os.path.dirname(__file__), "traces", f"{uuid.uuid4()}.zip")
    return trace_path


@pytest.fixture(autouse=True)
def trace_url(trace_path):
    """Фикстура для получения URL трассировки"""
    filename = os.path.split(trace_path)[-1]
    playwright_url = "https://trace.playwright.dev"
    artifact_url = f'{os.environ.get("CI_API_V4_URL")}/projects/{os.environ.get("CI_PROJECT_ID")}/jobs/{os.environ.get("CI_JOB_ID")}/artifacts/traces/{filename}'
    return f"{playwright_url}/?trace={artifact_url}"


@pytest.fixture
def locale():
    """Фикстура для получения локали"""
    return


@pytest.fixture
def browser_context(request, browser: Browser, browser_permissions, trace_path, trace_url,
                    locale) -> BrowserContext:  # type: ignore
    """
    Фикстура для создания браузерного контекста. Создается каждый тест
    https://playwright.dev/python/docs/browser-contexts
    """
    context_pages: List[Page] = []
    context = browser.new_context(
        screen={"width": 1440, "height": 1024},
        viewport=VIEWPORT,
        ignore_https_errors=True,
        permissions=browser_permissions,
        locale=locale
    )

    context.on("page", lambda page: context_pages.append(page))
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context
    failed = request.node.rep_call.failed if hasattr(request.node, "rep_call") else False
    context.tracing.stop(path=trace_path)

    # if failed:
    #     allure.attach.file(trace_path, name="Trace file")
    #     allure.attach(trace_url, "Trace URL", allure.attachment_type.URI_LIST)
    # else:
    #     os.remove(trace_path)

    os.remove(trace_path)
    context.close()


@pytest.fixture(autouse=True)
def page(browser_context: BrowserContext) -> Page:
    """
    Фикстура для создания страницы (вкладки). Создается каждый тест. Запускается автоматически
    https://playwright.dev/python/docs/pages
    """
    page = browser_context.new_page()
    page.messages = []

    page.set_default_timeout(WAIT_TIME_MSEC)
    # page.goto(AUTH_URL)

    yield page
    page.close()


@pytest.fixture(autouse=True)
def set_element_page(page):
    """
    Установка свежесозданного page для Element
    Это нужно для поиска элементов и работы с ними
    """
    Element.page = page


def get_har_path(name):
    """Получение полного пути до har-файла"""
    return os.path.abspath(os.path.join(ATTACHMENTS_DIR, f"{name}.har.zip"))


@pytest.fixture(scope="session", autouse=True)
def pages():
    """Фикстура для получения экземпляра Pages"""
    return Pages()


@pytest.fixture(scope="session", autouse=True)
def steps(pages):
    """Фикстура для получения экземпляра Steps"""
    return Steps(pages)


@pytest.fixture()
def authorize(pages: Pages, user: User, page: Page):
    """
    Фикстура для авторизации.
    Зависит от user, который в свою очередь может задаваться какой-то кастомной фикстурой user
    (главное, чтобы там возвращался объект с аттрибутами login и password)
    ИЛИ
    с помощью `@pytest.mark.conf(user=User(login='123', password='123'))`, что в целом одно и то же, но более явно
    """
    pages.auth.login_input.fill(user.login)
    pages.auth.password_input.fill(user.password)
    pages.auth.enter_btn.click()


# @pytest.fixture(scope="session")
# def server() -> Server:
#     return Server()

# @pytest.fixture(scope="session")
# def database():
#     db = Database(DB_CONFIG)
#     yield db
#
#     db.conn.close()

# @pytest.fixture(scope="session", autouse=True)
# def faker_session_locale():
#     return ["ru_RU"]
