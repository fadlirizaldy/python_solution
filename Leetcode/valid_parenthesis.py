class Solution:
    def isValid(self, s: str) -> bool:
        arr = []

        dct = {'(': ')', '[': ']', '{': '}'}

        for i in s:
            if i in dct:
                arr.append(dct[i])
            else:
                if not arr or i != arr.pop():
                    return False
        return len(arr) == 0
