from google.appengine.ext import ndb

# Create your models here.
"""class InstaUser(ndb.Model):
    id = ndb.IntegerProperty()
    username = ndb.StringProperty()
    full_name = ndb.StringProperty()
    user_name = ndb.StringProperty()
    profile_picture = ndb.StringProperty()
    bio = ndb.StringProperty()
    website = ndb.StringProperty()
    
    added_date = ndb.DateTimeProperty(auto_now_add=True)"""
    



class User(ndb.Model):
    username = ndb.StringProperty(max_length=20)
    token = ndb.StringProperty()
    password = ndb.StringProperty()
    e_mail = ndb.StringProperty()