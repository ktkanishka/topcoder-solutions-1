from functools import reduce

class ANDEquation(object):
    def restoreY(self, A):
        for index in xrange(len(A)):
            and_result = reduce(lambda x, y: x & y, A[:index] + A[index + 1:])
            if and_result == A[index]:
                return and_result
        return -1
