import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Read digital input
    digital_input = abb.send_and_wait(rrc.ReadDigital('di_1'))

    # Print value 
    print('Digital Input [di_1] = ', digital_input)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
