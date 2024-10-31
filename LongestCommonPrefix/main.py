from typing import List

class Solution:
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        pref = ""
        v=sorted(strs)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                pref+= first[i]
            else:
                break
        return pref
