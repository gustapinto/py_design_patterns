from abc import ABC, abstractmethod


class Creator(ABC):
    '''
    Simple factory implementa o conceito de fabrica de objetos a partir
    do uso de um ´unico método, normalmente estático, que a partir de uma
    condicional cria diretamente os objetos, sendo mais usado quando a
    instanciação dos produtos concretos é simples e depende de apenas
    uma condição.
    '''
    def create(choice):
        if choice == 'one':
            return ConcreteProductOne()
        elif choice == 'two':
            return ConcreteProductTwo()
        else:
            return None


class ConcreteProductOne:
    def operation(self):
        return 'First Product'


class ConcreteProductTwo:
    def operation(self):
        return 'Second Product'


if __name__ == '__main__':
    print(Creator.create('one').operation())
    print(Creator.create('two').operation())
