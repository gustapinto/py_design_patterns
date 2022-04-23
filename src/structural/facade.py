class Facade:
    '''
    O padrão de Facade (fachada) visa reduzir a complexidade de instanciação
    de objetos que dependem de outros objetos para serem criados, com as
    fachadas oferecendo uma interface mais simples para essa criação.

    São muito usadas em bibliotecas e frameworks para "esconder" os
    detalhes internos da implementação de uma classe.
    '''

    def __init__(self, component_one=None, component_two=None):
        '''
        Algumas implementações de facade podem permitir a injeção de
        seus componentes internos para evitar a alocação de novos recursos
        e, principalmente, para facilitar a criação de testes unitários
        ou de integração da facade
        '''
        self.__component_one = component_one or ComponentOne()
        self.__component_two = component_two or ComponentTwo()

    def operation(self):
        '''
        As operações implementadas pelas facades fazem uso de N métodos
        de seus componentes de acordo com as regras de negócio que ela
        implementa, facilitando o acesso dessas operações pelo usuário,
        no caso de uma biblioteca.

        Facades preferencialmente não devem adicionar novos comportamentos
        as operações de seus componentes, sendo responsáveis apenas por
        operá-los.
        '''
        result_one = self.__component_one.operation()
        result_two = self.__component_two.operation()

        return f'Executed {result_one} and {result_two} with Facade'


class StaticFacade:
    '''
    Facades também são comunmente implementadas utilizando-se puramente
    de métodos estáticos para realizar as operações com seus componentes,
    porém esse padrão dificulta a criação e manutenção de testes com a
    facade.

    Nesses casos a responsabilidade de instanciação dos componentes
    recai sobre os métodos estáticos da facade, com o uso de argumentos
    com os objetos dos componenetes também não sendo comum.
    '''
    @staticmethod
    def operation():
        component_one = ComponentOne()
        component_two = ComponentTwo()

        result_one = component_one.operation()
        result_two = component_two.operation()

        return f'Executed {result_one} and {result_two} with Static Facade'


class ComponentOne:
    def operation(self):
        return 'componente one operation'


class ComponentTwo:
    def operation(self):
        return 'componente two operation'


if __name__ == '__main__':
    # Aplicando os métodos dos componentes sem facades
    component_one = ComponentOne()
    component_two = ComponentTwo()

    print(f'Executed {component_one.operation()} and {component_two.operation()}')

    # Aplicando os métodos dos componentes com facades
    facade = Facade()

    print(facade.operation())  # Usando facade instanciada
    print(StaticFacade.operation())  # Usando facade estática
