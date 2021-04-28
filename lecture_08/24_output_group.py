import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Set analog 
    done = abb.send_and_wait(rrc.SetAnalog('ao_1', -3.33))

    # Set digital
    done = abb.send_and_wait(rrc.SetDigital('do_1',1))

    

    # Pulse digital 
    pulse_time = 2.5 # Unit [s]
    done = abb.send_and_wait(rrc.PulseDigital('do_1', pulse_time))

    # Set group
    done = abb.send_and_wait(rrc.SetGroup('go_1', 33))

    # Print feedback 
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
