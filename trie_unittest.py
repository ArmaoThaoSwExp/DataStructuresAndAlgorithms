"""
Author: Armao Thao

Description:
    This file is a simple trie example.
"""
from test_utilities import compare_var, summarize_results, compare_arr_similar
from trie import TrieNode, make_trie, printtrie, find, insert, remove


if __name__ == "__main__":
    results = []
    temp = []
    print("####################################################")
    print("Test setup")
    triedict = {"a": 1,
                "ap": 2,
                "app": 4,
                "appl": 5,
                "apple": 6,
                "appp": 7,
                "apppl": 8,
                "appple": 9,
                "acpe": 10,
                "appel": 11}
    trietree = make_trie(**triedict)
    printtrie(trietree, temp)
    results.append(compare_arr_similar(temp, [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]))

    print("")
    print("####################################################")
    print("Test case 1: insert 100")
    temp = []
    insert(trietree, "z", 100)
    printtrie(trietree, temp)
    results.append(compare_arr_similar(temp, [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 100]))

    print("")
    print("####################################################")
    print("Test case 2: insert 1111 for an old key")
    temp = []
    insert(trietree, "app", 1111)
    printtrie(trietree, temp)
    results.append(compare_arr_similar(temp, [1, 2, 1111, 5, 6, 7, 8, 9, 10, 11, 100]))

    print("")
    print("####################################################")
    print("Test case 3: remove app")
    temp = []
    remove(trietree, "app")
    printtrie(trietree, temp)
    results.append(compare_arr_similar(temp, [1, 2, 5, 6, 7, 8, 9, 10, 11, 100]))

    print("")
    print("####################################################")
    print("Test case 4: remove non-existent")
    temp = []
    remove(trietree, "car")
    printtrie(trietree, temp)
    results.append(compare_arr_similar(temp, [1, 2, 5, 6, 7, 8, 9, 10, 11, 100]))

    print("")
    print("####################################################")
    print("Test case 5: remove another")
    temp = []
    remove(trietree, "appel")
    printtrie(trietree, temp)
    results.append(compare_arr_similar(temp, [1, 2, 5, 6, 7, 8, 9, 10, 100]))

    print("")
    print("####################################################")
    print("Test case 6: find ap")
    result = find(trietree, "ap")
    results.append(compare_var(result, 2, "=="))

    print("")
    print("####################################################")
    print("Test case 7: find apple")
    result = find(trietree, "apple")
    results.append(compare_var(result, 6, "=="))

    print("")
    print("####################################################")
    print("Test case 8: find appel (does not exist)")
    result = find(trietree, "appel")
    results.append(compare_var(result, None, "=="))

    print("")
    print("####################################################")
    print("Test case 9: find appple")
    result = find(trietree, "appple")
    results.append(compare_var(result, 9, "=="))

    summarize_results(results)