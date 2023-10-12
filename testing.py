

result_dict = {"a": "a_value", "b": "b_value", "c": "c_value"}

my_iterator = iter(result_dict)
try:
    while True:
        item = next(my_iterator)
        print(item)
except:
    pass

# len(results_dic[next(iter(results_dic))]) < 2