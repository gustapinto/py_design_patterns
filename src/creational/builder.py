from abc import ABC, abstractmethod
from re import A


class Builder(ABC):
    '''
    Builder (construtor) é um padrão de projeto que busca oferecer um modo
    fácil de criação de objetos compostos ou complexos, permitindo que
    controlemos as características que esse vai possuir sem precisarmos
    instanciar muitas subclasses.

    Builder faz essa criação de objetos movendo a lógica de criação do mesmo
    fora de seu códigom, ou seja, sua instanciação é controlada por uma
    classe externa.

    A interface builder é a responsável por gerenciar quais são as regras
    de negócio que os construtores concretos devem implementar.
    '''
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass


class ConcreteBuilderOne(Builder):
    '''
    Os builders concretos são os responsáveis por dar vida a lógica de
    negócio definida pela classe Builder abstrata, providenciando uma
    forma concreta e aplicável de criar nocos produtos
    '''
    def __init__(self):
        self.reset()

    def reset(self):
        '''
        Os Builders devem possuir uma instancia "limpa" do objeto a 
        ser construído, por isso normalmente é definido um método
        que lide com a recriação do produto, para que possamos usar a
        mesma instancia do construtor para criarmos multiplos objetos
        '''
        self.__product = ProductOne()

    def product(self):
        '''
        Além do método de reinicialização de produtos o Builder também
        deve podr retornar o produto construído sem que esse interfira
        nas próximas construções
        '''
        product = self.__product
        self.reset()  # Reinicializa o builder para as próximas construções

        return product

    def produce_part_a(self):
        self.__product.add('Part A')

    def produce_part_b(self):
        self.__product.add('Part B')

    def produce_part_c(self):
        self.__product.add('Part C')


class ConcreteBuilderOneChain(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.__product = ProductOne()

    def product(self):
        product = self.__product
        self.reset()

        return product

    '''
    Builders também podem ser construidos de modo a retornarem sua própria
    instancia a cada produção, permitindo o uso de seus métodos como uma
    cadeia de demeter, embora esse método tenha caído em desuso, considerado
    um anti-padrão
    '''
    def produce_part_a(self):
        self.__product.add('Part A')
        return self

    def produce_part_b(self):
        self.__product.add('Part B')
        return self

    def produce_part_c(self):
        self.__product.add('Part C')
        return self


class ProductOne:
    def __init__(self):
        self.parts = []

    def add(self, part):
        '''
        Apesar do builder adicionar propriedades a objetos os produtos
        construídos que são responsáveis por saber como se montar,
        abstraindo essa responsabilidade do construtor
        '''
        self.parts.append(part)


if __name__ == '__main__':
    builder_one = ConcreteBuilderOne()

    builder_one.produce_part_a()
    builder_one.produce_part_b()

    product_ab = builder_one.product()

    builder_one.produce_part_c()

    product_c = builder_one.product()

    # Produtos montados pelo mesmo builder porém com partes diferenets
    print(product_ab.parts)
    print(product_c.parts)
    
    # Construindo um produto usando uma cadeia de deméter
    builder_one_chain = ConcreteBuilderOneChain()
    builder_one_chain.produce_part_a().produce_part_b().produce_part_c()

    product_abc = builder_one_chain.product()

    builder_one_chain.produce_part_a()

    product_a = builder_one_chain.product()

    print(product_abc.parts)
    print(product_a.parts)
