from bitflags import BitFlags

def main():
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ BITFLAGS")
    print("=" * 50)

    print("\n1. Создание множества размером 10")
    bf = BitFlags(10)
    print("Текущее состояние:", bf.to_list())

    print("\n2. Добавление элементов")
    bf.add(3)
    bf.add(7)
    print("После add(3), add(7):", bf.to_list())

    print("\n3. Проверка contains")
    print("contains(3) ->", bf.contains(3))
    print("contains(4) ->", bf.contains(4))

    print("\n4. Удаление элемента")
    bf.remove(3)
    print("После remove(3):", bf.to_list())

    print("\n5. Количество элементов")
    print("count() ->", bf.count())

    print("\n6. Очистка множества")
    bf.clear()
    print("После clear():", bf.to_list())

    print("\n7. Объединение множеств")
    a = BitFlags(10)
    b = BitFlags(10)

    a.add(2)
    a.add(5)

    b.add(5)
    b.add(7)

    u = a.union(b)

    print("A:", a.to_list())
    print("B:", b.to_list())
    print("Union:", u.to_list())

    print("\n8. Пересечение множеств")
    inter = a.intersection(b)

    print("Intersection:", inter.to_list())


if __name__ == "__main__":
    main()