#pylint: disable=too-few-public-methods, too-many-arguments
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional, Union, Tuple, cast
import math
from copy import deepcopy

from simpleurdf.utils.python_extension import switch_case
from simpleurdf.utils.python_extension.deepcopy_attribute import init_with_deepcopy

from .metamodel import (
  ClassicalMaterialModel,
  CollisionModel,
  ContinuousJointTypeModel,
  DynamicsModel,
  FixedJointTypeModel,
  Geometry,
  GeometryBoxModel,
  GeometryCylinderModel,
  Inertia,
  InertialModel,
  JointModel,
  JointTypeModel,
  LimitModel,
  LinkModel,
  MeshModel,
  ModelModel,
  PoseModel,
  PrismaticJointTypeModel,
  RevoluteJointTypeModel,
  VisualModel,
  XYZ,
)

DEFAULT_BEHAVIOR = None

LOWER_LIMIT = -math.inf
UPPER_LIMIT = math.inf

NO_EFFORT = -1
NO_VELOCITY_LIMIT = math.inf


class Pose(PoseModel):
    """builder for pose object"""
    @init_with_deepcopy
    def __init__(self, rpy=[0, 0, 0], xyz=[0, 0, 0]):  #pylint: disable=dangerous-default-value
        super().__init__(rpy, xyz)


class Mesh(MeshModel):
    @init_with_deepcopy
    def __init__(self, uri, scale: XYZ = XYZ(1.0, 1.0, 1.0)):
        super().__init__(uri, scale)


class GeometryBox(GeometryBoxModel):
    @init_with_deepcopy
    def __init__(self, size: XYZ = XYZ(1.0, 1.0, 1.0)):
        super().__init__(size)


class Capsule:
    def __init__(self, radius=0.5, length=1):
        self.radius = radius
        self.length = length


class Sphere:
    def __init__(self, radius=1):
        self.radius = radius


class GeometryCylinder(GeometryCylinderModel):
    pass


class Inertial(InertialModel):
    pass


class InertialCylinder(Inertial):
    @init_with_deepcopy
    def __init__(self,
                 radius: float = 1.0,
                 length: float = 1.0,
                 pose: Pose = Pose(),
                 mass: float = 1.) -> None:

        ixx = 1 / 12 * mass * (3 * radius**2 + length**2)
        iyy = ixx
        izz = 1 / 2 * mass * radius**2
        super().__init__(pose, mass, Inertia(ixx, 0.0, 0.0, iyy, 0.0, izz))


class InertialBox(Inertial):
    @init_with_deepcopy
    def __init__(self,
                 size: XYZ = XYZ(1.0, 1.0, 1.0),
                 pose: Pose = Pose(),
                 mass: float = 1.) -> None:

        width, height, depth = size
        ixx = 1 / 12 * mass * (height**2 + depth**2)
        iyy = 1 / 12 * mass * (width**2 + depth**2)
        izz = 1 / 12 * mass * (width**2 + height**2)
        super().__init__(pose, mass, Inertia(ixx, 0.0, 0.0, iyy, 0.0, izz))


DEFAULT_INERTIAL = Inertial(Pose(), 1, Inertia(1, 0, 0, 1, 0, 1))


class MaterialColor(ClassicalMaterialModel):
    @init_with_deepcopy
    def __init__(  #pylint: disable=dangerous-default-value
      self,
      name,
      ambient=[0, 0, 0, 0],
      diffuse=[0, 0, 0, 0],
      specular=[0, 0, 0, 0],
      emissive=[0, 0, 0, 0],
    ):
        super().__init__(name, ambient, diffuse, specular, emissive)


white = MaterialColor(name="white", ambient=[0, 0, 0, 1])


class Visual(VisualModel):
    @init_with_deepcopy
    def __init__(self, geometry: Geometry, pose=Pose(), material=white):
        super().__init__(geometry, material, pose)


class Collision(CollisionModel):
    @init_with_deepcopy
    def __init__(self, geometry, pose=Pose()) -> None:
        super().__init__(geometry, pose)


class CollisionBox(Collision):
    @init_with_deepcopy
    def __init__(self, geometry, pose) -> None:
        super().__init__(geometry, pose=pose)


class Limit(LimitModel):
    def __init__(
      self,
      lower=LOWER_LIMIT,
      upper=UPPER_LIMIT,
      effort=NO_EFFORT,
      velocity=NO_VELOCITY_LIMIT,
    ):
        super().__init__(lower, upper, effort, velocity)


