from .file_storage import FileStorage
from .db_storage import DBStorage

storage = DBStorage() if os.getenv('HBNB_TYPE_STORAGE') == 'db' else FileStorage()
storage.reload()
