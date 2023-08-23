def find_max_list (nums, size):
    result = []
    
    nums_size = len (nums)
    result_size = len (result)

    for i in range (nums_size):
        while (result_size > 0 and result[-1] < nums[i] and size - result_size < nums_size - i):
            result.pop ()
            result_size = result_size - 1
        
        if (result_size < size):
            result.append (nums[i])
            result_size = result_size + 1
    
    return result

def merge_lists (i, n, nums1, nums2):
    result = []
    status1 = 0
    status2 = 0
    

    l1= find_max_list (nums1, i)
    l2 = find_max_list (nums2, n - i)

    l1_size = len (l1)
    l2_size = len (l2)

    while (l1_size > 0 and l2_size > 0):
        if (status1 == 0):
            element1 = l1.pop (0)
            status1 = 1
        if (status2 == 0):
            element2 = l2.pop (0)
            status2 = 1

        if (element1 > element2):
            result.append (element1)
            status1 = 0
            l1_size = l1_size - 1
        elif (element1 < element2):
            result.append (element2)
            status2 = 0
            l2_size = l2_size - 1
        else:
            if (l1 > l2):
                result.append (element1)
                status1 = 0
                l1_size = l1_size - 1
            else:
                result.append (element2)
                status2 = 0
                l2_size = l2_size - 1

    if (l1_size > 0):
        if (status1 == 0):
            result.extend (l1)
        else:
            result += [element1] + l1
    
    if (l2_size > 0):
        if (status2 == 0):
            result.extend (l2)
        else:
            result += [element2] + l2
    
    return result

n = int (input ())
nums1 = str (input ()).split ()
nums2 = str (input ()).split ()

nums1 = list (map (int, nums1))
nums2 = list (map (int, nums2))

max_index = min (len (nums1), n)
min_index = max (0, n - len (nums2))

for i in range (min_index, max_index + 1):
    num_list = merge_lists (i, n, nums1, nums2)

    if (i == min_index):
        max_num_list = num_list
    elif (max_num_list < num_list):
        max_num_list = num_list

print (*max_num_list)
