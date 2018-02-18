import gi
import libtorrent

gi.require_version('Gio', '2.0')

from gi.repository import Gio
from helpers.utils import user_data_dir

session = libtorrent.session()
session.listen_on(6881, 6891)

class Torrent(object):

  def __init__(self):
    self.handlers = []

  def from_url(self, url):
    stream = Gio.File.new_for_uri(url)
    result = list(stream.load_contents())[1]

    self._add_torrent(result)

  def from_path(self, path):
    stream = Gio.File.new_for_path(path)
    result = list(stream.load_contents())[1]

    self._add_torrent(result)

  def _add_torrent(self, data):
    info    = self._get_info(data)
    params  = self._get_params(info)
    handler = session.add_torrent(params)

    handler.set_sequential_download(True)
    self.handlers.append(handler)

  def _get_info(self, data):
    data = libtorrent.bdecode(data)
    info = libtorrent.torrent_info(data)

    return info

  def _get_params(self, info):
    folder = "%s/torrents" % user_data_dir()
    store  = libtorrent.storage_mode_t.storage_mode_sparse
    params = { 'save_path': folder, 'storage_mode': store, 'ti': info }

    return params
