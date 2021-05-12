import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Read analog input
    analog_input = abb.send_and_wait(rrc.ReadAnalog('ai_1'))

    # Print value
    print('Analog Input [ai_1] = ', round(analog_input, 3))

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
