class Solution:
    dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            }

    @staticmethod
    def toInteger(roman: str) -> int:
        num = 0
        for idx, char in enumerate(roman):
            if char in ["I", "X", "C"] and idx+1 < len(roman):
                if char != roman[idx+1]:
                    num += Solution.dictionary[roman[idx+1]]-Solution.dictionary[char]
            num+=Solution.dictionary[char]
        return num



# "IV"
# Char = I idx = 1 
