from abc import ABC, abstractmethod


class Creator(ABC):
    '''
    Factory method implementa o conceito de fábrica de objetos a partir da
    implementação de um 'criador' abstrato e da sobreescrita de seu método
    de criação para os criadores concretas.
    '''
    @abstractmethod
    def create(self):
        '''
        Define o método abstrato de criação que será sobreescrito pelos
        objetos concretos
        '''
        pass


class Product(ABC):
    '''
    O produto abstrato que será criado pelos criadores concretos, atua
    tanto como interface para os produtos concretos quanto mantenedor
    das regras de negócio dos produtos produzidos pelas classes criadoras
    '''
    @abstractmethod
    def operation(self):
        '''
        Define o método abstrato de operação dos produtos, essa operação
        normalmente envolverá o uso das principais regras de negócio dos
        produtos, não importando seus tipos concretos
        '''
        pass


'''
Definindo as classes concretas que implementam o Criador e Produto abstratos
'''


class ConcreteCreatorOne(Creator):
    def create(self):
        return ConcreteProductOne()


class ConcreteCreatorTwo(Creator):
    def create(self):
        return ConcreteProductTwo()


class ConcreteProductOne(Product):
    def operation(self):
        return 'First Product'


class ConcreteProductTwo(Product):
    def operation(self):
        return 'Second Product'


if __name__ == '__main__':
    def client(creator):
        '''
        Aplicando a classe criadora em uma função, onde essa desconhece
        quaisquer implementações concretas de Creator ou Product, apenas
        suas abstraçoes
        '''
        print(f'{creator.create().operation()}')  # Usando cadeia por simplicidade

    client(ConcreteCreatorOne())
    client(ConcreteCreatorTwo())
