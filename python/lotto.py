# 1 모듈 불러오기
import random

# 2 숫자 통 (1~45)
#lottos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
lottos = range(1,46)   #이상 미만

# 3 그중 6개 sample
#my_luck = [random.choice(lottos),random.choice(lottos),random.choice(lottos),random.choice(lottos),random.choice(lottos),random.choice(lottos)]
my_luck = random.sample(lottos,6)

# 4 그 결과를 출력
print(my_luck)


## 5개 추가 
## for i in range(5):
## 기타 한줄컷 
print(sorted(random.sample(range(1,46),6)))

