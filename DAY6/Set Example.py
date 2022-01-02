# 파티에 참석한 사람이 다음과 같을 때 집합 생성하고 그림과 같이 출력

partyA = {"Park", 'Kim', 'Lee'}
partyB = {'Park', '길동', '몽룡'}

absum = partyA | partyB
aball = partyA & partyB
aonly = partyA - partyB
bonly = partyB - partyA
print('파티에 참석한 모든 사람')
print(absum)
print('------------------------------------------')
print('2개의 파티에 모두 참석한 사람')
print(aball)
print('------------------------------------------')
print('파티A에만 참석한 사람')
print(aonly)
print('------------------------------------------')
print('파티B에만 참석한 사람')
print(bonly)