#Pohsun Chang
#830911
#MSITM6341
#12/08/2019


with open("emails.txt",'a+') as f:                    # Use 'a+' Create a file
    f.seek(0)                                         # Find the file
    contents = f.read()
    search_word = input("enter a word you want to search in file: ")  # Information I am looking for
    
    if search_word in contents:                       # Check is there any email in the content
        print("Email address loaded: " + contents)    # Yes, then print the content
    else:
        print ("No store information found.")         # No, then input the email into file
        myemail = input("Enter the email address you would like to store? ")
        f.write(myemail)                              # Save myemail onto file
        print("Information saved")
        
        




        



