class Solution:
    dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,

            }

    @staticmethod
    def toInteger(roman: str) -> int:
        num = 0
        for char in roman:
            num+=1
        return num
