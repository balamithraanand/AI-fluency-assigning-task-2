import json


def get_course_fee(course_code):

    with open("course_data.json", "r") as file:
        course_data = json.load(file)

    course_code = course_code.upper()

    if course_code in course_data:
        return {
            "course": course_code,
            "fee": course_data[course_code]
        }

    return {
        "error": f"Course {course_code} was not found."
    }


def calculate_scholarship(amount, percentage):

    discount = amount * percentage / 100
    final_amount = amount - discount

    return {
        "original_amount": amount,
        "scholarship_percentage": percentage,
        "discount": discount,
        "final_amount": final_amount
    }