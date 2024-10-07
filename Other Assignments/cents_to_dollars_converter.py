get_nickles = float(input())
get_dimes = float(input())
get_quarters = float(input())

def_nickle = 0.05
def_dime = 0.10
def_quarter = 0.25

compute_nickles = def_nickle * get_nickles
compute_dimes = def_dime * get_dimes
compute_quarters = def_quarter * get_quarters

total_final_amount = compute_nickles + compute_dimes + compute_quarters

print(f'Amount: ${total_final_amount:.2f}')