def mergeTwoList_first_way(list1, list2):
    end_list = sorted(list1 + list2)
    print(end_list)


def mergeTwoList_second_way(list1, list2):
    sorted_list = []
    for nums in range(3):
        print(f"x = {list1[nums]}")
        print(f"y = {list2[nums]}")

    

x = [1, 2, 4]
y = [3, 5, 6]
mergeTwoList_second_way(x, y)