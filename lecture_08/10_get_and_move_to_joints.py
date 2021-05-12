import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Read value of joints
    robot_joints, external_axes = abb.send_and_wait(rrc.GetJoints())

    # Print received values
    print(robot_joints, external_axes)

    # Change a joint value [°]
    robot_joints.rax_1 += 15 

    # Set speed [mm/s]
    speed = 100
    
    # Move robot the new pos
    done = abb.send_and_wait(rrc.MoveToJoints(robot_joints, external_axes, speed, rrc.Zone.FINE))

    # Print feedback 
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
