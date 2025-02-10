# Python class 선언

class 포유류:
    def __init__(self):
        pass
    def 새끼를낳는다(self):
        print('새끼를 낳는다')
    def 젖을먹인다(self):
        print('젖을 먹인다')

# class 클래스명(부모클래스):
class Cat(포유류):
    # 포유류 : 새끼를 낳는다, 젖을 먹인다
    # 다리 4개, 잡식, 소형
    # 엄청 귀엽다, 울음소리가 : 야옹
    외모 = '귀엽다'
    울음소리 = '애옹'

    def 꾹꾹이(self):
        print('꾹꾹')
        print(self.울음소리)
    
    # 오버로딩, 오버라이딩의 대표적인예 : 다형성
    # 중복정의 오버로딩 합하면 8글자
    # 재정의 오버라이딩 합하면 8글자
    # 함수 재정의(Overriding)
    def 젖을먹인다(self):
        print('귀엽게 먹인다')