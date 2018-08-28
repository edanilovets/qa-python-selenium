class Group:
    def __init__(self, name=None, header=None, footer=None, gid=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.gid = gid

    def __repr__(self):
        return "%s:%s" % (self.gid, self.name)

    def __eq__(self, other):
        return (int(self.gid) == 1000 or self.gid == other.gid) and self.name == other.name

    def get_name(self):
        return self.name
