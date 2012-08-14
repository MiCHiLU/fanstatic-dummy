__all__ = ["Library", "Resources", "Groups", "GroupResource"]

class Dummy(object):
  def __init__(self, *argv, **keargv):
    return super(Dummy, self).__init__()

class Library(Dummy):
  pass

class Resources(Dummy):
  pass

class Group(Dummy):
  pass

class GroupResource(Dummy):
  pass
