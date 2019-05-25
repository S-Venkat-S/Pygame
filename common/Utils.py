

class Utils:

    def __init__(self):
        pass

    @staticmethod
    def is_collide(x1, y1, w1, h1, x2, y2, w2, h2, recur=False):
        if (x2 <= x1 <= (x2 + w2)) and (y2 <= y1 <= (y2 + h2)):
            return True
        elif (x2 <= (x1 + w1) <= (x2 + w2)) and (y2 <= y1 <= (y2 + h2)):
            return True
        elif (x2 <= x1 <= (x2 + w2)) and (y2 <= (y1 + h1) <= (y2 + h2)):
            return True
        elif (x2 <= (x1 + w1) <= (x2 + w2)) and (y2 <= (y1 + h1) <= (y2 + h2)):
            return True
        elif not recur:
            return Utils.is_collide(x2, y2, w2, h2, x1, y1, w1, h1, True)
        return False
