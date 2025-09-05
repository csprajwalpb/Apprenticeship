class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks  

    def calculate_percentage(self):
        total = sum(self.marks)
        return total / len(self.marks)

    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "F"
        return grade

    def display_details(self):
        print("\n Student Details")
        print("="*30)
        print(f"Name       : {self.name}")
        print(f"Roll No    : {self.roll}")
        print(f"Marks      : {self.marks}")
        print(f"Percentage : {self.calculate_percentage():.2f}%")
        print(f"Grade      : {self.calculate_grade()}")
        print("="*30)


student1 = Student("Prajwal", 101, [85, 90, 78, 92, 88])
student1.display_details()

student2 = Student("Ravi", 102, [45, 55, 60, 50, 40])
student2.display_details()
