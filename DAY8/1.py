f = open('yesterday.txt','r')

f_read = f.read()
f_split = f_read.split()
dic = {}

f_sort = f_split.sort(key=str.lower)
print(f_sort)