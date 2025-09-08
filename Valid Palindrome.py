class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPointer = 0
        rightPointer = len(s) - 1
        palindrome = s.lower()
        while leftPointer < rightPointer:
            leftPointerLetter = palindrome[leftPointer]
            rightPointerLetter = palindrome[rightPointer]
            leftPointerIsAlNum = leftPointerLetter.isalnum()
            rightPointerIsAlNum = rightPointerLetter.isalnum()

            if leftPointerIsAlNum and rightPointerIsAlNum:
                if leftPointerLetter != rightPointerLetter:
                    return False
                leftPointer += 1
                rightPointer -= 1
            else:
                if not leftPointerIsAlNum:
                    leftPointer += 1
                if not rightPointerIsAlNum:
                    rightPointer -= 1
        return True
