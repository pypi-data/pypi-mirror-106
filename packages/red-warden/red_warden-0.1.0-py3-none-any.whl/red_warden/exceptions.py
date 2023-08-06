class RWException(Exception):
    message = "Generic Red Warden Exception"
    params = {"code": 500}

    def __init__(self, message=None, details=None):
        if details:
            self.params["details"] = details
        super().__init__(message or self.message)


class RWQueryNavigatorException(RWException):
    message = "Query Navigator error"


class RWNotFoundException(RWException):
    message = "Not Found"
    params = {"code": 404}


class RWUnauthenticatedException(RWException):
    message = "Unauthenticated"
    params = {"code": 401}


class RWUnauthorizedException(RWException):
    message = "Unauthorized"
    params = {"code": 403}


"""
class RWMissingRouteConfig(RWException):
    message = "Missing route config"

    def __init__(self, route, type=None):
        self.params["route"] = route
        if type:
            self.params["type"] = type
        super().__init__()



"""
