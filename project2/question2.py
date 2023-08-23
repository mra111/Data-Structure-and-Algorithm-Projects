n = int (input ())
nums = str (input ()).split ()
nums = list (map (int, nums))

stack = []
results = []

for i in range (n):
    if (i == 0):
        stack.append ([i + 1, n, nums[i], nums[i]])
    
    if (i > 0):
        if (nums[i] > nums[i - 1]):
            stack.append ([i + 1, n, nums[i] - nums[i - 1], nums[i]])
    
    if (i < n - 1):
        if (nums[i] > nums[i + 1]):
            stack_size = len (stack)
            
            while (stack[stack_size - 1][3] - stack[stack_size - 1][2] > nums[i + 1]):
                results.extend ([[stack[stack_size - 1][0], i + 1]] * stack[stack_size - 1][2])
                stack.pop ()
                stack_size = stack_size - 1
            
            if (stack[stack_size - 1][3] > nums[i + 1]):
                results.extend ([[stack[stack_size - 1][0], i + 1]] * (stack[stack_size - 1][3] - nums[i + 1]))
                stack[stack_size - 1] = [stack[stack_size - 1][0], n, stack[stack_size - 1][2] - stack[stack_size - 1][3] + nums[i + 1], nums[i + 1]]

for i in stack:
    results.extend ([[i[0], n]] * i[2])

results.sort ()

for i in results:
    print (*i)
