def pytest_addoption(parser):
    parser.addoption(
        "--seal",
        action="append",
        default=[],
        help="list of seals to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    if "seal" in metafunc.fixturenames:
        metafunc.parametrize("seal", metafunc.config.getoption("seal"))