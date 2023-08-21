'''
To make this program, we will break it into different segments
and combine them at all in end for final execution
'''

'''
To begin with, we will define a function order(), 
whose work is to take order of coffee from user
'''

def order():

    '''
    This function will take order from user.
    Keep in mind machine can make espresso, latte and cappuccino only, if anything else is given as order 
    machine will discard and ask again for order recursively.
    '''
    
    print('What would you like to have?')                                   # will ask from user "What would you like to have?"

    a = str(input()).lower()                                                # user will give order
    b = a                                                                   # a local variable which stores the value of string a

    if (a == 'espresso' or a == 'latte' or a == 'cappuccino'):              # if order is espresso, latte or cappuccino a is returned as it is

        a = b
    
    else:                                                                   # else recursively, machine again takes the order from user

        print('Sorry, we do not serve this.')                               # displaying, "Sorry, we don't serve this."
        print(' ')                                                          # to move to next line.
        a = order()                                                         # again function be called till condition of if is satisfied

    return a                                                                # returns the order in string to be used further

'''
We are going to work on resource part.
Resouces in machine when turned on after reset.
Ingredients required to make different coffee and their cost.
'''

'''
First element represents water, second milk, third coffee, fouth sugar and fifth money
'''

Report = [1000,500,200,100,0]                                               # resources in machine after reset

'''
Ingredients required to make these coffees and their price
'''

latte = [200,100,20,10,300]                         
espresso = [150,150,25,5,250]
cappuccino = [300,0,30,0,400]

'''
Machine need to check if it has enough resources to make coffee.
'''

def resource_check(A,B):

    '''
    Compare A and B for resource checking.
    A represent current igredients in machine and B represents the details of coffee 
    If there are enough resources to make coffee, it returns 1 
    else it returns 0
    '''

    a = 0

    for i in range(4):                                                      # only first four elements needs to be compared

        if (A[i] >= B[i]):                                                  # if condition is satisfied a is updated by 1
            a = a + 1
    
    if (a == 4):                                                            # finally if a = 4
        b = 1                                                               # b is assigend 1
    
    else:
        b = 0                                                               # else b is assigned 0
    
    return b                                                                # b is returned as 1 if there are enough resources else 0

'''
If a user has coupon code to avail for discount, that also needs to be executed before inserting money.
If a valid coupon is inserted, user will get a discount of 20%.
But user will get only one chance to enter correct code.
'''

def coupon_code():

    '''
    Firstly, it will ask user, if he has a coupon code to avail discount.
    if user has an coupon code, it will ask to enter the code, if it is correct discount will be availed else no concessions.
    '''

    print("Do you have a coupon code to redeem?")                           # asks the user for coupon code
    a = str(input()).lower()                                                # to be answered in yes/no only

    if (a == 'yes'):                                                        # if yes

        print(' ')                                                          # to have a line sepration, when ran in terminal
        print('Enter the coupon code.')                                     # asks the user to enter coupon code
        b = str(input())                                                    # inputs the coupon code

        if b == 'super_20':                                                 # if coupon code matches, discount of 20% is availed
            c = 20                  
            print('Yay!! you got 20 percent discount.')
        else:                                                               # else no discounts
            c = 0           
            print('Sorry :( No coupon applied.' )
    if (a == 'no'):                                                         # if user has no coupon code
        c = 0                                                               # simply no discounts
    
    if a!= 'yes' and a != 'no':                                             # if user entered something unexpected
        c = coupon_code()

    return c                                                                # returns c, which determines the discount %

'''
Machine has took the order, user will pay now.
User can by cash or by UPI
A function is now to be made for the transaction purpose
'''

def money_paid():

    '''
    Firstly machine will ask from user whether money is to paid by cash or by UPI mode.
    if user decides to pay by cash, he will insert notes of different denominations, net amount then be calculated by machine and returned.
    and if user decides to pay by UPI mode, a QR code will be displayed and user enters the amount paid via UPI and this is returned.
    '''

    print("Insert the cash in following denominations.")                  # asks the user in which mode he wants to pay
    print(' ')                                                              # to move to next line

    five = int(input("Rs 500 notes = "))                                    # maximum denomination is Rs 500 note
    two = int(input("Rs 200 notes = "))                                 
    one = int(input("Rs 100 notes = "))
    fifty = int(input("Rs 50 notes = "))
    twenty = int(input("Rs 20 notes = "))
    ten = int(input("Rs 10 notes = "))                                      # minimum denomination is Rs 10 note

    amount = 500*five + 200*two + 100*one + 50*fifty + 20*twenty * 10*ten   # calculate the net amount paid by user which will be returned
    
    return amount                                                           # amount paid by user is now returned.

'''
Report updation needs to be done now. we will update the report after the order is processed.
'''

def update_report(A,B,c):

    '''
    A represents report and B represents coffee.
    All first four elements of coffee will be deducted from report and 
    last element, cost of coffee will be added in last element of report representing money part.
    '''

    for i in range(4):                                                      # first four need to be deducted                                                                       

        A[i] = A[i] - B[i]
    
    A[4] = A[4] + B[4]*(100-c)/100                                           # net amount needs to be added

    return A                                                                # returns the updated report


'''
At last, feedback is to be taken from user. for this a function is to defined now.
'''

