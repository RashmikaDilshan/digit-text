X = {'0':'zero',
     '1':'one',
     '2':'two',
     '3':'three',
     '4':'four',
     '5':'five',
     '6':'six',
     '7':'seven',
     '8':'eight',
     '9':'nine' }

Y = {'1':'eleven',
     '2':'twelve',
     '3':'thirteen',
     '4':'fourteen',
     '5':'fifteen',
     '6':'sixteen',
     '7':'seventeen',
     '8':'eighteen',
     '9':'nineteen' }

Z = {'1':'ten',
     '2':'twenty',
     '3':'thirty',
     '4':'forty',
     '5':'fifty',
     '6':'sixty',
     '7':'seventy',
     '8':'eighty',
     '9':'ninety'}



#Take user input as integer
try:
    x = int(input("Enter a number: "))
    print("The entered number is:", x)
except ValueError:
    print("Invalid input. Please enter an integer.without spaces")

#print(len(str(x)))



#find no of groups have to divide
no_of_groups = int(len(str(x))/3)
if ( ( len(str(x))%3 == 1 ) or ( len(str(x))%3 == 2 )):
    no_of_groups = int(len(str(x))/3) + 1

#print( "required no of groups", no_of_groups)


#initialize an empty array & Store user input number as string in a array
num_arr = []

#Store user input number in temp_arr 
for i in str(x):
    num_arr.append(i)
#print(num_arr)



#Grouping elements in a temp array


temp_arr = [] 
j = 0
i = 0


if( int(len(str(x)))%3 == 0 ):

    #print("divide as 3 digit  groups")
    while (i < no_of_groups):
        x = str(num_arr[j])
        y = str(num_arr[j+1])
        z = str(num_arr[j+2])    
        t = x+y+z
        temp_arr.append(t)
        i = i+1
        j = j+3
    #print(temp_arr)

elif( int(len(str(x)))%3 == 1 ):
    
    #print("arrange 1st digit as one group")
    w = str(num_arr[j])
    temp_arr.append(w)
    j = j+1

    #print("arrange remaining as 3 digit  groups")
    while (i < (no_of_groups-1)):
        x = str(num_arr[j])
        y = str(num_arr[j+1])
        z = str(num_arr[j+2])    
        t = x+y+z
        temp_arr.append(t)
        i = i+1
        j = j+3
    #print(temp_arr)

elif( int(len(str(x)))%3 == 2 ):

    #print("arrange 1st two digits as one group")
    v = str(num_arr[j])
    w = str(num_arr[j+1])
    temp_arr.append(v+w)
    j = j+2

    #print("arrange remaining as 3 digit  groups")
    while (i < (no_of_groups-1)):
        x = str(num_arr[j])
        y = str(num_arr[j+1])
        z = str(num_arr[j+2])    
        t = x+y+z
        temp_arr.append(t)
        i = i+1
        j = j+3
    #print(temp_arr)

#main array
main_group = ['', 'thousand', 'million', 'billion', 'trillion']
#print(main_group)

#print elements
print("Given Number in Words: ", end="")
  
for i in range(len(temp_arr)):

    if( len(temp_arr[i]) == 1 ):
        print( X[str(temp_arr[i])],end=" " )

    elif( len(temp_arr[i]) == 2):
        seperated_string = [*str(temp_arr[i])]
        #print(seperated_string)

        if((seperated_string[1] == '0')):
            print( Z[seperated_string[0]],end=" " )
        elif( (seperated_string[0] == '1') and (seperated_string[1] != '0')):
            print(Y[seperated_string[1]],end=" " )     
        else:
            print(Z[seperated_string[0]], X[seperated_string[1]], end=" " )
        
    elif( len(temp_arr[i]) == 3 ):
        seperated_string = [*str(temp_arr[i])]
        #print(seperated_string)

        if((seperated_string[1] == '0') and (seperated_string[2] == '0')):
            print(X[seperated_string[0]],"hundred", end=" ")
        elif((seperated_string[2] == '0')):
            print(X[seperated_string[0]],"hundred",Z[seperated_string[1]], end=" ")
        elif((seperated_string[1] == '1') and (seperated_string[2] != '0')):
            print(X[seperated_string[0]],"hundred",Y[seperated_string[2]], end=" ")
        else:
            print(X[seperated_string[0]], "hundred", Z[seperated_string[1]], X[seperated_string[2]], end=" ")

    if (no_of_groups == 1):
        print(main_group[0],"\n")
    elif(no_of_groups == 2):
        print(main_group[1],",", end=" ")
    elif(no_of_groups == 3):
        print(main_group[2],",", end=" ")
    elif(no_of_groups == 4):
        print(main_group[3],",", end=" ")
    elif(no_of_groups == 5):
        print(main_group[4],",", end=" ")

    no_of_groups = no_of_groups - 1



   
