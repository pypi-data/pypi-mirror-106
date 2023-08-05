import subprocess
import os
import re
import simpleurdf
import shutil
from simpleurdf.urdf2model import ModelModel


class ModelIntegration:
    def __init__(self, model: ModelModel):
        self.model = model

    def _replace_model_in_template(file: str):
        replace_model = re.sub("<model>", self.model.name, file)

    def create_ros2_pkg(self, path2workspace: str, package_name: str):
        name_file = self.model.name + ".py"
        path_simpleurdf = simpleurdf.__path__[0]
        path_package = os.path.join(path2workspace, package_name)
        demo_launch_template_path = os.path.join(path_simpleurdf,
                                                 "createpackage",
                                                 "python_templates",
                                                 "demo.launch.py")
        state_publisher_template_path = os.path.join(path_simpleurdf,
                                                     "createpackage",
                                                     "python_templates",
                                                     "state_publisher.py")
        ros2_command_script = os.path.join(path_simpleurdf, "createpackage/ros2_command.sh")
        demo_launch_final_path = os.path.join(path_package, "launch", "demo.launch.py")
        state_publisher_final_path = os.path.join(path_package, package_name, "state_publisher.py")
        output = ""
        try:
            shutil.copy2(demo_launch_template_path, demo_launch_final_path)
        except subprocess.CalledProcessError as error:
            print(error.output)

        a = 8
