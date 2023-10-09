import random
from datetime import datetime, timedelta
import json


def random_generate_date():
    # Define a start and end date
    start_date = datetime(2023, 10, 1)
    end_date = datetime(2023, 12, 31)

    # Calculate the time difference between the start and end dates
    time_difference = end_date - start_date

    # Generate a random number of days within the time difference
    random_days = random.randint(0, time_difference.days)

    # Create a random datetime by adding the random number of days to the start date
    random_datetime = start_date + timedelta(days=random_days)

    return random_datetime.strftime("%Y-%m-%d")


student_volunteer_activities = [
    "Tutor kids in math or reading",
    "Clean up parks",
    "Help at an animal shelter",
    "Collect food donations",
    "Visit seniors",
    "Plant trees",
    "Run charity races",
    "Mentor younger students",
    "Garden for food banks",
    "Assist at events",
    "Serve at shelters",
    "Join youth groups",
    "Fundraise for disasters",
    "Aid at hospitals",
    "Recycle materials",
    "Organize charity auctions",
    "Read to kids",
    "Assist nonprofits",
    "Coach youth sports",
    "Promote understanding"
]


data = []

for i in range(len(student_volunteer_activities)):
    temp_dict = {
        "model": "sservice.activity",
        "pk": i + 1
    }

    # Generate datetime that the volunteering event occurs
    organize_date = random_generate_date()

    # Generate a number of spots available
    num_of_spots = random.randint(3, 200)

    fields = {
        "id": i + 1,
        "activity_num": i + 1,
        "activity_name": student_volunteer_activities[i],
        "date_time_to_organize": organize_date,
        "num_of_spots": num_of_spots
    }
    temp_dict['fields'] = fields

    # Append to the data list
    data.append(temp_dict)

# JSON file path to be saved
file_path = "sservice/fixtures/activity_data.json"

with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)