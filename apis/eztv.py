from helpers.request import Request

class Eztv(Request):

  def __init__(self):
    self.base_url = 'https://eztv.ag/api'

  def torrents(self):
    return self.get('get-torrents')
