class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_dic = {}
        for letter in magazine:
            if letter in letter_dic:
                letter_dic[letter] += 1
            else:
                letter_dic[letter] = 1
        
        for letter in ransomNote:
            if letter in letter_dic:
                letter_dic[letter] -= 1
                if letter_dic[letter] < 0:
                    return False
            else:
                return False
        return True
