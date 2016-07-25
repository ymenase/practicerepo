# largest = None
# smallest = None
# while True:
    # try: 
        # #num = str(int(raw_input("Enter a number: ")))
        # num = str(int(input("Enter a number: ")))
    # except: 
        # if num == "done" : exit()
        # else: print ("Invalid Input")
    # for itervar in num:
        # if largest is None or itervar > largest:
            # largest = itervar
        # print ('Loop:', itervar, largest)
        # if smallest is None or itervar < smallest:
            # smallest = itervar
        # print ('Loop:', itervar, smallest)
    # print ('Largest:', largest)
    # print ('Smallest:', smallest)
# print ("Minimum", smallest)   
# print ("Maximum", largest)

largest = None
smallest = None
while True:
    try:
        # save the input before you throw the exception so you can test it in the exception
        num = input("enter a number: ")
        num = int(num)
    except:
        if num == "done":
            # print statements need to happen before exiting the program
            print ("Minimum", smallest) 
            print ("Maximum", largest)

            exit()
        else:
            print ("invalid input")

        # use a continue to skip this iteration and try the loop again
        continue
    
    # you would need a loop if you were traversing a list of saved inputs,
    # you're discarding inputs though so just check against the two variables
    # Also, since the largest/smallest are not initialized to a value, check the types
    if type(largest) != type(int()):
       largest = num
    else:
       if num > largest:
          largest = num

    if type(smallest) != type(int()):
       smallest = num
    else:
       if num < smallest:
          smallest = num
