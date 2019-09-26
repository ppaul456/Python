# Name:
# Student ID:
# Due Date:
# MSITM 6341
#
#
######################## Instructions ############################
#
# 1. Resolve any compiler errors
# 2. Follow any instructions given in comments starting with TODO
# 3. Resolve any runtime errors
# 4. Resolve any logical errors until the program outputs EXACTLY as the sample output below shows
#
############## Sample Output of Functioning Program ##############
#
# 1st The Way of Kings
# 2nd Mistborn
# 7th Hunger Games
#
##################################################################




ordered_list_of_books = ['The Way of Kings', 'Mistborn', 'Harry Potter', 'The Martian', 'Codex Alera', 'A Song of Ice and Fire', 'Hunger Games' ]

requested_books = ['The Way of Kings', 'Mistborn', 'Hunger Games']

book_ranking_numbers = [ num for num in range(1,len(ordered_list_of_books)+1)]#TODO: Use a list comprehension to generate a list of numbers between 1 and the number of books.
# set a lsit for the book ranking numbers, range(stratindex,endindex+1)= range(1,len(ordered_list_of_books)+1)

book_ordinal_ranking_numbers = []
# emty List to be added

for book_ranking in book_ranking_numbers:
    if book_ranking == 1:
        book_ordinal_ranking_numbers.append(str(book_ranking) + "st")
    elif book_ranking == 2:
        book_ordinal_ranking_numbers.append(str(book_ranking) + "nd")
    elif book_ranking == 3:
        book_ordinal_ranking_numbers.append(str(book_ranking) + "rd")
    else:
        book_ordinal_ranking_numbers.append(str(book_ranking) + "th")
# use elif to add st,nd,rd,th behinf ranking numbers

print(book_ordinal_ranking_numbers)

book_idx = 0
for book in ordered_list_of_books:          # ordered_list_of_books have all books
    if book in requested_books:             # to check if they are requested_books
        print(book_ordinal_ranking_numbers[book_idx] + " " + book)

    book_idx = book_idx + 1