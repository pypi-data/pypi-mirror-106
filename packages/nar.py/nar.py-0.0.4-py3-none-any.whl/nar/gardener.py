from typing import Any
from requests import post
from _thread import start_new_thread
from time import sleep

class Gardener():
  def __init__(self, token: str = None, **kwds) -> None:
    if token: self.token = token if token.split()[0] == 'Bearer' else 'Bearer ' + token.strip()
    else: self.token_update_init(kwds.get('username'), kwds.get('password'))
    self.base_url = 'https://www.nationsatrisk.com/api/'
  
  def update_token(self, token: dict):
    token_ = token['token'] if type(token) == dict else token
    self.token = 'Bearer ' + token_

  def token_update_init(self, username: str, password: str):
    def cycle(username: str, password: str):
      while True:
        print('-->[TOKEN]: Updating token')
        response = post(self.base_url + 'auth/login', data={"name":username,"password":password,"remember":True})
        if response.status_code != 200: print('-->[TOKEN]: Invalid Credentials. Aborting Token update')
        else: token = response.json()
        print(f'-->[TOKEN]: Token updated is {token["token"][:20:]}...{token["token"][-20::]}')
        self.update_token(token)
        sleep(60)
    start_new_thread(cycle, (username, password))

  def fetch(self, route: str) -> Any:
    if route[0] == '/': route = route[1::]
    def decorator(func):
      def wrapper(*args: Any, **kwds: Any) -> Any:
        print(f'-->[POST]: Fetching from {"/api/" + route} with payload {kwds.get("payload")}')
        response = post(self.base_url + route, headers={'authorization': self.token}, data=kwds.get('payload'))
        if response.status_code != 200:
          print('XXX Something went wrong. Invalid path or token. XXX')
          return
        data = response.json()
        if 'data' in data.keys(): data = data['data']
        result = func(data, *args, **kwds)
        return result
      return wrapper
    return decorator

  def fetchall(self, route:str):
    if route[0] == '/': route = route[1::]
    def decorator(func):
      def wrapper(*args, **kwds):
        if kwds.get('total_pages'):
          total_pages = kwds.get('total_pages') 
          del kwds['total_pages']
        else: total_pages = 99999
        data = []
        print(f'-->[POST]: Fetching all from {"/api/" + route} with payload {kwds.get("payload")} with max pages {total_pages}')
        response = post(self.base_url + route, headers={'authorization': self.token}, data=kwds.get('payload'))
        if response.status_code != 200:
          print('XXX Something went wrong. Invalid path or token. XXX')
          return
        first_fetch = response.json()
        data.extend(first_fetch['data'])
        i=1
        run = True
        while run:
          i += 1
          response = post(f'{self.base_url + route}?page={i}', headers={'authorization': self.token}, data=kwds.get('payload'))
          if response.status_code != 200:
            print('XXX Something went wrong. Invalid path or token. XXX')
            return
          fetch = response.json()
          data.extend(fetch['data'])
          if fetch['next_page_url'] == None or i == total_pages: run = False
        result = func(data, *args, **kwds)
        return result
      return wrapper
    return decorator