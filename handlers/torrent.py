import gi
import libtorrent

gi.require_version('Gio', '2.0')

from gi.repository import Gio
from helpers.utils import user_data_dir

session = libtorrent.session()
session.listen_on(6881, 6891)

class Torrent(object):

  def __init__(self):
    self.info    = None
    self.params  = None
    self.handler = None

  def from_url(self, url):
    stream = Gio.File.new_for_uri(url)
    result = list(stream.load_contents())[1]

    self.add_torrent(result)

  def from_path(self, path):
    stream = Gio.File.new_for_path(path)
    result = list(stream.load_contents())[1]

    self.add_torrent(result)

  def add_torrent(self, data):
    self.info    = self.get_info(data)
    self.params  = self.set_params()
    self.handler = session.add_torrent(self.params)

    self.handler.set_sequential_download(True)

  def get_info(self, data):
    data = libtorrent.bdecode(data)
    info = libtorrent.torrent_info(data)

    return info

  def set_params(self):
    folder = "%s/torrents" % user_data_dir()
    store  = libtorrent.storage_mode_t.storage_mode_sparse
    params = { 'save_path': folder, 'storage_mode': store, 'ti': self.info }

    return params
