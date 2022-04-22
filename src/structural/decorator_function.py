def decorator(func):
    '''
    Decorators (decoradores) são padrões de projeto que visam adicionar
    novos comportamentos a funções já existenstes.

    Funções decoradoras são a forma mais comum e simples de decorador em
    Python, sendo normalmente utilizados para adicionar comportamentos
    que devem acontecer antes ou depois da execução de uma função.
    '''
    def wrapper():
        return f'Decorate {func()} by a function decorator'

    return wrapper


@decorator # Aplicando decoradores na definição da função
def operation_one():
    return 'operation one'


def operation_two():
    return 'operation two'


if __name__ == '__main__':
    # Aplicando decoradores em execução, normalmente mais utilizado
    # quando trabalhamos com uma factory de funções
    decorated_operation_two = decorator(operation_two)

    print(operation_one())
    print(operation_two())
    print(decorated_operation_two())
