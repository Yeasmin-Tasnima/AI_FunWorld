import sys

sys.path.append("D:\extra\Python\learn_python")
import functions as f

list1 = [100, 200, 300]
list2 = [100.10, 200.20, 300.30]
list1_total = f.calculate_total(list1)
list2_total = f.calculate_total(list2)
print("list1_total: {}, list2_total: {}".format(list1_total, round(list2_total, 4)))
