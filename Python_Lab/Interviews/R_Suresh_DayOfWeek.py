
# R. Suresh
# Day of Week.

daysInWeek = {'1':'Monday','2':'Tuesday','3':'Wednesday','4':'thu','5':'fri','6':'sat', '7':'sund'}
choice = input("enter number: ")
print(daysInWeek.keys())
print(daysInWeek.values())
print(daysInWeek.get(choice, "Please enter 1-7 as input"))
#if choice in daysInWeek.keys():
#    print(daysInWeek[choice])
#else:
#    print("Please enter 1-7 as input")




















































#if choice in daysInWeek:
print(daysInWeek.get(choice, "Invalid Day"))
#else:
#    print("Invalid day")

