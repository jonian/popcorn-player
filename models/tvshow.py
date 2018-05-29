from models.model import Model
from apis.tmdb import Tmdb
from apis.eztv import Eztv

tmdb_api = Tmdb()
eztv_api = Eztv()

class TvShow(Model):

  @classmethod

  def search(self, term):
    data = tmdb_api.search('tv', term)
    data = [TvShow(item) for item in data['results']]

    return data

  @classmethod

  def popular(self):
    data = tmdb_api.tvshows(sort_by='popular')
    data = [TvShow(item) for item in data['results']]

    return data

  @classmethod

  def top_rated(self):
    data = tmdb_api.tvshows(sort_by='top_rated')
    data = [TvShow(item) for item in data['results']]

    return data

  @classmethod

  def find(self, show_id):
    data = tmdb_api.tvshow(show_id)
    data = TvShow(data)

    return data

  def _initialize(self):
    self.imdb_code = tmdb_api.external_ids('tv', self.id)['imdb_id']
    self.torrents  = eztv_api.tvshow(self.imdb_code.split('tt')[-1])

    if self.poster_path:
      self.poster_path = "%s/w370_and_h556_bestv2%s" % (Tmdb.IMG_URL, self.poster_path)

    if self.backdrop_path:
      self.backdrop_path = "%s/w1400_and_h450_face%s" % (Tmdb.IMG_URL, self.backdrop_path)
