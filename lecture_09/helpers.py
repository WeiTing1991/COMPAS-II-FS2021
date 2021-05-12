from __future__ import print_function
import time

from compas.topology import breadth_first_ordering


class Rate(object):
    def __init__(self, hz):
        self.hz = hz
        self.last_time = time.time_ns()
        self.sleep_duration = int(1e9 / hz)

    def sleep(self):
        t1 = time.time_ns()
        elapsed = t1 - self.last_time
        sleep_ns = (self.sleep_duration - elapsed)
        if sleep_ns > 0:
            time.sleep(sleep_ns / 1e9)
        self.last_time = self.last_time + self.sleep_duration


def traversal_linearly_ordered(assembly):
    return sorted(assembly.nodes())


def traversal_breadth_first_ordering(assembly):
    root = assembly.leaves()[0]
    return breadth_first_ordering(assembly.adjacency, root)


def traversal_buildup_sequence(assembly):
    visited = set()
    elements = []
    for key in assembly.nodes():
        if assembly.degree_out(key) == 0:
            get_dependencies(assembly, key, elements, visited)

    return list(reversed(elements))


def get_dependencies(assembly, key, elements, visited):
    if key not in visited:
        elements.append(key)
        visited.add(key)
    for n in assembly.neighbors_in(key):
        get_dependencies(assembly, n, elements, visited)
