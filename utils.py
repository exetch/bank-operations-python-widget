from datetime import datetime

def mask_number(account):
    elements = account.split(' ')
    if 'Счет' in elements:
        # Маскировка номера счета
        masked_number = 'Счет **' + elements[-1][-4:]
    else:
        # Маскировка номера карты
        card_number = ''.join(elements[-1])
        masked_number = ' '.join(elements[:-1]) + ' ' + card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]

    return masked_number



def format_date(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    return date.strftime('%d.%m.%Y')


def display_recent_operations(operations):
    # Сортируем операции по дате в обратном порядке
    sorted_operations = sorted(operations, key=lambda x: x.get('date', ''), reverse=True)

    # Выводим 5 последних выполненных операций
    count = 0
    for operation in sorted_operations:
        if operation['state'] == 'EXECUTED':
            date = format_date(operation['date'])
            description = operation['description']
            from_account = operation.get('from', '')
            to_account = operation['to']
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['name']

            # Замаскировать номера карты и счета
            from_account = mask_number(from_account) if from_account else ''
            to_account = mask_number(to_account)

            # Выводим информацию об операции
            print(f'{date} {description}')
            print(f'{from_account} -> {to_account}')
            print(f'{amount} {currency}\n')

            count += 1

        if count >= 5:
            break

