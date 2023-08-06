from typing import Any, Union
from requests import post
from _thread import start_new_thread
from time import sleep
from nar.utils import Utils

class Gardener():
  base_url = 'https://www.nationsatrisk.com/api/'

  def __init__(self, token: str = None, **kwds) -> None:
    if token: self.token = token if token.split()[0] == 'Bearer' else 'Bearer ' + token.strip()
    else: self.token_update_init(kwds.get('username'), kwds.get('password'))
  
  def update_token(self, token: dict):
    token_ = token['token'] if type(token) == dict else token
    self.token = 'Bearer ' + token_

  def token_update_init(self, username: str, password: str):
    def cycle(username: str, password: str, thread: bool = True):
      while True:
        print('-->[TOKEN]: Updating token')
        response = post(self.base_url + 'auth/login', data={"name":username,"password":password,"remember":True})
        token = 'placeholder'
        if response.status_code != 200: 
          print('-->[TOKEN]: Invalid Credentials. Aborting Token update')
          return
        else: 
          token = response.json()
          if token == {'error': 'This username or email does not exist.'}:
            print('-->[TOKEN]: Invalid Credentials. Aborting Token update')
            return
        print(f'-->[TOKEN]: Token updated is {token["token"][:20:]}...{token["token"][-20::]}')
        self.update_token(token)
        if thread: sleep(1800)
        else: break
    cycle(username=username, password=password, thread=False)
    start_new_thread(cycle, (username, password))

  def fetch(self, route: str) -> Any:
    if route[0] == '/': route = route[1::]
    def decorator(func):
      def wrapper(*args: Any, **kwds: Any) -> Any:
        print(f'-->[POST]: Fetching from {"/api/" + route} with payload {kwds.get("payload")}')
        if kwds.get('payload'):
          payload = kwds.get('payload')
          del kwds['payload']
        response = post(self.base_url + route, headers={'authorization': self.token}, data=payload)
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
        if kwds.get('payload'):
          payload = kwds.get('payload')
          del kwds['payload']
        data = []
        print(f'-->[POST]: Fetching all from {"/api/" + route} with payload {kwds.get("payload")} with max pages {total_pages}')
        response = post(self.base_url + route, headers={'authorization': self.token}, data=payload)
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

  def get(self, path: str, payload: dict = {}):
    if path[0] == '/': path = path[1::]
    target_url = self.base_url + path
    header = {'Authorization': self.token}
    r = post(target_url, data = payload, headers = header)
    if r.status_code != 200:
      print('Something went wrong with the request. dumped in dump.html')
      open('dump.html', 'w').write(r.text)
      return
    try: return r.json()
    except: print('response was not json.')

  def get_all(self, path: str,  payload: dict = None, total_pages: int = 99999) -> Any:
    data = []
    first_fetch = self.get(path, payload)
    data.extend(first_fetch['data'])
    i=1
    run = True
    while run:
      i += 1
      fetched = self.get(f'{path}?page={i}', payload)
      data.extend(fetched['data'])
      if fetched['next_page_url'] == None or i == total_pages: run = False
    return data

  def members(self, id: str, with_points=False) -> Union[list, dict]:
    if id is not str: id = str(id)
    out_data = list() if not with_points else dict()
    for member in self.get_all(Utils.Urls.alliance_members, payload={'id': id}):
      out_data.append(member['name']) if not with_points else out_data.update({member['name']: member['points']})
    return out_data