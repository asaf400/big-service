class counter:
    # initialize class attribute
    count = 0

    # on new instance
    def __init__(self):
        # set class attribute count to itself +1
        counter.count += 1
        pass

    def get_count(self):
        # return class attribute
        return counter.count
