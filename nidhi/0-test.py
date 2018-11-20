input_string=input('enter string:') # take input from user i.e. Aayusha123456

#defining a function
def f(string):
    empno=string[-6:] # breaking the string according to question last six charecters assigned to empno
    emp_name=string[:-6]# breaking the string according to question last remaining charecters assigned to emp_name
    emp_name=emp_name.casefold() #to make case Sensative comment this line
    output_string='' #initializing output_string
    if emp_name[0]==emp_name[-1]: #condition.1 as in ques. 
        output_string +=emp_name
    s=0 #initializing sum to zero
    for digit in empno: #iterating for digit in empno
        s +=int(digit) #summing the digits for each iteration
    if s%2==0: #condition.2 checking divisiblity
        output_string +=str(s) #updating output_string according to question
    if emp_name[0]==emp_name[1]: #condition 3. as in question
        output_string+='a' #updating output_string according to question
    if empno[-1]==empno[-2]: #condition 4 according to question
        output_string+=str(empno[-1]) #updating output_string according to question
    if len(output_string)==0: # condition. 5 according to question
        output_string+='F' # updating output_string according to question

    return output_string # return output_string


print(f(input_string)) #calling function f with parameter as input_string and printing the return statement
