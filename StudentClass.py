from datetime import datetime


class Student:
    def __init__(self, StudentID, Name,DOB, classification):
        self.__StudentID = StudentID
        self.__Name = Name
        self.__DOB = DOB
        self.__classification = classification

    def calculate_age(self):
        today = datetime.today()
        DOB_year = int(self.__DOB.split('/')[2])
        
        age = today.year - DOB_year
        return age

    def student_registration(self):
        registration_dates = {
            'Senior': '4/1 thru 4/3',
            'Junior': '4/4 thru 4/6',
            'Sophomore': '4/7 thru 4/9',
            'Freshmen': '4/10 thru 4/12'
        }
        return registration_dates[self.__classification]
    
    def display_info(self):
        age = self.calculate_age()
        registration_dates = self.student_registration()

        print(f'The student is {age} and can register {registration_dates}.')


        