import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Set digital output high
    done = abb.send_and_wait(rrc.SetDigital('do_1',1))

    # Wait for a bit
    done = abb.send_and_wait(rrc.WaitTime(2))

    # Set digital output low
    done = abb.send_and_wait(rrc.SetDigital('do_1',0))
    
    # Wait for a bit
    done = abb.send_and_wait(rrc.WaitTime(2))

    # Pulse digital output high
    pulse_time = 2.5 # Unit [s]
    done = abb.send_and_wait(rrc.PulseDigital('do_1', pulse_time))

    # Print feedback 
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
