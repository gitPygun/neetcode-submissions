class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap_n = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in hashmap_n:
                if stack and stack[-1] == hashmap_n[c]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(c)

        return True if not stack else False

        
        
        