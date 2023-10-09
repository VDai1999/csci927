import json
import random
import string
from datetime import datetime, timedelta

def random_generate_dob():
    # Define a start and end date
    start_date = datetime(1995, 1, 1)
    end_date = datetime(2003, 12, 31)

    # Calculate the time difference between the start and end dates
    time_difference = end_date - start_date

    # Generate a random number of days within the time difference
    random_days = random.randint(0, time_difference.days)

    # Create a random datetime by adding the random number of days to the start date
    random_datetime = start_date + timedelta(days=random_days)

    return random_datetime.strftime("%Y-%m-%d")

data = []
for i in range(10):
    temp_dict = {
        "model": "sservice.student",
        "pk": i + 1
    }

    # Get first name and last name
    first_name = f"first{i + 1}"
    last_name = f"last{i + 1}"

    # Student number
    student_num = random.randint(100000, 999999)

    # User name
    user_name = f"user{i + 1}"

    # Password
    password = f"pass{i + 1}"

    # Email
    email = ''.join((random.choice(string.ascii_letters) for i in range(5))) + ".uowmail.edu.au"

    # Date of birth
    dob = random_generate_dob()

    # Phone number
    phone = ''.join((random.choice(string.digits) for i in range(8)))

    fields = {
        "id": i + 1,
        "student_num": student_num,
        "user_name": user_name,
        "first_name": first_name,
        "last_name": last_name,
        "password": password,
        "email": email,
        "dob": dob,
        "phone": phone
    }
    temp_dict['fields'] = fields

    # Append to the data list
    data.append(temp_dict)


# JSON file path to be saved
file_path = "sservice/fixtures/student_data.json"

with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)