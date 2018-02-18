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

  BASE_URL = None
  HEADERS  = {}
  JSON_API = True

  def _get_uri(self, url_string, params={}):
    tup = (self.BASE_URL, url_string)
    url = "%s/%s" % tup if self.BASE_URL else url_string
    uri = Soup.URI.new(url)

    params = dict([(k, str(v)) for k, v in params.items()])
    uri.set_query_from_form(params)

    return uri

  def _send_message(self, message_type, uri):
    message = Soup.Message.new_from_uri(message_type, uri)
    self._message_headers(message)
    session.send_message(message)

    return message.response_body.data

  def _message_headers(self, message):
    if self.JSON_API:
      self.HEADERS['accept'] = self.HEADERS.get('accept', 'application/json')

    for key, value in self.HEADERS.items():
      message.request_headers.append(key, value)

  def _request(self, request_type, url, params={}):
    url  = self._get_uri(url, params)
    data = self._send_message(request_type, url)

    return self._parse_response(data)

  def get(self, url, params={}):
    return self._request('GET', url, params)

  def post(self, url, params={}):
    return self._request('POST', url, params)

  def _parse_response(self, text):
    data = self._to_json(text) if self.JSON_API else text
    return data

  def _to_json(self, text):
    data = {}
    html = re.compile('<.*>')
    text = re.sub(html, '', str(text))

    try:
      data = json.loads(text) if text else data
    except JSONDecodeError as error:
      print('JSON Decode Error', error)

    return data
