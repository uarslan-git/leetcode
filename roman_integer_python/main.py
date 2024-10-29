class Solution:


    @staticmethod
    def toInteger(s: str) -> int:
        dictionary = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
                }
        num = 0
        for a,b in zip(s, s[1:]):
            if dictionary[a] < dictionary[b]:
                num-=dictionary[a]
            else:
                num+=dictionary[a]
        return num + dictionary[s[-1]]
