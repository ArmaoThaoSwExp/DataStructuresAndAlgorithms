__author__ = 'Armao'

"""

"""


def permutate(in_str):
    result = []

    if len(in_str) <= 1:
        return [in_str]

    perms = permutate(in_str[1:])

    # For all the items from the sub permutate list,
    # we need to insert element 0 into each different position
    for perm in perms:
        for i in range(len(in_str)):
            result.append(perm[:i] + in_str[0:1] + perm[i:])
    return result


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]



if __name__ == '__main__':
    print permutate([1, 2, 3])
    print permutate([1, 2, 3, 4, 5])
    print sorted(permutate('abcde'))
    print permutate('')

    # for i in all_perms([1, 2, 3]):
    #     print i