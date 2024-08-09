# name = input("Enter the name: ")
# date = input("Enter the date in (dd-mm-yyyy): ")
# print(f"Dear {name},You are selected!, {date}")

letter = '''
 Dear <|Name|>,
 You are selected!
 <|Date|>
          '''


print(letter.replace("<|Name|>", "Sonalika").replace("<|Date|>","17-07-2021"))