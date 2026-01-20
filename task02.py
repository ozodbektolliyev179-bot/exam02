def  atm_operation(balance: int, action: str, amount: int) -> int:
    if action not in ['deposit''withdraw']:
        print(f'{action} bunday action mavjud emas ')


    if amount < 0:
        print('maxfiy amount kiriting.')

    if action == 'withdraw':
        if amount > balance:
            print('balansda yetarlicha mablag mavjut emas.')
        else:
            balance -=amount
    else:
        balance += amount

    return balance

print(atm_operation(100000, "deposit", 50000)) # 150000

print(atm_operation(100000, "withdraw", 20000)) # 80000


