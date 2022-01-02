a = {}

while True:
   b = input('영어 단어 등록 (종료는 quit) : ')
   if b != 'quit' and b not in a :
      c = input('%s의 뜻 입력 (종료는 quit) : '%b)
      if c != 'quit':
         a[b]=c
      else:
         print('종료합니다.')
         break
   elif b != 'quit' and b in a :
      print('%s는 이미 등록된 단어 입니다.'%b)
   else:
      print('종료합니다.')
      break

while True:
   d = input('검색할 단어 입력 (종료는 quit) : ')
   if d != 'quit' and d in a:
      e = a[d]
      print('%s의 뜻은 %s입니다.'%(d,e))
   elif d != 'quit' and d not in a:
      print('%s는 사전에 없는 단어 입니다.'%d)
   else:
      print('종료합니다.')
      break