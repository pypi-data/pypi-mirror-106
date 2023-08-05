from typing import Callable, Dict, Optional, Type, cast, List
import functools

from lxml.builder import ElementMaker
from lxml.etree import ElementTree

from simpleurdf.utils.python_extension import switch_case

from simpleurdf.urdf2model.metamodel import (
  CollisionModel,
  ContinuousJointTypeModel,
  FixedJointTypeModel,
  FullPathUri,
  GeometryBoxModel,
  GeometryCylinderModel,
  GeometryTypes,
  InertialModel,
  JointModel,
  LimitModel,
  LinkModel,
  MaterialModel,
  MeshModel,
  ModelModel,
  PackageUri,
  PoseModel,
  PrismaticJointTypeModel,
  RevoluteJointTypeModel,
  VisualModel,
  JointTypeModelAvailable,
)


def _create_nothing_if_null_decorator(method):
    @functools.wraps(method)
    def create_nothing_if_null(self, fst_arg):
        if fst_arg is None:
            return None
        return method(self, fst_arg)

    return create_nothing_if_null


def _create_message_function(message: str):
    def raise_exception(obj):
        raise Exception(message)

    return raise_exception


def _remove_none_value(list_with_none):
    return [elem for elem in list_with_none if elem is not None]


class Urdf2ToUrdf:
    """This class builds a string containing a urdf definition of a robot
    defined using the urdf2 specification"""
    URDF_TYPE_JOINT_MAPPING = cast(
      Dict[Optional[Type], Callable[[JointModel], str]],
      {
        FixedJointTypeModel: lambda joint: "fixed",
        ContinuousJointTypeModel: lambda joint: "continuous",
        PrismaticJointTypeModel: lambda joint: "prismatic",
        RevoluteJointTypeModel: lambda joint: "revolute",
        None: _create_message_function("type was not found")
      })

    def __init__(self):
        self.em = ElementMaker()

    def create_pose(self, pose: PoseModel):
        x_position, y_position, z_position = pose.xyz
        r, p, y = pose.rpy
        return self.em.origin({
          "rpy": f"{r} {p} {y}", "xyz": f"{x_position} {y_position} {z_position}"
        })

    def create_robot(self, robot: ModelModel) -> ElementTree:
        all_links = []
        all_joints = []
        for model in robot.nested_models:
            all_links += model.links
            all_joints += model.joints
        all_links += robot.links
        all_joints += robot.joints

        links_urdf = []
        for link in all_links:
            links_urdf.append(self.create_link(link))
        joints_urdf = []
        for joint in all_joints:
            joints_urdf.append(self.create_joint(joint))
        final_urdf = _remove_none_value([{"name": robot.name}] + links_urdf + joints_urdf)
        return self.em.robot(*final_urdf)

    def create_link(self, link: LinkModel) -> ElementTree:
        return self.em.link(*_remove_none_value([
          {
            "name": link.name
          },
          self.create_collision(link.collision),
          *self.create_visual(link.visuals),
          self.create_inertial(link.inertial),
        ]))

    @_create_nothing_if_null_decorator
    def create_collision(self, collision: Optional[CollisionModel]):
        return self.em.collision(
          self.create_pose(collision.pose),
          self.create_geometry(collision.geometry),
        )

    def create_visual(self, visuals: List[VisualModel]):
        urdf_visuals = []
        for visual in visuals:
            urdf_visuals.append(
              self.em.visual(
                self.create_pose(visual.pose),
                self.create_geometry(visual.geometry),
                self.create_material(visual.material),
              ))
        return urdf_visuals

    def create_geometry(self, shape):
        def default(geometry):
            raise Exception(f"geometryModel not recognized, found {geometry.__class__}")

        assert len(GeometryTypes) == 3
        geometry = switch_case(
          shape,
          {
            MeshModel: self.create_mesh,
            GeometryBoxModel: self.create_box,
            GeometryCylinderModel: self.create_cylinder,
            None: default
          })
        return self.em.geometry(geometry)

    def create_mesh(self, shape: MeshModel):
        x_scale, y_scale, z_scale = shape.scale
        path = switch_case(
          shape.uri,
          {
            FullPathUri: lambda uri: uri.path,
            PackageUri: lambda uri: f"package://{uri.package}/{uri.path}"
          })
        return self.em.mesh({"filename": path, "scale": f"{x_scale:g} {y_scale:g} {z_scale:g}"})

    def create_box(self, shape: GeometryBoxModel):
        width, depth, length = shape.size
        return self.em.box({"size": f"{width:g} {depth:g} {length:g}"})

    def create_cylinder(self, shape: GeometryCylinderModel):
        return self.em.cylinder({"radius": str(shape.radius), "length": str(shape.length)})

    def create_material(self, material: MaterialModel):
        return self.em.material({"name": material.name})

    @_create_nothing_if_null_decorator
    def create_inertial(self, inertial: InertialModel):
        ixx, ixy, ixz, iyy, iyz, izz = inertial.inertia
        return self.em.inertial(
          self.create_pose(inertial.pose),
          self.em.mass({"value": f"{inertial.mass:g}"}),
          self.em.inertia({
            "ixx": f"{ixx:g}",
            "ixy": f"{ixy:g}",
            "ixz": f"{ixz:g}",
            "iyy": f"{iyy:g}",
            "iyz": f"{iyz:g}",
            "izz": f"{izz:g}",
          }),
        )

    def create_joint(self, joint) -> ElementTree:
        def default(joint_characteristics):
            raise Exception(f"JointType not recognized, found {joint_characteristics.__class__}")

        # _used to add to the xml axis and limit if it makes sense for the joint
        assert len(JointTypeModelAvailable) == 4
        joint_type_related_attributes = switch_case(
          joint.joint_characteristics,
          {
            FixedJointTypeModel:
            lambda joint_characteristics: [],
            PrismaticJointTypeModel:
            lambda joint_characteristics: [
              self.create_axis(joint_characteristics.translation_axis),
              self.create_limit(joint_characteristics.limit),
            ],
            ContinuousJointTypeModel:
            lambda joint_characteristics: [self.create_axis(joint_characteristics.rotation_axis)],
            RevoluteJointTypeModel:
            lambda joint_characteristics: [
              self.create_axis(joint_characteristics.rotation_axis),
              self.create_limit(joint_characteristics.limit),
            ],
            None:
            default
          })

        return self.em.joint(
          {
            "name": joint.name,
            "type": switch_case(joint.joint_characteristics, Urdf2ToUrdf.URDF_TYPE_JOINT_MAPPING),
          },
          *joint_type_related_attributes,
          self.create_pose(joint.pose),
          self.em.parent({"link": joint.parent.name}),
          self.em.child({"link": joint.child.name}),
        )

    def create_axis(self, axis: List[float]):
        x, y, z = axis
        return self.em.axis({"xyz": f"{x:g} {y:g} {z:g}"})

    def create_limit(self, limit: LimitModel):
        return self.em.limit({
          "lower": f"{limit.lower:g}",
          "upper": f"{limit.upper:g}",
          "effort": f"{limit.effort:g}",
          "velocity": f"{limit.velocity:g}",
        })
