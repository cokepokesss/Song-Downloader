import os

class Config(object):
    DATABASE = os.environ.get("mongodb+srv://cokepokesmusic:<888999Qq>@cluster0.fvj2o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "2038003838").split())
    SUPPORT = os.environ.get("SUPPORT")
    BOT_NAME = os.environ.get("AdamhakliSong")
    BOT_USERNAME = os.environ.get("cokepokesmusic_bot")
