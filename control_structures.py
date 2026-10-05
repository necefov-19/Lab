# exam_mark = int(input("Enter exam mark : "))
# if 100>=exam_mark >= 90:
#     print("Your grade is A")
# elif 89>=exam_mark>=75:
#     print("Your grade is B")
# elif 74>=exam_mark>=50:
#     print("Your grade is C")
# else:
#     print("Your grade is F")

for i in range(1, 11):  # Sətrlər (1-dən 10-a qədər vurulan ədədlər)
  for j in range(1, 11):  # Sütunlar (1-dən 10-a qədər ədədlərin özü)
    # Hər ifadəni yan-yana yazmaq üçün end="\t" istifadə edirik
    print(f"{j} x {i} = {j * i:2}", end="\t")
  print()



