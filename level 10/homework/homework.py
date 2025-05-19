# 1. ტოლი
print(5 == 5)         # True
print(5 == 3)         # False

# 2. არ არის ტოლი
print(5 != 3)         # True
print(5 != 5)         # False

# 3. დიდი
print(5 > 3)          # True
print(3 > 5)          # False

# 4. მცირე
print(3 < 5)          # True
print(5 < 3)          # False

# 5. დიდი თუ თანაბარი
print(5 >= 5)         # True
print(3 >= 5)         # False

# 6. მცირე თუ თანაბარი
print(3 <= 3)         # True
print(5 <= 3)         # False

# 7. ტოლი (სტრინგები)
print("apple" == "apple")  # True
print("apple" == "orange")  # False

# 8. არ არის ტოლი (სტრინგები)
print("apple" != "orange")  # True
print("apple" != "apple")    # False

# 9. დიდი (სტრინგები)
print("banana" > "apple")    # True (ალფაბეტური მახასიათებელი)
print("apple" > "banana")     # False

# 10. მცირე (სტრინგები)
print("apple" < "banana")     # True
print("banana" < "apple")      # False

# 11. დიდი თუ თანაბარი (სტრინგები)
print("apple" >= "apple")      # True
print("banana" >= "apple")      # True

# 12. მცირე თუ თანაბარი (სტრინგები)
print("apple" <= "apple")      # True
print("banana" <= "apple")      # False

# 13. ლოგიკური და
print((5 > 3) and (3 < 4))     # True
print((5 > 3) and (3 > 4))     # False

# 14. ლოგიკური ან
print((5 > 3) or (3 > 4))      # True
print((5 < 3) or (3 < 4))      # True

# 15. უარყოფითი
print(not (5 > 3))             # False
print(not (3 > 5))             # True

# 16. ჩამოკიდებული შემოწმება
x = 10
print(x == 10)                 # True
print(x != 5)                  # True

# 17. ერთიანობა
y = 20
print(x + y == 30)             # True
print(x + y != 25)             # True

# 18. კომპარატივი
print(15 > 10)                 # True
print(10 < 5)                  # False

# 19. მაგალითი სტრინგებთან
name1 = "Alice"
name2 = "Bob"
print(name1 == name2)          # False

# 20. მაგალითი ლიფტერთან
age = 18
print(age >= 18)               # True

# 21. სპექტრი
value = 75
print(value <= 100 and value >= 0)  # True

# 22. პლუსი
num = 7
print(num + 3 == 10)           # True

# 23. ფუნდამენტური
print(2 * 2 == 4)              # True

# 24. სტრინგების ზომა
print(len("hello") == 5)       # True

# 25. ცვლადების შედარება
a = 5
b = 10
print(a < b)                   # True

# 26. მრავალფეროვნება
print(5 >= 5)                  # True
print(0 <= 1)                  # True

# 27. შედარება და ძიება
fruits = ["apple", "banana"]
print("apple" in fruits)       # True

# 28. შედარება
print(1 == True)               # True
print(0 == False)              # True

# 29. ცვლადის ჩათვლა
c = 2
d = 3
print(c + d == 5)              # True

# 30. ჩამოთვლა
print(1 < 2 < 3)               # True



# 1. ლოგიკური და (and)
print((5 > 3) and (2 < 4))      # True
print((5 > 3) and (2 > 4))      # False

# 2. ლოგიკური ან (or)
print((5 > 3) or (2 < 4))       # True
print((5 < 3) or (2 < 4))       # True
print((5 < 3) or (2 > 4))       # False

# 3. უარყოფითი (not)
print(not (5 > 3))               # False
print(not (3 < 5))               # False
print(not (2 == 2))              # False

# 4. მრავალი მდგომარეობა
print((5 > 3) and (2 < 4) and (1 == 1))  # True
print((5 < 3) or (2 < 4) or (1 != 1))   # True

# 5. ლოგიკური კომბინაცია
x = 10
y = 20
print((x > 5) and (y < 25))      # True
print((x < 5) or (y > 25))       # False

# 6. შიდა ლოგიკური ოპერაცია
is_sunny = True
is_weekend = False
print(is_sunny and not is_weekend)  # True

# 7. შედარება
a = 15
b = 10
c = 5
print(a > b and b > c)           # True
print(a < b or b < c)            # False

# 8. 
num = 7
print(num > 5 and num < 10)      # True
print(num < 5 or num > 10)       # False

# 9. ლოგიკური ალგებრა
print(not ((5 == 5) and (3 > 4)))  # True
print(not ((2 < 3) or (4 < 2)))    # False

# 10. 
is_raining = False
temperature = 30
print(is_raining or (temperature > 25))  # True