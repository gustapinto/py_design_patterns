from abc import ABC, abstractmethod


class Template(ABC):
    '''
    Templates são padrões de projeto que visam oferecer um esqueleto para
    a construção de sublclasses, oferencendo um conjunto de métodos
    abstratos que devem ser implementados pelas classes filhas e um
    conjunto de métodos concretos que usam os métodos abstratos para
    aplicar uma regra de negócio.

    Elas são comulmente utilizadas ao aplicar o principio da inversão
    de dependência, onde uma função sabe como operar sobre a Template
    abstrata e não sobre suas implementações concretas.
    '''

    @abstractmethod
    def required_operation_one(self):
        '''
        Um método abstrato que deve ser sobreescrito pelas implementações
        concretas da template method.
        '''
        pass

    @abstractmethod
    def required_operation_two(self):
        pass

    def operation(self):
        '''
        O método concreto que implementa os métodos abstratos na regra
        de negócio representada, esse é o método chamado de "template method",
        que nomeia o padrão.
        '''
        result_one = self.required_operation_one()
        result_two = self.required_operation_two()

        return f'Template operated on {result_one} and {result_two}'


class ConcreteTemplateOne(Template):
    '''
    As subclasses de template devem implementar seus métodos abstratos
    conforme a necessidade a que atendem.
    '''

    def required_operation_one(self):
        return 'concrete operation one by template one'

    def required_operation_two(self):
        return 'concrete operation two by template one'


class ConcreteTemplateTwo(Template):
    def required_operation_one(self):
        return 'concrete operation(?) one by template two'

    def required_operation_two(self):
        return 'concrete operation(?) one by template two'


if __name__ == '__main__':
    concrete_one = ConcreteTemplateOne()
    concrete_two = ConcreteTemplateTwo()

    print(concrete_one.operation())
    print(concrete_two.operation())
