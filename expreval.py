from stack import Stack

class ExpressionEvaluator:

    def __init__(self, invert_precedence=False):
        self.invert_precedence = invert_precedence

        # usage of integers to define the precedence
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2} if not invert_precedence else {'+': 2, '-': 2, '*': 1, '/': 1}
        self.operators = set(self.precedence.keys())

    def parse(self, expression):
        """
        Reads an infix notation and returns a reverse polish notation
        """

        # the final reverse polish notation expression
        output = []
        stack = Stack()

        # splits the string expression by white space
        # reads every token
        for token in expression.split():

            # push into output if its a operand
            if token.isdigit():
                output.append(token)

            # push into stack if left parenthesis
            elif token == '(':
                stack.push(token)

            # pop from the stack until a left parenthesis is encountered, and add into output
            elif token == ')':
                while stack and stack.peek() != '(':
                    output.append(stack.pop())
                
                # Remove the '(' from the stack
                stack.pop()  
            
            # current token is an operator
            else:

                # while the operator on the top of the stack has greater or equal precedence than the current operator, pop operators from the stack to the output list
                # refers to constructor which defines the precedence 
                while (stack and stack.peek() in self.operators and self.precedence[stack.peek()] >= self.precedence[token]):
                    output.append(stack.pop())
                
                # push the current token (an operator) into the stack
                stack.push(token)

        # pop remaining operators into final output
        while stack:
            output.append(stack.pop())
        
        # return expression as concatenated string with space
        return ' '.join(output)

    def evaluate(self, expression):
        """
        Evaluates a reverse polish notation

        Push into the stack if operand
        Otherwise, pop 2 elements from the stack, perform the mathematical operation using the current operator, push result back to stack
        """
        stack = Stack()
        for token in expression.split():
            if token.isdigit():
                stack.push(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.push(a + b)
                elif token == '-':
                    stack.push(a - b)
                elif token == '*':
                    stack.push(a * b)
                elif token == '/':
                    stack.push(a // b)  # Assuming integer division
        return stack.pop()
