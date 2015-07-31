from chronicle.app import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.Text)
    type = db.Column(db.Text)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)

    def __repr__(self):
        return '<Event %s[%s]>' % (self.year, self.type)

    def date(self):
        return {
            "year": self.year,
            "month": self.month,
            "day": self.day,
        }
