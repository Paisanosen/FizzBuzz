# arr = temp array
# merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return
    # middle index = length of array divided by two, rounded down
    mid = len(arr) // 2
    # left array = everything to the left of the middle index
    left = arr[:mid]
    # right array = everything to the right of the middle index
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a, b ,arr):
    # len_a = length of left array
    len_a = len(a)
    # len_b = length of right array
    len_b = len(b)
    # initialize counters
    # i = left index, j = right index, k = main index
    i = j = k = 0

    # while i < length of left array and j < length of right array
    while i < len_a and j < len_b:
        # display two choices
        message = a[i] + " or " + b[j] + "\n"
        userChoice = input(message).upper()
        if userChoice == "L":
        # if a[i] <= b[j]:
            # main array index = left array dex
            arr[k] = a[i]
            # increase left array index
            i += 1
        elif userChoice == "R":
            # main array index = right array index
            arr[k] = b[j]
            # increase right array index
            j += 1
        # increase main array index
        k += 1

    # stop when you reach the end of the list
    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    # stop when you reach the end of the list
    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
    test_cases = [
        ["Hinamatsuri", "White Album 2", "Ping Pong", "Naruto", "Bleach", "Monogatari", "Vinland Saga",
        "Mushoku Tensei", "Run With the Wind", "The Great Passage", "Fate Stay Night", "Eighty Six",
        "Jujutsu Kaisen", "Clannad", "ODDTAXI"],
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)