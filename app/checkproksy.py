import requests

URL = "http://google.com"
TIMEOUT = (3.05,27)

def check_proxy(proxy):
    '''
        Function for check proxy return ERROR
        if proxy is Bad else
        Function return None
    '''
    try:
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        session.max_redirects = 300
        proxy = proxy.split('\n',1)[0]
        print(Fore.LIGHTYELLOW_EX + 'Checking ' + proxy)
        session.get(URL, proxies={'http':'http://' + proxy}, timeout=TIMEOUT,allow_redirects=True)
    except requests.exceptions.ConnectionError as e:
        print(Fore.LIGHTRED_EX + 'Error!')
        return e
    except requests.exceptions.ConnectTimeout as e:
        print(Fore.LIGHTRED_EX + 'Error,Timeout!')
        return e
    except requests.exceptions.HTTPError as e:
        print(Fore.LIGHTRED_EX + 'HTTP ERROR!')
        return e
    except requests.exceptions.Timeout as e:
        print(Fore.LIGHTRED_EX + 'Error! Connection Timeout!')
        return e
    except urllib3.exceptions.ProxySchemeUnknown as e:
        print(Fore.LIGHTRED_EX + 'ERROR unkown Proxy Scheme!')
        return e
    except requests.exceptions.TooManyRedirects as e:
        print(Fore.LIGHTRED_EX + 'ERROR! Too many redirects!')
        return e