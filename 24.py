"""
twenty_four_answers

Description: Given four numbers, it looks for a way to make
them add, subtract, multiply, and/or divide in any order to make 24
"""
import copy as cp



# Input is a 4 element list of 4 integers
# returns list length 24 of all the permutations of 4 lists

def shuffle_four(list1) :
    results = []
    num_list = cp.deepcopy(list1)
    c = 0
    for i in range(4) :
        # Shuffle first value
        shuff_list = cp.deepcopy(list1)
        shuff_list[0], shuff_list[i] = shuff_list[i], shuff_list[0]
        for j in range(6) :
            # perform the swaps on the remaining three
            if j % 2 == 0 :
                shuff_list[1], shuff_list[2] = shuff_list[2], shuff_list[1]
                append_value = cp.deepcopy(shuff_list)
                results.append(append_value)
            elif j % 2 != 0:
                shuff_list[2], shuff_list[3] = shuff_list[3], shuff_list[2]
                append_value = cp.deepcopy(shuff_list)
                results.append(append_value)
    return results            


           
# Input is an equation with 4 numbers (string length 7)
# returns list of string that are equations with all combinations of parentheses
# "a+b+c+d"
# "0123456"
def parentheses_combos(eqString) :
    list_combos = []
    solutions = []
    # One pair first one at beginning
    list_combos.append("(" + eqString[0:] + ")")
    list_combos.append("(" + eqString[0:5] + ")" + eqString[5:])
    list_combos.append("(" + eqString[0:3] + ")" + eqString[3:])
    # One pair first one at second term
    list_combos.append(eqString[0:2]  + "(" + eqString[2:5] + ")" + \
        eqString[5:])
    list_combos.append(eqString[0:2]  + "(" + eqString[2:] + ")")
    # One pair at the end
    list_combos.append(eqString[0:4] + "(" + eqString[4:] + ")")
    # Two Pairs no overlap
    list_combos.append("(" + eqString[0:3] + ")" + eqString[3] + "(" + \
        eqString[4:] + ")")
    # Two pairs overlap
    list_combos.append("(" + eqString[0:2] + "(" + eqString[2:5] + "))" + \
        eqString[5:])
    list_combos.append("((" + eqString[0:3] + ")" + eqString[3:5] + ")" + \
        eqString[5:])
    list_combos.append(eqString[0:2] + "(" + eqString[2:4] + "(" + 
        eqString[4:] + "))")
    list_combos.append(eqString[0:2] + "((" + eqString[2:5] + ")" + \
        eqString[5:] + ")")
    return list_combos
   
   
# Inputs are 4 element list of 4 integers between 1 and 13
# puts operations between numbers in all possible combinations
# returns list of strings of numbers and operations all possible combinations
def operations_combos(num_list) :
    results = []
    shuffled_operations = []
    operations = ["+", "-", "*", "/"]
    rolls = 3
    # Get list of all combinations/permutations of three operations
    for i in range(len(operations)) :
        counter1 = 0
        operators = [operations[i] for q in range(len(operations))]
        for j in range(len(operations)) :
            operators[1] = operations[counter1]
            counter1 += 1
            counter2 = 0
            for k in range(len(operations)) :
                operators[2] = operations[counter2]
                counter2 += 1
                append_val1 = str(num_list[0]) + operators[0]
                append_val2 = str(num_list[1]) + operators[1]
                append_val3 = str(num_list[2]) + operators[2] + str(num_list[3])
                results.append(append_val1 + append_val2 + append_val3)
    return results


   
   
   
# Input is 4 integers and optional input limit is also integer default is "NONE"
# another optional integer input is answer that the function is looking for
# default is 24
# checks first four numbers in all combinations of parentheses and operations
# returns a list of strings that match the answer argument
# If no solutions found, it returns "NO SOLUTIONS FOUND"
def solution24(n1, n2, n3, n4, limit="NONE", answer=24) :
   
    # Initializing values and lists
    counter = 0
    solutions = []
    possibilities = []
   
    # Defining variable names for the string equations
    w,x,y,z = n1, n2, n3, n4
    var_list = ['w', 'x', 'y', 'z']
   
    # Getting all permutations of the four numbers
    shuffled_vars = shuffle_four(var_list)

    # Goes through all permutations of numbers
    for set_of_vars in shuffled_vars :
        # get the equations with operations
        for equations in operations_combos(set_of_vars) :
            # get the equations with the parentheses 
            # puts them in list possibilities
            possibilities.append(parentheses_combos(equations))
        for candidate in possibilities :
            # find the equations equal to the answer
            for i in range(len(candidate)) :
                try :
                    # User specifies number of solutions they want
                    if counter == limit :
                        return solutions
                    if eval(candidate[i]) == answer :
                        # Convert string with variable names 
                        # to string with actual numbers
                        can_list = [j for j in candidate[i]]
                        w_index = candidate[i].find('w')
                        x_index = candidate[i].find('x')
                        y_index = candidate[i].find('y')
                        z_index = candidate[i].find('z')
                        can_list[w_index] = str(n1)
                        can_list[x_index] = str(n2)
                        can_list[y_index] = str(n3)
                        can_list[z_index] = str(n4)
                        can_string = ''.join(can_list)
                        # Put solutions as strings into list
                        solutions.append(can_string)
                        counter += 1
                # Avoids ZeroDivisionError
                except ZeroDivisionError :
                    continue
                except NameError :
                    continue

    # Lets user know if there are not found solutions
    if len(solutions) >= 1 :
        return solutions
    else :
        return "NO SOLUTIONS FOUND"
       

def game(the_answer=24, num_of_solutions="ALL") :
    solved = solution24(int(input("Number 1: ")),int(input("Number 2: ")), \
        int(input("Number 3: ")), int(input("Number 4: ")), \
         limit=num_of_solutions, answer=the_answer)
    # In case function returns "NO SOLUTIONS FOUND"
    try :
        eval(solved[0])
        print("There are solutions, do you want to see them? (y/n) ")
        answer = input().upper()
        for i in range(len(solved)) :
            # Prints answer and evaluation of string
            # to show that it is indeed equal to 24
            if answer == "Y" or answer == "YES" :
                print(solved[i] + "=" + str(eval(solved[i])))
            elif answer == "N" or "NO" :
                game()
            else :
                continue
        print("I think " + str(i + 1) + " solutions are enough.")
    except NameError :
        print(solved)
    except IndexError :
        pass



while True :
    amount = input("How many solutions do you want?: ")
    try :
        amount = int(amount)
        game(num_of_solutions=amount)
    except :
        game()

