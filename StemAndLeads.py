group3 = [84, 49, 61, 40, 83, 67, 45, 66, 70, 69, 80, 58, 68, 60, 67, 72, 73, 70, 57, 63, 70, 78, 52, 67,53, 67, 75, 61, 70, 81, 76, 79, 75, 76, 58, 31]

#group3 = [5.9, 7.2, 7.3, 6.3, 8.1, 6.8, 7.0, 7.6, 6.8, 6.5, 7.0, 6.3, 7.9, 9.0, 8.2, 8.7, 7.8, 9.7, 7.4, 7.7, 9.7, 7.8, 7.7, 11.6, 11.3, 11.8, 10.7]

#First validation
def validatingDigits(lista):
    #If the number doesn't have two o more digits it'll add zero
     if len(lista) < 2:
        lista.insert(0,'0')
#Second validation
def validatingDecimal(lista):
    #If the number have a point we gonna delete
    if '.' in lista:
        lista.remove('.')
   
#Stem and leaf statical technique 
def stem(group):

    #Putting the first digit into a set
    setting_first_digit = set()
    group = sorted(group)

    for i in group:
        #Each number convert in a string for taking a digit
        i = str(i)
        #Converting in a list
        list_two_numbers = list(i)
        #First validation
        validatingDigits(list_two_numbers)
        #Second validation
        validatingDecimal(list_two_numbers) 
        #Taking the first digit
        setting_first_digit.add(list_two_numbers[0])
    
    #print(setting_first_digit)
    listing_first_digit = sorted(list(setting_first_digit))
    print('Resulting list of stem function', listing_first_digit)

    #dicting_first_digit = dict.fromkeys(setting_first_digit, 0)

    def leaf(group):
        lista = []
        group = sorted(group)
        #We gonna take the index of the result variable from the last function
        for num, lfd in enumerate(listing_first_digit):
           
           for i in group:
            i = str(i)
            list_two_numbers = list(i)

            #First validation
            validatingDigits(list_two_numbers)
            #Second validation
            validatingDecimal(list_two_numbers)

            #print(f"estos son los numeros del resultado de la funcion tallo {lfd} y su tipo es {type(int(lfd))} y estos son los numeros de i {list_two_numbers[0]} y su tipo es {type(lfd)}")
            
            #Taking second digit as appropriate:
            if listing_first_digit[num] == list_two_numbers[0]:
                #print(f"Funciona {listing_first_digit[num]} y {list_two_numbers[0]} son iguales")
                lista.append(list_two_numbers[1])
                print("Para ", lfd, "los numeros correspondientes son ", lista)
                #dicting_first_digit[num] = lista
                lista.clear()
#Result              
    leaf(group3)
stem(group3)
