class NumberSeat(Exception): # 자리수가 4자리가 아닐 때 발생하는 클래스
    def __init__(self):            # 성적 클래스에 상속되게 하였음
        super().__init__('자리수가 맞지 않습니다. 다시 입력해주세요.')
class OverTimesInput(Exception):
    def __init__(self):
      super().__init__('중복되어 사용할 수 없습니다. 다시 입력해주세요.')
class MustUseEnglish(Exception):
  def __init__(self):
    super().__init__('대문자 영문자를 사용해주세요. 다시 입력해주세요.')
class MustUseInt(Exception):
  def __init__(self):
    super().__init__('정수를 입력해주세요. 다시 입력해주세요.')
class RightName(Exception):
  def __init__(self):
    super().__init__('이름을 다시 입력해주세요. 다시 입력해주세요.')
class ScoreError(Exception):
  def __init__(self):
      super().__init__('점수를 다시 입력해 주세요. 다시 입력해주세요.')
class RightRange(Exception):
    def __init__(self):
        super().__init__('올바른 범위의 숫자를 입력해주세요. 다시 입력해주세요.')

class Sungjuk(): # 현재 : 자릿수 클래스 상속 중 + 다중 상속 사용해서 클래스 더 상속받기
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
    self._hakbun = hakbun
  hakbun = property(get_hakbun, set_hakbun)

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
      used = [] # 빈 리스트를 반복문 안에 넣으면 계속해서 초기화된다.
      english = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U','V', 'W','X','Y', 'Z']
      follow_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

      while True:
          try:
              self._hakbun = input('학번 입력 =>>') # 학번 입력
              # 입력하고 나면 문자형식(str)
              if 4 != len(self._hakbun):
                raise NumberSeat()

              if self._hakbun in used:
                raise OverTimesInput()

              if self._hakbun[0] not in english:
                raise MustUseEnglish()
              for i in range(1,4):
                if self._hakbun[i] not in follow_number:
                  raise MustUseInt()
              print(self._hakbun)


              self._irum = input("이름 입력 => ")
              if 3 != len(self._irum):
                raise NumberSeat()

              for i in self._irum:
                if i in follow_number:
                  raise RightName()

              self._kor = int(input("국어 점수 입력 => "))
              if len(str(self._kor)) > 3:
                raise NumberSeat()
              if self._kor < 0 or self._kor > 100:
                raise ScoreError()


              self._eng = int(input("영어 점수 입력 => "))
              if len(str(self._eng)) > 3:
                raise NumberSeat()
              if self._eng < 0 or self._eng > 100:
                raise ScoreError()


              self._math = int(input("수학 점수 입력 => "))
              if len(str(self._math)) > 3:
                raise NumberSeat()
              if self._math < 0 or self._math > 100:
                raise ScoreError()

          except Exception as e: # 예외가 발생했을 때
              print('예외가 발생했습니다.', e)
          else:
            used.append(self._hakbun)# 예외가 발생하지 않았을 때 실행할 코드
            break


# 추가 수정
  def update_sungjuk(self):
      while True:
          try:
              self._kor = int(input("국어 점수 입력 => "))
              if len(str(self._kor)) > 3:
                  raise NumberSeat()
              if self._kor < 0 or self._kor > 100:
                  raise ScoreError()

              self._eng = int(input("영어 점수 입력 => "))
              if len(str(self._eng)) > 3:
                  raise NumberSeat()
              if self._eng < 0 or self._eng > 100:
                  raise ScoreError()

              self._math = int(input("수학 점수 입력 => "))
              if len(str(self._math)) > 3:
                  raise NumberSeat()
              if self._math < 0 or self._math > 100:
                  raise ScoreError()

          except Exception as e:  # 예외가 발생했을 때
              print('예외가 발생했습니다.', e)
          else:
              break

  def process_sungjuk(self ):
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
    else:
      self._grade = "가"

  def output_sungjuk(self):
    print("%4s %3s %4d  %4d  %4d  %4d  %5.2f  %2s" %
          (self._hakbun, self._irum, self._kor, self._eng, self._math,
           self._tot, self._avg, self._grade))

if __name__ == "__main__":
  obj = Sungjuk()
  obj.input_sungjuk()
  obj.process_sungjuk()
  print("\n\t\t\t *** 성적관리 ***")
  print("==============================================")
  print("학번   이름   국어   영어  수학   총점   평균  등급")
  print("==============================================")
  obj.output_sungjuk()
  print("===============================================")