# # This program determines the number of days in
# # February for a particular year.
# year = int(input('Enter the year: '))
# if year % 100 == 0:  # Determine if year is divisible by 100
#     if year % 400 == 0:  # If it is then determine if it also divisible by 400
#         leap_year = True
#     else:
#         leap_year = False
# else:
#     if year % 4 == 0:  # determine if year is divisible by 4, but only if it is not divisible by 100
#         leap_year = True
#     else:
#         leap_year = False
# if leap_year:
#     print('That is a leap year. February has 29 days.')
# else:
#     print('That is not a leap year. February has 28 days.')
condition = 1
while condition < 10:
    print(condition)
    condition += 1
