from stack import Stack

class ExpressionEvaluator:
    def __init__(self, invert_precedence=False):
        self.invert_precedence = invert_precedence
        self.operators = {
            '+': (1, lambda x, y: x + y),
            '-': (1, lambda x, y: x - y),
            '*': (2, lambda x, y: x * y),
            '/': (2, lambda x, y: x // y)  # Use integer division
        }

    def parse(self, expression):
        output = []
        operators = []
        tokens = expression.split()

        precedence = {op: (1 if self.invert_precedence else prec) for op, (prec, _) in self.operators.items()}

        for token in tokens:
            if token.isdigit():
                output.append(token)
            elif token in self.operators:
                while (operators and operators[-1] in self.operators and
                       precedence[token] <= precedence[operators[-1]]):
                    output.append(operators.pop())
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Pop '('
        
        while operators:
            output.append(operators.pop())

        return ' '.join(output)

    def evaluate(self, expression):
        stack = Stack()
        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                stack.push(int(token))
            elif token in self.operators:
                y = stack.pop()
                x = stack.pop()
                result = self.operators[token][1](x, y)
                stack.push(result)
        
        return stack.pop()
