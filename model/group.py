class Group:
    def __init__(self, gid=None, name=None, header=None, footer=None):
        self.gid = gid
        self.name = name
        self.header = header
        self.footer = footer

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.gid, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (int(self.gid) == 900 or self.gid == other.gid) and self.name == other.name

    def get_name(self):
        return self.name
