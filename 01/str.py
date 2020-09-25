# \n means newline
s = 'First line.\nSecond line.'
# with print(), \n produces a new line
print(s)

# here \n means newline!
print('C:\some\name')

# note the r before the quote
print(r'C:\some\name')
print('C:\\some\\name')

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to\
""")
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to\
""")

print(3 * 'un' 'ium')

print('Py' 'thon')

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

word = 'Python'
print(word[0])
print(word[5])
print(word[-1])
print(word[-6])

# s[:i] + s[i:] 总是等于 s
word[:2] + word[2:]

# 切片的索引有默认值；省略开始索引时默认为0，省略结束索引时默认为到字符串的结束:

word.lower()

'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)

r = 2.5
s = 3.14 * r * r
print(f'The area of a circle with radius {r} is {s:.2f}')

