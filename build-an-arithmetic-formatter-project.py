def arithmetic_arranger (problems,show_answer=False) :
    dashes=[]
    operand_1=[]
    operand_2=[]
    answers=[]
    if len(problems)>5:
        return "Error: Too many problems."
    for problem in problems:
        for char in problem :
            if char in ['*','/']:
                return "Error: Operator must be '+' or '-'."
        list_problem=problem.split()
        num1=list_problem[0]
        operator=list_problem[1]
        num2=list_problem[2]
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'  
        if len(num1) > 4 or len(num2) > 4 :
            return 'Error: Numbers cannot be more than four digits.' 
        width=max(len(num1),len(num2))+2
        dashes.append('-' * width)
        operand_1.append(num1.rjust(width))
        operand_2.append(operator+' '+num2.rjust(width-2))
        if show_answer:
            if operator== '+':
                answer=str(int(num1)+int(num2))
            if operator=='-':
                answer=str(int(num1)-int(num2))
            answers.append(answer.rjust(width)) 
        #now we just format the answer:
    formated_problems='    '.join(operand_1)+'\n'+'    '.join(operand_2)+'\n'+'    '.join(dashes)
    if show_answer:
        formated_problems='    '.join(operand_1)+'\n'+'    '.join(operand_2)+'\n'+'    '.join(dashes)+'\n'+'    '.join(answers)        
    return formated_problems  

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')