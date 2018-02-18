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

  def __init__(self):
    self.base_url = None

  def uri(self, url_string, params={}):
    tup = (self.base_url, url_string)
    url = "%s/%s" % tup if self.base_url else url_string
    uri = Soup.URI.new(url)

    params = dict([(k, str(v)) for k, v in params.items()])
    uri.set_query_from_form(params)

    return uri

  def message(self, message_type, uri):
    message = Soup.Message.new_from_uri(message_type, uri)
    session.send_message(message)

    return message.response_body.data

  def request(self, request_type, url, params={}):
    url  = self.uri(url, params)
    data = self.message(request_type, url)

    return self.to_json(data)

  def get(self, url, params={}):
    return self.request('GET', url, params)

  def post(self, url, params={}):
    return self.request('POST', url, params)

  def to_json(self, text):
    data = {}
    html = re.compile('<.*>')
    text = re.sub(html, '', text)

    try:
      data = json.loads(text)
    except JSONDecodeError as error:
      print(error)

    return data
