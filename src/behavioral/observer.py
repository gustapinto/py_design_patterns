from abc import ABC, abstractmethod


class Observer(ABC):
    '''
    O padrão de observer (observador) visa implementar um modelo de
    diparo de métodos a partir de eventos, no qual sempre que um atributo
    de uma classe observável é mudado é realizada a notificação de seus
    observadores para que esses possam agir.
    '''
    @abstractmethod
    def update(self, subject):
        '''
        O método responsável por lidar com as atualizações no objeto que
        está sendo observado.
        '''
        pass


class Subject(ABC):
    '''
    Subject é o objeto observável, ele é o responsável por adicionar novos
    observadores e por notificá-los quando o atributo observável é
    atualizado.
    '''

    def __init__(self):
        self.__observers = []

    def attach(self, observer):
        '''
        O método responśavel por adicionar novos observadores a lista de
        notificação
        '''
        self.__observers.append(observer)

    def detach(self, observer):
        '''
        O método responsável por remover observadores da lista de
        notificação
        '''
        self.__observers.remove(observer)

    def detach_all(self):
        '''
        Algumas implementações de observáveis também permitem que todos
        os seus observadores sejam removidos de uma só vez, para que novos
        sejam conectados
        '''
        self.__observers = []

    def notify(self):
        '''
        É o metodo que lida com a notificação de todos os observadores,
        chamando seu método de atualização e passando o estado atual da
        instância observável
        '''
        for observer in self.__observers:
            observer.update(self)


class ConcreteObserverOne(Observer):
    def update(self, subject):
        '''
        Os observadores concretos são os responsáveis por reagir as
        atualizações de estado dos objetos observáveis, e enquanto os
        sujeitos não conhecem os observadores, esses conhecem os atributos
        públicos (getters) dos sujeitos
        '''
        print(f'Observer one: {subject.state}')


class ConcreteObserverTwo(Observer):
    def update(self, subject):
        print(f'Observer two: {subject.state}')


class ConcreteSubject(Subject):
    '''
    Os observáveis concretos são os responsáveis por definir quando e 
    porquê os observadores serão notificados, normalmente apenas uma
    fração do observável é responsável por lidar com os observadores, com
    o resto de seu código fonte implementando as regas de negócio.
    '''

    def __init__(self):
        self.__state = None
        super().__init__()

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        '''
        Note que o setter do atributo da classe observável é responsável
        tanto por atualizar seu estado quanto por disparar o notificador
        dos observadores
        '''
        self.__state = state
        self.notify()

    def operation(self):
        return 'A important operation'


if __name__ == '__main__':
    subject = ConcreteSubject()
    observer_one = ConcreteObserverOne()
    observer_two = ConcreteObserverTwo()

    subject.attach(observer_one)
    subject.attach(observer_two)

    subject.state = 'state'

    subject.detach(observer_two)

    subject.state = 'new state'

    subject.detach_all()

    subject.state = 'another new state'

    print(subject.operation())
