def pytest_addoption(parser):
    parser.addoption(
        "--seal",
        action="append",
        default=[],
        help="list of seals to pass to test functions",
    )
    parser.addoption(
        "--debugLevel",
        action="append",
        default=[],
        help="DEBUG level",
    )


def pytest_generate_tests(metafunc):
    if "seal" in metafunc.fixturenames:
        metafunc.parametrize("seal", metafunc.config.getoption("seal"))
    if "debugLevel" in metafunc.fixturenames:
        metafunc.parametrize("debugLevel", metafunc.config.getoption("debugLevel"))