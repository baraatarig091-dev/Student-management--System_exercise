while True:
         print("\n\n====calculates====")
         print("1:add")
         print("2:sub")
         print("3:mul")
         print("4:div")
         choice = int(input("Enter your  choice: "))
         if choice == 1:
          number1 = int(input("Enter your  number: "))
          number2 = int(input("Enter your  number: "))
          print(f"{number1} + {number2} = {number1 + number2}")
         elif choice == 2:
          number1 = int(input("Enter your  number: "))
          number2 = int(input("Enter your  number: "))
          print(f"{number1} - {number2} = {number1 - number2}")
         elif choice == 3:
          number1 = int(input("Enter your  number: "))
          number2 = int(input("Enter your  number: "))
          print(f"{number1} * {number2} = {number1 * number2}")
         elif choice == 4:
            number1 = int(input("Enter your  number: "))
            number2 = int(input("Enter your  number: "))
            print(f"{number1} / {number2} = {number1 / number2}")
         elif choice == 5:
             break
