def do_calculation(list1, list2):
    Japan = [i for i in list1]
    Reid = [i for i in list2]
    if Japan[0] > 5 and Reid[0] > 5:
            mylist=[True]
    else: 
            mylist=[False]
    for j in range(1,len(list1)):
        if Japan[j] > 5 and Reid[j] > 5:
            mylist.append(True)
        else:
            mylist.append(False)
    print(mylist)
        