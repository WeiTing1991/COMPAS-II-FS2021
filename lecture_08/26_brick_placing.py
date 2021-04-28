import compas_rrc as rrc
from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Vector

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Reset signals
    abb.send(rrc.SetDigital('doNewBrick',0))
    abb.send(rrc.SetDigital('doVacuumOn',0))

    # Set tool
    abb.send(rrc.SetTool('t_RRC_Vacuum_Gripper'))

    # Set work object
    abb.send(rrc.SetWorkObject('ob_RRC_Brick_Pallet'))

    # Create a new brick
    done = abb.send_and_wait(rrc.PulseDigital('doNewBrick',0.2))

    # Define pick positions
    pre_pick_position = Frame(Point(68.5, 48.5, 50), Vector(0, -1, 0), Vector(-1, 0, 0))
    pick_position = Frame(Point(68.5, 48.5, 36), Vector(0, -1, 0), Vector(-1, 0, 0))

    # Define speeds
    speed = 100

    # Move over pick postion
    abb.send(rrc.MoveToFrame(pre_pick_position, speed, rrc.Zone.Z10))

    # Move to pick postion
    abb.send(rrc.MoveToFrame(pick_position, speed, rrc.Zone.FINE))

    # Vacuum on
    abb.send(rrc.SetDigital('doVacuumOn',1))

    # Move over pick postion
    abb.send(rrc.MoveToFrame(pre_pick_position, speed, rrc.Zone.Z10))

    # Set work object
    abb.send(rrc.SetWorkObject('ob_RRC_Build_Space'))

    # Define pick positions
    pre_place_position = Frame(Point(150, 50, 50), Vector(0, -1, 0), Vector(-1, 0, 0))
    place_position = Frame(Point(150, 50, 12), Vector(0, -1, 0), Vector(-1, 0, 0))

    # Move over place postion
    abb.send(rrc.MoveToFrame(pre_place_position, speed, rrc.Zone.Z10))

    # Move to place postion
    abb.send(rrc.MoveToFrame(place_position, speed, rrc.Zone.FINE))

    # Vacuum off
    abb.send(rrc.SetDigital('doVacuumOn',0))

    # Move over place postion
    abb.send(rrc.MoveToFrame(pre_place_position, speed, rrc.Zone.Z10))

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
