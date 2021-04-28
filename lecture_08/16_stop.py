import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Stop the motion tast
    future = abb.send(rrc.Stop(feedback_level=rrc.FeedbackLevel.DONE))

    # Execute other code
    print('Press Play on the FlexPendant to continue.')

    # Wait for future feedback
    done = future.result()

    # Print feedback
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
