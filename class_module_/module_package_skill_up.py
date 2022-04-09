import class_skill_up #class_module_ 패키지의 class_skill_up 모듈을 import해옴

a = class_skill_up.FourCal(5,1)#class_skill_up의 FourCal 클래스를 불러와서 a객체에 저장
print(a.add())#FourCal 클래스의 메소드를 사용

from class_skill_up import FourCal#파이썬 파일로부터 클래스를 불러온다.
a = FourCal(5,1)
print(a.add())

from class_skill_up import FourCal as F#파이썬 파일로부터 클래스를 불러와 별칭을 붙인다.
a = F(5,1)
print(a.add())

import class_module_.class_skill_up# 패키지.파이썬 파일을 import
a = class_module_.class_skill_up.FourCal(5,1)
print(a.add())

from class_module_.class_skill_up import * # 패키지.파이썬파일로 부터 모든 것(클래스,함수 등)을 import
a = FourCal(5,1)
print(a.add())

from class_module_ import class_skill_up# 패키지로 부터 파이썬 파일을 import
a = class_skill_up.FourCal(5,1)
print(a.add())

