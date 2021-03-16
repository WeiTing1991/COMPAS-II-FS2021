from compas_fab.backends import RosClient

with RosClient('localhost') as client:
    print('Connected:', client.is_connected)
