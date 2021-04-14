from functools import partial

import compas_rhino

from compas.utilities import color_to_colordict

colordict = partial(color_to_colordict, colorformat='rgb', normalize=False)

def draw_directed_edges(artist, edges=None, color=None):
    node_xyz = artist.node_xyz
    edges = edges or list(artist.network.edges())
    edge_color = colordict(color, edges, default=artist.color_edges)
    lines = []
    for edge in edges:
        lines.append({
            'start': node_xyz[edge[0]],
            'end': node_xyz[edge[1]],
            'color': edge_color[edge],
            'arrow': 'end',
            'name': "{}.edge.{}-{}".format(artist.network.name, *edge)})
    return compas_rhino.draw_lines(lines, layer=artist.layer, clear=False, redraw=False)

