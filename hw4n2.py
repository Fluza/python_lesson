my_list = [14, 15, 3, 4, 1, 7, 5, 4, 11]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)
