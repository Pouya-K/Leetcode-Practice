def productExceptSelf(nums):
    hasZero = False
    has2OrMoreZero = False
    hasNonZero = False
    totalProduct = 0
    output = []
    for num in nums:
        if num == 0:
            if hasZero:
                has2OrMoreZero = True
            else:
                hasZero = True
        else:
            if not hasNonZero:
                totalProduct = 1
                hasNonZero = True
            totalProduct *= num
    for num in nums:
        if has2OrMoreZero:
            output.append(0)
        elif hasZero and num != 0:
            output.append(0)
        else:
            newProduct = int(totalProduct / num) if num !=0 else totalProduct
            output.append(newProduct)

    return output


print(productExceptSelf([0,4,0]))