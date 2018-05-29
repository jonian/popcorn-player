import os

from helpers.request import Request

API_KEY = os.environ.get('TMDB_API_KEY')

class Tmdb(Request):

  BASE_URL = 'https://api.themoviedb.org/3'
  IMG_URL  = 'https://image.tmdb.org/t/p'
  PARAMS   = { 'api_key': API_KEY }

  def find(self, imdb_id, **params):
    params['external_source'] = 'imdb_id'
    return self.get('find/%s' % imdb_id, params)

  def search(self, model, term, **params):
    params['query'] = term
    return self.get('search/%s' % model, params)

  def external_ids(self, model, model_id, **params):
    return self.get('%s/%s/external_ids' % (model, model_id), params)

  def movies(self, sort='popular', **params):
    return self.get('movie/%s' % sort, params)

  def movie(self, movie_id, **params):
    return self.get('movie/%s' % movie_id, params)

  def tvshows(self, sort='popular', **params):
    return self.get('tv/%s' % sort, params)

  def tvshow(self, show_id, **params):
    return self.get('tv/%s' % show_id, params)
