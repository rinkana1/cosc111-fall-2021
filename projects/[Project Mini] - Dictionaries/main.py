# Project Mini - Dictionaries

# Function 1: Grade map

def GetGradeMap():
  return {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}

# Function 2- Create Student Record

def CreateStudentRecord(firstname, lastname, age, grades):
  return {'firstname': firstname,
          'lastname': lastname,
          'age': age,
          'grades': grades}

# Function 3 - Get Student GPA

def CalculateGPA(student):
  gpa = 0
  grademap = GetGradeMap()

  for grade in student['grades']:
    gpa += grademap[grade]

  gpa /= len(student['grades'])

  return gpa