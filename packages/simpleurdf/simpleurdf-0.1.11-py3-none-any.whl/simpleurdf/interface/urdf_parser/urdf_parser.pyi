from simpleurdf.urdf2model import Model as Model
from typing import Any


class UrdfParser:
    def create_urdf_string(self, robot: Model) -> str:
        ...

    def create_urdf_file(self, robot: Model, path_to_file: str) -> Any:
        ...
