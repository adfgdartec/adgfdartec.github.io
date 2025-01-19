from js import document

        # Example classesList
classesList = [
            {"class": "Math", "type": "Honors GT", "numberGrade": 95},
            {"class": "History", "type": "Normal", "numberGrade": 88},
            {"class": "Science", "type": "AP", "numberGrade": 91},
            {"class": "PE", "type": "Normal", "numberGrade": 98},
        ]

def get_grade_and_gpa(number_grade, scale):
            """Given a number grade and scale, return the letter grade and GPA."""
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

def convert_number_grades():
            scales = {
                "Honors GT": [5.5, 5.3, 5.1, 4.9, 4.7, 4.5, 4.3, 4.1, 3.9, 3.7],
                "Normal": [5.0, 4.8, 4.6, 4.4, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2],
                "AP": [6.0, 5.8, 5.6, 5.4, 5.2, 5.0, 4.8, 4.6, 4.4, 4.2],
            }

            for c in classesList:
                class_type = c["type"]
                if class_type in scales:
                    scale = scales[class_type]
                    letter_grade, gpa_grade = get_grade_and_gpa(c["numberGrade"], scale)
                    c["letterGrade"] = letter_grade
                    c["gpaGrade"] = gpa_grade

def update_html():
            """Update the HTML elements with the data."""
            for i, c in enumerate(classesList, start=1):
                document.getElementById(f"class-{i}").textContent = c["class"]
                document.getElementById(f"grade-{i}").textContent = f"Grade: {c['letterGrade']}"
                document.getElementById(f"GPA-{i}").textContent = f"GPA: {c['gpaGrade']}"

        # Initialize data and update HTML
convert_number_grades()
update_html()