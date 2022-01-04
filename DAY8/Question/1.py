# 단어 수 출력

# except_str = ''
# my_set = set()
# ls = []
# with open('yesterday.txt', 'r') as f:
#     while True:
#         a = f.readline()
#         ls.append(a.lower().split('\n')[0].split(' '))
#         if not a:
#             break
# ls = [i for i in ls if i[0] != except_str]
# my_list = sum(ls, [])
#
# for l in my_list:
#     my_set.add(l)
#
# with open('output.txt', 'w') as f:
#     for s in my_set:
#         f.write(f"'{s}' : {my_list.count(s)}\n")




# f = open('yesterday.txt','r')
# yesterday = f.readlines()
# f.close()
# words = []
#
# for line in yesterday:
#     line = line.split()
#     for w in line:
#         words.append(w.lower())
#
# wordL = list(set(words))
# wordL.sort()
#
# wordDict = dict()
# for w in wordL:
#     wordDict[w] = words.count(w)
#
# for w in wordDict.items():
#     print(w)



path = '/Users/iyujin/develop/pythonProject/Day8_0103/FileIO'

d ={}
with open(path+'/Yesterday.txt','r') as f:
    data = f.read().split()
    data = [i.lower() for i in data]

for i in data:
    val = data.count(i)
    d[i] = val
#
# print(sorted(d.items())