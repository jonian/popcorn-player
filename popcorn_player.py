#! /usr/bin/python3

import gi
import signal
import argparse

gi.require_version('Gtk', '3.0')
gi.require_version('GLib', '2.0')

from gi.repository import Gtk, GLib
from helpers.gtk import add_custom_css, relative_path


class PopcornPlayer(object):

  def __init__(self):
    GLib.set_prgname('popcorn-player')
    GLib.set_application_name('Popcorn Player')

    add_custom_css('ui/styles.css')

    self.argparse = argparse.ArgumentParser(prog='popcorn-player')
    self.argparse.add_argument('url', metavar='URL', nargs='?', default=None)

    self.main = Gtk.Builder()
    self.main.add_from_file(relative_path('ui/main.ui'))
    self.main.connect_signals(self)

    self.window = self.main.get_object('window_main')

  def run(self):
    self.window.show_all()
    Gtk.main()

  def quit(self):
    Gtk.main_quit()

  def on_window_main_destroy(self, _event):
    self.quit()


if __name__ == '__main__':
  signal.signal(signal.SIGINT, signal.SIG_DFL)

  player = PopcornPlayer()
  player.run()
