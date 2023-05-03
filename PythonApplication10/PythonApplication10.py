def read_int_input(message):
    while True:
        try:
            value = input(message)
            if value.isdigit():
                return int(value)
            else:
                print("Помилка: введені дані некоректні. Будь ласка, введіть ціле число.")
        except ValueError:
            print("Помилка: введені дані некоректні. Будь ласка, введіть ціле число.")

def read_deposit_amount():
    """
    Функція для зчитування суми вкладу та перевірки на коректність.
    """
    while True:
        amount = read_int_input("Введіть суму вкладу (мінімальна сума 1000 грн): ")
        if amount >= 1000:
            break
        else:
            print("Помилка: сума вкладу має бути не менше 1000 грн.")
    return amount


def read_deposit_term():
    """
    Функція для зчитування строку вкладу та перевірки на коректність.
    """
    while True:
        term = read_int_input("Введіть строк вкладу (від 36 до 60 місяців): ")
        if 36 <= term <= 60:
            break
        else:
            print("Помилка: строк вкладу (від 36 до 60 місяців)")
    return term

def calculate_monthly_interest(deposit_amount, deposit_term):
    annual_interest_rate = 20.0  # 20% річних
    interest_rate = float(annual_interest_rate) / 12.0 / 100.0  # обчислення місячної ставки відсотка
    total_amount = deposit_amount  # загальна сума на вкладі
    interest_schedule = []  # графік нарахувань
    total_interest = 0  # перемінна для сумування значення interest
    amount = deposit_amount  # змінна для розрахунку підсумкової суми на рахунку вкладу

    for month in range(1, deposit_term  + 1):
        interest = total_amount * interest_rate
        total_interest += interest
        amount += interest  # збільшення загальної суми на вкладі
        if month % 12 == 0:
            total_amount += total_interest
            total_interest = 0
        interest_schedule.append((month, round(interest, 2), round(amount, 2), round(total_amount, 2)))

    return interest_schedule, round(total_amount, 2)
def print_interest_schedule(interest_schedule):
    """
    Функция для вывода графика начислений на экран в виде таблицы.
    """
    print("|{: <10}|{: <15}|{: <20}|{: <30}|".format("Місяць", "Сума нарахувань", "Поточна сума", "Загальна сума на вкладі"))
    print("|{: <10}|{: <15}|{: <20}|{: <30}|".format("-"*10, "-"*15, "-"*20, "-"*30))
    for month, interest, amount, total_amount in interest_schedule:
        print("|{: <10}|{: <15}|{: <20}|{: <30}|".format(month, interest, amount, total_amount))

print("Калькулятор нарахування відсотків на вкладі")
print("---------------------------------------------")

deposit_amount = read_deposit_amount()
deposit_term = read_deposit_term()

interest_schedule, total_amount = calculate_monthly_interest(deposit_amount, deposit_term)
profit = total_amount - deposit_amount

print_interest_schedule(interest_schedule)
print("Клієнт заробив:", profit)