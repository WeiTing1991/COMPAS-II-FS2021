import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Send and defer waiting
    future = abb.send(rrc.PrintText('Send instructions to the robot and check the feedack later.',feedback_level=rrc.FeedbackLevel.DONE))

    # Here you can execute other operations
    print('Execute other code.')

    # Wait for feedback
    done = future.result(timeout=3.0)

    # Print feedback
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
