def removeElement(nums, val):
    
    k = 0    #initializing K

    for i in range(len(nums)):     #iterating through the array using the for loop

        if nums[i] != val:   # If the current element is not equal to val

            nums[k] = nums[i]  # Place it in the position indicated by the counter

            k += 1   # Increment the counter


    return k    # Return the number of elements that are not equal to val

nums = [3, 2, 4, 3]
val = 2
result = removeElement(nums, val)
print(result)  
