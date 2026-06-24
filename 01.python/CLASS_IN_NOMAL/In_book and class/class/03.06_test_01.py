class Person:
    def greeting(self):
        print("안녕하세요.")

class PersonList:
    def __init__(self):
        self.person_list = [] # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person): # 리스트 속성에 Person인스턴스를 추가하는 함수
        self.person_list.append(person)

if __name__ == "__main__":
    person = Person()
    person.greeting()
    pl = PersonList()
    pl.append_person(person)
    print(pl.person_list)
    pl.person_list[0].greeting()