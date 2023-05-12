from datetime import datetime
from dateutil.relativedelta import relativedelta
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
    interest_rate = annual_interest_rate / 12.0 / 100.0  # обчислення місячної ставки відсотка
    interest_schedule = []  # графік нарахувань
    total_interest = 0  # перемінна для сумування значення interest
    amount = deposit_amount  # змінна для розрахунку підсумкової суми на рахунку вкладу
    start_date = datetime.now()
    total_amount = deposit_amount  # загальна сума на вкладі

    for month in range(1, deposit_term + 1):
        interest = total_amount * interest_rate
        total_interest += interest
        amount += interest  # збільшення загальної суми на вкладі
        if month % 12 == 0:
            total_amount += total_interest
            total_interest = 0
        current_date_parts = start_date.strftime("%d/%m/%Y").split("/")
        month_int = int(current_date_parts[1])
        year_int = int(current_date_parts[2])
        month_int += 1
        if month_int > 12:
            month_int = 1
            year_int += 1
        start_date = start_date + relativedelta(months=1)
        current_date_str = start_date.strftime("%d/%m/%Y")
        interest_schedule.append((month, current_date_str, round(interest, 2), round(amount, 2)))

    return interest_schedule, round(total_amount, 2)



def print_interest_schedule(interest_schedule):
    """
    Функция для вывода графика начислений на экран в виде таблицы.
    """
    print("|{: ^10}|{: ^10}|{: >15}|{: >20}|".format("Місяць", "Дата", "Сума нарахувань", "Поточна сума"))
    print("|{: ^10}|{: ^10}|{: >15}|{: >20}|".format("-"*10, "-"*10, "-"*15, "-"*20, ))
    for month, current_date, interest, amount in interest_schedule:
        print("|{: ^10}|{: ^10}|{: >15}|{: >20}|".format(month, current_date, interest, amount))

print("Калькулятор нарахування відсотків на вкладі")
print("---------------------------------------------")

deposit_amount = read_deposit_amount()
deposit_term = read_deposit_term()

interest_schedule, total_amount = calculate_monthly_interest(deposit_amount, deposit_term)
profit = total_amount - deposit_amount

print_interest_schedule(interest_schedule)
print("Банк віддав ", total_amount)
print("Клієнт заробив" ,profit)