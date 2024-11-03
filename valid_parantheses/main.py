from typing import List

class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        mapping = {
                "[": "]",
                "{": "}",
                "(": ")",
                }
        st = []

        for char in s:
            if char in mapping.keys():
                st.append(char)
            elif char in mapping.values():
                if not st or char != mapping[st[-1]:
                    return False

        return len(st)==0
