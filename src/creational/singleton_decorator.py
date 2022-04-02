def singleton(class_):
    '''
    Singleton busca oferecer um ponto de acesso único e centralizado
    para as informações de um ojbeto, assim sendo esse padrão de projeto
    busca manter apenas uma instância do objeto

    Nesse exemplo Singleton é definido um decorador, permitindo a criaçao
    desses de forma mais simples e idiomática
    '''
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            '''
            Cria uma nova instância do Singleton, caso nenehuma tenha
            sido criada anteriormente e a adiciona ao controle de
            instancias
            '''
            instances[class_] = class_(*args, **kwargs)

        return instances[class_]

    return getinstance


@singleton
class ConcreteSingleton:
    '''
    Enquanto o decorador de Singleton é focado em gerenciar a lógica de
    criação da instância, suas classes concretas visam a manutenção das
    regras de negócio
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
