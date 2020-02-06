string1="tfpdofjdkfllkvcvjd"
string2="jdrghflgnkv"
string3=""
for c in string1:
  if string2.count(c) and c!=' ':
    string3=string3+c
print(string3)