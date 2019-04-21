from app import db

class YelpUsers(db.Model):
    __tablename__ = 'yelpuser'

    userid = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    avgstar = db.Column(db.String())
    usersince = db.Column(db.String())
    fans = db.Column(db.Integer)
    cool = db.Column(db.Integer)
    funny = db.Column(db.Integer)
    useful = db.Column(db.Integer)
    review_count = db.Column(db.Integer)
    latitude = db.Column(db.String())
    longitude = db.Column(db.String())


class Business(db.Model):
    __tablename__ = 'business'

    busid = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    zipcode = db.Column(db.Integer)
    numcheckins = db.Column(db.Integer)
    stars = db.Column(db.Float())
    numreviews = db.Column(db.Integer)
    avgrating = db.Column(db.Float())
    isopen = db.Column(db.Integer)
    latitude = db.Column(db.String())
    longitude = db.Column(db.String())


class Checkin(db.Model):
    __tablename__ = 'checkin'

    busid = db.Column(db.String(), db.ForeignKey(Business.busid), primary_key=True)
    day = db.Column(db.String(), primary_key=True)
    hour = db.Column(db.String(), primary_key=True)
    numcheck = db.Column(db.Integer)


class Review(db.Model):
    __tablename__ = 'review'

    reviewid = db.Column(db.String(), primary_key=True, nullable=False)
    busid = db.Column(db.String(), db.ForeignKey(Business.busid), nullable=False)
    userid = db.Column(db.String(),db.ForeignKey(YelpUsers.userid), nullable=False)
    date = db.Column(db.String())
    stars = db.Column(db.Integer)
    text = db.Column(db.String())
    useful = db.Column(db.Integer)
    funny = db.Column(db.Integer)
    cool = db.Column(db.Integer)


class Hours(db.Model):
    __tablename__ = 'hours'

    busid = db.Column(db.String(), db.ForeignKey(Business.busid), primary_key=True)
    day = db.Column(db.String(), primary_key=True)
    openclose = db.Column(db.String(), primary_key=True)


class Category(db.Model):
    __tablename__ = 'category'

    busid = db.Column(db.String(), db.ForeignKey(Business.busid), primary_key=True)
    category_name = db.Column(db.String(), primary_key=True)


class Attribute(db.Model):
    __tablename__ = 'attribute'

    busid = db.Column(db.String(), db.ForeignKey(Business.busid), primary_key=True)
    attribute_name = db.Column(db.String(), primary_key=True, nullable=False)
    value = db.Column(db.String())


class Friends(db.Model):
    __tablename__ = 'friends'

    friendsid = db.Column(db.String(), db.ForeignKey(YelpUsers.userid), primary_key=True)
    userid = db.Column(db.String(), db.ForeignKey(YelpUsers.userid), primary_key=True)