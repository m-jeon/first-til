##모듈???
# 1 모듈 불러오기
import random

# 2 점심 메뉴 리스트를 만들자
lunch = ['김밥', '라면', '빵', '초밥']

# 3 하나를 랜덤으로 선택하여 저장한다
today_menu = random.choice(lunch)
print(today_menu)

# 4 동일표현
print(random.choice(lunch))

print(lunch)
print(lunch[1])
