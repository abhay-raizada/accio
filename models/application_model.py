from orator import Model
from orator import DatabaseManager
import yaml

config = yaml.load(open('orator.yml'))['databases']
db = DatabaseManager(config)
Model.set_connection_resolver(db)

class ApplicationModel(Model):
    __fillable__ = ['user_id', 'name', 'url']