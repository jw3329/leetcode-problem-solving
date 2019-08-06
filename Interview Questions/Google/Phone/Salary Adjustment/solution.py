def salary_adjustment(salaries, budget):
    sorted_salaries = sorted(salaries)
    salaries = sorted_salaries
    for i in range(len(salaries)):
        left_length = len(salaries) - i
        if (budget / left_length) <= salaries[i]:
            return budget // left_length
        else:
            budget -= salaries[i]
    return salaries[-1]



salaries = [100, 300, 200, 400]

budget = 800

print(salary_adjustment(salaries,budget))
