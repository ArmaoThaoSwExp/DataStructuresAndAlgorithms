"""
Author: Armao Thao

Description:
    Tower of Hanoi
        There are 3 pegs: source, the helper, and the target
        The goal is to move all disks from the source peg to the target peg using the helper as needed.
        For any given n disks, its takes (2^n - 1) moves to complete the task.

    Algorithm
        For each given disk
            move the top disk from source to the helper peg,
            then move the next disk from source to dest,
            finally, move the disk from the helper peg to the dest

"""


def hanoi(disc, source, destination, helper, totalmoves=1):
    """
    :param disc: total discs on the source peg
    :param source: the source peg.
        Must be in the following format:
            ([list of discs], "name to help with debugging")
    :param destination: the destination peg.
        Must be in the following format:
            ([list of discs], "name to help with debugging")
    :param helper: the helper peg.
        Must be in the following format:
            ([list of discs], "name to help with debugging")
    :param totalmoves: keeps track of number of moves performed.
    """
    # If disc is not empty
    if disc > 0:
        # Move the top disc from the source to the helper peg
        totalmoves = hanoi(disc - 1, source, helper, destination, totalmoves=totalmoves)

        # If source is not empty, move the top disc from the source to the target
        if source[0]:
            disc = source[0].pop()
            destination[0].append(disc)
            print("\t[Step {0}]Move {1} from {2} to {3}".format(totalmoves, disc, source[1], destination[1]))
        totalmoves += 1

        # Move the disc from the helper to the destination peg
        totalmoves = hanoi(disc - 1, helper, destination, source, totalmoves=totalmoves)

    return totalmoves


if __name__ == "__main__":
    print("Tower of Hanoi")
    source = ([i for i in range(6, 0, -1)], "source")  # from 10..1
    destination = ([], "destination")
    helper = ([], "helper")

    print("source\t\tdestination\t\thelper")
    print(str(source) + "\t\t" + str(destination) + "\t\t" + str(helper))
    totalmoves = hanoi(len(source[0]), source, destination, helper)
    print(str(source) + "\t\t" + str(destination) + "\t\t" + str(helper))
    print("Total moves: {0}".format(totalmoves))
