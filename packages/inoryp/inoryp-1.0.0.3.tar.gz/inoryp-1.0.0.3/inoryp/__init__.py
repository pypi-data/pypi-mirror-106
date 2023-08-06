from requests import get

class Inoryp():
    @property
    def myIP(self): # BRASIL
        API = get("http://informa-ip.cf/py.php").text
        return API
    
    @property
    def myCode(self): # BRASIL
        API = get("http://informa-ip.cf/py.php").status_code
        return API
    
    @property
    def myDic(self): # BRASIL
        API = get("http://informa-ip.cf/py.php")
        API_Dicionario = {
            "myIP": "{}".format(API.text),
            "myCode": "{}".format(API.status_code)
        }
        return API_Dicionario

def inoryp(value):
    if value == 0: # BRASIL
        API = get("http://informa-ip.cf/py.php").text
        return API

    elif value == 1: # BRASIL
        API = get("http://informa-ip.cf/py.php").status_code
        return API
    
    elif value == 2: # BRASIL
        API = get("http://informa-ip.cf/py.php")
        API_Dicionario = {
            "myIP": "{}".format(API.text),
            "myCode": "{}".format(API.status_code)
        }
        return API_Dicionario
        
    else: # BRASIL
        pass