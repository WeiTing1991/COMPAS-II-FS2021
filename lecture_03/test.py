from compas_rhino.artists import RobotModelArtist
from compas_rhino.artists import FrameArtist
from compas.robots import RobotModel
urdf = """<?xml version="1.0"?>
<robot name="origins">
 <link name="base">
   <visual>
     <geometry>
       <cylinder length="0.6" radius="0.1"/>
     </geometry>
     <origin rpy="0 0 0" xyz="0 0 0.3"/>
   </visual>
 </link>
 <link name="link_1">
   <visual>
     <geometry>
       <capsule start="0 0 0" end="0 0 10" radius="0.07"/>
     </geometry>
     <origin rpy="0 0 0" xyz="0 0 0.3"/>
   </visual>
 </link>
 <link name="link_2">
   <visual>
     <geometry>
       <sphere radius="0.04"/>
     </geometry>
     <origin rpy="0 0 0" xyz="0 0 0.3"/>
   </visual>
 </link>
 <joint name="joint_1" type="fixed">
   <parent link="base"/>
   <child link="link_1"/>
   <origin xyz="0 0 0.6"/>
 </joint>
 <joint name="joint_2" type="fixed">
   <parent link="link_1"/>
   <child link="link_2"/>
   <origin xyz="0 0 0.6"/>
 </joint>
</robot>
"""
model = RobotModel.from_urdf_string(urdf)
artist = RobotModelArtist(model, layer='COMPAS::Robot Viz')
artist.clear_layer()
artist.draw_visual()
print model.get_configurable_joints()
for frame in model.transformed_frames(dict()):
    fartist = FrameArtist(frame, layer='COMPAS::Robot Viz', scale=0.04)
    fartist.draw()

