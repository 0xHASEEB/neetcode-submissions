class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        count = 0
        for c in s:
            if c == ')' or c == '}' or c == ']':
                if count == 0:
                    return False
                else:
                    last_one = stack.pop(-1)
                    count -= 1
                    if c == ')' and last_one != '(':
                        return False
                    elif c == '}' and last_one != '{':
                        return False
                    elif c == ']' and last_one != '[':
                        return False
                    else:
                        continue
            else:
                stack.append(c)
                count += 1
        return count == 0
        