import re
import gi
import json

gi.require_version('Soup', '2.4')

from gi.repository import Soup
from json.decoder import JSONDecodeError

caching = Soup.Cache.new(None, Soup.CacheType.SHARED)
session = Soup.Session.new()
session.add_feature(caching)

class Request(object):

  json_api   = True
  base_url   = None
  user_agent = 'Soup/2.4 (PopcornPlayer/0.1; https://github.com/jonian/popcorn-player)'

  def uri(self, url_string, params={}):
    tup = (self.base_url, url_string)
    url = "%s/%s" % tup if self.base_url else url_string
    uri = Soup.URI.new(url)

    params = dict([(k, str(v)) for k, v in params.items()])
    uri.set_query_from_form(params)

    return uri

  def message(self, message_type, uri):
    message = Soup.Message.new_from_uri(message_type, uri)
    message.request_headers.append('user-agent', self.user_agent)
    session.send_message(message)

    return message.response_body.data

  def request(self, request_type, url, params={}):
    url  = self.uri(url, params)
    data = self.message(request_type, url)

    return self.parse_response(data)

  def get(self, url, params={}):
    return self.request('GET', url, params)

  def post(self, url, params={}):
    return self.request('POST', url, params)

  def parse_response(self, text):
    data = self.to_json(text) if self.json_api else text
    return data

  def to_json(self, text):
    data = {}
    html = re.compile('<.*>')
    text = re.sub(html, '', text)

    try:
      data = json.loads(text) if text else data
    except JSONDecodeError as error:
      print('JSON Decode Error', error)

    return data
