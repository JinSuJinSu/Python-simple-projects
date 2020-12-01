def arithmetic_arranger(problems,display=False):

    operators = []
    dashes = []
    list1 = []
    list2 = []
    results=[]
    new_list1=[]
    new_list2=[]
    new_results=[]

    list1_length = 0
    list2_length = 0
    
    if len(problems)>5:
        return 'Error: Too many problems.'

    for problem in range(len(problems)):
        if '+' in problems[problem] or '-' in problems[problem]:
            problems[problem] = problems[problem].split(' ')
            list1.append(problems[problem][0])
            operators.append(problems[problem][1])
            list2.append(problems[problem][2])

            if problems[problem][0].isdigit() == False or problems[problem][2].isdigit() == False:
                return 'Error: Numbers must only contain digits.'

            elif len(problems[problem][0]) > 4 or len(problems[problem][2]) > 4:
                return 'Error: Numbers cannot be more than four digits.'

        else:
            return "Error: Operator must be '+' or '-'."

    for operator in range(len(operators)):
        if '+' in operators[operator]:
            result = int(list1[operator]) + int(list2[operator])
            results.append(str(result))

        elif '-' in operators[operator]:
            result = int(list1[operator]) - int(list2[operator])
            results.append(str(result))

        else:
            pass


    for problem in range(len(problems)):
        width = max(len(list1[problem]),len(list2[problem]))+2
        if problem==0:
            dashes.append('-'*width)
            new_list1.append(' '*(width-len(list1[problem]))+list1[problem])
            new_list2.append(operators[problem] + ' '*(width-len(list2[problem])-1)+list2[problem])
            new_results.append(' '*(width-len(results[problem]))+results[problem])

        else:
            dashes.append('    ' + '-'*width)
            new_list1.append('    ' +(' '*(width-len(list1[problem]))+list1[problem]))
            new_list2.append('    ' + (operators[problem] + ' '*(width-len(list2[problem])-1)+list2[problem]))
            new_results.append('    ' +(' '*(width-len(results[problem]))+results[problem]))

    if display == True:
        arranged_problems = ''.join(new_list1) + '\n' + ''.join(new_list2) + '\n' + ''.join(dashes) + '\n' + ''.join(new_results)

    else:
        arranged_problems = ''.join(new_list1) + '\n' + ''.join(new_list2) + '\n' + ''.join(dashes)

    return arranged_problems



