"""
Author: Armao Thao

Description:
    This is a simple program to implement a depth first search of a graph.
"""
from test_utilities import compare_var, summarize_results, compare_arr_similar
from depthfirstsearch import DfsNode, dfs, dfs_print


if __name__ == "__main__":
    runtime = []
    results = []
    print("")
    print("####################################################")
    print("Test Setup")
    print("Create nodes A, B, C, D, E, and F")
    nodea = DfsNode('A')
    nodeb = DfsNode('B')
    nodec = DfsNode('C')
    noded = DfsNode('D')
    nodee = DfsNode('E')
    nodef = DfsNode('F')
    print("Node A children: B, C")
    nodea.adjacent_nodes = [nodeb, nodec]
    print("Node B children: A, D, E")
    nodeb.adjacent_nodes = [nodea, noded, nodee]
    print("Node C children: A, F")
    nodec.adjacent_nodes = [nodea, nodef]
    print("Node D children: B")
    noded.adjacent_nodes = [nodeb]
    print("Node E children: B, F")
    nodee.adjacent_nodes = [nodeb, nodef]
    print("Node F children: C, E")
    nodef.adjacent_nodes = [nodec, nodee]
    print("####################################################")

    print("")
    print("####################################################")
    print("Test 1")
    print("\nFind node 'A' in graph")
    result = dfs(nodea, "A")
    result = compare_var(result, True, "==")
    results.append(result)
    print("####################################################")

    print("")
    print("####################################################")
    print("Test 2")
    print("\nFind node 'B' in graph")
    result = dfs(nodea, "B")
    result = compare_var(result, True, "==")
    results.append(result)
    print("####################################################")

    print("")
    print("####################################################")
    print("Test 3")
    print("\nFind node 'C' in graph")
    result = dfs(nodea, "C")
    result = compare_var(result, True, "==")
    results.append(result)
    print("####################################################")

    print("")
    print("####################################################")
    print("Test 4")
    print("\nFind node 'D' in graph")
    result = dfs(nodea, "D")
    result = compare_var(result, True, "==")
    results.append(result)
    print("####################################################")

    print("")
    print("####################################################")
    print("Test 5")
    print("\nFind node 'E' in graph")
    result = dfs(nodea, "E")
    result = compare_var(result, True, "==")
    results.append(result)
    print("####################################################")

    print("")
    print("####################################################")
    print("Test 6")
    print("\nFind node 'F' in graph")
    result = dfs(nodea, "F")
    result = compare_var(result, True, "==")
    results.append(result)
    print("####################################################")

    print("")
    print("####################################################")
    print("Test 7")
    print("\nFind node 'G' in graph")
    result = dfs(nodea, "G")
    result = compare_var(result, False, "==")
    results.append(result)
    print("####################################################")

    print("")
    print("####################################################")
    print("Test 8")
    print("\nFind node 'M' in graph")
    result = dfs(nodea, "M")
    result = compare_var(result, False, "==")
    results.append(result)
    print("####################################################")

    print("")
    print("####################################################")
    print("Test 9")
    print("\nFind node 'Z' in graph")
    result = dfs(nodea, "Z")
    result = compare_var(result, False, "==")
    results.append(result)
    print("####################################################")

    print("")
    print("####################################################")
    print("Test 10")
    print("\nFind node '-' in graph")
    result = dfs(nodea, "-")
    result = compare_var(result, False, "==")
    results.append(result)
    print("####################################################")

    print("")
    print("####################################################")
    print("Test 11")
    print("\nFind node '9' in graph")
    result = dfs(nodea, "9")
    result = compare_var(result, False, "==")
    results.append(result)
    print("####################################################")

    print("")
    print("####################################################")
    print("Test 12")
    print("Print all nodes")
    result = dfs_print(nodea, returnresult=True)
    result = compare_arr_similar(result, ['A', 'B', 'C', 'D', 'E', 'F'])
    results.append(result)
    print("####################################################")

    summarize_results(results)
