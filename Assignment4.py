def main():

    #Input Groups
    group1 = ['Pradnya', 'Anisha']
    group2 = ['Austin', 'Pradnya']
    group3 = ['Austin', 'Melburne']
    group4 = ['Vishal', 'Akash']
    group5 = ['Rahul', 'Pawan']


    #values= {'Pradnya':'1', 'Anisha':'2', 'Austin':'3', 'Melburne':'4', 'Vishal':'5', 'Rahul':'6', 'Pawan':'7', 'Akash':'8'}

    #Creating a dictionary where keys are person and values are numbers assigned to them
    values = {'Pradnya':1, 'Anisha':2, 'Austin':3, 'Melburne':4, 'Vishal':5, 'Rahul':6, 'Pawan':7, 'Akash':8}
    key_list = list(values.keys())     # Key List of the Dictionary
    val_list = list(values.values())   #Value List of Dictionary

    #The groups are converted from text to their respective numbers
    groupval1 = [values[group1[0]], values[group1[1]]]
    groupval2 = [values[group2[0]], values[group2[1]]]
    groupval3 = [values[group3[0]], values[group3[1]]]
    groupval4 = [values[group4[0]], values[group4[1]]]
    groupval5 = [values[group5[0]], values[group5[1]]]

    temp = [groupval1]
    #print(temp)

    groupval = [groupval2, groupval3, groupval4, groupval5]

    # Iterating through groupval (list of groups)
    for i in groupval:
        #print(i)
        val1 = i[0]     # first element
        val2 = i[1]     # second element
        temp1=1
            #print(j)
        for k in temp:  #Iterating through connected peoples group
            if val1 in k and val2 not in k:
                k.append(val2)
                temp1=0
            if val1 not in k and val2 in k:
                k.append(val1)
                temp1=0
        if temp1==1:    #If temp is 1, then no list contains this pair of people, so n
            temp.append(i)

    for s in temp:
        for l in s:
            print(key_list[val_list.index(l)],end=" ")
        print("\n")



    #Second Part:

    # test1=['Pradnya','Melburne']
    #test1=['Pawan','Vishal']
    test1 = ['Anisha', 'Melburne']
    index1Oftest1 = values[test1[0]]
    index2Oftest2 = values[test1[1]]

    z=0
    for s in temp:
        if index1Oftest1 in s and index2Oftest2 in s:
            print("Yes")
            z=1
    if z ==0:
        print("No")
    #print(temp)


if __name__ == "__main__":
    main()





