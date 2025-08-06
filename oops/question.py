import os

class Student:
    def __init__(self, name, scores):
        self.__name = name                 # Encapsulation
        self.__scores = scores            # Private attribute

    def save_to_file(self):
        try:
            filename = self.__name.lower().replace(" ", "_") + "_scores.txt"
            with open(filename, "w") as file:
                for score in self.__scores:
                    file.write(str(score) + "\n")
            print(f"✅ Scores saved to {filename}")
        except Exception as e:
            print("❌ Error saving file:", e)

    def read_from_file(self):
        try:
            filename = self.__name.lower().replace(" ", "_") + "_scores.txt"
            with open(filename, "r") as file:
                scores = [int(line.strip()) for line in file if line.strip().isdigit()]
            self.__scores = scores
            print(f"📖 Scores loaded from {filename}")
        except FileNotFoundError:
            print("❌ File not found for student:", self.__name)
        except Exception as e:
            print("❌ Error reading file:", e)

    def display(self):
        print(f"👤 Student: {self.__name}")
        if self.__scores:
            print("📊 Scores:", self.__scores)
            print("📈 Average:", sum(self.__scores) / len(self.__scores))
        else:
            print("⚠️ No scores available.")

class HighSchoolStudent(Student):
    def display(self):
        print("🏫 High School Student Info")
        super().display()  # Call parent class method     

try:
    name = input("Enter student name: ")
    scores_input = input("Enter scores separated by commas: ")
    scores = [int(score.strip()) for score in scores_input.split(",")]

    student = HighSchoolStudent(name, scores)  # Polymorphism
    student.save_to_file()                     # Abstraction
    student.read_from_file()
    student.display()

except ValueError:
    print("❌ Invalid score input. Please enter only numbers.")
except Exception as e:
    print("❌ Unexpected error occurred:", e)
