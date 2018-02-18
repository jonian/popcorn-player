from helpers.request import Request

class Eztv(Request):

  base_url = 'https://eztv.ag/api'

  def torrents(self):
    return self.get('get-torrents')
