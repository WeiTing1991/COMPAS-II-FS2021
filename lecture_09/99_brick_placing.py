import compas_rrc as rrc
from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Vector

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient('ros-vzby-dzht.yaler.io', port=80)
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Reset signals
    abb.send(rrc.SetDigital('doUnitC106Out2',0))

    # Set tool
    abb.send(rrc.SetTool('t_RRC_Vacuum_Gripper'))

    # Set work object
    abb.send(rrc.SetWorkObject('wobj0'))

    # Define pick position
    approach_pick_frame = Frame(Point(300.0, 520.0, 90), Vector(0, -1, 0), Vector(-1, 0, 0))
    pick_frame = Frame(Point(300.0, 520.0, 32.3), Vector(0, -1, 0), Vector(-1, 0, 0))

    # Define place positions
    approach_place_frame = Frame(Point(0, 415, 90), Vector(0, -1, 0), Vector(-1, 0, 0))
    place_frame = Frame(Point(0, 415, 33.0), Vector(0, -1, 0), Vector(-1, 0, 0))

    # Define speed
    speed = 50

    # Move over pick position
    abb.send(rrc.MoveToFrame(approach_pick_frame, speed, rrc.Zone.Z10))

    # Move to pick position
    abb.send(rrc.MoveToFrame(pick_frame, speed, rrc.Zone.FINE))

    # Vacuum on
    abb.send(rrc.SetDigital('doUnitC106Out2',1))

    # Move over pick position
    abb.send(rrc.MoveToFrame(approach_pick_frame, speed, rrc.Zone.Z10))

    # Move over place position
    abb.send(rrc.MoveToFrame(approach_place_frame, speed, rrc.Zone.Z10))

    # Move to place position
    abb.send_and_wait(rrc.MoveToFrame(place_frame, speed, rrc.Zone.FINE))

    # Vacuum off
    abb.send_and_wait(rrc.SetDigital('doUnitC106Out2',0))

    # Move over place position
    abb.send(rrc.MoveToFrame(approach_place_frame, speed, rrc.Zone.Z10))

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
