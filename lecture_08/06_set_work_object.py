import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Set work object
    done = abb.send_and_wait(rrc.SetWorkObject('wobj0'))

    # Print feedback
    print('Feedback = ', done)
        
    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
