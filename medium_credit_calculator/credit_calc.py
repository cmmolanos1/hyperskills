import argparse
import math
import sys
# Create the parser
parser = argparse.ArgumentParser()

# Add the arguments
parser.add_argument('--type', type=str)
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('nums', nargs='*')

args = parser.parse_args()
argv = sys.argv

tipo = args.type
payment = args.payment

flag = 1
error = "Incorrect parameters"
if payment and payment < 0:
    print(error)
    flag = 0
principal = args.principal
if principal and principal < 0:
    print(error)
    flag = 0
periods = args.periods
if periods and periods < 0:
    print(error)
    flag = 0
if args.interest:
    interest = (args.interest / 100) / 12
    if interest < 0:
        print(error)
        flag = 0
else:
    print(error)
    flag = 0

if tipo == None or tipo not in ['annuity', 'diff']:
    print(error)
    flag = 0
elif tipo == 'diff' and payment:
    print(error)
    flag = 0
elif len(argv) < 4:
    print(error)
    flag = 0


if tipo == 'diff' and flag == 1:
    total_paid = 0
    for month in range(1, periods + 1):
        differential = math.ceil((principal / periods) + interest * (principal - principal * (month - 1) / periods))
        total_paid += differential
        print(f'Month {month}: paid out {differential}')
    print(f'\nOverpayment = {total_paid - principal}')

elif tipo == 'annuity' and flag == 1 and  args.payment is None:
    annuity = math.ceil(principal * interest * pow(1 + interest, periods) / (pow(1 + interest, periods) - 1))
    print(f'Your annuity payment = {annuity}!')
    print(f'Overpayment = {annuity * periods - principal}')

elif tipo == 'annuity' and flag == 1 and  args.principal is None:
    principal =  math.floor(payment / (interest * pow(1 + interest, periods) / (pow(1 + interest, periods) - 1)))
    print(f'Your credit principal = {principal}!')
    print(f'Overpayment = {payment * periods - principal}')

elif tipo == 'annuity' and flag == 1 and  args.periods is None:
    number = payment / (payment - interest * principal)
    months = math.ceil(math.log(number, 1 + interest))

    if months < 12:
        answer = f'{months} months'
    elif months % 12 == 0:
        if months == 12:
            answer = '1 year'
        else:
            answer = f'{math.floor(months / 12)} years'
    else:
        answer = f'{math.floor(months / 12)} years and {months % 12} months'

    print(f'You need {answer} to repay this credit!')
    print(f'Overpayment = {payment * months - principal}')
