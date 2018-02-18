from helpers.request import Request

class Subtitles(Request):

  base_url = 'https://subtitle-api.org'

  def video(self, imdb_id):
    return self.get('videos/%s' % imdb_id)

  def subtitles(self, imdb_id):
    return self.get('videos/%s/subtitles' % imdb_id)

  def subtitle(self, imdb_id, sub_id, **params):
    return self.get('videos/%s/subtitles/%s' % (imdb_id, sub_id), params)
