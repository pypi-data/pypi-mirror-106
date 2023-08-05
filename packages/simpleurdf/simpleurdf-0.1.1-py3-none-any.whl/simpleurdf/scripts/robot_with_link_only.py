from simpleurdf.urdf2model import UrdfFactory
from simpleurdf.urdf2model import Model, Link


class RobotWithLinkOnly(UrdfFactory):
    def build_model(self) -> Model:
        return Model(name="test_robot", root_link=Link(name="base_link"))
