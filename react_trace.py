from tools import get_course_fee, calculate_scholarship


question = """
What is the total fee for CS101 and AI202
after applying a 10% scholarship?
"""


print("=" * 60)
print("REACT AGENT")
print("=" * 60)

print("\nQUESTION:")
print(question)

print("\n" + "=" * 60)
print("REACT TRACE")
print("=" * 60)


# STEP 1

print("\nTHOUGHT:")
print("I need the fee of CS101.")


print("\nACTION:")
print("get_course_fee('CS101')")

cs101_result = get_course_fee("CS101")


print("\nOBSERVATION:")
print(cs101_result)


# STEP 2

print("\nTHOUGHT:")
print("I also need the fee of AI202.")


print("\nACTION:")
print("get_course_fee('AI202')")

ai202_result = get_course_fee("AI202")


print("\nOBSERVATION:")
print(ai202_result)


# STEP 3

cs101_fee = cs101_result["fee"]
ai202_fee = ai202_result["fee"]

total_fee = cs101_fee + ai202_fee


print("\nTHOUGHT:")
print(
    f"The total fee is ₹{cs101_fee} + "
    f"₹{ai202_fee} = ₹{total_fee}."
)


# STEP 4

print("\nACTION:")
print("calculate_scholarship(38000, 10)")


scholarship_result = calculate_scholarship(
    total_fee,
    10
)


print("\nOBSERVATION:")
print(scholarship_result)


# STEP 5

final_amount = scholarship_result["final_amount"]


print("\nTHOUGHT:")
print(
    f"After applying the 10% scholarship, "
    f"the final amount is ₹{final_amount}."
)


# FINAL

print("\nFINAL ANSWER:")

print(
    f"The total fee for CS101 and AI202 is "
    f"₹{total_fee}. After applying a 10% scholarship, "
    f"the final fee is ₹{final_amount}."
)