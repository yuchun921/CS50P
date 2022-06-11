score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# --------------------------

#  match case (just like "switch")
def grade(score):
    match score:
        case score if score >= 90:
            print("Grade: A")
        case score if score >= 90:
            print("Grade: B")
        case score if score >= 70:
            print("Grade: C")
        case score if score >= 60:
            print("Grade: D")
        case _:
            print("Grade: F")

grade(score)