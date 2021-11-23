#Purpose of this code is to delete the word spam from this list

data = [["spam", "eggs", "toast", "spam"], [ "cheese", "spam", "toast"], ["tomato", "dosa", "spam","idli"],["bread","avacado","milk"],["eggs","cookies","pancakes"]]


# for meal in data:
#     for index in meal:
#         if "spam" in meal:
#             meal.remove("spam")
# print(data)

for meal in data:
    for index in range(len(meal)-2,-2):
        print(index,meal)