class Dynamics(DynamicsModel):
    def __init__(self, damping=0.0) -> None:
        super().__init__(damping)


# region Link


class Link:
    """Builder for LinkModel"""
    @init_with_deepcopy
    def __init__(  #pylint: disable=dangerous-default-value
      self,
      name: str,
      collision: Optional[Collision] = None,
      visuals: List[VisualModel] = [],
      inertial: Optional[Inertial] = None,
      joints: List[Joint] = [],
      pose: Pose = Pose(),
    ):
        """if collision and inertial are None, they will not be specified in the model,
        and any tools requiring them are expected to throw an error for this model"""

        if visuals == []:
            visuals = deepcopy(visuals)
        if joints == []:
            joints = deepcopy(joints)

        self.link_model = LinkModel(name, collision, visuals, inertial, pose)
        self.joints = joints
        for joint in self.joints:
            joint.set_parent(self)

        self.parent_node = None

    def set_parent(self, parent):
        self.parent_node = parent

    def build(self):
        for joint in self.joints:
            joint.build()


class Cylinder(Link):
    @init_with_deepcopy
    def __init__(  #pylint: disable=dangerous-default-value
      self,
      name,
      radius: float,
      length: float,
      mass: float = 1,
      joints: List[Joint] = [],
      pose=Pose(),
      collision_pose: Optional[Pose] = DEFAULT_BEHAVIOR,
    ):
        """
        if collision_pose value is DEFAULT_BEHAVIOR it is the same as the pose value specified
        """
        """Do not modify joints without making a deepcopy !!!"""  #pylint: disable=pointless-string-statement

        self._name = name
        self._radius = float(radius)
        self._length = float(length)
        self._mass = float(mass)
        self._pose = pose

        geometry_cylinder = GeometryCylinder(self._radius, self._length)

        if collision_pose is not None:
            collision = Collision(geometry_cylinder, collision_pose)
        else:
            collision = Collision(geometry_cylinder, pose)

        visuals: List[VisualModel] = [Visual(geometry_cylinder, self._pose)]

        inertial = InertialCylinder(self._radius, self._length, self._pose, self._mass)

        super().__init__(name, collision, visuals, inertial, joints, pose)


class Box(Link):
    @init_with_deepcopy
    def __init__(  #pylint: disable=dangerous-default-value
      self,
      name,
      material,
      width: float = 1.0,
      depth: float = 1.0,
      height: float = 1.0,
      mass: float = 1.0,
      joints: List[Joint] = [],
      pose=Pose(),
      collision_pose: Optional[Pose] = DEFAULT_BEHAVIOR,
    ):
        """
        if collision_pose value is DEFAULT_BEHAVIOR, it is the same as the pose value specified
        """
        """Do not modify joints without making a deepcopy !!!"""  #pylint: disable=pointless-string-statement

        self._name = name
        self._size = XYZ(float(width), float(depth), float(height))
        self._mass = float(mass)
        self._pose = pose

        # if collection_pose was set
        if collision_pose is not None:
            collision = Collision(GeometryBox(self._size), collision_pose)
        # if not set, put pose of visual
        else:
            collision = Collision(GeometryBox(self._size), pose)

        # create visuals
        visuals: List[VisualModel] = [
          Visual(GeometryBox(self._size), self._pose, material=material)
        ]

        # create inertials
        inertial = InertialBox(self._size, self._pose, self._mass)

        super().__init__(name, collision, visuals, inertial, joints, pose)


# endregion

# region joints


class JointType(ABC):
    @abstractmethod
    def build(self) -> JointTypeModel:
        pass


class FixedJointType(JointType):
    @init_with_deepcopy
    def __init__(self, dynamics: DynamicsModel) -> None:
        self.joint_type = FixedJointTypeModel(dynamics)

    def build(self) -> FixedJointTypeModel:
        return self.joint_type


class PrismaticJointType(JointType):
    @init_with_deepcopy
    def __init__(  #pylint: disable=dangerous-default-value
      self,
      translation_axis,
      limit=Limit(),
    ) -> None:
        super().__init__()
        self.joint_type = PrismaticJointTypeModel(DynamicsModel(1),
                                                  translation_axis=translation_axis,
                                                  limit=deepcopy(limit))

    def build(self) -> PrismaticJointTypeModel:
        return self.joint_type


