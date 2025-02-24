class parenthesis:
    def __init__(self, string):
        self.stack = []
        self.string = string

    def find_parenthesis(self):
        expression = {')': '(', '}': '{', ']': '['}
        if self.string is None:
            return False
        for char in self.string:
            if char in "({[":
                self.stack.append(char)
            elif char in ")}]":
                top = self.stack.pop()
                if top != expression[char]:
                    return False

        return True
# ✅ Test Cases from the Question
test_1 = "I { love [ the {rains}()]} "
test_2 = "I { love [ the {rains ] () "
P = parenthesis(test_1)
print("Test 1:", P.find_parenthesis())
P1 = parenthesis(test_2)

 # Expected Output: True
print("Test 2:", P1.find_parenthesis())  # Expected Output: False


