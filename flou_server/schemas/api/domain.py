from flou_server import models

class DomainCreate(models.PydanticModelBase):
    name: str
