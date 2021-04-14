from compas.datastructures import Datastructure
from compas.datastructures import Network
from compas.geometry import Transformation
from compas.geometry import Translation


class Assembly(Network):
    def __init__(self):
        super(Assembly, self).__init__()

    @property
    def approach_offset(self):
        return self.attributes['approach_offset']

    @approach_offset.setter
    def approach_offset(self, value):
        self.attributes['approach_offset'] = value

    @property
    def pick_t0cf_frame(self):
        return self.attributes['pick_t0cf_frame']

    @pick_t0cf_frame.setter
    def pick_t0cf_frame(self, frame):
        self.attributes['pick_t0cf_frame'] = frame.copy()

    def pick_t0cf_frames(self):
        if self.approach_offset:
            approach_frame = self.pick_t0cf_frame.copy()
            approach_frame.transform(Translation.from_vector([0, 0, self.approach_offset]))
            return [approach_frame, self.pick_t0cf_frame, approach_frame]

        return [self.pick_t0cf_frame]

    @property
    def pick_trajectory(self):
        return self.attributes['pick_trajectory']

    @pick_trajectory.setter
    def pick_trajectory(self, trajectory):
        self.attributes['pick_trajectory'] = trajectory

    def add_element(self, element, key=None, attr_dict={}, **kwattr):
        attr_dict.update(kwattr)
        x, y, z = element.frame.point
        key = self.add_node(key=key, attr_dict=attr_dict,
                            x=x, y=y, z=z, element=element)
        return key

    def element(self, key):
        return self.node[key]['element']

class Element(Datastructure):
    def __init__(self, frame=None, approach_frame=None, geometry_at_origin=None):
        super(Element, self).__init__()
        self.frame = frame
        self.approach_frame = approach_frame
        self.geometry_at_origin = geometry_at_origin
        self.trajectory = None

    @property
    def data(self):
        return dict(
            frame=self.frame,
            approach_frame=self.approach_frame,
            geometry_at_origin=self.geometry_at_origin,
            trajectory=self.trajectory,
        )

    @data.setter
    def data(self, data):
        self.frame = data['frame']
        self.approach_frame = data['approach_frame']
        self.geometry_at_origin = data['geometry_at_origin']
        self.trajectory = data['trajectory']

    @property
    def geometry_at_placement(self):
        T = Transformation.from_frame(self.frame)
        return self.geometry_at_origin.transformed(T)

