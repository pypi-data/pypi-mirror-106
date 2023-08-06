# It Finances Api
A wrapper for It Finances Api

## Official api documentation
https://api-test.itfinance.it/IT4FRest/rest/swagger-ui.html

## how to use it
``` python
    import json
    from it_finance_api import ItFinanceApi
    from it_finance_api.models import CreditScoreDetailData
    
    with open('credentials.json', 'rb') as f:
        c = json.load(f)
        USERNAME = c.get('username')
        PASSWORD = c.get('password')
    
    api = ItFinanceApi()
    api.login(USERNAME, PASSWORD)
    
    res: CreditScoreDetailData  = api.get_score_companies_detail('02162745')
```

## Disclaimer
This wrapper is made only for those who have access to the api.
You have to directly contact It Finance to gain access to the endpoints.

The calls to this api are not free, the cost is defined with a contract with itFinance

## Collab
This wrappper is maintained by Telnet Servizi srl
By the software division Telnet Data https://www.telnetdata.it/


## Contact 
http://www.itfinance.it

## Release notes
Look in the Github releases section for the update info