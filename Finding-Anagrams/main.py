# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(str1, str2):
    # [assignment] Add your code here
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if find_anagrams(str1, str2):
    print(
        """
    True
    anagrams
    """
    )
else:
    print(
        """
    False
    not anagrams
    """
    )
find_anagrams(str1, str2)
