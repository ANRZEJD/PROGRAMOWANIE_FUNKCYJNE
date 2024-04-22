def partition_list(lst, condition):
    true_list = [item for item in lst if condition(item)]
    false_list = [item for item in lst if not condition(item)]
    return true_list, false_list
