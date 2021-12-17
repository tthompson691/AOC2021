from utils import read_input
import numpy as np
import networkx as nx


def get_neighbors(pos):
    i = pos[0]
    j = pos[1]
    nu = nd = nl = nr = None
    # up
    if i > 0:
        nu = (i - 1, j)
    # down
    if i < cavern.shape[0] - 1:
        nd = (i + 1, j)
    # left
    if j > 0:
        nl = (i, j - 1)
    # right
    if j < cavern.shape[1] - 1:
        nr = (i, j + 1)
    return [neighbor for neighbor in [nu, nd, nl, nr] if neighbor is not None]


def risk(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


if __name__ == "__main__":
    cavern_list = [list(map(int, i)) for i in read_input("day15_input.txt")]
    cavern = np.array(cavern_list)
    G = nx.DiGraph()
    # populate nodes
    for i, x in enumerate(cavern_list):
        for j, y in enumerate(x):
            G.add_node((i, j))

    # populate edges
    for node in G.nodes:
        neighbors = get_neighbors(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor, weight=cavern[neighbor] + cavern[node])

    a = nx.astar_path(
        G,
        (0, 0),
        (cavern.shape[0] - 1, cavern.shape[1] - 1),
        heuristic=risk,
        weight="weight",
    )

    risk_total = 0
    for g in a[1:]:
        risk_total += cavern[g]

    print(f"part 1: {risk_total}")
