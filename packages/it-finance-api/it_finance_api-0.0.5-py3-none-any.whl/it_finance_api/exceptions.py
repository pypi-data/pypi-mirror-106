from it_finance_api.models.base import ResponseStatusData


class DefaultException(Exception, ResponseStatusData):

    def __init__(self, data):
        ResponseStatusData.__init__(self, data)

    def __str__(self):
        return f'code: {self.code} message: {self.message}'


class NetworkError(Exception):
    pass


class InvalidLicenseError(Exception):

    def __init__(self, capabilities):
        self.capabilities = capabilities

    def __str__(self):
        return f'You are missing some capabilities to perform this action: {self.capabilities}'


class UnauthorizedError(DefaultException):
    pass


class InvalidParametersError(DefaultException):
    pass


class NotFoundError(DefaultException):
    pass


class MaxRequestsExceededError(DefaultException):
    pass


class GenericError(DefaultException):
    pass


class NotAvailableError(DefaultException):
    pass
