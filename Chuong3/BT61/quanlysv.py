from datetime import datetime


class Address:
    def __init__(self, streetAddress, city, state, zipCode):
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.zipCode = zipCode

    def __str__(self):
        return f"{self.streetAddress}, {self.city}, {self.state}, {self.zipCode}"


class Student:
    def __init__(self, firstName, lastName, birthDate, homeAddress, schoolAddress):
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.age = 2025 - birthDate.year
        self.homeAddress = homeAddress
        self.schoolAddress = schoolAddress

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.birthDate.strftime('%d/%m/%Y')} - {self.age} years old - Home: {self.homeAddress} - School: {self.schoolAddress}"


class StudentBody:
    def __init__(self):
        self.students = []

    def add_student(self):
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        birthDate = input("Enter birth date (dd/mm/yyyy): ")

        try:
            birthDate = datetime.strptime(birthDate, "%d/%m/%Y")
        except ValueError:
            print("Lỗi, hãy thử lại!")
            return

        print("Enter home address:")
        homeStreet = input("  Street: ")
        homeCity = input("  City: ")
        homeState = input("  State: ")
        homeZip = input("  Zip Code: ")
        homeAddress = Address(homeStreet, homeCity, homeState, homeZip)

        print("Enter school address:")
        schoolStreet = input("  Street: ")
        schoolCity = input("  City: ")
        schoolState = input("  State: ")
        schoolZip = input("  Zip Code: ")
        schoolAddress = Address(schoolStreet, schoolCity, schoolState, schoolZip)

        student = Student(firstName, lastName, birthDate, homeAddress, schoolAddress)
        self.students.append(student)
        print("Student added successfully!")

    def remove_student(self):
        lastName = input("Enter last name of the student to remove: ")
        self.students = [s for s in self.students if s.lastName.lower() != lastName.lower()]
        print("Student removed successfully!")

    def list_students(self):
        for student in self.students:
            print(student)

    def filter_by_address(self):
        addressType = input("Filter by (home/school) address: ").strip().lower()
        city = input("Enter city to filter: ")

        for student in self.students:
            if addressType == "home" and student.homeAddress.city.lower() == city.lower():
                print(student)
            elif addressType == "school" and student.schoolAddress.city.lower() == city.lower():
                print(student)


if __name__ == "__main__":
    body = StudentBody()
    while True:
        print("1. Add Student")
        print("2. Remove Student")
        print("3. List Students")
        print("4. Filter by Address")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            body.add_student()
        elif choice == "2":
            body.remove_student()
        elif choice == "3":
            body.list_students()
        elif choice == "4":
            body.filter_by_address()
        elif choice == "5":
            break
        else:
            print("Lỗi, hãy thử lại!")
