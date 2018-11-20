import sys

#verify loan
def calculate_loan(salary,account_balance,loan_amount_expected):
    loan={
            'sallary':[25000,50000,75000],
            'loan_type':['car','house','business'],
            'eligible_loan_amount':[500000,6000000,750000],
            'no_of_emi_required':[36,60,84]
            }

    eligible_loan_amount=0
    bank_emi_expected=0
    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expectedi
    if account_balance > 100000:
        rate=5
        eligible_loan_amount=0.5*no_of_emi*sallary
        bank_emi_expected=(eligible_loan_amount*rate*(1+rate)**no_of_emi)/(1+rate)**(no_of_emi-1))
    
    return {'eligible_loan_amount':eligible_loan_amount,'bank_emi_expected':bank_emi_expected}

#display Loan 
def display_format(account_number,eligible_loan_amount,bank_emi_expected,loan_amount_expected,no_of_emi,loan_ammount,loan_type):
    

    #Use the below given print statements to display the output, in case of success
    print("Account number:", account_number)
    print("The customer can avail the amount of Rs.", eligible_loan_amount)
    print("Eligible EMIs :", bank_emi_expected)
    print("Requested loan amount:", loan_amount_expected)
    print("Requested EMI's:",customer_emi_expected)
    #Use the below given print statements to display the output, in case of invalid
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work

def main():
    account_number=input("Please enter your account number:")
    if len(account_number)!=4 or account_number[0]!='1':
        print("Invalid account number")
        sys.exit()
    account_number=int(account_number)
    account_balance=int(input("Please enter your account balance:"))
    if account_balance <100000 :
        print('Insufficient account Balance')
        sys.exit()
    sallary=int(input('Please enter your sallary:'))
    loan_type=input('Type of loan:')
    loan_ammount_expected=int(input('Enter the ammount of loan you need:'))
    customer_emi_expected=int(input('Expected emi:'))
    loan=calculate_loan(sallary,account_balance,loan_amount_expected);
    display_format(account_number,


if __name__=="__main__":
    main()





'''
    if elligble:
        display_format(sallary,customer_emi_expected,loan_ammount,loan_type)
    else:
        print('You cant have loan for this format')
        sys.exit()
'''
