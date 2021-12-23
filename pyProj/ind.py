#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_goods():
    """
    Запросить данные о товаре.
    """

    name = input("Название товара: ")
    shop = input("Название магазина: ")
    price = float(input("Стоимость: "))

    # Создать словарь.
    return {
        'name': name,
        'shop': shop,
        'price': price,
    }


def display_goods(goods):
    """
    Отобразить список товаров.
    """
    print(goods)
    # Проверить, что список товаров не пуст.
    if goods:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Название",
                "Магазин",
                "Цена"
            )
        )
        print(line)
        # Вывести данные о всех товарах.
        for idx, good in enumerate(goods, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    good.get('name', ''),
                    good.get('shop', ''),
                    good.get('price', 0)
                )
            )
        print(line)

    else:
        print("Список товаров пуст.")


def select_goods(goods, shop):
    """
    Выбрать товары магазина.
    """

    # Счетчик записей.
    count = 0

    # Сформировать список товаров.
    result = []

    for good in goods:
        if shop == good.get('shop', shop):
            count += 1
            result.append(good)

    # Проверка на отсутствие товаров или выбранного магазина.
    if count == 0:
        print("Такого магазина не существует либо нет товаров.")
    else:
        # Возвратить список выбранных товаров.
        return result


def main():
    """
    Главная функция программы.
    """

    # Список товаров.
    goods = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о товаре.
            good = get_goods()

            # Добавить словарь в список.
            goods.append(good)
            # Отсортировать список в случае необходимости.
            if len(goods) > 1:
                goods.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            # Отобразить все товары.
            display_goods(goods)

        elif command.startswith('select '):
            # Разбить команду на части для выделения стажа.
            parts = command.split(' ', maxsplit=1)
            # Получить требуемые товары.
            shop = parts[1]

            # Выбрать товары ммагазина.
            selected = select_goods(goods, shop)
            # Отобразить выбранные товары.
            display_goods(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить товар;")
            print("list - вывести список товаров;")
            print("select <имя магазина> - запросить товары магазина;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
