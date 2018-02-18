import os


def relative_path(filepath):
  root = os.path.dirname(os.path.realpath(__file__))
  root = os.path.dirname(root)

  return os.path.join(root, filepath)


def user_data_dir():
  path = "%s/.config/popcorn-player" % os.path.expanduser('~')

  if not os.path.exists(path):
    os.makedirs(path)

  return path


def database_dir(db_name):
  db_dir = os.path.join(user_data_dir(), db_name)

  if not os.path.exists(db_dir):
    open(db_dir, 'w+')

  return db_dir
