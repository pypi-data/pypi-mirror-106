# from .URDFRepresentation import URDFRepresentation
# from .UrdfToUrdf2 import UrdfToUrdf2

import os
from lxml import etree

from simpleurdf.urdf2model import Model

from .urdf2_to_urdf import Urdf2ToUrdf

#import simpleurdf.urdfParser.urdf as urdf


class UrdfParser:
    """class used to load, traverse, and create URDF files"""
    def create_urdf_string(self, robot: Model) -> str:
        model = robot.build()
        tree_robot = Urdf2ToUrdf().create_robot(model)
        return etree.tostring(tree_robot, pretty_print=True, encoding=str)
        # world = urdfSerializer.createWorld(world)
        # etree.indent(world)
        # etree.ElementTree(world).write(open(pathToFile, "wb"))

    def create_urdf_file(self, robot: Model, path_to_file: str):
        urdf_robot = self.create_urdf_string(robot)
        path_to_directory, _ = os.path.split(path_to_file)
        os.makedirs(path_to_directory)
        with open(path_to_file, "w+") as file:
            file.write(urdf_robot)
