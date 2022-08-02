class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for letter in ransomNote:
            print(letter)
            if (letter in magazine) == False:
                return False
            else:
                magazine = magazine.replace(letter," ",1)
        return True

s1 = Solution()

ransomNote = "aa"
magazine ="ab"

print(s1.canConstruct(ransomNote, magazine))
