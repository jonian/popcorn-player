from models.model import Model
from apis.yts import Yts

yts_api = Yts()

class Movie(Model):

  @classmethod

  def search(self, term):
    data = yts_api.search(term, sort_by='title')
    data = [Movie(item) for item in data['data']['movies']]

    return data

  @classmethod

  def popular(self):
    data = yts_api.movies(sort_by='download_count')
    data = [Movie(item) for item in data['data']['movies']]

    return data

  @classmethod

  def top_rated(self):
    data = yts_api.movies(sort_by='rating')
    data = [Movie(item) for item in data['data']['movies']]

    return data

  @classmethod

  def find(self, movie_id):
    data = yts_api.movie(movie_id)
    data = Movie(data['data']['movie'])

    return data
