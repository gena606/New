def different(list1, list2):
    unic_list = []
    for i in list1:
        if not (i in list2):
            unic_list.append(i)
    for j in list2:
        if not (j in list1):
            unic_list.append(j)
    return unic_list


first_list = [1, 2, 3, 4, 5, 3]
second_list = [2, 5, 7, 12, 15]
print(different(first_list, second_list))
