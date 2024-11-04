# Manacher's Algorithm
'''
Manacher’s algorithm finds longest palindromic substring in liner time. 
If a palindrome exists in another palindrome, this algorithm exploits 
mirrored property of palindromes and reuses already computed data before 
the center to find the longest palindrome centered at characters after 
the center. That way avoids unnecessary comparisons because it is not 
necessary to expand every center of a possible palindrome outwards.
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        newString = self.insertBogusCharacters(s, "|")
        palindromeRadii = [0]*len(newString)
        longestPalindromeCenter = 0
        
        center = 0
        radius = 0
        
        while center < len(newString):

            expandedRadius = radius + 1
            while center - expandedRadius >= 0 and center + expandedRadius < len(newString) and newString[center-expandedRadius] == newString[center + expandedRadius]:
                radius = expandedRadius
                expandedRadius = radius + 1
                
            palindromeRadii[center] = radius
            if palindromeRadii[center] > palindromeRadii[longestPalindromeCenter]:
                longestPalindromeCenter = center
            
            oldCenter = center
            oldRadius = radius
            oldCenterRightBorder = oldCenter + oldRadius
            center += 1
            radius = 0
            while center <= oldCenterRightBorder:
                mirroredCenter = 2 * oldCenter - center
                maxMirroredRaidus = oldCenterRightBorder - center
                if palindromeRadii[mirroredCenter] < maxMirroredRaidus:
                    palindromeRadii[center]  = palindromeRadii[mirroredCenter] 
                    center += 1
                elif palindromeRadii[mirroredCenter] > maxMirroredRaidus:
                    palindromeRadii[center] = maxMirroredRaidus
                    center += 1
                else: # palindromeRadii[mirroredCenter] == maxMirroredRaidus
                    radius = maxMirroredRaidus
                    break
                
        
        longestPanlidrome = newString[
            longestPalindromeCenter - palindromeRadii[longestPalindromeCenter]:
            longestPalindromeCenter + palindromeRadii[longestPalindromeCenter]+1]

        print("palindromeRadii", palindromeRadii)
        return self.trimBogusCharacters(longestPanlidrome, "|")
    
    def insertBogusCharacters(self, s, bogusCharacter):
        newString = [bogusCharacter]
        for char in s:
            newString.append(char)
            newString.append(bogusCharacter)
        return "".join(newString)
    
    def trimBogusCharacters(self, s, bogusCharacter):
        trimmedString = []
        for char in s:
            if char != bogusCharacter:
                trimmedString.append(char)
        return "".join(trimmedString)


def test1():
    word = "aabab"
    s = Solution().longestPalindrome(word)
    assert s == "aba"

"""
output:
('palindromeRadii', [0, 1, 2, 1, 0, 3, 0, 3, 0, 1, 0])
('the longest palindrome', 'aba')
"""

