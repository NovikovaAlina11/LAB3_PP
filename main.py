import re
print("Input text:")
pattern = r"z.{3}z"
text = str(input())
match_object = re.findall(pattern, text)
print(match_object)
