def construct_z_array(string):
    z_array = [0 for _ in string]
    for i in xrange(1, len(string)):
        j = i
        k = 0
        while j < len(string) and string[k] == string[j]:
            j += 1
            k += 1
        z_array[i] = j - i
    return z_array

def construct_z_array_efficiently(string):
    z_array = [0 for _ in string]
    left, right = 0, 0
    for i in xrange(1, len(string)):
        if i >= right:
            j = i
            k = 0
            while j < len(string) and string[k] == string[j]:
                j += 1
                k += 1
            length = j - i
            z_array[i] = length
            if length > 0:
                left = i
                right = left + length - 1
        else:
            k = min(right - i, z_array[i - left]) 
            j = i + k
            length = 1 if string[k] == string[j] else 0
            while j < len(string) and string[k] == string[j]:
                j += 1
                k += 1
            length = j - i
            z_array[i] = length
            if length > 0:
                left = i
                right = left + length - 1
    return z_array
