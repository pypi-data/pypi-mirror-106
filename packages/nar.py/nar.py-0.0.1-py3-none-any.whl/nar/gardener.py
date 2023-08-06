from typing import Any
from requests import post

class Gardener():
  def __init__(self, token: str) -> None:
    self.token = token if token.split()[0] == 'Bearer' else 'Bearer ' + token.strip()
    self.base_url = 'https://www.nationsatrisk.com/api/'

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
        func(data, *args, **kwds)
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
        data.extend(first_fetch.get('data') if not first_fetch.get('data') else first_fetch)
        i=1
        run = True
        while run:
          i += 1
          response = post(f'{self.base_url + route}?page={i}', headers={'authorization': self.token}, data=kwds.get('payload'))
          if response.status_code != 200:
            print('XXX Something went wrong. Invalid path or token. XXX')
            return
          fetch = response.json()
          data.extend(fetch.get('data') if fetch.get('data') else fetch)
          if fetch['next_page_url'] == None or i == total_pages: run = False
        func(data, *args, **kwds)
      return wrapper
    return decorator