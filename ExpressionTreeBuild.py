"""
Definition of ExpressionTreeNode:
"""
class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None


# class Solution:
#     """
#     @param: expression: A string array
#     @return: The root of expression tree
#     """
#     def build(self, expression):
#         # write your code here
#         stack = []
#         for item in expression:
#



expression = ["2","*","6","-","(","23","+","7",")","/","(","1","+","2",")"]
# print(expression)