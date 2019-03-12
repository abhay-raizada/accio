from .application_model import ApplicationModel

class Resource(ApplicationModel):
    __fillable__ = ['user_id', 'name', 'url']