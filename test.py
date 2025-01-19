"""import json
from pyscript import write
# Example classesList for testing
classesList = [
    {"class": "Math", "type": "Honors GT", "numberGrade": 95},
    {"class": "History", "type": "Normal", "numberGrade": 88},
    {"class": "Science", "type": "AP", "numberGrade": 91}
]

def get_grade_and_gpa(number_grade, scale):
    Given a number grade and scale, return the letter grade and GPA.
    # Define grade ranges for each class type scale
    grade_ranges = [
        (96.5, 'A+', scale[0]),
        (93.5, 'A', scale[1]),
        (89.5, 'A-', scale[2]),
        (86.5, 'B+', scale[3]),
        (83.5, 'B', scale[4]),
        (79.5, 'B-', scale[5]),
        (76.5, 'C+', scale[6]),
        (73.5, 'C', scale[7]),
        (70.5, 'C-', scale[8]),
        (70, 'D', scale[9]),
        (0, 'F', 0.0)
    ]
    
    for lower, letter_grade, gpa in grade_ranges:
        if number_grade >= lower:
            return letter_grade, gpa

def convertNumberGrades():
    # Define GPA scales for different class types
    scales = {
        "Honors GT": [5.5, 5.3, 5.1, 4.9, 4.7, 4.5, 4.3, 4.1, 3.9, 3.7],
        "Honors": [5.5, 5.3, 5.1, 4.9, 4.7, 4.5, 4.3, 4.1, 3.9, 3.7],
        "Level III": [5.5, 5.3, 5.1, 4.9, 4.7, 4.5, 4.3, 4.1, 3.9, 3.7],
        "Normal": [5.0, 4.8, 4.6, 4.4, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2],
        "Regular": [5.0, 4.8, 4.6, 4.4, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2],
        "Level II": [5.0, 4.8, 4.6, 4.4, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2],
        "AP": [6.0, 5.8, 5.6, 5.4, 5.2, 5.0, 4.8, 4.6, 4.4, 4.2],
        "IB": [6.0, 5.8, 5.6, 5.4, 5.2, 5.0, 4.8, 4.6, 4.4, 4.2],
        "Level IV": [6.0, 5.8, 5.6, 5.4, 5.2, 5.0, 4.8, 4.6, 4.4, 4.2]
    }
    
    for c in classesList:
        class_type = c["type"]
        
        if class_type in scales:
            # Get the appropriate GPA scale based on class type
            scale = scales[class_type]
            
            # Get letter grade and GPA for the number grade
            letter_grade, gpa_grade = get_grade_and_gpa(c["numberGrade"], scale)
            
            # Assign grade and GPA to the class
            c["letterGrade"] = letter_grade
            c["gpaGrade"] = gpa_grade
            
            # Print the result
            print(f"{c['class']}: {gpa_grade}")

def averageMaintainer(goal=70):
    grades = []
    goal = float(input("What is your goal grade? "))
    while True:
        try:
            grade = input("Enter your grades (Type 'Q' if you're done or 'R' if you would like to reenter the previous grade): ")
            if grade != 'Q' and grade != 'R':
                grades.append(float(grade))
                print(grades)
            elif grade == 'R':
                grades.pop()
                # removes the last entered grade and goes to start of loop
            elif grade == 'Q':
                sumGrades = sum(grades)
                numGrades = len(grades)
                average = sumGrades / numGrades
                print("Your average is:", average)
                neededGrade = (((goal*numGrades) + goal) - sumGrades)
                neededGrade = round(neededGrade, 3) 
                # this sets the equation of: goal = sumGrades + neededGrade / numGrades + 1
                # and puts it in terms of neededGrade!
                if neededGrade > 100:
                    print(f"To average a {goal} in the class, you need at least a {neededGrade} on the next assignment.\n Unfortunately, you can't hit your goal, but make sure to try your best!")
                    break
                else:
                    print(f"To average a {goal} in the class, you need at least a {neededGrade} on the next assignment.\
                        You can do this!")
                    break
        except:
            # if the user doesn't enter anything at all, this will print
            # if the user enters an invalid type (e.g. string) this will print
            # if the user does anything that they're not supposed to, this will print!!
            print("Please enter a valid grade!")

def prepare_classes_list():

    Prepares the classesList for output in a format suitable for PyScript.
    Returns the list of classes as a JSON-serializable object.

    return classesList

# Process the grades
convertNumberGrades()

# Write the prepared classes list for PyScript
pyscript.write("classesListOutput", json.dumps(prepare_classes_list()))"""
from datetime import datetime
def convert_date_string(date_str):
            date_str = date_str.replace('st', '').replace('nd', '').replace('rd', '').replace('th', '')
            return datetime.strptime(date_str, '%B %d %Y')