def feedback():

    '''
    Asks the user if he wants to give feedback,
    if he wants to give, takes the feedback else returns empty string.
    '''

    print("We will be pleased with your feedback, would you like to give us your feedback?")        # asks the user for feedback
    a = str(input()).lower()
    b = ''

    if a == 'yes':                                                          # if user wants to give feedback

        print('')
        print('Your feedback please')
        b = str(input())                                                    # takes the feedback and stores in b
    
    if a == 'no':                                                           # if not
        
        b = ''                                                              # b is an empty string
    print("Thankyou, have a nice day.")
    return b                                                                # string b is returned

'''
a function generated to print bill
'''

def bill(a,b,c):                                                            # takes string a, int b and c as parameters

    '''
    a represents the coffe, b represents the price of coffee,
    and c represents the discount percentage.
    '''

    print('Order :',a)                                                      # prints order
    print('Price : Rs',b)                                                   # prints price of coffee
    d = b*c/100
    print('discount : Rs',d)                                                # prints discount given
    print('Net amount : Rs',b-d)                                            # prints the net amount paid

'''
A function to ask user for report or to move next or turn off machine or for reset.
'''

def instruction(report,A):                                    # takes report as parameter
    print('')                                                
    print("For seeing the available resources: type 'report'")
    print("For ordering coffee: type 'order'")
    print("For seeing previous feedbacks: type 'feedbacks'")
    print('')
    a = str(input()).lower()                                                # inputs a string value

    if a == 'report':                                                       # if user enters report

        print(' ')                                                          # report of current resources in machine will be printed
        print('water :',report[0])
        print('milk :',report[1])
        print('coffee :',report[2])
        print('sugar :',report[3])
        print('')

        g = instruction(report,A)                                           # and again same function called till next or off
    
    if a == 'off':                                                          # when off g is assigned 0
        g = 0

    if a == 'order':                                                         # when pressed next g is assigned 1
        g = 1
    
    if a=='money_collected':
        print('')
        print('money collected: Rs',report[4])
        print('')
        g=instruction(report,A)

    if a == 'feedbacks':                                                    # if user wants feedbacks stored
        print(' ')
        print(A)
        print(' ')
        g = instruction(report,A)

    if a != 'report' and a != 'off' and a != 'order' and a!= 'feedbacks' and a!= 'money_collected':    # if user gave some unexpected input

        print('Give valid instruction.')
        g = instruction(report,A)

    return g                                                                # returns g which will be used further

'''
Here comes the final part, combining them all to get desired execution from machine
'''

A = []                                                                      # an empty list to store feedbacks
report = [1000,500,200,100,0]                                               # resources are resetm = 0                                                                       # a local variable assigned 1 for condition of while
m = 0

while (m == 0):

    print(' ')                                                              # menu will be printed first
    print('Latte : Rs 300')                                                 # different coffees along with price is printed
    print('Espresso : Rs 250')
    print('Cappuccino : Rs 400')
    print(' ')

    a = order()                                                             # takes order from user and store it in string a

    if a == 'latte':
        coffee = latte
    if a == 'espresso':
        coffee = espresso
    if a == 'cappuccino':
        coffee = cappuccino
    
    b = resource_check(report,coffee)                                    # it checks, if there are suffecient resources to make latte

    if b == 1:                                                          # if there are sufficient resources

        print(' ')                                                      # to get to new line in terminal
        c = coupon_code()                                               # asks user for coupon 
        print(' ')
        d = money_paid()                                                # then asks user to pay

        if d>= coffee[4]:                                                # if paid money is greater than cost of coffee

            d = d - ((coffee[4] * (100 - c))/100)                        # this much monet is returned as change
            report = update_report(report,coffee,c)                        # and resources are updated in machine
            print(' ')
            print('Here is your Rs ',d,'in change.')
            print('Enjoy your',a,'!!')
            print(' ')

            bill(a,coffee[4],c)                                          # prints the bill 
            print(' ')

            f = feedback()                                              # after successful completion of order, asks user for feedback
            A.append(f)                                                 # to access the feedbacks later, they are stored in A
            print('')

            g = instruction(report,A)                                     # runs this function for ending, if report is input, prints the report

            if g == 0:                                                  # if off command is given, breaks the condition of while loop
                m = 1                                                   # by assigning m = 1
                
            if g == 1:                                                  # if next command is given, it continues to take order
                print('')

        else:

            print(' ')
            print('Not Sufficient money, money returned.')
            print(' ')
            g = instruction(report,A)                                   # runs this function for ending, if report is input, prints the report

            if g == 0:                                                  # if off command is given, breaks the condition of while loop
                m = 1                                                   # by assigning m = 1
                
            if g == 1:                                                  # if next command is given, it continues to take order
                print('')

    else:

        print(' ')
        print('Resources are insufficient to fulfill order.')           # if resources are insufficient, informs the user

        print('Would you like to reset the resources in machine?')      # and asks if they want to reset the resources
        a = str(input())
        if a == 'yes':                                                  # if yes
                
            f = report[4]
            report = [1000,500,200,100,0]                               # resources are reset
            report[4] = f
            print(' ')
            print('Resources are reset.')
            
        print(' ')

        g = instruction(report,A)                                   # runs this function for ending, if report is input, prints the report

        if g == 0:                                                  # if off command is given, breaks the condition of while loop
            m = 1                                                   # by assigning m = 1
                
        if g == 1:                                                  # if next command is given, it continues to take order
            print('')
