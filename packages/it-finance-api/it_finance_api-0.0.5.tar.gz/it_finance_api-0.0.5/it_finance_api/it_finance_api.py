import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta
from it_finance_api.response import ItFinanceResponse
from it_finance_api.exceptions import InvalidLicenseError
from it_finance_api.endpoints import *
from it_finance_api.models.account import (
    AccountData,
    CapabilitiesType,
)
from it_finance_api.models.credit_score import (
    CreditScoreDetailData,
    CreditScoreOverviewData,
)


class ItFinanceApi:

    def __init__(
            self,
            base_uri='https://api.itfinance.it/IT4FRest/rest/',
            raise_exception=True,
            fiscal_code_user=None,
    ):
        """
        :param base_uri: the url of the api
        :param raise_exception: raise exception or ignore exception and return empty obj
        """
        self.fiscal_code_user = fiscal_code_user
        self.base_uri = base_uri
        self.raise_exception = raise_exception
        self.__auth = ''

        self._account_partner_data = None

    def login(self, username, password):
        self.__auth = HTTPBasicAuth(username, password)

        self._account_partner_data = self.get_account_partner()

    def _get(self, uri, wrapper_obj):
        """
        Base get request with data wrapper
        :param uri: the full url of the endpoint
        :param wrapper_obj: the wrapper obj that will load the data
        :return:
        """
        res = requests.get(
            self.base_uri+uri,
            auth=self.__auth
        )

        data = ItFinanceResponse(res)()
        return wrapper_obj(data, data.get('result', {}))

    def _evaluate_license(self, capabilities):
        """
        Check if the endpoint can be called based on the user licenses
        :param capabilities: list of capabilities
        :return: none
        :raise: InvalidLicenseError: if the endpoint cant be called
        """
        self._account_partner_data: AccountData
        if datetime.now() - self._account_partner_data.last_call_update > timedelta(hours=5):
            # update the partner data
            self._account_partner_data = self.get_account_partner()

        if not self._account_partner_data.has_capabilities(capabilities):
            diff = list(set(capabilities) - set(self._account_partner_data.capabilities_list))
            raise InvalidLicenseError(diff)

    def _get_fiscal_code_user(self, fiscal_code_user):
        if not fiscal_code_user and not self.fiscal_code_user:
            raise Exception('Required fiscal_code_user. Define it globally or as kwarg')

        return fiscal_code_user if fiscal_code_user else self.fiscal_code_user

    def force_update_account_partner(self) -> None:
        self._account_partner_data = self.get_account_partner()

    def get_account_partner(self) -> AccountData:
        """
        :return: user's partner
        """
        return self._get(
            ACCOUNT_PARTNER,
            AccountData
        )

    def get_score_companies_detail(
            self,
            fiscal_id,
            fiscal_code_user=None,
            search_type='fiscalCode'
    ) -> CreditScoreDetailData:
        """
        :param fiscal_id: The Fiscal ID of the company, can be a VAT CODE or a FISCAL CODE depending on the search type
        :param fiscal_code_user: The fiscal code of the user sending the request (company)
        :param search_type: The kind of search between:
                - fiscalCode
                - vatNumber
        :return:
        """
        self._evaluate_license([
            CapabilitiesType.CREDIT_SCORE,
        ])

        fiscal_code_user = self._get_fiscal_code_user(fiscal_code_user)

        uri_params = f'?fiscalCodeUser={fiscal_code_user}&fiscalId={fiscal_id}&searchType={search_type}'
        return self._get(
            SCORE_COMPANIES_DETAIL + uri_params,
            CreditScoreDetailData
        )

    def get_score_companies_overview(
            self,
            fiscal_id,
            fiscal_code_user=None,
            search_type='fiscalCode'
    ) -> CreditScoreOverviewData:
        """
        :param fiscal_id: The Fiscal ID of the company, can be a VAT CODE or a FISCAL CODE depending on the search type
        :param fiscal_code_user: The fiscal code of the user sending the request (company)
        :param search_type: The kind of search between:
                - fiscalCode
                - vatNumber
        :return:
        """
        self._evaluate_license([
            CapabilitiesType.CREDIT_SCORE,
        ])

        fiscal_code_user = self._get_fiscal_code_user(fiscal_code_user)

        uri_params = f'?fiscalCodeUser={fiscal_code_user}&fiscalId={fiscal_id}&searchType={search_type}'
        return self._get(
            SCORE_COMPANIES_OVERVIEW + uri_params,
            CreditScoreOverviewData
        )
