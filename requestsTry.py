import requests as reqs
from requests.exceptions import HTTPError


def urlcheck(url):
    try:
        response = reqs.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
    return 0


# Get page info

# get POST information from EXCEL

# get new info from POST

# save info from last

if __name__ == '__main__':
    list_url = ['https://www.sefaz.salvador.ba.gov.br/IPTU/certidaoDadosCadastrais'
        , 'https://dti.sefaz.salvador.ba.gov.br/Modulos/DTI/ItivDeclaracaoFrm.aspx']

    for url in list_url:
        urlcheck(url)

    response = reqs.get(r'https://dti.sefaz.salvador.ba.gov.br/Modulos/DTI/ItivDeclaracaoFrm.aspx')
    print(response.status_code)
    print(response.text)
