from persons import Person


def class_attr():
    # Objetos são instancias de Classe
    p1 = Person()
    p2 = Person()
    p3 = Person()

    # print(p1)
    # print(p2)
    # print(p3)
    # print()

    # print(type(p1))
    # print(type(p2))
    # print(type(p3))

    # Tipo de dado imutável
    p1.number_of_teeth = 10
    # print(p1.number_of_teeth)
    # print(p2.number_of_teeth)
    # print(p3.number_of_teeth)

    # Tipo de dado mutável
    p1.limbs.remove("arms")
    print(p1.limbs)
    print(p2.limbs)
    print(p3.limbs)


def instance_attr():
    pedro = Person("Pedro", "111")
    lucira = Person("Lucira", "222")
    alexandre = Person("Alexandre", "333")

    # print(pedro)
    # print(lucira)
    # print(alexandre)

    # print(pedro.name)
    # print(lucira.name)
    # print(alexandre.name)

    pedro.spoken_languages.append("English")
    # print(f"Pedro -> {pedro.spoken_languages}")
    print(f"{pedro.spoken_languages=}")
    print(f"{lucira.spoken_languages=}")
    print(f"{alexandre.spoken_languages=}")


def methods():
    pedro = Person("Pedro", "111")
    lucira = Person("Lucira", "222")
    alexandre = Person("Alexandre", "333")

    pedro.atributo_novo = 2
    print(pedro.atributo_novo)
    # print(Person.__dict__)

    # pedro.say_hello("M5")

    # Métodos de Instancia
    # pedro.save_person()
    # print(Person.persons_list)
    # pedro.save_person()
    # lucira.save_person()
    # print(Person.persons_list)
    # print()

    # Métodos de Classe
    # pedro.delete_person("222")
    # print(Person.persons_list)
    # Person.delete_person("111")
    # print(Person.persons_list)
    # Person.save_person()


def dunder_methods():
    pedro = Person("Pedro", "111")
    lucira = Person("Lucira", "222")
    alexandre = Person("Alexandre", "333")

    # print(pedro)
    # print(lucira)
    # print(alexandre)
    # print(len(pedro))
    # pedro.spoken_languages.append("English")
    # print(len(pedro))


def main():
    # class_attr()
    # instance_attr()
    methods()
    # dunder_methods()


if __name__ == "__main__":
    main()
