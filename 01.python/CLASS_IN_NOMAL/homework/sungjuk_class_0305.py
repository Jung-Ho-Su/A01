class Sungjuk:
    def __init__(self):
        self._hakbun = ""
        self._irum = ""
        self._kor = 0
        self._eng = 0
        self._math = 0
        self._tot = 0
        self._avg = 0.0
        self._grade = ""

    def get_hakbun(self):
        return self._hakbun
    def set_hakbun(self, hakbun):
        self._hakhun = hakbun
    hakbun = property(get_hakbun, set_hakbun)
    # 값을 읽기 위한 작업을 하면 property에서 get 메서드로 읽기를 수행하고, 수정을 하면 set 매서드로 수정을 시행한다.

    def get_irum(self):
        return self._irum
    def set_irum(self, irum):
        self._irum = irum
    irum = property(get_irum, set_irum)

    def get_kor(self):
        return self._kor
    def set_kor(self, kor):
        self._kor = kor
    kor = property(get_kor, set_kor)

    def get_eng(self):
        return self._eng
    def set_eng(self, eng):
        self._eng = eng
    eng = property(get_eng, set_eng)

    def get_math(self):
        return self._math
    def set_math(self, math):
        self._math = math
    math = property(get_math, set_math)

    def get_tot(self):
        return self._tot
    def set_tot(self, tot):
        self._tot = tot
    tot = property(get_tot, set_tot)

    def get_avg(self):
        return self._avg
    def set_avg(self, avg):
        self._avg = avg
    avg = property(get_avg, set_avg)

    def get_grade(self):
        return self._grade
    def set_grade(self, grade):
        self._grade = grade
    grade = property(get_grade, set_grade)

    def input_sungjuk(self):
        self._hakbun = input("\n학번 입력 => ")
        self._irum = input("이름 입력 => ")
        self._kor = int(input("국어 점수 입력 => "))
        self._eng = int(input("영어 점수 입력 => "))
        self._math = int(input("수학 점수 입력 => "))

    def process_sungjuk(self):
        self._tot = self._kor + self._eng + self._math
        self._avg = self._tot / 3

        if self._avg >= 90:
            self._grade = "수"
        elif self._avg >= 80:
            self._grade = "우"
        elif self._avg >= 70:
            self._grade = "미"
        elif self._avg >= 60:
            self._grade = "양"
        elif self._avg < 60:
            self._grade = "가"

    def output_sungjuk(self):
        print("%4s  %3s  %4d  %4d  %4d  %4d  %5.2f  %2s" %
               (self._hakbun, self._irum, self._kor, self._eng, self._math, self._tot, self._avg, self._grade))

if __name__ == "__main__":
    obj = Sungjuk()
    obj.input_sungjuk()
    obj.process_sungjuk()
    print("\n\t\t\t *** 제품관리 ***")
    print("=============================================")
    print("학번    이름   국어 영어 수학  총점  평균  등급")
    print("=============================================")
    obj.output_sungjuk()
    print("=============================================")