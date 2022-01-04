# 한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와서 두 숫자를 더한 연산 결과를 저장

# def sum(inputname, savename):
#     except_str = ''
#     with open(inputname, 'r') as f:
#         a = f.readlines()
#     ls = [i.split('\n')[0] for i in a]
#     ls = [i for i in ls if i != except_str]
#     ls = [i.split(' ') for i in ls]
#     with open(savename, 'w') as f:
#         for l in ls:
#             f.write(f'{l[0]}+{l[1]}={float(l[0]) + float(l[1])}\n')
#
# if __name__ == '__main__':
#     sum('list_num.txt', 'list_num_save.txt')



with open('../list_num.txt', 'r') as f:
    data = f.readlines()

with open('../list_num_save.txt', 'w') as w:
    for d in data:
        if d.replace('\n','') != '':
            value1, value2 = d.split()
            result1 = int(value1)+int(value2)
            w.write(f'{value1}+{value2}={result1}')
        else:
            continue

with open('../list_num_save.txt', 'r') as f:
    output = f.read()

print(output)

