print("don't use v (or ^) as a variable until I make this better")

#boolean variable setting
sets = {}
while True:
    if input('Add a set? Y/N ') not in ['N', 'n']:
        new_set = input('Set: ').split(':')
        sets[new_set[0]] = new_set[1].split(',')
    else:
        break

#expression getting + formatting
def get_exp():
    exp = input('Enter Boolean expression. ')
    form_exp = []
    for x in exp:
        if x in sets or x in operators:
            form_exp.append(x)
    return form_exp

#solve the formatted expression
def solve_exp(exp):
    for x in range(0,len(exp)):
        if exp[x] in operators:
            #TODO add more here so it can do more than one operation at a time
            #TODO and also make it actually do what it says not just adding lol
            solved = sets[exp[x - 1]] + sets[exp[x + 1]]
    return solved
            

#where the expression parsing are called
operators = ['^', 'v']

while True:
    exp = get_exp()
    print(solve_exp(exp))
    if input('Again? Y/N ') in ['N', 'n']:
        break

