def bubbleSort(ListValue: list):
    for i in range(0, len(ListValue)-1):
        for j in range(0, len(ListValue)-1):
            if(ListValue[i] > ListValue[j+1]):
                ListValue[i], ListValue[j+1] = ListValue[j+1], ListValue[i]
    return ListValue
print(bubbleSort([2,4,5,7,1]))