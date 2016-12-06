class RepeatedStrings(object):
    def findKth(self, string, k):
        pass
'''
This just checks if string is valid. 
We still need to figure out how to store and retrieve valid strings
'''
def is_valid_string(string):
    left_paren, right_paren = string[0], string[len(string) - 1]
    if left_paren == '(' and right_paren == ')':
        stack = []
        for char in string[1:len(string) - 1]:
            if char == '(':
                stack.append(char)
            else:
                if not len(stack):
                    return False
                else:
                    stack.pop()
        if not len(stack):
            return True
    return False
