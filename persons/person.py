# PascalCase
class Person:
    # Atributo de Classe
    # Compartilhados pela Classe e pelas Instancias

    # Imutável
    number_of_teeth = 32
    # Mutáveis
    limbs = ["arms", "pernas", "hands", "feets"]
    persons_list = []

    # Inicializador de Instancias
    # Atributo de Instancia
    def __init__(self, name: str, cpf: str) -> None:
        # Self é referente a instacia dessa Classe
        self.name = name
        self.cpf = cpf
        self.hair = True
        self.spoken_languages = ["Portuguese"]

    # Métodos são funções dentro de uma classe, normalmente eles iniciam com um verbo

    # Métodos Estáticos
    # Não precisam da declaração do self e o cls
    @staticmethod
    def say_hello(module: str):
        print(f"Olá {module}!")

    # Dunder Methods/ Métodos Mágicos
    # São utilizados para definir/redefir comportamentos que as classes tem por padrão

    def __repr__(self) -> str:
        return f"<{self.name} - {self.cpf}>"

    def __len__(self) -> int:
        return len(self.spoken_languages)

    # Métodos de Instancia
    def save_person(self) -> str:
        # self.persons_list.append(self)
        # return f"Person {self.name} adicionado!"
        self.number_of_teeth
        self.cpf
        person_found = self.retrive_person(self.cpf)

        if person_found:
            return print(f"Person com cpf {self.cpf} já cadastrado")
        else:
            self.persons_list.append(self)
            return print(f"Person {self.name} cadastrado")

    # Método de Classe
    @classmethod
    def delete_person(cls, person_cpf: str) -> str:
        cls.number_of_teeth
        # cls é o self de uma classe
        # for person in cls.persons_list:
        #     if person.cpf == person_cpf:
        #         cls.persons_list.remove(person)
        #         return f"Person {person.name} removida!"
        # return f"Person {person.name} não encontrada!"

        person_found = cls.retrive_person(person_cpf)

        if not person_found:
            return print(f"Person {person_cpf} não encontrada!")
        else:
            cls.persons_list.remove(person_found)
            return print(f"Person {person_found.name} removida!")

    @classmethod
    def retrive_person(cls, person_cpf: str) -> object:
        for person in cls.persons_list:
            if person.cpf == person_cpf:
                return person
