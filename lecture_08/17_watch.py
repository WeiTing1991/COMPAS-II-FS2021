import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Start watch on robot controller
    abb.send(rrc.StartWatch())

    # Add a wait time of 1.6 seconds
    abb.send(rrc.WaitTime(1.6))

    # Stop watch on robot controller
    abb.send(rrc.StopWatch())

    # Read time from watch on robot controller
    watch_time = abb.send_and_wait(rrc.ReadWatch())

    # Print robot watch time
    print('Time [s] = ', watch_time)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
