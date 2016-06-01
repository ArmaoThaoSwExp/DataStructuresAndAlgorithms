"""
Author: Armao Thao

Description:
    This file is a simple trie example.
"""


class TrieTypeError(Exception):
    pass


class TrieNode(object):
    def __init__(self, value=None, children=None):
        children = {} if children is None else children
        assert isinstance(children, dict), \
            "Children must be of type dictionary or None, but received type {0}".format(type(children))
        self.value = value
        self.children = children


def make_trie(**words):
    """
    Word is a dictionary that has keys and values.

    :param words:
    :return:
    """
    root = TrieNode()
    for word in words:
        insert(root, word, words[word])
    return root

def printtrie(node, returnresult=False):
    assert isinstance(returnresult, list) or isinstance(returnresult, bool) or isinstance(returnresult, None), \
        "returnresult must be one of the following types: list, None or False" \
        "\nInstead, received type {0}".format(type(returnresult))

    if not node:
        return

    if node.value:
        print(node.value)
        if isinstance(returnresult, list):
            returnresult.append(node.value)

    for child in node.children:
        printtrie(node.children[child], returnresult=returnresult)


def find(node, key):
    assert isinstance(node, TrieNode) or node is None, \
        "node must be of type TrieNode, but received type {0}".format(type(node))
    assert isinstance(key, str), "node must be of type string, but received type {0}".format(type(key))
    if node is None:
        return False
    for child in node.children:
        if key[0] == child:
            if len(key) == 1:
                return node.children[child].value
            return find(node.children[child], key[1:])
    return False


def insert(node, key, value):
    assert isinstance(node, TrieNode) or node is None, \
        "node must be of type TrieNode, but received type {0}".format(type(node))
    assert isinstance(key, str), "node must be of type string, but received type {0}".format(type(key))
    if node is None:
        return

    for child in node.children:
        if key[0] == child:
            if len(key) == 1:
                node.children[child].value = value
            else:
                insert(node.children[child], key=key[1:], value=value)
            return
    node.children[key[0]] = TrieNode()
    if len(key) == 1:
        node.children[key[0]].value = value
    elif len(key) > 1:
        insert(node.children[key[0]], key=key[1:], value=value)


def remove(node, key):
    assert isinstance(node, TrieNode) or node is None, \
        "node must be of type TrieNode, but received type {0}".format(type(node))
    assert isinstance(key, str), "node must be of type string, but received type {0}".format(type(key))

    if not node:
        return

    for child in node.children:
        if key[0] == child:
            if len(key) == 1:
                node.children[child].value = None
                return True
            else:
                return remove(node.children[child], key=key[1:])
    return False


if __name__ == "__main__":
    print("Trie test!")
