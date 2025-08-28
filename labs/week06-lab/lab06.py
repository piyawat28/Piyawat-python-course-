def welcome_message(name, course):
 
    print(f"Welcome {name} to {course}!")
 
welcome_message("Nueng","Python course")
pass
 
def calculate_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference
 
radius = 5
area, circumference = calculate_circle(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()
 
def create_user_profile(username, age=18, premium=False):
    if premium:
        return username + age + "- Premium User"
    else:
        return username + age + "- Standard User"
   
def analyze_scores(scores):
    if not scores:
        return "Empty list"
   
    total = sum(scores)
    count = len(scores)
    average = total / count
    lowest = min(scores)
    highest = max(scores)
    passed = 0
    for score in scores:
        if score >= 70:
            passed += 1
 
    return {
        "total" : total,
        "average" : average,
        "highest" : highest,
        "lowest"  : lowest,
        "passed" : passed,
    }
 def count_vowels_consonants(text):
     test = text.replace("","")
     text = text.lower()
     vower = text.count('a')+ text.count('e')+ text.count('i')+ text.count('o')+ text.count('u')+ text.count
     number =  text.count('0')+ text.count('1')+ text.count('2')+ text.count('3')+ text.count('4')+ text.count('5')+ text.count('6')+ text.count('7')+ text.count('8')+ text.count('9')
     return {
            "vowels":vowels,
            "consonants": consonants
     }