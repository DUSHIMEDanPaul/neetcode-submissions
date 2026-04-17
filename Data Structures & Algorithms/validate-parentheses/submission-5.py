class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        res={')':'(',']':'[','}':'{'}
        for r in s:
            if stack and r in res and stack[-1]==res[r]:
                stack.pop()
            elif stack and  r in res  and stack[-1]!=res[r]:
                return False
            else:
                stack.append(r)
        return True if not stack else False

                