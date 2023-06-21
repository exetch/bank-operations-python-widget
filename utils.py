from datetime import datetime


def mask_number(account):
    """
        Mask the account number or card number.

        Args:
            account (str): The account number or card number to be masked.

        Returns:
            str: The masked account number or card number.
    """
    elements = account.split(' ')
    if 'Счет' in elements:
        masked_number = elements[-1][-4:]
        return f'Счет ** {masked_number}'
    else:
        card_number = ''.join(elements[-1])
        card_name = ' '.join(elements[:-1])
        masked_number = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]
        return f'{card_name} {masked_number}'


def format_date(date_str):
    """
    Format the date string into the specified format.

    Args:
        date_str (str): The date string to be formatted. It should be in the format 'YYYY-MM-DDTHH:MM:SS.ssssss'.

    Returns:
        str: The formatted date string in the format 'DD.MM.YYYY'.

    Examples:
        >>> format_date('2019-08-26T10:50:58.294041')
        '26.08.2019'
    """
    date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    return date.strftime('%d.%m.%Y')


def display_recent_operations(operations):
    """
    Display the details of the five most recent executed operations.

    This function sorts the operations by date in descending order and displays the details of the executed operations
    with the 'EXECUTED' state. It prints the operation date, description, masked from_account, masked to_account, amount,
    and currency.

        Args:
            operations (list): A list of operation dictionaries.

        Returns:
            None
        """
    sorted_operations = sorted(operations, key=lambda x: x.get('date', ''), reverse=True)

    count = 0
    for operation in sorted_operations:
        if operation['state'] == 'EXECUTED':
            date = format_date(operation['date'])
            description = operation['description']
            from_account = operation.get('from', '')
            to_account = operation['to']
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['name']

            from_account = mask_number(from_account) if from_account else ''
            to_account = mask_number(to_account)

            print(f'{date} {description}')
            print(f'{from_account} -> {to_account}')
            print(f'{amount} {currency}\n')

            count += 1

        if count >= 5:
            break
