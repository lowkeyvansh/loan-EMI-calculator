def loan_emi(principal, rate, time):
    rate = rate / (12 * 100)
    time = time * 12
    emi = (principal * rate * (1 + rate) ** time) / ((1 + rate) ** time - 1)
    return emi

print(loan_emi(100000, 10, 5))
