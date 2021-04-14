import functools
import random

from compas.geometry import Box

# random but repeatable ;)
random.seed(2666)

@functools.total_ordering
class BoxComparer(object):
    def __init__(self, box, *args):
        self.box = box

    def __eq__(self, other):
        return self.box.data == other.box.data

    def __lt__(self, other):
        return self.box.dimensions < other.box.dimensions

bricks = set()

for i in range(10):
    w, h, d = random.random(), random.random(), random.random()
    brick = Box.from_width_height_depth(w, h, d)
    bricks.add(brick)

print('No sorting guaranteed (depends on implementation)')
for b in bricks:
    print('{:.3f}, {:.3f}, {:.3f}'.format(*b.dimensions))
print()

print('Defined total ordering')
for b in sorted(bricks, key=BoxComparer):
    print('{:.3f}, {:.3f}, {:.3f}'.format(*b.dimensions))
