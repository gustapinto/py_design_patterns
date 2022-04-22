from abc import ABC


class Target:
    '''
    A classe principal, para qual outros objetos devem ser adaptados
    '''

    def request(self):
        return 'I am a request'


class Adaptee:
    '''
    Uma classe que deve ser adaptada para lidar com a interface do objeto
    principal
    '''

    def weird_request(self):
        return 'Sooo, i am a very very specific request'


class AdapterToTarget(Adaptee):
    '''
    Adapter (adaptadores) é um padrão de projeto que visa permitir que
    dois objetos ou classes que aplicam interfaces não compatíveis
    possam interoperar, criando uma interface que sirva como "tradutor"
    para qualquer objeto compatível com ela
    '''

    def request(self) -> str:
        return f'Adapted - {self.weird_request()}'


def client(target):
    '''
    A função ou método que suporta qualquer objeto que implemente a
    mesma interface que a classe principal (Target)
    '''
    try:
        print(target.request())
    except AttributeError:
        print('Ooops, this class is not compatible with Target')


if __name__ == '__main__':
    client(Target())

    # A classe Adaptee não funcionará com uma função feita para lidar com Target
    client(Adaptee())

    # Mas seu adapater vai
    client(AdapterToTarget())
