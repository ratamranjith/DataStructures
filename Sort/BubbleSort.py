from array import array

#----------
# Sort List
def bubbleSortList(ListValue: list):
    for i in range(0, len(ListValue)-1):
        for j in range(0, len(ListValue) - i - 1):
            if(ListValue[j] > ListValue[j+1]):
                ListValue[j], ListValue[j+1] = ListValue[j+1], ListValue[j]
    return ListValue
print(bubbleSortList([2,4,5,7,1]))

#-----------
# Sort Array
def bubbleSortArray(arrayValue):
    while(True):
        flag = True
        for i in range(0, len(arrayValue)-1):
            if(arrayValue[i] > arrayValue[i+1]):
                arrayValue[i], arrayValue[i+1] = arrayValue[i+1], arrayValue[i]
                flag = False
        if(flag == True):
            break
    return arrayValue

arrayValue = array('i', [2,4,5,7,1])
print(bubbleSortArray(arrayValue))