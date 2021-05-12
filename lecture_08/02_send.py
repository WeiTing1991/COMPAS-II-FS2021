import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Send an instruction without waiting for any kind of feedback
    abb.send(rrc.PrintText('Hello.'))

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
