
def create_string(current_string, N, K, num_B, num_C):
    if N <= 0:
        raise Exception('Length of string must be >= 1')
    if N == 1:
        if num_B + num_C == K:
            return 'A' + current_string
        elif num_C == K:
            return 'B' + current_string
        else:
            return ''
    else:
        result_A = create_string('A' + current_string, N - 1, K - num_B - num_C, num_B, num_C)
        if result_A:
            return result_A
        else:
             result_B = create_string('B' + current_string, N - 1, K - num_C, num_B + 1, num_C)
             if result_B:
                 return result_B
             else:
                result_C = create_string('C' + current_string, N - 1, K, num_B, num_C + 1)
                return result_C

class ABC(object):
    def createString(self, N, K):
        return create_string('', N, K, 0, 0)
