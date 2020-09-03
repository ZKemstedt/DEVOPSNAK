s1 = "Jag tYcker om äGg"
s2 = "inte"
s3 = "SPAM"
s4 = " "
with open(__file__, s1[9]) as f:
    lines = f.readlines()
print()  # newline
print("".join(lines[len(s4.strip()):len(s2)]))  # print lines[0:4]

s1.capitalize()
# line: 10 (index 9) = len(s2)+len(s3)+len(s4)
print(lines[len(s2)+len(s3)+len(s4)], s4, s1)
# print(s1.capitalize())
# line: 13 (index 12) = len(s2)+len(s2)+len(s2)
print(f"{lines[len(s2)+len(s2)+len(s2)]}{s4}{s4}{s4}{s1.capitalize()}".lstrip(
    lines[len(s2)+len(s2)+len(s2)][:len(s4+s4)]))  # and remove the comment
s1 = s1.capitalize()
# line: 17 (index 16) = len(s1)-len(s4)
print(f"{lines[len(s1)-len(s4)]}{s4}{s4}{s4}{s1}")
