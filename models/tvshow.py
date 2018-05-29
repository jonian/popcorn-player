from models.model import Model
from apis.tmdb import Tmdb

tmdb_api = Tmdb()

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
