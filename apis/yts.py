from helpers.request import Request

class Yts(Request):

  base_url = 'https://yts.am/api/v2'

  def search(self, term, **params):
    params['query_term'] = term
    return self.movies(**params)

  def upcoming(self):
    return self.get('list_upcoming.json')

  def movies(self, **params):
    return self.get('list_movies.json', params)

  def movie(self, movie_id, **params):
    params['movie_id'] = movie_id
    return self.get('movie_details.json', params)

  def suggestions(self, movie_id, **params):
    params['movie_id'] = movie_id
    return self.get('movie_suggestions.json', params)

  def comments(self, movie_id, **params):
    params['movie_id'] = movie_id
    return self.get('movie_comments.json', params)

  def reviews(self, movie_id, **params):
    params['movie_id'] = movie_id
    return self.get('movie_reviews.json', params)
