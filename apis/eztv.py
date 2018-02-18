from helpers.request import Request

class Eztv(Request):

  BASE_URL = 'https://eztv.ag/api'

  def tvshow(self, imdb_id):
    return self.torrents(imdb_id=imdb_id)

  def torrents(self, **params):
    return self.get('get-torrents', params)
