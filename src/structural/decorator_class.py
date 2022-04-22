from abc import ABC, abstractmethod


class Decorator(ABC):
    '''
    Decorators (decoradores) são padrões de projeto que visam adicionar
    novos comportamentos a objetos já existenstes, "embrulhando" os
    objetos que irão receber as novas funcionalidades com um objeto ou
    uma classe que contenha esses comportamentos.
    '''
    def __init__(self, component):
        self.__component = component

    @property
    def component(self):
        '''
        O decorador oferece um ponto de entrada/saída para o componente
        decorado, pois esse deve lidar com todas as operações e as regras
        de negócio
        '''
        return self.__component

    @abstractmethod
    def operation(self):
        '''
        O método do decorador que será utilizado para agregar novos
        comportamentos a métodos do componente instanciado
        '''
        pass


class ConcreteDecoratorOne(Decorator):
    def operation(self):
        return f'Decorate {self.component.operation()} by decorator one'

    def new_operation(self):
        '''
        Decoradores também podem ser utilizados para adicionar novas
        funcionalidades ao componente, porém essa prática deve ser usada
        de forma escassa, dando preferência, nesses casos a subclasses,
        pois adicionar novos métodos viola o principio da responsabilidade
        única, pois o decorador iria tanto modificar métodos existentes
        quanto adicionar novas funções a classe.
        '''
        return 'This is a new operation, please avoid using it'


class ConcreteDecoratorTwo(Decorator):
    def operation(self):
        return f'Decorate {self.component.operation()} by decorator two'


class Component:
    def operation(self):
        return 'a concrete operarion'


if __name__ == '__main__':
    component = Component()
    decorated_component_one = ConcreteDecoratorOne(component)
    decorated_component_two = ConcreteDecoratorTwo(component)

    print(component.operation())
    print(decorated_component_one.operation()) 
    print(decorated_component_one.new_operation()) 
    print(decorated_component_two.operation())
