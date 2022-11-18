def calculate_total(exp):
    """
    Calculate sum of each list item.
    :param exp: input list
    :return: total of each item of the list
    """
    total = 0
    for item in exp:
        total += item
    return total


list1 = [100, 200, 300]
list2 = [100.10, 200.20, 300.30]
list1_total = calculate_total(list1)
list2_total = calculate_total(list2)
print("list1_total: {}, list2_total: {}".format(list1_total, round(list2_total, 4)))