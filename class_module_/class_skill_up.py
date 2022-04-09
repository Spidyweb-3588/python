class FourCal:
    def __init__(self, first, second):#생성자
        self.first = first
        self.second = second

    def setdata(self, first, second):#초기 생성자에 의한 인수설정 이후에 새로운 인자를 대입할 때 사용 하는 메소드
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):#클래스 상속
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal):#클래스 상속
    def div(self):#메소드 오버라이딩
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second

#main안에 클래스 불러오기 확인하기
if __name__=="__main__":
    a = FourCal(5,1) #객체 = class(인자1, 인자2), a객체는 FourCal의 인스턴스, a는 객체
    print(a.add()) # 객체.메소드()

    b= FourCal(5,1)#객체 = class()
    b.setdata(4,3)
    print(b.add())#객체.메소드(인자1, 인자2)