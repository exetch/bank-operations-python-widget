import sys, io
from utils import mask_number, format_date, display_recent_operations


def test_mask_number():
    # Тестирование маскировки счета
    account = 'Счет 35383033474447895560'
    expected_result = 'Счет **5560'
    assert mask_number(account) == expected_result

    # Тестирование маскировки номера карты
    account = 'Visa Classic 6831982476737658'
    expected_result = 'Visa Classic 6831 98** **** 7658'
    assert mask_number(account) == expected_result


def test_format_date():
    # Тестирование форматирования даты в формате '%Y-%m-%dT%H:%M:%S.%f'
    date_str = '2023-06-01T10:30:45.123456'
    expected_result = '01.06.2023'
    assert format_date(date_str) == expected_result

    # Тестирование форматирования пустой строки
    date_str = ''
    expected_result = None
    assert format_date(date_str) == expected_result


def test_display_recent_operations():
    # Создаем тестовые данные
    operations = [
        {
            'state': 'EXECUTED',
            'date': '2023-06-01T10:30:45.123456',
            'description': 'Operation 1',
            'from': 'Visa Classic 6831982476737658',
            'to': 'Visa Classic 6831982476737658',
            'operationAmount': {
                'amount': '100.00',
                'currency': {
                    'name': 'USD',
                    'code': 'USD'
                }
            }
        },
        {
            'state': 'EXECUTED',
            'date': '2023-06-02T15:20:30.654321',
            'description': 'Operation 2',
            'from': 'Visa Classic 6831982476737658',
            'to': 'Visa Classic 6831982476737658',
            'operationAmount': {
                'amount': '50.00',
                'currency': {
                    'name': 'EUR',
                    'code': 'EUR'
                }
            }
        },

    ]

    # Предполагаемый результат вывода операций
    expected_output = """\
02.06.2023 Operation 2
Visa Classic 6831 98** **** 7658 -> Visa Classic 6831 98** **** 7658
50.00 EUR

01.06.2023 Operation 1
Visa Classic 6831 98** **** 7658 -> Visa Classic 6831 98** **** 7658
100.00 USD

"""

    # Перехватываем вывод print для проверки
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Вызываем функцию для отображения операций
    display_recent_operations(operations)

    # Восстанавливаем stdout
    sys.stdout = sys.__stdout__

    # Проверяем, что вывод совпадает с ожидаемым результатом
    assert captured_output.getvalue() == expected_output
