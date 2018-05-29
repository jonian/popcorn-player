class Model(object):

  def __init__(self, data):
    self._set_attrs_to_values(data)
    self._initialize()

  def _initialize(self):
    pass

  def _set_attrs_to_values(self, data={}):
    if isinstance(data, dict):
      for key in data.keys():
        if not hasattr(self, key) or not callable(getattr(self, key)):
          setattr(self, key, data[key])
