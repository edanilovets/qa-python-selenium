from sys import maxsize


class Contact:
    def __init__(self, first_name=None, last_name=None, home_phone=None,
                 mobile_phone=None, work_phone=None, cid=None, all_phones=None):
        self.first_name = first_name
        self.last_name = last_name
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.cid = cid
        self.all_phones = all_phones

    def __repr__(self):
        return "%s:%s %s" % (self.cid, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.cid is None or other.cid is None or self.cid == other.cid)\
                and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.cid:
            return int(self.cid)
        else:
            return maxsize
