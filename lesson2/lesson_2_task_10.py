def bank(amount, years):
    percent = 10 / 100
    result = amount
    for i in range(years):
        result += percent * result
    return result
print(bank(100, 5))