class ContinuousJointType(JointType):
    @init_with_deepcopy
    def __init__(  #pylint: disable=dangerous-default-value
      self,
      rotation_axis: XYZ,
      joint_physic=Dynamics(),
    ):
        self.joint_type = ContinuousJointTypeModel(deepcopy(joint_physic), rotation_axis)

    def build(self) -> ContinuousJointTypeModel:
        return self.joint_type


class RevoluteJointType(JointType):
    @init_with_deepcopy
    def __init__(  #pylint: disable=dangerous-default-value
      self,
      rotation_axis: XYZ,
      limit: LimitModel,
      joint_physic=Dynamics(),
    ):
        self.joint_type = RevoluteJointTypeModel(
          deepcopy(joint_physic),
          rotation_axis,
          limit,
        )

    def build(self) -> RevoluteJointTypeModel:
        return self.joint_type


class Joint:
    @init_with_deepcopy
    def __init__(  #pylint: disable=dangerous-default-value
      self,
      name: str,
      child: Union[Tuple[Model, int], Link],
      joint_type_characteristics: JointType,
      pose=Pose(),
    ):
        self._name_param = name
        self._pose_param = deepcopy(pose)
        self.child_node = child
        self._joint_type_characteristics_param = joint_type_characteristics
        self.parent_node = None
        self.joint_model = None

    def set_parent(self, parent: Union[Tuple[Model, int], Link]):
        self.parent_node = parent

    def get_node_link(self, node) -> Link:
        def case_link(link: Link) -> Link:
            return link

        def case_model(model: Tuple[Model, int]) -> Link:
            return model[0].get_link(model[1])

        def default(value_seen) -> Link:
            raise Exception(f"the node has an invalid type {value_seen.__class__}")

        return switch_case(node, {tuple: case_model, Link: case_link, None: default})

    def next(self):
        return self.child_node

    def build(self) -> JointModel:

        # from child_node, extract link or model in variable child_model_or_link
        assert self.child_node is not None
        child_model_or_link = self.child_node
        if isinstance(self.child_node, tuple):
            child_model_or_link = self.child_node[0]
        assert isinstance(child_model_or_link, (Link, Model))
        child_model_or_link.build()
        joint_type_characteristics = self._joint_type_characteristics_param.build()

        self.joint_model = JointModel(
          self._name_param,
          self._pose_param,
          self.get_node_link(self.parent_node).link_model,
          self.get_node_link(self.child_node).link_model,
          joint_type_characteristics,
        )
        return self.joint_model


# endregion


class Model:
    @init_with_deepcopy
    def __init__(  #pylint: disable=dangerous-default-value
      self,
      name: str,
      root_link: Link,
      linksInterface: List[Link] = [],
      pose=Pose(),
    ):

        self.name = name
        self.root_link = root_link
        self.links_interface = linksInterface
        self.pose = pose
        self.model = None
        self.parent_node = None

    def get_link(self, interface_nb: int):
        return self.links_interface[interface_nb]

    def set_parent(self, parent):
        self.parent_node = parent

    def build(self) -> ModelModel:
        self.root_link.build()

        links: List[LinkModel] = []
        joints: List[JointModel] = []
        nested_models: List[ModelModel] = []

        def next_model(model: Tuple[Model, int]) -> None:
            assert model[0].model is not None
            nested_models.append(model[0].model)

        def next_joint(joint: Joint) -> None:
            joints.append(cast(JointModel, joint.joint_model))
            switch_case(joint.child_node, {
              tuple: next_model, Link: next_link, None: lambda x: None
            })

        def next_link(link: Link) -> None:
            links.append(link.link_model)
            for joint in link.joints:
                next_joint(joint)

        next_link(self.root_link)

        # if no links were given, we supposed that the model is a tree
        # and that the root_link is an interface
        if self.links_interface == []:
            self.links_interface = [self.root_link]

        self.model = ModelModel(self.name,
                                links,
                                joints,
                                nested_models, {"default": [0. for joint in joints]})
        return self.model


class Node(ABC):
    @abstractmethod
    def next(self):
        pass


class World:
    def __init__(self, models):
        self.models = models


class MoveModel:
    def __init__(self, model: ModelModel):
        self.model = model

    def active_joints(self):
        return [joint for joint in self.model.joints if not isinstance(joint, FixedJointTypeModel)]
