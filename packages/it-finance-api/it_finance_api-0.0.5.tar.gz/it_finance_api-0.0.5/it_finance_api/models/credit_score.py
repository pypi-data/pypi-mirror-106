from typing import List
from it_finance_api.models.base import (
    AddressData,
    BaseData,
    WrapperDataInterface,
    KeyValueData,
)


class CreditScoreDetailData(BaseData, WrapperDataInterface):

    class AtecoList(KeyValueData):
        pass

    class SicList(KeyValueData):
        pass

    def __init__(self, data: dict, result: dict):
        super(CreditScoreDetailData, self).__init__(data)

        self.address: AddressData = AddressData(result.get('address', {}))
        self.ateco_list: List[CreditScoreDetailData.AtecoList] = [
            self.AtecoList(el) for el in result.get('atecoList', [])
        ]
        self.capital: int = result.get('capital', 0)
        self.cciaa: str = result.get('cciaa', '')
        self.constitution_date = self.datetime_converter(result.get('constitutionDate'))
        self.employees: int = result.get('employees', 0)
        self.fax: str = result.get('fax', '')
        self.fiscal_code: str = result.get('fiscalCode', '')
        self.iban: str = result.get('iban', '')
        self.id: int = result.get('id', 0)
        self.last_account_closure_date = self.datetime_converter(result.get('lastAccountClosureDate'))
        self.legal_nature: str = result.get('legaNature', '')
        self.legal_nature_code: str = result.get('legalNatureCode', '')
        self.name: str = result.get('name', '')
        self.pec: str = result.get('pec', '')
        self.politically_exposed: bool = result.get('politically_exposed', False)
        self.politically_exposed_details: str = result.get('politicallyExposedDetails', '')
        self.rea_number: str = result.get('reaNumber', '')
        self.revenue: int = result.get('revenue', 0)
        self.sic_list: List[CreditScoreDetailData.SicList] = [
            self.SicList(el) for el in result.get('sicList', [])
        ]
        self.status: str = result.get('status', '')
        self.technical_id: str = result.get('technicalId', '')
        self.tel_home: str = result.get('telHome', '')
        self.tel_mobile: str = result.get('telMobile', '')
        self.tel_office: str = result.get('telOffice', '')
        self.vat_code: str = result.get('vatCode', '')

    def __repr__(self):
        return f'{self.id}-{self.vat_code}'


class CreditScoreOverviewData(BaseData, WrapperDataInterface):

    def __init__(self, data: dict, result: dict):
        super(CreditScoreOverviewData, self).__init__(data)

        self.address: AddressData = AddressData(result.get('address', {}))
        self.ateco_sector_code: str = result.get('atecoSectorCode', '')
        self.ateco_sector_code_description: str = result.get('atecoSectorCodeDescription', '')
        self.cciaa: str = result.get('cciaa', '')
        self.fiscal_code: str = result.get('fiscalCode', '')
        self.legal_form_type_code: str = result.get('legalFormTypeCode', '')
        self.legal_form_type_description: str = result.get('legalFormTypeDescription', '')
        self.name: str = result.get('name', '')
        self.rea_number: str = result.get('reaNumber', '')
        self.vat_code: str = result.get('vatCode', '')

    def __repr__(self):
        return f'{self.name}-{self.vat_code}'
