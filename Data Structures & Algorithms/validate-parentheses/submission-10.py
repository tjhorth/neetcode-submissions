class Solution:
    def isValid(self, s: str) -> bool:
        # hashmap

        # add all opening brackets to a stack
        # if you come a across a closing bracket, the last opening bracket in the stack should match
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # if opening bracket, add to stack
            # if closing bracket, make sure we have a corresponding open as latest on stack
            # if stack we have a closing bracket and stack is empty, False
            if char in mapping:
                if stack and mapping[char] == stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(char)
        
        # if stack is not empty, return False
        if stack:
            return False
        return True

