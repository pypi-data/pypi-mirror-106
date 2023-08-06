import json
from it_finance_api.exceptions import (
    NetworkError,
    UnauthorizedError,
    InvalidParametersError,
    NotFoundError,
    MaxRequestsExceededError,
    GenericError,
    NotAvailableError,
)


class ItFinanceResponse:

    def __init__(self, response):
        self.response = response

    def __call__(self, *args, **kwargs):

        content = self.response.content
        if not content:
            raise NetworkError

        data = json.loads(content)

        if self.response.ok:
            # returns status and data
            return data

        elif self.response.status_code == 400:
            raise InvalidParametersError(data)

        elif self.response.status_code == 401:
            raise UnauthorizedError(data)

        elif self.response.status_code == 404:
            raise NotFoundError(data)

        elif self.response.status_code == 422:
            raise InvalidParametersError(data)

        elif self.response.status_code == 429:
            raise MaxRequestsExceededError(data)

        elif self.response.status_code == 500:
            raise GenericError(data)

        elif self.response.status_code == 503:
            raise NotAvailableError(data)

        else:
            raise GenericError(data)
