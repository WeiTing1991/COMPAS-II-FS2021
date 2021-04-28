# COMPAS II: Robot control with COMPAS RRC

Online non-real time control of industrial robots.

Components of an RRC deployment.

Communication primitives (blocking, futures, cyclic).

Instructions.

Multi controller & location coordination.

👉 [Slides](lecture_08.pdf)

## Examples

Before running this examples, you have to:

1. Install [ABB RobotStudio](https://new.abb.com/products/robotics/robotstudio) (see [more installation notes here](https://github.com/compas-rrc/compas_rrc_start#robotstudio))
2. Install [SCARA RRC IRB910SC robot station](https://github.com/compas-rrc/compas_rrc_start/blob/main/robotstudio-stations/COMPAS_RRC_IRB-910SC-3_0.65.rspag) (`Pack&Go .rspag` files are installed simply by opening them from RobotStudio).
3. Start (`compose up`) the [RRC driver container](../docker/rrc_virtual_controller/docker-compose.yml)

* Communication
  * [Hello World](01_hello_world.py)
  * [Send instruction](02_send.py)
  * [Send instruction with feedback (blocking)](03_send_and_wait.py)
  * [Send instruction with deferred feedback (non-blocking)](04_send_and_wait_in_the_future.py)

* Basic setup
  * [Set tool](05_set_tool.py)
  * [Set work object](06_set_work_object.py)
  * [Set acceleration](07_set_acceleration.py)
  * [Set max speed](08_set_max_speed.py)

* Motion instructions
  * [Get/Move to frame](09_get_and_move_to_frames.py)
  * [Get/Move to joints (Configuration)](10_get_and_move_to_joints.py)
  * [Get/Move to Robtarget](11_get_and_move_to_robtarget.py)
  * [Move to home configuration](12_move_to_home.py)

* Utilities
  * [No-op/ping](13_no-op.py)
  * [Print Text on flex pendant](14_print_text.py)
  * [Wait time](15_wait_time.py)
  * [Stop/Pause program](16_stop.py)
  * [Stopwatch on the robot](17_watch.py)
  * [Custom instruction](18_custom_instruction.py)

* Input/Output signals
  * [Read analog input](19_input_analog.py)
  * [Read digital input](20_input_digital.py)
  * [Read group input](21_input_group.py)
  * [Set analog output](22_output_analog.py)
  * [Set digital output](23_output_digital.py)
  * [Set group output](24_output_group.py)
  
* Brick assembly
  * [Work objects](25_work_objects.py)
  * [Pick and Place bricks](26_brick_placing.py)
