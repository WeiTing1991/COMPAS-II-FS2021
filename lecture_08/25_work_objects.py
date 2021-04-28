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

    # Set tool
    abb.send(rrc.SetTool('t_RRC_Vacuum_Gripper'))

    # Define pick positions
    frame_on_pick = Frame(Point(50, 50, 50), Vector(0, -1, 0), Vector(-1, 0, 0))
    frame_on_place = Frame(Point(50, 50, 50), Vector(0, -1, 0), Vector(-1, 0, 0))

    # Define speeds
    speed = 100

    # Move to frame on pickup pallet (work object)
    abb.send(rrc.SetWorkObject('ob_RRC_Brick_Pallet'))
    abb.send_and_wait(rrc.MoveToFrame(frame_on_pick, speed, rrc.Zone.FINE))


    # Move to frame on place (work object)
    abb.send(rrc.SetWorkObject('ob_RRC_Build_Space'))
    abb.send_and_wait(rrc.MoveToFrame(frame_on_place, speed, rrc.Zone.FINE))

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
