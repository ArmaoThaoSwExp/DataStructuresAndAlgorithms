"""
Author: Armao Thao

Description:
    This is a simple program to implement a depth first search of a graph.
"""


class DfsNode(object):
    def __init__(self, value, adjacent_nodes=None):
        adjacent_nodes = [] if adjacent_nodes is None else adjacent_nodes
        assert isinstance(adjacent_nodes, list), "adjacent_nodes must be a list"
        self.value = value
        self.adjacent_nodes = adjacent_nodes


def dfs(rootnode, value):
    assert isinstance(rootnode, DfsNode), "rootnode must be of type DfsNode"
    visited_nodes = []
    search_stack = [rootnode]
    while search_stack:
        curr = search_stack.pop()
        visited_nodes.append(curr)
        if curr.value == value:
            return True
        for node in curr.adjacent_nodes:
            if node not in visited_nodes:
                search_stack.append(node)
    return False


def dfs_print(rootnode, returnresult=False):
    assert isinstance(rootnode, DfsNode), "rootnode must be of type DfsNode"
    visited_nodes = []
    search_stack = [rootnode]
    if returnresult:
        result = []
    while search_stack:
        curr = search_stack.pop()
        if curr not in visited_nodes:
            print(curr.value)
            if returnresult:
                result.append(curr.value)
            visited_nodes.append(curr)
            for node in curr.adjacent_nodes:
                if node.value not in visited_nodes:
                    search_stack.append(node)
    return result if returnresult else None


if __name__ == "__main__":
    print("Depth First Search")

