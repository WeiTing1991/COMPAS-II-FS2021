import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Print before
    abb.send(rrc.PrintText('RRC will wait 1 second'))

    # Wait time for robot cotroller
    time = 1.0
    abb.send(rrc.WaitTime(time))

    # Print after
    done = abb.send_and_wait(rrc.PrintText('Waiting time completed'))

    # Print feedback
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
