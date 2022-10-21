#importing regular expressions module
import re

print("The given DFA only accepts words where the vowels are in alphabetical order")
inp = input("Enter the word\n")

res = re.search("([^aeiou])*a([^aeiou])*e([^aeiou])*i([^aeiou])*o([^aeiou])*u([^aeiou])*",inp)
if not(res is None):
    print("The word was accepted")
else:
    print('The word was rejected')