import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Read digital group input
    group_input = abb.send_and_wait(rrc.ReadGroup('gi_1'))

    # Print value 
    print('Group Input [gi_1] = ', group_input)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
