

def customers_with_name_startswith(letter):
    "Selecciono clientes con nombres que empiezan con la letra @letter"
    selected_customers = []
    for customer in customers:
        if customer.name.startswith(letter):
            selected_customers.append(customer)
        return selected_customers


def overdraw_accounts():
    "Selecciono las cuentas que tiene giro en descubierto"
    selected_accounts = []
    for account in accounts:
        if account.is_overdraw():
            selected_accounts.append(account)
        return selected_accounts


def select():
    "Selecciono los objectos que cumplen una condicion"
    selected = []
    for object in objects:
        if condition(an_object):
            selecteds.append(an_object)
        return selected


select(customers, lambda customer: customer.name.startswith(letter))
select(account, lambda account: account.is_overdraw())
