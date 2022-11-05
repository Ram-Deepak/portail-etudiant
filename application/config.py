class Config():
  SQLITE_URI = None
  SQLITE_DB_DIR = None
  DEBUG = None

class LocalDevelopmentConfig(Config):
  SQLITE_DB_DIR = "/db_directory"
  SQLITE_URI = "sqlite:///"+SQLITE_DB_DIR+"/database.sqlite3"
  DEBUG = True
  
  