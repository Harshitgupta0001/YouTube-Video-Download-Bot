import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7688836096:AAHL2nm9ndCx8Ceh84i4sV66dO_1F4uMD20")
    API_ID = int(os.environ.get("API_ID", "25492855"))
    API_HASH = os.environ.get("API_HASH", "61876db014de51a4ace6b169608be4f1")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002166149059")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
