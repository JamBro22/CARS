# declaring a random list
cars = [56, 78, 34, 21, 56, 34, 125, 45, 89, 75, 12, 56]


# return sorted list, default ascending order, if reverse_list is set to true then descending order
def sort_list(list_to_sort, reverse_list=False):
    list_to_sort.sort(reverse=reverse_list)
    return list_to_sort


# get the min and max values from a list of numbers
def get_min_max(list_to_get_min_max):
    min_number = min(list_to_get_min_max)
    max_number = max(list_to_get_min_max)
    return "min: {}, max: {}".format(min_number, max_number)


# add the numbers of a list
def add_numbers_in_list(list_to_add):
    return sum(list_to_add)


# remove duplicated items in a list
def remove_duplicates_from_list(list_to_remove_duplicates_from):
    return list(dict.fromkeys(list_to_remove_duplicates_from))


# run from main
if __name__ == "__main__":
    # print list sorted in ascending order
    carsAscending = sort_list(cars)
    print("carsAscending:", carsAscending)
    # print list sorted in descending order
    carsDescending = sort_list(cars, True)
    print("carsDescending:", carsDescending)

    # get the min and max values of a list
    min_max = get_min_max(cars)
    print(min_max)

    # get the sum of the values in the list
    sum_of_list = add_numbers_in_list(cars)
    print("sum:", sum_of_list)

    list_without_duplicates = remove_duplicates_from_list(cars)
    print("List without duplicates:", list_without_duplicates)
