from compas_fab.backends import RosClient

with RosClient() as client:
    client.reset_planning_scene()

