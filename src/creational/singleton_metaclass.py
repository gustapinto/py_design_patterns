class Singleton(type):
    '''
    Singleton busca oferecer um ponto de acesso único e centralizado
    para as informações de um ojbeto, assim sendo esse padrão de projeto
    busca manter apenas uma instância do objeto

    Nesse exemplo Singleton é definido como uma metaclasse, que são
    classes especiais, voltadas a criação e composição de outras classes
    '''
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            '''
            Cria uma nova instância do Singleton, caso nenehuma tenha
            sido criada anteriormente e a adiciona ao controle de
            instancias
            '''
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance

        # Retorna a instancia privada do Singleton
        return cls.__instances[cls]


class ConcreteSingleton(metaclass=Singleton):
    '''
    Enquanto a classe abstrata de Singleton é focada em gerenciar a
    lógica de criação da instância suas classes concretas visam a
    manutenção das regras de negócio
    '''

    def operation(self):
        pass


if __name__ == '__main__':
    singleton1 = ConcreteSingleton()
    singleton2 = ConcreteSingleton()

    # Verificando se ambas as intancias do Singleton realmente apontam
    # para a mesma instancia em memória
    if id(singleton1) == id(singleton2):
        print('Singleton worked :D')
    else:
        print('Singleton did not worked :c')
