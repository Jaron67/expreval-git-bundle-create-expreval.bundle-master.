from expreval import ExpressionEvaluator

def test_expression_evaluator():
    evaluator = ExpressionEvaluator()

    assert evaluator.parse("3 + 4 * 2 / ( 1 - 5 )") == "3 4 2 * 1 5 - / +"
    assert evaluator.evaluate("3 4 2 * 1 5 - / +") == 1

    evaluator = ExpressionEvaluator(invert_precedence=True)
    assert evaluator.parse("3 + 4 * 2 / ( 1 - 5 )") == "3 4 + 2 * 1 5 - /"
    assert evaluator.evaluate("3 4 + 2 * 1 5 - /") == -5

if __name__ == "__main__":
    test_expression_evaluator()
    print("test_expreval.py passed")

