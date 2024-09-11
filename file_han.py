import pandas as pd
import os
import openpyxl

list_of_students = []

def get_student_data():
    name = input("Enter your Name: \n")
    roll_no = input("Enter your Roll Number: \n")
    age = input("Enter your Age: \n")
    phone = input("Enter your Phone: \n")

    student = {
        "Name": name,
        "Roll Number": roll_no,
        "Age": age,
        "Phone": phone
    }

    list_of_students.append(student)

def excel_save(file_name):
    if os.path.exists(file_name):
        try:
            
            existing_df = pd.read_excel(file_name, engine='openpyxl')
        except Exception as e:
            print(f"Error reading the existing file: {e}")
        
            existing_df = pd.DataFrame()
    else:
        existing_df = pd.DataFrame()
    

    new_df = pd.DataFrame(list_of_students)
    
    
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    

    try:
        combined_df.to_excel(file_name, index=False, engine='openpyxl')
    except Exception as e:
        print(f"Error saving to Excel file: {e}")

while True:
    get_student_data()

    next_action = input("Do you want to add another student info? Press y/n: ").lower()

    if next_action != 'y':
        break

excel_save('students.xlsx')
