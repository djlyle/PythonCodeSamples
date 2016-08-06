#Runs in python 3.5.0
from enum import Enum

class Operator(Enum):
    NONE=0
    ADD=1
    SUB=2
    MUL=3
    DIV=4

numbers = [1,3,4,6]
operators = [Operator.NONE,Operator.ADD,Operator.SUB,Operator.MUL,Operator.DIV]
    
def evalPostFix(postFixList):
    tmpStack = []
    for i in range(0,len(postFixList)):
        item = postFixList[i]
        if(item in operators):
            if(len(tmpStack) > 1):
                operand2 = tmpStack.pop()
                operand1 = tmpStack.pop()
                tmpResult = applyOp(item,operand1,operand2)
                tmpStack.append(tmpResult)
        else:
            tmpStack.append(item)
    return tmpStack
        
def applyOp(operator,x,y):
    if(operator == Operator.ADD):
        return x + y
    elif(operator == Operator.SUB):
        return x - y
    elif(operator == Operator.MUL):
        return x * y
    elif(operator == Operator.DIV):
        return float(x) / float(y)
    return -1

def backtrack(operands,operators,goal,postfixAttempt,numOperatorsLeft,solutions):
    lenOperands = len(operands)
    if((lenOperands == 0) and (numOperatorsLeft == 0)):
        try:
            tmpResult = evalPostFix(postfixAttempt)
            if(len(tmpResult) == 1 and tmpResult[0] == goal):
                solutions.append(postfixAttempt)
        except Exception as err:
            pass
            #print("err:{}".format(err))
        return
    
    if(numOperatorsLeft > 0):
        for i in range(0,len(operators)):
            op = operators[i]
            if(op == Operator.NONE):
                for j in range(0,lenOperands):
                    newOperands = list(operands)
                    newPostfixAttempt = list(postfixAttempt)
                    newPostfixAttempt.append(newOperands.pop(j))
                    backtrack(newOperands,operators,goal,newPostfixAttempt,numOperatorsLeft,solutions)
            else:
                newPostfixAttempt = list(postfixAttempt)
                newPostfixAttempt.append(op)
                backtrack(operands,operators,goal,newPostfixAttempt,numOperatorsLeft-1,solutions)
    else:
        for j in range(0,lenOperands):
            newOperands = list(operands)
            newPostfixAttempt = list(postfixAttempt)
            newPostfixAttempt.append(newOperands.pop(j))
            backtrack(newOperands,operators,goal,newPostfixAttempt,numOperatorsLeft,solutions)
        
def solve(numbers,operators,goal):
    solutions = []
    lenNumbers = len(numbers)
    numOperatorsLeft = lenNumbers-1
    for i in range(0,lenNumbers):
        nextItem = numbers[i]
        newoperands = list(numbers)
        newoperands.pop(i)
        postfixAttempt = []
        postfixAttempt.append(nextItem)
        backtrack(newoperands,operators,goal,postfixAttempt,numOperatorsLeft,solutions)
    print("solutions:{}".format(solutions))

#This is a demonstration of a simple brute force method to solve the following puzzle from the book
#"Hacking the Art of Exploitation, 2nd Edition":
#>>>
#Use each of the numbers 1, 3, 4, and 6 exactly once with any of the four basic math operations
#(addition, subtraction,multiplication, and division) to total 24. Each number must be used once and only once,
#and you may define the order of operations; for example, 3 * (4 + 6) + 1 = 31 is valid, however incorrect,
#since it doesn't total 24.
#<<<    
#The possible solutions are provided in a list of lists.
#Each solution in the list of solutions is itself a list.
#Each solution is a list of operands (numbers) and operators (add,subtract,multiply or divide)
#in postfix order.  For example the list [6,1,3,4,<Operator.DIV: 4>, <Operator.SUB: 2>, <Operator.DIV: 4>]
#is equivalent to the infix expression "(6 / (1 - 3/4))" and evaluates to the value of 24

solve(numbers,operators,24)
l1 = [6,1,3,4,Operator.DIV,Operator.SUB,Operator.DIV]
l2 = [Operator.DIV,0,1,2,Operator.ADD]
r1 = evalPostFix(l1)
print("r1:{}".format(r1))
r2 = evalPostFix(l2)
print("r2:{}".format(r2))

