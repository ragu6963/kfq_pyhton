import re
# p = re.compile("ab*")
# m = p.match('ac')
# print(m)

# m1 = p.search('babbcc')
# print(m1)
e = re.compile('^[a-zA-z][0-9a-zA-Z]{4,}@[a-z]+.[a-z]{2,5}$')

email = "bhjas51d@15d.com"
print(e.match(email))