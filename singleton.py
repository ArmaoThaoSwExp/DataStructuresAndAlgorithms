"""
Author: Armao Thao

Description:
    An example singleton design pattern.
"""


class AppleSingleton(object):
    instance = None

    @classmethod
    def getinstance(cls):
        if cls.instance is None:
            cls.instance = AppleSingleton()
        return cls.instance

    def printapple(self):
        print("Apple!")


if __name__ == "__main__":
    print("Singleton design pattern")