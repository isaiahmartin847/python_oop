def mergeTwoList_first_way(list1, list2):
    end_list = sorted(list1 + list2)
    print(end_list)


def mergeTwoList_second_way(list1, list2):
    sorted_list = []
    list_len = len(list1 + list2)
    i = 0
    while i < list_len:
        for n in list1:
            y = n
            print(f"y = {y}")
        for nums in list2:
            x = nums
            print(f"x = {x}")



        if x > y:
            sorted_list.append(y)
        elif y > x:
            sorted_list.append(x)
        else:
            sorted_list.append(x)
        i = i + 1
    

x = [1, 2, 4]
y = [3, 5, 6]
mergeTwoList_second_way(x, y)