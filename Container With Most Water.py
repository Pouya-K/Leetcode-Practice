def maxArea(height):
    leftPointer = 0
    rightPointer = len(height) - 1
    maximumArea = 0
    while rightPointer > leftPointer:
        area = min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer)
        if area > maximumArea:
            maximumArea = area
        if height[leftPointer] < height[rightPointer]:
            leftPointer += 1
        else:
            rightPointer -= 1
    print(maximumArea)
    return maximumArea
