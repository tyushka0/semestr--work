from bitflags import BitFlags

def run_tests():
    print("=" * 50)
    print("ЗАПУСК ТЕСТОВ")
    print("=" * 50)

    bf = BitFlags(10)
    bf.add(3)
    assert bf.contains(3) is True
    print("Тест add / contains пройден")

    bf.remove(3)
    assert bf.contains(3) is False
    print("Тест remove пройден")

    bf.add(1)
    bf.add(2)
    bf.add(5)
    assert bf.count() == 3
    print("Тест count пройден")

    bf.clear()
    assert bf.count() == 0
    print("Тест clear пройден")

    a = BitFlags(10)
    b = BitFlags(10)

    a.add(1)
    a.add(3)

    b.add(3)
    b.add(5)

    u = a.union(b)
    assert u.contains(1)
    assert u.contains(3)
    assert u.contains(5)
    print("Тест union пройден")

    inter = a.intersection(b)
    assert inter.contains(3)
    assert not inter.contains(1)
    print("Тест intersection пройден")

    print("\nВсе тесты успешно пройдены!")


if __name__ == "__main__":
    run_tests()