date=input("Enter today's date.\n")

while True:
    mood = int(input("How do you rate your mood today from 1 to 10?\n"))
    if 1 <= mood <= 10:
        break
    else:
        print("Please enter a number between 1 and 10.")

thoughts=input("Let your thoughts flow:\n")

with open(f"{date}.txt", 'a') as file:
    file.write(str(mood) + '\n')
    file.write(thoughts)