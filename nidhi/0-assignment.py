import sys

#verify loan
def is_eligible(sallary,no_of_emi,loan_ammount):
    if sallary*no_of_emi < loan_ammount:
        return True
    else :
        return False

#display Loan 
def display_format(sallary,no_of_emi,loan_ammount,loan_type):

    print('sallary   Loan type  Eligible loan amount    No. of EMIs to repay')

def main():
    account_number=input("Please enter your account number:")
    if len(account_number)!=4 or account_number[0]!='1':
        print('Invalid account number')
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

    elligble=is_eligible(sallary,customer_emi_expected,loan_ammount_expected)
    if elligble:
        display_format(sallary,customer_emi_expected,loan_ammount,loan_type)
    else:
        print('You cant have loan for this format')
        sys.exit()

if __name__=="__main__":
    main()






