import requests

import socketio
from socketio.exceptions import BadNamespaceError, ConnectionError

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

sio = socketio.Client()


class InsertMendoza:
    '''
        Cliente para sistema SARyS
        Versión 6.x
    '''

    def __init__(self, domain='insertmendoza.com.ar', https=True, port=8000):
        self.auth = {
            'username': None,
            'password': None,
            'domain': domain,
            'https': https,
            'token': None,
            'port': None if https is True else port
        }

        self.headers = {}

    def ViewConfig(self):
        return self.auth

    def Login(self, username, password):
        self.auth.update(username=username, password=password)

        data, code = self.Request(
            method=POST, url='token',
            data={'username': username, 'password': password},
        )

        if code == 200:
            self.auth.update(token=data['token'])

            self.headers['Authorization'] = f'Token {data["token"]}'

            if self.auth['https']:
                sio.disconnect()
                try:
                    sio.connect(
                        f"https://api.{self.auth['domain']}", headers=self.headers, auth={'token': data["token"]})
                except ConnectionError:
                    print("Error a conectar socket")

            return True

        return False

    def Request(self, url, data, method):
        if self.auth['https'] is True:
            _url = f'https://api.{self.auth["domain"]}'
        else:
            _url = f'http://{self.auth["domain"]}'

        if self.auth['port']:
            _url = _url + f':{self.auth["port"]}'

        url = _url + '/' + url + '/'

        try:
            if method == GET:
                r = requests.get(url, headers=self.headers)

            elif method == POST:
                r = requests.post(url, json=data, headers=self.headers)

            elif method == PUT:
                r = requests.put(url, json=data, headers=self.headers)

            elif method == DELETE:
                r = requests.delete(url, json=data, headers=self.headers)

            print(f'{r.status_code} Method: {method} in {r.elapsed.total_seconds()}')

            return [r.json(), r.status_code]

        except ConnectionError:
            return {'detail': 'Connection timed out'}, 1

        except Exception:
            return {'detail': 'Error in SDK method Platform'}, 1

    def close(self):
        sio.disconnect()
        self.auth = {
            'username': None,
            'password': None,
            'domain': None,
            'https': None,
            'token': None,
            'port': None,
        }

        self.headers = {}

    def AccountView(self):
        return self.Request(url='accounts/accounts', method=GET, data={})
    
    def ManagerView(self):
        return self.Request(url='managers', method=GET, data={})

    def ManagerAdd(self, phone, first_name, last_name):
        return self.Request(url='managers', method=POST, data={
            'phone': phone, 'first_name': first_name, 'last_name': last_name,
        })

    def ManagerUpdate(self, uuid, data):
        return self.Request(url=f'managers/{uuid}', method=PUT, data=data)

    def ManagerDelete(self, uuid, data):
        return self.Request(url=f'managers/{uuid}', method=DELETE, data=data)

    
    def BiometricView(self):
        return self.Request(url='biometrics/biometrics', method=GET, data={})

    def BiometricAdd(self, data):
        return self.Request(url='biometrics/biometrics', method=POST, data=data)

    def BiometricUpdate(self, uuid, data):
        return self.Request(url=f'biometrics/biometrics/{uuid}', method=PUT, data=data)

    def BiometricDelete(self, uuid, data):
        return self.Request(url=f'biometrics/biometrics/{uuid}', method=DELETE, data=data)


    def MemoryView(self):
        return self.Request(url='biometrics/memories', method=GET, data={})

    def MemoryAdd(self, data):
        return self.Request(url='biometrics/memories', method=POST, data=data)

    def MemoryUpdate(self, uuid, data):
        return self.Request(url=f'biometrics/memories/{uuid}', method=PUT, data=data)

    def MemoryDelete(self, uuid, data):
        return self.Request(url=f'biometrics/memories/{uuid}', method=DELETE, data=data)

    
    def CustomersView(self):
        return self.Request(url='customers', method=GET, data={})

    def CustomersAdd(self, phone, first_name, last_name):
        return self.Request(url='customers', method=POST, data={
            'phone': phone, 'first_name': first_name, 'last_name': last_name,
        })

    def CustomersUpdate(self, uuid, data):
        return self.Request(url=f'customers/{uuid}', method=PUT, data=data)

    def CustomersDelete(self, uuid, data):
        return self.Request(url=f'customers/{uuid}', method=DELETE, data=data)

    
    def EmployeeAdd(self, phone, first_name, last_name):
        return self.Request(url='employee', method=POST, data={
            'phone': phone, 'first_name': first_name, 'last_name': last_name,
        })

    def EmployeeView(self):
        return self.Request(url='employee', method=GET, data={}) 

    def EmployeeUpdate(self, uuid, data):
        return self.Request(url=f'employee/{uuid}', method=PUT, data=data)

    def EmployeeDelete(self, uuid, data):
        return self.Request(url=f'custoemployeemers/{uuid}', method=DELETE, data=data)