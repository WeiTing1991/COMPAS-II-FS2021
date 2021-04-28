import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Set max speed
    override = 100 # Unit [%]
    max_tcp = 2500 # Unit [mm/s]
    done = abb.send_and_wait(rrc.SetMaxSpeed(override, max_tcp))

    # Print feedback 
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
