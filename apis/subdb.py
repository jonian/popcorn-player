import os
import hashlib

from helpers.request import Request

class SubDB(Request):

  json_api   = False
  base_url   = 'http://api.thesubdb.com'
  user_agent = 'SubDB/1.0 (PopcornPlayer/0.1; https://github.com/jonian/popcorn-player)'

  def get_hash(self, name):
    readsize = 64 * 1024

    with open(name, 'rb') as f:
      data = f.read(readsize)
      f.seek(-readsize, os.SEEK_END)
      data += f.read(readsize)

    return hashlib.md5(data).hexdigest()

  def search(self, name, **params):
    params['action'] = 'search'
    params['hash']   = self.get_hash(name)

    return self.get('', params)

  def download(self, name, **params):
    params['action'] = 'download'
    params['hash']   = self.get_hash(name)

    return self.get('', params)
