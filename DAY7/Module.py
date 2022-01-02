# 모듈 ( Module ) : 함수, 변수, 클래스 들을 모아 놓은 파일 (.py)
# 패키지 : 여러 모듈들을 모아 놓은 디렉토리

# 코드의 재사용 : 자주 사용되는 함수를 한 번 작성해 놓고 여러 곳에서 import해서 사용
# 코드를 기능에 따라 모듈 단위로 분리하여 설계함으로써 효율적인 개발 및 유지보수 가능

# 표준 모듈 : 파이썬 언어 패키지 안에 기본으로 포함되어 있는 모듈
# 사용자 정의 모듈 : 개발자가 직접 정의한 모듈
# 써드 파티 모듈 : 다른 업체나 개인이 만들어서 제공하는 모듈


# 표준 모듈
import sys

builtModules = sys.builtin_module_names
print(builtModules)


# import 모듈명
import random       # random 안에 있는 모든 함수를 다 참조하겠다는 의미

# import 모듈명 as 별칭
import pandas as pd     # 모듈명이 길기 때문에 짧게 별칭으로 바꿔서 사용

# 모듈 내 함수를 참조
# import 모듈
# 모듈.함수명
#
# import random
# random.randint()


# 모듈 내에서 일부만 참조
from random import randint      # from 모듈명 import 함수명

# from 모듈명 import 함수명 as 별칭 