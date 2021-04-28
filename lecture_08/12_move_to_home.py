import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Set start values
    robot_joints, external_axes = [90, 90, 0, 0],  []

    # Move robot to start position
    done = abb.send_and_wait(rrc.MoveToJoints(robot_joints, external_axes, 1000, rrc.Zone.FINE))

    # Print feedback
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
