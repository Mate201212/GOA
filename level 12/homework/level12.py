
# 1. მარტივი if-else
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 2. რამდენიმე მდგომარეობა
temperature = 30
if temperature > 25:
    print("It's a hot day.")
else:
    print("It's a cool day.")

# 3. if-elif-else
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# 4. ცვლადის შედარება
num = 10
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 5. ლოგიკური პირობები
is_raining = True
if is_raining:
    print("Take an umbrella.")
else:
    print("No need for an umbrella.")

# 6. სინგლის პირობები
name = "Alice"
if name == "Alice":
    print("Hello, Alice!")
else:
    print("Hello, stranger!")

# 7. ასაკის გადამოწმება
age = 15
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# 8. ფასების შედარება
price = 100
if price > 50:
    print("Expensive item")
else:
    print("Affordable item")

# 9. სტატუსის გადამოწმება
is_logged_in = False
if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in.")

# 10. კომბინირებული მდგომარეობები
x = 5
y = 10
if x < y and y > 5:
    print("Both conditions are true.")
else:
    print("One or both conditions are false.")
