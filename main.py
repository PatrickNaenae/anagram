# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word1, word2):
    # Write code here
    if sorted(word1.lower()) == sorted(word2.lower()):
        return True
    else:
        return False

answer = find_anagram('Elbow', 'Below' )
print(answer)