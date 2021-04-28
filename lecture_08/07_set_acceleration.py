import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Set acceleration
    acc = 100 # Unit [%]
    ramp = 100  # Unit [%]
    done = abb.send_and_wait(rrc.SetAcceleration(acc, ramp))

    # Print feedback 
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
