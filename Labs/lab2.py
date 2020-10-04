#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        #
        # Enter your own print statements below:
        #

        # print only first and last of the sentence:
        print(message[0])   #print the first character in message
        length = len(message)   #find how many characters message has
        print(message[length-1])    #print the last character in message

        # use slice notation:
        print(message[0:1])



        # escaping a character:

        print("He said \"that’s fantastic\"!")


        # find all a's in the input word and count how many there are:
        x = message.find('a')   # x will be the index number of the first a found
        print(x)
        a_count = message.count("a")    # a_count will be the number of times a appears in message
        print(a_count)
        length = len(message)   # count how many characters in message
        print("message has %d characters" % (length))


        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        new_message = message.replace("a","-")  # replace all a's with -
        print(new_message)



    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:
        my_list = list(message.split(" "))
        print(my_list)


        # append a new element to the list and print:
        my_list.append(("hello"))
        print(my_list)

        # remove from the list in 3 ways:
        del my_list[1]  #delete the second item (index 1) in list
        print(my_list)

        element_to_delete = my_list.pop(2) #Removes an item at a specific index location and returns it
        print(element_to_delete)
        print(my_list)

        my_list.remove("andrea")    #delete the list item andrea
        #^ if the word specified is not in the list you get an error "ValueError: list.remove(x): x not in list"

        print(my_list)


        # check if the word cake is in your input list:
        if "cake" in my_list:
            print("Yes, 'cake' found in List : ", my_list)

        # reverse the items in the list and print:
        my_list.reverse()   # this reverses the list and does not need to be passed to a variable
        print(my_list)

        # reverse the list with the slicing trick:
        my_list.reverse()   # putting the list back in it's original order after the previous reverse
        print(my_list)
        print(my_list[::-1])    # slicing trick
        # slicing a list with “[::-1]” produces a reversed copy
        # Reversing a list this way takes up a more memory compared to an in-place reversal because
        # it creates a (shallow) copy of the list. And creating the copy requires allocating
        # enough space to hold all of the existing elements.


        # print the list 3 times by using multiplication:
        print(my_list * 3)  # the output will look like one list with elements on the same line


tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()
