class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in mapping:
                if stack and mapping[char] != stack[-1]:
                    return False
                elif not stack:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        if stack != []:
            return False
        return True
        