class AttendanceDetails:
    excused_absences = {
        "absence1": {
            "type": "medical appointment",
            "date": "December 9th 2024",
            "period": "4"
        }, 
        "absence2": {
            "type": "religious holiday",
            "date": "December 6th 2024",
            "period": "6"
        }
    }
    unexcused_absences = {
        "absence1": {
            "type": "Unexcused Advisory",
            "date": "December 19th 2024", 
            "period": "7" 
        }
    }
    tardies = {
        "tardy1": {
            "type": "tardy", 
            "date": " November 9th 2024", 
            "period": "2"
        }, 
        "tardy2": {
            "type": "tardy", 
            "date": "February 19th 2025",
            "period": "4"
        }
    }
    blue_absence = {
        "absence1": {
            "type": "State Reporting Absence",
            "date": "May 14th 2025",
            "period": "3"
        }, 
        "absence2": {
            "type": "State Reporting Absence",
            "date": "May 16th 2025",
            "period": "6"  
        }
    }
    bad_absence = {
        "absence1": {
            "type": "Suspended",
            "date": "March 4th 2025",
            "period": "4"
        }, 
        "absence2": {
            "type": "Suspended", 
            "date": "November 7th 2024",
            "period": "2"
        }
    }
        

    @classmethod
    def get_excuse_absence_details(cls, absence_key, detail):
        try:       
            return cls.excused_absences[absence_key][detail]
        except KeyError:
            return f"No details found for {absence_key} and {detail}."

                
    @classmethod
    def get_unexcuse_absence_details(cls, absence_key, detail):
        try:
            return cls.unexcused_absences[absence_key][detail]
        except KeyError:
            return f"No details found for {absence_key} and {detail}."

    @classmethod
    def get_tardy_details(cls, absence_key, detail):
        try:
            return cls.tardies[absence_key][detail]
        except KeyError:
            return f"No details found for {absence_key} and {detail}."
    @classmethod
    def get_blue_absence_details(cls, absence_key, detail):
        try:
            return cls.blue_absence[absence_key][detail]
        except KeyError:
            return f"No details found for {absence_key} and {detail}."
    @classmethod
    def get_bad_absence_details(cls, absence_key, detail):
        try: 
            return cls.bad_absence[absence_key][detail]
        except KeyError:
            return f"No details found for {absence_key} and {detail}."
            


def tardy():
    global year, month
    details = ["type", "date", "period"]
    grouped_details = []
    for absence_key in AttendanceDetails.excused_absences:
        current_group = []
        for detail in details:
            absence_info = AttendanceDetails.get_excuse_absence_details(absence_key, detail)
            if "No Details Found" not in absence_info:
                current_group.append(absence_info)
        if current_group:
            grouped_details.append(current_group)
            
    print(grouped_details)
    """matched_lists = []
    sorted_lists = sorted(grouped_details, key=lambda x: convert_date_string(x[1]))
    for group in sorted_lists:
        absence_type = group[0]
        if absence_type.lower() == "tardy":
            matched_lists.append(group)"""

tardy()

