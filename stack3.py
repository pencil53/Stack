#given an expression string
#write a python prgram to find whether a given string has balanced parentheses or not

#one approach to check balanced parenthesis is to use stack
#each time, when an open parentheeses is encountered push it in the stack,
# and when closed parenthesis is encountered, match it with the top of stack and pop it.
#if stack is empty at the end, return balanced otherwise, unbalanced.

open_list = ["[", "{", "("]
close_list = [ "]", "}", ")"]

#Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i) #stack = [{()}]
        elif i in close_list:
            pos = close_list.index(i) #pos = 1
            if ((len(stack) > 0) and 
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
    

#Driver code
string = "{Hello}"
print(string,"-", check(string))