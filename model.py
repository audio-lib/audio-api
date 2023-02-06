import peewee
from database import db


class Records(peewee.Model):
    id = peewee.IdentityField(unique=True, index=True)
    link = peewee.CharField()
    author = peewee.CharField()
    title = peewee.CharField()

    class Meta:
        database = db
