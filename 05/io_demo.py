# with open('/Users/lvbing/test', 'r') as f:
#     line = f.readline()
#     while line:
#         print(line.strip())
#         line = f.readline()
#
#     for li in f:
#         print(li)
#
# with open('/Users/lvbing/test', 'a') as f:
#     f.write('test')

from io import StringIO
from io import BytesIO

s_f = StringIO()
b_f = BytesIO()

b_f.write('中文'.encode('utf-8'))
print(b_f.getvalue())

import os

s = [x for x in os.listdir('/Users/lvbing/workspace/python/trainingCamp') if os.path.isdir(x)]

for x in os.listdir('/'):
    if os.path.isdir('/' + x):
        print(x)

print(s)
