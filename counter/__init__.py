class counter:
    count = 0

    def __init__(self):
        counter.count += 1
        pass

    def get_count(self):
        return counter.count
