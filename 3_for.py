"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по количеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


def main():
    phone_list = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    total_sold, medium, all_count, all_items = [], [], 0, 0
    for phone in phone_list:
        count, i = 0, 0
        for item in phone['items_sold']:
            count += item
            i += 1
        all_count += count
        all_items += i
        total_sold.append({"product": phone['product'], "total": count})
        print(f"Суммарно продано смартфонов {phone['product']} - {count}")
        medium.append({"product": phone['product'], "medium": format((count/i), '.2f')})
        print(f"Среднее число продаж смартфона {phone['product']} - {format((count/i), '.2f')}")
    print(f"Всего продано {all_count} смартфонов")
    print(f"В среднем продавалось по {format((all_count / all_items), '.2f')} смартфонов")


if __name__ == "__main__":
    main()
