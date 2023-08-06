from pydantic.main import BaseModel
from pydantic import BaseConfig as _BaseConfig

from ginodantic.gino_model_meta import GinoModelMeta


class BaseConfig(_BaseConfig):
    allow_population_by_field_name = True
    arbitrary_types_allowed = True
    orm_mode = True


class BaseModelSchema(BaseModel, metaclass=GinoModelMeta):
    class Config(BaseConfig):
        pass

