def debugEnable(debugLevel):
    if debugLevel == 1:
        import logging
        from http.client import HTTPConnection

        log = logging.getLogger("urllib3")
        log.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        log.addHandler(ch)
        HTTPConnection.debuglevel = 1
