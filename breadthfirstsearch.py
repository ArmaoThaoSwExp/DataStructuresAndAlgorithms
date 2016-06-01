"""
Author: Armao Thao

Description:
    This is a simple program to implement a breadth first search of a graph.
"""


class BfsNode(object):
    def __init__(self, value, adjacent_nodes=None):
        self.value = value
        if adjacent_nodes is None:
            adjacent_nodes = []
        self.adjacent_nodes = adjacent_nodes


def bfs(rootnode, value):
    visited_nodes = []
    search_queue = [rootnode]
    while search_queue:
        curr = search_queue.pop(0)
        if curr not in visited_nodes:
            visited_nodes.append(curr)
            if curr.value == value:
                return True
            for node in curr.adjacent_nodes:
                if node not in visited_nodes:
                    search_queue.append(node)
    return False


def bfs_print(rootnode, returnresult=False):
    visited_nodes = []
    search_queue = [rootnode]
    result = [] if returnresult else None
    while search_queue:
        curr = search_queue.pop(0)
        if curr not in visited_nodes:
            visited_nodes.append(curr)
            print(curr.value)
            if returnresult:
                result.append(curr.value)
            for node in curr.adjacent_nodes:
                if node not in visited_nodes:
                    search_queue.append(node)
    return result if returnresult else None


if __name__ == "__main__":
    print("Breadth first search")

