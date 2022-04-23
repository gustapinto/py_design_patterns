from abc import ABC, abstractmethod


class Strategy(ABC):
    '''
    Strategy (estratégia) visa oferecer uma interface simplificada para
    lidarmos com multiplas implementações que retornam os mesmos 
    resultados finais ("forma"), fazendo isso de forma que o
    comportamento dos algoritimos sejam abstraídos em suas próprias classes,
    com o objeto strategy lidando apenas com a escolha do algoritimo.
    '''

    @abstractmethod
    def operation(self):
        '''
        A strategy em si opera apenas como uma interface para os métodos
        ou funções que irão fazer uso de sua implementação, esses sim irão
        implementar a lógica e regras de negócios de seleção.
        '''
        pass


class ConcreteStrategyOne(Strategy):
    def operation(self):
        return 'concrete strategy one'


class ConcreteStrategyTwo(Strategy):
    def operation(self):
        return 'concrete strategy two'


class Context:
    '''
    A classe que realmente vai fazer uso das strategies
    '''

    def __init__(self, strategy):
        '''
        A classe de contexto deve aceitar uma strategy a partir de seu
        construtor, mas também deve garantir que a mesma possa ser 
        substituida livremente durante a execução do programa sem que um
        novo contexto seja instanciado.
        '''
        self.__strategy = strategy

    @property
    def strategy(self):
        '''
        A classe de contexto normalmente deve oferecer um ponto de acesso
        a strategy com a qual foi instranciada, pois o contexto apenas
        conhece uma parcela dos métodos da strategy, não fazendo uso de
        seu todo.
        '''
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy):
        '''
        Assim como o contexto torna a strategy acessível ele também deve
        permitir sua troca sem a necessidade de instanciação de um novo
        contexto, permitindo um usod mais flexível do mesmo
        '''
        self.__strategy = strategy

    def do_operation(self):
        '''
        Aplica a strategy concreta fornecida pelo usuário juntamente
        com as regras de negócio do contexto
        '''
        result = self.__strategy.operation()

        return f'Executed {result} with context {id(self)}'


if __name__ == '__main__':
    ctx = Context(ConcreteStrategyOne())

    print(ctx.do_operation())

    ctx.strategy = ConcreteStrategyTwo()

    print(ctx.do_operation())
