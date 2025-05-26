nums = [5, 10, 15, 20, 25, 30, 35, 40]
first_four = nums[:4]
print("პირველი ოთხი ელემენტი:", first_four)
last_three = nums[-3:]
print("ბოლო სამი ელემენტი:", last_three)
middle_three = nums[3:6]
print("შუა სამი ელემენტი:"), middle_three
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(1, len(letters), 2):
    print(letters[i])
print("სიის ელემენტები უკუღმა:", letters[::-1])
sub_list = letters[2:5]
print("ამოღებული ელემენტები ['c', 'd', 'e']:", sub_list)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_four = nums[:4]
print("პირველი ოთხი ელემენტი nums:", first_four)

last_three = nums[-3:]
print("ბოლო სამი ელემენტი nums:", last_three)
