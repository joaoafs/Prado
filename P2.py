"""
FP2021 @ IST - Projeto 2 - O Prado
Feito por Joao Amadeu
"""

# -------------------------------------- 2.1.1 TAD posicao -------------------------------------- #
#                                                                                                 #
#       (O TAD posicao e usado para representar uma posicao (x, y) de um prado arbitrariamente    #
#        grande, sendo x e y dois valores inteiros nao negativos.)                                #
#                                                                                                 #
# ----------------------------------------------------------------------------------------------- #

#Construtor
def cria_posicao(num1,num2):
    """
    Cria posicao

    :param num1: int
    :param num2: int
    :return: posicao

    Esta funcao recebe os valores correspondentes as coordenadas de uma
    posicao e devolve a posicao correspondente
    Exemplo de uso:

    >>> p1 = cria_posicao(2, 3)
    >>> print(p1)
    (2,3)
    """

    if type(num1) == int and type(num2) == int and num1 >= 0 and num2 >= 0:
        return (num1,num2)
    raise ValueError('cria_posicao: argumentos invalidos')

def cria_copia_posicao(pos):
    """
    Cria copia da posicao

    :param pos: posicao
    :return: posicao

    Esta funcao recebe uma posicao e devolve uma copia nova da posicao
    Exemplo de uso:

    >>> p1 = cria_copia_posicao((1, 1))
    >>> print(p1)
    (1,1)
    """

    if type(pos) == dict:
        pos = tuple(pos.values())
    return tuple(pos[:])

#Seletores
def obter_pos_x(pos):
    """
    Obtem coluna da posicao

    :param pos: posicao
    :return: int

    Esta funcao devolve a componente x da posicao.
    Exemplo de uso:

    >>> obter_pos_x(cria_posicao(3,4))
    3
    """

    if type(pos) == dict:
        aux = tuple(pos)
        return pos[aux[0]]
    return pos[0]

def obter_pos_y(pos):
    """
    Obtem linha da posicao

    :param pos: posicao
    :return: int

    Esta funcao devolve a componente y da posicao.
    Exemplo de uso:

    >>> obter_pos_y(cria_posicao(3,4))
    4
    """

    if type(pos) == dict:
        aux = tuple(pos)
        return pos[aux[1]]
    return pos[1]

#Reconhecedor
def eh_posicao(pos):
    """
    Verifica Argumento (posicao)

    :param pos: universal
    :return: int

    Esta funcao devolve True caso o seu argumento seja um TAD posicao e False caso contrario.
    Exemplo de uso:

    >>> eh_posicao((2,1))
    True
    >>> eh_posicao((2,"1"))
    False
    """

    return len(pos) == 2 and type(obter_pos_x(pos)) == int  and type(obter_pos_y(pos)) == int and \
        obter_pos_x(pos) >= 0 and obter_pos_y(pos) >= 0

#Teste
def posicoes_iguais(pos1, pos2):
    """
    Verifica se pos1 e pos2 sao posicoes iguais

    :param pos1: posicao
    :param pos2: posicao
    :return: bool

    Esta funcao devolve True apenas se pos1 e pos2 sao posicoes e sao iguais.
    Exemplo de uso:

    >>> posicoes_iguais((2,1), (2,1))
    True
    """

    return eh_posicao(pos1) and eh_posicao(pos2) and pos1 == pos2

#Transformador
def posicao_para_str(pos):
    """
    Transforma posicao em string

    :param pos: posicao
    :return: str

    Esta funcao devolve a cadeia de caracteres "(x, y)" que representa o
    seu argumento, sendo os valores x e y as coordenadas de pos.
    Exemplo de uso:

    >>> posicao_para_str((4,6))
    '(4, 6)'
    """

    return str(cria_posicao(obter_pos_x(pos),obter_pos_y(pos)))

#Funcoes de alto nivel
def obter_posicoes_adjacentes(pos):
    """
    Obtem posicoes adjacentes

    :param pos: posicao
    :return: tuple

    Esta funcao devolve um tuplo com as posicoes adjacentes a posicao pos,
    comecando pela posicao acima de pos e seguindo no sentido horario.
    Exemplo de uso:

    >>> obter_posicoes_adjacentes(cria_posicao(2,2))
    ((2, 1), (3, 2), (2, 3), (1, 2))
    """

    res = ()
    adjacentes = {"c" : (obter_pos_x(pos),obter_pos_y(pos)-1), "d": (obter_pos_x(pos)+1,obter_pos_y(pos)),
                  "b" : (obter_pos_x(pos),obter_pos_y(pos)+1), "e": (obter_pos_x(pos)-1,obter_pos_y(pos))}
    for p in ("c","d","b","e"):
        if eh_posicao(adjacentes[p]):
            res += (adjacentes[p],)
    return res

def ordenar_posicoes(tuplo):
    """
    Ordena posicoes pela ordem de leitura do prado

    :param tuplo: tuple
    :return: tuple

    Esta funcao devolve um tuplo contendo as mesmas posicoes do tuplo fornecido como argumento,
    ordenadas de acordo com a ordem de leitura do prado.
    Exemplo de uso:

    >>> ordenar_posicoes(obter_posicoes_adjacentes(cria_posicao(2,2)))
    [(2, 1), (1, 2), (3, 2), (2, 3)]
    """

    tuplo_aux = ()
    for pos in tuplo:
        if type(pos) == dict:
            pos = cria_posicao(obter_pos_x(pos),obter_pos_y(pos))
            tuplo_aux += (pos,)
            tuplo = tuplo_aux
        else:
            tuplo_aux += (tuple(pos),)
            tuplo = tuplo_aux
    return sorted(tuplo, key=lambda k: [k[1], k[0]])


# -------------------------------------- 2.1.2 TAD animal -------------------------------------- #
#                                                                                                #
#       (O TAD animal e usado para representar os animais do simulador de ecossistemas que       #
#       habitam o prado, existindo de dois tipos: predadores e presas. Os predadores sao         #
#       caracterizados pela especie, idade, frequencia de reproducao, fome e frequencia de       #
#       alimentacao. As presas sao apenas caracterizadas pela especie, idade e frequencia        #
#       de reproducao.)                                                                          #
#                                                                                                #
# ---------------------------------------------------------------------------------------------- #

#Construtor
def cria_animal(especie,freq_r,freq_a):
    """
    Cria animal

    :param especie: str
    :param freq_r: int
    :param freq_a: int
    :return: animal

    Esta funcao recebe uma cadeia de caracteres nao vazia correspondente a especie do animal e
    dois valores inteiros correspondentes a frequencia de reproducao e a frequencia de alimentacao
    e devolve o animal.
    Exemplo de uso:

    >>> cria_animal("rabbit", -5, 0)
    Traceback (most recent call last): <...>
    ValueError: cria_animal: argumentos invalidos
    >>> cria_animal("rabbit", 5, 0)
    ['rabbit', 5, 0, 0, 0]
    """

    if type(especie) == str and len(especie) > 0 and type(freq_r) == int and type(freq_a) == int \
            and freq_r > 0 and freq_a >= 0:
        return list((especie,freq_r,freq_a,0,0))
    raise ValueError('cria_animal: argumentos invalidos')

def cria_copia_animal(animal):
    """
     Cria copia do animal

     :param animal: animal
     :return: animal

     Esta funcao recebe um animal (predador ou presa) e devolve uma nova copia do animal.
     Exemplo de uso:

     >>> cria_copia_animal(['rabbit', 5, 0, 0, 0])
     ['rabbit', 5, 0, 0, 0]
     """

    if type(animal) == dict:
        animal = list(animal.values())
    return list(animal[:])

#Seletores
def obter_especie(animal):
    """
     Obtem especie do animal

     :param animal: animal
     :return: str

     Esta funcao devolve a cadeia de caracteres correspondente a especie do animal.
     Exemplo de uso:

     >>> obter_especie(cria_animal("rabbit", 5, 0))
     'rabbit'
     """

    if type(animal) == dict:
        animal = list(animal.values())
    return animal[0]

def obter_freq_reproducao(animal):
    """
     Obtem frequencia de reproducao do animal

     :param animal: animal
     :return: int

     Esta funcao devolve a frequencia de reproducao do animal.
     Exemplo de uso:

     >>> obter_freq_reproducao(cria_animal("rabbit", 5, 0))
     5
     """

    if type(animal) == dict:
        animal = list(animal.values())
    return animal[1]

def obter_freq_alimentacao(animal):
    """
     Obtem frequencia de alimentacao do animal

     :param animal: animal
     :return: int

     Esta funcao devolve a frequencia de alimentacao do animal.
     Exemplo de uso:

     >>> obter_freq_alimentacao(cria_animal("rabbit", 5, 0))
     0
     """

    if type(animal) == dict:
        animal = list(animal.values())
    return animal[2]

def obter_idade(animal):
    """
     Obtem idade do animal

     :param animal: animal
     :return: int

     Esta funcao devolve a idade do animal.
     Exemplo de uso:

     >>> obter_idade(cria_animal("rabbit", 5, 0))
     0
     """

    if type(animal) == dict:
        animal = list(animal.values())
    return animal[3]

def obter_fome(animal):
    """
     Obtem fome do animal

     :param animal: animal
     :return: int

     Esta funcao devolve a fome do animal
     Exemplo de uso:

     >>> obter_fome(cria_animal("rabbit", 5, 0))
     0
     """

    if type(animal) == dict:
        animal = list(animal.values())
    return animal[4]

#Modificadores
def aumenta_idade(animal):
    """
     Aumenta a idade do animal

     :param animal: animal
     :return: animal

     Esta funcao modifica destrutivamente o animal incrementando o valor da sua idade
     em uma unidade, e devolve o proprio animal.
     Exemplo de uso:

     >>> aumenta_idade(aumenta_idade(cria_animal("rabbit", 5, 0)))
     ['rabbit', 5, 0, 2, 0]
     """

    if type(animal) == dict:
        animal = list(animal.values())
    animal[3] += 1
    return animal

def reset_idade(animal):
    """
     Restabelece a idade do animal de volta a zero

     :param animal: animal
     :return: animal

     Esta funcao modifica destrutivamente o animal definindo o valor da sua
     idade igual a 0, e devolve o proprio animal.
     Exemplo de uso:

     >>> reset_idade(['rabbit', 5, 0, 2, 0])
     ['rabbit', 5, 0, 0, 0]
     """

    if type(animal) == dict:
        animal = list(animal.values())
    animal[3] = 0
    return animal

def aumenta_fome(animal):
    """
     Aumenta a fome do animal

     :param animal: animal
     :return: animal

     Esta funcao modifica destrutivamente o animal predador incrementando o valor da sua
     fome em uma unidade, e devolve o proprio animal. Esta operacao nao modifica os animais presa.
     Exemplo de uso:

     >>> aumenta_fome(cria_animal("fox", 5, 3))
     ['fox', 5, 3, 0, 1]
     """

    if type(animal) == dict:
        animal = list(animal.values())
    if obter_freq_alimentacao(animal) > 0:
        animal[4] += 1
    return animal

def reset_fome(animal):
    """
     Restabelece a fome do animal de volta a zero

     :param animal: animal
     :return: animal

     Esta funcao modifica destrutivamente o animal predador definindo o valor
     da sua fome igual a 0, e devolve o proprio animal. Esta operacao nao modifica os animais presa.
     Exemplo de uso:

     >>> reset_fome(['fox', 5, 3, 0, 1])
     ['fox', 5, 3, 0, 0]
     """

    if type(animal) == dict:
        animal = list(animal.values())
    animal[4] = 0
    return animal

#Reconhecedores
def eh_animal(animal):
    """
     Verifica Argumento (animal)

     :param animal: universal
     :return: bool

     Esta funcao devolve True caso o seu argumento seja um TAD animal e False caso contrario.
     Exemplo de uso:

     >>> eh_animal(['fox', 5, 3, 0, 0])
     True
     """

    return len(animal) == 5 and type(obter_especie(animal)) == str and type(obter_freq_reproducao(animal)) == int \
            and type(obter_freq_alimentacao(animal)) == int and type(obter_idade(animal)) == int and \
            type(obter_fome(animal)) == int and obter_freq_reproducao(animal) > 0 and \
            obter_freq_alimentacao(animal) >= 0 and obter_idade(animal) >= 0 and obter_fome(animal) >= 0

def eh_predador(animal):
    """
     Verifica Argumento (predador)

     :param animal: universal
     :return: bool

     Esta funcao devolve True caso o seu argumento seja um TAD animal do tipo predador e False caso contrario.
     Exemplo de uso:

     >>> eh_predador(['fox', 5, 3, 0, 0])
     True
     """

    return eh_animal(animal) and obter_freq_alimentacao(animal) > 0

def eh_presa(animal):
    """
     Verifica Argumento (presa)

     :param animal: universal
     :return: bool

     Esta funcao devolve True caso o seu argumento seja um TAD animal do tipo presa e False caso contrario.
     Exemplo de uso:

     >>> eh_presa(['fox', 5, 3, 0, 0])
     False
     """

    return eh_animal(animal) and obter_freq_alimentacao(animal) == 0 and obter_fome(animal) == 0

#Teste
def animais_iguais(animal1, animal2):
    """
     Compara animais e verifica se sao iguais

     :param animal1: animal
     :param animal2: animal
     :return: bool

     Esta funcao devolve devolve True apenas se animal1 e animal2 sao animais e sao iguais.
     Exemplo de uso:

     >>> animais_iguais(cria_animal("rabbit", 5, 0), cria_animal("rabbit", 5, 0))
     True
     """

    return eh_animal(animal1) and eh_animal(animal2) and animal1 == animal2

#Transformadores
def animal_para_char(animal):
    """
     Retorna letra (caracter) correspondente ao animal

     :param animal: animal
     :return: str

     Esta funcao devolve a cadeia de caracteres dum unico elemento correspondente ao primeiro caracter
     da especie do animal passado como argumento, em maiuscula para animais predadores e em minuscula
     para animais presa.
     Exemplo de uso:

     >>> animal_para_char(cria_animal("fox", 5, 3))
     'F'
     """

    if eh_predador(animal):
        return list(obter_especie(animal))[0].upper()
    else:
        return list(obter_especie(animal))[0].lower()

def animal_para_str(animal):
    """
     Devolve string do animal

     :param animal: animal
     :return: str

     Esta funcao devolve a cadeia de caracteres que representa o animal como pedido no enunciado.
     Exemplo de uso:

     >>> animal_para_str(cria_animal("fox", 5, 3))
     'fox [0/5;0/3]'
     """

    if eh_predador(animal):
        return str(obter_especie(animal))+ " ["+ str(obter_idade(animal))+"/"+str(obter_freq_reproducao(animal))+\
               ";"+str(obter_fome(animal))+"/"+str(obter_freq_alimentacao(animal))+"]"
    return str(obter_especie(animal)) + " [" + str(obter_idade(animal)) + "/" + str(obter_freq_reproducao(animal))+"]"

#Funcoes de alto nivel
def eh_animal_fertil(animal):
    """
     Verifica se animal esta fertil

     :param animal: animal
     :return: bool

     Esta funcao devolve True caso o animal tenha atingido a idade de reproducao e False caso contrario.
     Exemplo de uso:

     >>> eh_animal_fertil(["sheep",2,0,2,0])
     True
     """

    if eh_animal(animal) == True and obter_idade(animal) == obter_freq_reproducao(animal):
        return True
    else:
        return False

def eh_animal_faminto(animal):
    """
     Verifica se animal esta faminto

     :param animal: animal
     :return: bool

     Esta funcao devolve True caso o animal tenha atingindo um valor de fome igual ou superior a
     sua frequencia de alimentacao e False caso contrario. As presas devolvem sempre False.
     Exemplo de uso:

     >>> eh_animal_faminto(["sheep",2,0,0,0])
     False
     >>> eh_animal_faminto(["fox",5,3,0,3])
     True
     """

    if eh_animal(animal) == True and obter_fome(animal) >= obter_freq_alimentacao(animal) and eh_presa(animal) == False:
        return True
    else:
        return False

def reproduz_animal(animal):
    """
     Reproduz animal, cria bebe

     :param animal: animal
     :return: animal

     Esta funcao recebe um animal a devolvendo um novo animal da mesma especie com idade e fome igual a 0,
     e modificando destrutivamente o animal passado como argumento alterando a sua idade para 0.
     Exemplo de uso:

     >>> reproduz_animal(aumenta_idade(aumenta_idade(cria_animal("sheep",2,0))))
     ['sheep', 2, 0, 0, 0]
     """

    animal = reset_idade(animal)
    new_animal = cria_copia_animal(animal)
    new_animal = reset_fome(new_animal)
    return new_animal

# -------------------------------------- 2.1.3 TAD prado --------------------------------------- #
#                                                                                                #
#       (O TAD prado e usado para representar o mapa do ecossistema e as animais que se          #
#        encontram dentro.)                                                                      #
#                                                                                                #
# ---------------------------------------------------------------------------------------------- #

#Construtor
def cria_prado(d,r,a,p):
    """
     Cria prado

     :param d: posicao
     :param r: tuple
     :param a: tuple
     :param p: tuple
     :return: prado

     Esta funcao recebe uma posicao d correspondente a posicao que ocupa a montanha do canto inferior direito
     do prado, um tuplo r correspondentes aos rochedos que nao sao as montanhas dos limites exteriores do prado,
     um tuplo a de 1 ou mais animais, e um tuplo p da mesma dimensao do tuplo a com as posicoes correspondentes
     ocupadas pelos animais; e devolve o prado que representa internamente o mapa e os animais presentes.
     Exemplo de uso:

     >>> cria_prado(cria_posicao(11, 4),(cria_posicao(4,2), cria_posicao(5,2)), \
                tuple(cria_animal("rabbit", 5, 0) for i in range(3))+ (cria_animal("lynx", 20, 15),), \
                tuple(cria_posicao(p[0],p[1]) for p in ((5,1),(7,2),(10,1),(6,1))))
     [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0],\
     ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     """

    if eh_posicao(d) != True or type(r) != tuple or type(a) != tuple or type(p) != tuple or \
        len(a) < 1 or len(p) < 1 or len(a) != len(p):
        raise ValueError("cria_prado: argumentos invalidos")
    if obter_pos_x(d) < 3 or obter_pos_y(d) < 3:
        raise ValueError("cria_prado: argumentos invalidos")
    if r != ():
        for pos in r:
            if not eh_posicao(pos):
                raise ValueError("cria_prado: argumentos invalidos")
            if obter_pos_x(pos) == 0 or obter_pos_x(pos) >= obter_pos_x(d) or obter_pos_y(pos) == 0 or \
                    obter_pos_y(pos) >= obter_pos_y(d):
                raise ValueError("cria_prado: argumentos invalidos")
    for pos2 in p:
        if not eh_posicao(pos2):
            raise ValueError("cria_prado: argumentos invalidos")
        if obter_pos_x(pos2) == 0 or obter_pos_x(pos2) >= obter_pos_x(d) or obter_pos_y(pos2) == 0 or \
                obter_pos_y(pos2) >= obter_pos_y(d):
            raise ValueError("cria_prado: argumentos invalidos")
        if pos2 in r:
            raise ValueError("cria_prado: argumentos invalidos")
    return [d,r,a,p]

def cria_copia_prado(prado):
    """
     Cria copia prado

     :param prado: prado
     :return: prado

     Esta funcao recebe um prado e devolve uma nova copia do prado.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> cria_copia_prado(prado)
     [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0],\
     ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     """

    if type(prado) == dict:
        prado = list(prado.values())
    return list(prado[:])

#Seletores
def obter_tamanho_x(prado):
    """
     Obtem tamanho da dimensao Nx do Prado

     :param prado: prado
     :return: int

     Esta funcao devolve o valor inteiro que corresponde a dimensao Nx do prado.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> obter_tamanho_x(prado)
     12
     """

    if type(prado) == dict:
        prado = list(prado.values())
    return prado[0][0] + 1

def obter_tamanho_y(prado):
    """
     Obtem tamanho da dimensao Ny do Prado

     :param prado: prado
     :return: int

     Esta funcao devolve o valor inteiro que corresponde a dimensao Ny do prado.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> obter_tamanho_y(prado)
     5
     """

    if type(prado) == dict:
        prado = list(prado.values())
    return prado[0][1] + 1

def obter_numero_predadores(prado):
    """
     Obtem numero de animais predadores

     :param prado: prado
     :return: int

     Esta funcao devolve o numero de animais predadores no prado.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> obter_numero_predadores(prado)
     1
     """

    if type(prado) == dict:
        prado = list(prado.values())
    contador = 0
    for predador in prado[2]:
        if eh_predador(predador):
            contador +=1
    return contador

def obter_numero_presas(prado):
    """
     Obtem numero de animais presas

     :param prado: prado
     :return: int

     Esta funcao devolve o numero de animais presas no prado.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> obter_numero_presas(prado)
     3
     """

    if type(prado) == dict:
        prado = list(prado.values())
    contador = 0
    for presa in prado[2]:
        if eh_presa(presa):
            contador +=1
    return contador

def obter_posicao_animais(prado):
    """
     Obtem posicoes ocupadas por animais (presas+predadores)

     :param prado: prado
     :return: tuple

     Esta funcao devolve um tuplo contendo as posicoes do prado ocupadas por animais,
     ordenadas em ordem de leitura do prado.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> obter_posicao_animais(prado)
     ((5, 1), (6, 1), (10, 1), (7, 2))
     """

    if type(prado) == dict:
        prado = list(prado.values())
    return tuple(ordenar_posicoes(prado[3]))

def obter_animal(prado,pos):
    """
     Obtem animal da respestiva posicao

     :param prado: prado
     :param pos: posicao
     :return: animal

     Esta funcao devolve devolve o animal do prado que se encontra na posicao pos.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> obter_animal(prado,(6,1))
     ['lynx', 20, 15, 0, 0]
     """

    if type(prado) == dict:
        prado = list(prado.values())
    n = 0
    while prado[3][n] != pos:
        n +=1
    return prado[2][n]

#Modificadores
def eliminar_animal(prado,pos):
    """
     Elimina animal da respestiva posicao

     :param prado: prado
     :param pos: posicao
     :return: prado

     Esta funcao modifica destrutivamente o prado eliminando o animal da posicao pos deixando-a livre.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> eliminar_animal(prado,(6,1))
     [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0]), \
     ((5, 1), (7, 2), (10, 1))]
     """

    n = 0
    lista_animais = list(prado[2])
    lista_pos = list(prado[3])
    while prado[3][n] != pos:
        n += 1
    del lista_animais[n]
    del lista_pos[n]
    prado[2] = tuple(lista_animais)
    prado[3] = tuple(lista_pos)
    return prado

def mover_animal(prado,pos_i,pos_f):
    """
     Movimenta animal da respestiva posicao inicial para a posicao escolhida

     :param prado: prado
     :param pos_i: posicao
     :param pos_f: posicao
     :return: prado

     Esta funcao modifica destrutivamente o prado movimentando o animal da posicao pos_i para
     a nova posicao pos_f, deixando livre a posicao onde se encontrava (pos_i)
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> mover_animal(prado,(6,1),(7,1))
     [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
     ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (7, 1))]
     """

    n = 0
    lista_pos = list(prado[3])
    while not posicoes_iguais(prado[3][n],pos_i):
        n += 1
    lista_pos[n] = pos_f
    prado[3] = tuple(lista_pos)
    return prado

def inserir_animal(prado,animal,pos):
    """
     Insere animal na respestiva posicao

     :param prado: prado
     :param animal: animal
     :param pos: posicao
     :return: prado

     Esta funcao modifica destrutivamente o prado acrescentando na posicao pos do prado o
     animal passado como argumento.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> inserir_animal(prado,cria_animal("sheep",2,0,),(7,1))
     [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
     ['lynx', 20, 15, 0, 0], ['sheep', 2, 0, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1), (7, 1))]
     """

    if pos not in prado[3]:
        prado[2] += (animal,)
        prado[3] += (pos,)
    else:
        eliminar_animal(prado,pos)
        inserir_animal(prado,animal,pos)
    return prado

#Reconhecedores
def eh_prado(prado):
    """
     Verifica Argumento (prado)

     :param prado: prado
     :return: bool

     Esta funcao devolve True caso o seu argumento seja um TAD prado e False caso contrario.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> eh_prado(prado)
     True
     """

    if type(prado) == dict:
        prado = list(prado.values())
    n,j = 0,1
    if type(prado) != list or len(prado) != 4 or eh_posicao(prado[0]) == False or type(prado[1]) != tuple \
            or type(prado[2]) != tuple or type(prado[3]) != tuple:
        return False
    if len(prado[2]) < 1 or len(prado[2]) != len(prado[3]):
        return False
    if len(prado[1]) > 0:
        for e in prado[1]:
            if not eh_posicao(e):
                return False
    for animal in prado[2]:
        if not eh_animal(animal):
            return False
    for pos in prado[3]:
        if not eh_posicao(pos) or len(pos) == 0 or pos in prado[1] \
                or obter_pos_x(pos) == 0 or obter_pos_y(pos) == 0 \
                or obter_pos_y(pos) == obter_pos_y(prado[0]) \
                or obter_pos_x(pos) == obter_pos_x(prado[0]):
            return False
    while n < len(obter_posicao_animais(prado)):
        while j < len(obter_posicao_animais(prado)):
            if obter_posicao_animais(prado)[n] == obter_posicao_animais(prado)[j]:
                return False
            j+=1
        n += 1
        j = n + 1
    return True

def eh_posicao_animal(prado,pos):
    """
     Verifica Argumento (posicao ocupada por um animal)

     :param prado: prado
     :param pos: posicao
     :return: bool

     Esta funcao devolve True apenas no caso da posicao do prado estar ocupada por um animal.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> eh_posicao_animal(prado,(4,2))
     False
     """

    if type(prado) == dict:
        prado = list(prado.values())
    return pos in obter_posicao_animais(prado) and eh_prado(prado) and eh_posicao(pos)

def eh_posicao_obstaculo(prado,pos):
    """
     Verifica Argumento (posicao ocupada por um animal)

     :param prado: prado
     :param pos: posicao
     :return: bool

     Esta funcao devolve True apenas no caso da posicao do prado corresponder a uma montanha ou rochedo.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> eh_posicao_obstaculo(prado,(4,2))
     True
     >>> eh_posicao_obstaculo(prado,(11,4))
     True
     """

    if type(prado) == dict:
        prado = list(prado.values())
    if eh_prado(prado) == False or eh_posicao(pos) == False:
        return False
    if obter_pos_x(pos) == 0 or obter_pos_y(pos) == 0 or obter_pos_x(pos) == obter_pos_x(prado[0]) \
        or obter_pos_y(pos) == obter_pos_y(prado[0]):
        return True
    if pos in prado[1]:
        return True
    return False

def eh_posicao_livre(prado,pos):
    """
     Verifica Argumento (posicao livre)

     :param prado: prado
     :param pos: posicao
     :return: bool

     Esta funcao devolve True apenas no caso da posicao p do prado corresponder a um
     espaco livre (sem animais, nem obstaculos).
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> eh_posicao_livre(prado,(4,2))
     False
     >>> eh_posicao_livre(prado,(1,1))
     True
     """

    if eh_posicao_animal(prado,pos) == False and eh_posicao_obstaculo(prado,pos) == False and eh_prado(prado) == True \
            and eh_posicao(pos) == True:
        return True
    return False

#Teste
def prados_iguais(prado1,prado2):
    """
     Compara prados e verifica se sao iguais

     :param prado1: prado
     :param prado2: prado
     :return: bool

     Esta funcao devolve True apenas se prado1 e prado2 forem prados e forem iguais.
     Exemplo de uso:

     >>> prado1 = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> prado2 = cria_copia_prado(prado1)
     >>> prados_iguais(prado1,prado2)
     True
     """

    return eh_prado(prado1) and eh_prado(prado2) and prado1 == prado2

#Transformador
def prado_para_str(prado):
    """
     Obtem string do prado

     :param prado: prado
     :return: str

     Esta funcao devolve uma cadeia de caracteres que representa o prado como pedido no enunciado.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> prado_para_str(prado)
     '+----------+\n|....rL...r|\n|...@@.r...|\n|..........|\n+----------+'
     """

    if type(prado) == dict:
        prado = list(prado.values())
    res,res_f = "",""
    res += "+{}+\n".format("-"*(obter_pos_x(prado)[0]-1))
    res += "|{}|\n".format("."*(obter_pos_x(prado)[0]-1)) * (obter_pos_y(prado[0])-1)
    res += "+{}+".format("-"*(obter_pos_x(prado)[0]-1))
    lista_aux = list(res)
    for pos in prado[3]:
        lista_aux[(prado[0][0] + 2) * pos[1] + pos[0]] = animal_para_char(obter_animal(prado,pos))
    for obstaculo in prado[1]:
        lista_aux[(prado[0][0] + 2) * obstaculo[1] + obstaculo[0]] = "@"
    for caracter in lista_aux:
        res_f+= caracter
    return res_f


#Funcoes de alto nivel
def obter_valor_numerico(prado,pos):
    """
     Obtem valor numerico da posicao no prado

     :param prado: prado
     :param pos: posicao
     :return: int

     Esta funcao devolve o valor numerico da posicao correspondente a ordem de leitura no prado.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> obter_valor_numerico(prado,(5,1))
     17
     """

    if obter_pos_x(pos) <= obter_pos_x(prado[0]) and pos[1] <= obter_pos_y(prado[0]) and eh_posicao(pos) == True:
            return (obter_pos_x(prado[0]) + 1) * obter_pos_y(pos) + obter_pos_x(pos)

def obter_movimento(prado,pos):
    """
     Devolve movimento(posicao "nova") para certo animal, na posicao pos, consoante as regras estipuladas

     :param prado: prado
     :param pos: posicao
     :return: posicao

     Esta funcao devolve a posicao seguinte do animal na posicao pos dentro do prado de acordo com
     as regras de movimento dos animais no prado.
     Exemplo de uso:

     >>> prado = [(11, 4), ((4, 2), (5, 2)), (['rabbit', 5, 0, 0, 0], ['rabbit', 5, 0, 0, 0], \
            ['rabbit', 5, 0, 0, 0], ['lynx', 20, 15, 0, 0]), ((5, 1), (7, 2), (10, 1), (6, 1))]
     >>> obter_movimento(prado,(5,1))
     (4, 1)
     """

    if type(prado) == dict:
        prado = list(prado.values())
    contador = 0
    pos_livres,pos_livres2 = [],[]
    animal = obter_animal(prado,pos)
    num = obter_valor_numerico(prado, pos)
    pos_adj = ordenar_posicoes(obter_posicoes_adjacentes(pos))
    pos_final = [pos_adj[0], pos_adj[-2], pos_adj[-1], pos_adj[1]]
    if eh_predador(animal):
        for pos_aux in pos_final:
            if pos_aux in obter_posicao_animais(prado):
                if eh_presa(obter_animal(prado,pos_aux)):
                    return pos_aux
            else:
                if eh_posicao_livre(prado,pos_aux):
                    contador += 1
                    pos_livres.append(pos_aux)
        if len(pos_livres) == 0:
            return pos
        else:
            aux = num % contador
            return pos_livres[aux]
    if eh_presa(animal):
        for pos_aux2 in pos_final:
            if eh_posicao_livre(prado,pos_aux2):
                contador += 1
                pos_livres2.append(pos_aux2)
        if len(pos_livres2) == 0:
            return pos
        else:
            aux2 = num%contador
            return pos_livres2[aux2]


# -------------------------------------- FUNÇOES ADICIONAIS -------------------------------------- #
#                                                                                                  #
#                                          #2.2.1 geracao                                          #
#                                                                                                  #
# ------------------------------------------------------------------------------------------------ #

def geracao(prado):
    """
     Executa uma geracao no prado

     :param prado: prado
     :return: prado

     Esta funcao e a funcao auxiliar que modifica o prado fornecido como argumento de
     acordo com a evolucao correspondente a uma geracao completa, e devolve o proprio
     prado. Isto e, seguindo a ordem de leitura do prado, cada animal (vivo) realiza o seu
     turno de acao de acordo com as regras descritas.
     Exemplo de uso:

     >>> prado = cria_prado(cria_posicao(11, 4),  (cria_posicao(4,2), cria_posicao(5,2)), \
                tuple(cria_animal("sheep", 2, 0) for i in range(3))+(cria_animal("wolf", 10, 3),),  \
                tuple(cria_posicao(p[0],p[1]) for p in ((2,2),(4,3),(10,2),(3,2))))
     >>> print(prado_para_str(geracao(prado)))
     +----------+
     |..W.......|
     |s..@@.....|
     |....s....s|
     +----------+
     """

    if type(prado) == dict:
        prado = list(prado.values())
    n = 0
    tamanho = len(prado[3])
    bubble_sort(prado)
    while n < tamanho:
        aux = obter_movimento(prado,prado[3][n])
        if eh_animal_fertil(prado[2][n]) and aux == prado[3][n]:
            n+=1
        else:
            aumenta_idade(obter_animal(prado,prado[3][n]))
        if eh_predador(prado[2][n]):
            aumenta_fome(prado[2][n])
            if eh_animal_faminto(prado[2][n]):
                eliminar_animal(prado, prado[3][n])
                tamanho -= 1
                continue
        if eh_animal_fertil(prado[2][n]):
            pos_aux = prado[3][n]
            mover_animal(prado,prado[3][n],obter_movimento(prado,prado[3][n]))
            bebe = reproduz_animal(prado[2][n])
            inserir_animal(prado,bebe,pos_aux)
        else:
            mover_animal(prado, prado[3][n], obter_movimento(prado, prado[3][n]))
        n += 1
    return prado


def bubble_sort(prado):
    """
     Funcao auxiliar (organiza posicoes)

     :param prado: prado
     :return: None

     Esta funcao tem o intuito de organizar as posicoes dos animais pela ordem de leitura do prado.
     Exemplo de uso:

     >>> prado = cria_prado(cria_posicao(11, 4),  (cria_posicao(4,2), cria_posicao(5,2)), \
                tuple(cria_animal("sheep", 2, 0) for i in range(3))+(cria_animal("wolf", 10, 3),),  \
                tuple(cria_posicao(p[0],p[1]) for p in ((2,2),(4,3),(10,2),(3,2))))
     >>> bubble_sort(prado)
     >>> print(prado)
     [(11, 4), ((4, 2), (5, 2)), (['sheep', 2, 0, 0, 0], ['wolf', 10, 3, 0, 0], ['sheep', 2, 0, 0, 0], \
     ['sheep', 2, 0, 0, 0]), ((2, 2), (3, 2), (10, 2), (4, 3))]
     """

    if type(prado) == dict:
        prado = list(prado.values())
    lista_pos = list(prado[3])
    lista_animais = list(prado[2])
    for i in range(len(lista_pos)):
        for j in range(len(lista_pos) - 1):
            if obter_valor_numerico(prado,lista_pos[j]) > obter_valor_numerico(prado,lista_pos[j+1]):
                lista_pos[j], lista_pos[j + 1] = lista_pos[j + 1], lista_pos[j]
                lista_animais[j], lista_animais[j + 1] = lista_animais[j + 1], lista_animais[j]
    prado[3] = tuple(lista_pos)
    prado[2] = tuple(lista_animais)

# -------------------------------------- FUNÇOES ADICIONAIS -------------------------------------- #
#                                                                                                  #
#                                    #2.2.2 simula ecossistema                                     #
#                                                                                                  #
# ------------------------------------------------------------------------------------------------ #

def simula_ecossistema(f,g,v):
    """
     Simula ecossistema, executa varias geracoes

     :param f: str
     :param g: int
     :param v: bool
     :return: tuplo

     Esta funcao e a funcao principal que permite simular o ecossistema de um
     prado. A funcao recebe uma cadeia de caracteres f, um valor inteiro g e um valor booleano v e
     devolve o tuplo de dois elementos correspondentes ao numero de predadores e
     presas no prado no fim da simulacao. A cadeia de caracteres f passada por argumento
     corresponde ao nome do ficheiro de configuracao da simula¸cao. O valor inteiro g corresponde
     ao numero de geracoes a simular. O argumento booleano v ativa o modo verboso
     (True) ou o modo quiet (False).
     Exemplo de uso:

     >>> simula_ecossistema("config.txt", 200, False)
     Predadores: 1 vs Presas: 3 (Gen. 0)
     +----------+
     |..........|
     |.mL@@....m|
     |...m......|
     +----------+
     Predadores: 0 vs Presas: 28 (Gen. 200)
     +----------+
     |mmmmmmmmmm|
     |mmm@@mmmmm|
     |mmmmmmmmmm|
     +----------+
     (0, 28)

     Observacao: "config.txt": ficheiro defenido e disponivel no enunciado
     """

    n,p,x = 2,0,0
    lista_f = []
    obstaculos,animais,pos_animais = (),(),()
    ficheiro = open(f,"r")
    for linhas in ficheiro:
        lista_f.append(eval(linhas))
    d = cria_posicao(lista_f[0][0],lista_f[0][1])
    for tuplo_obstaculo in lista_f[1]:
        obstaculos += (cria_posicao(tuplo_obstaculo[0],tuplo_obstaculo[1]),)
    while n < len(lista_f):
        animais += (cria_animal(lista_f[n][0],lista_f[n][1],lista_f[n][2]),)
        pos_animais += (cria_posicao(lista_f[n][3][0],lista_f[n][3][1]),)
        n += 1
    prado = cria_prado(d,obstaculos,animais,pos_animais)
    ficheiro.close()
    if v == False and type(v) == bool:
        contador_predadores = obter_numero_predadores(prado)
        contador_presas = obter_numero_presas(prado)
        print("Predadores: {} vs Presas: {} (Gen. {})".format(contador_predadores,contador_presas,0))
        print(prado_para_str(prado))
        while x < g:
            geracao(prado)
            x += 1
        contador_predadores = obter_numero_predadores(prado)
        contador_presas = obter_numero_presas(prado)
        print("Predadores: {} vs Presas: {} (Gen. {})".format(contador_predadores,contador_presas,g))
        print(prado_para_str(prado))
        return contador_predadores, contador_presas
    if v == True and type(v) == bool:
        contador_predadores = obter_numero_predadores(prado)
        contador_presas = obter_numero_presas(prado)
        print("Predadores: {} vs Presas: {} (Gen. {})".format(contador_predadores,contador_presas,0))
        print(prado_para_str(prado))
        while x < g:
            geracao(prado)
            contador_predadores = obter_numero_predadores(prado)
            contador_presas = obter_numero_presas(prado)
            print("Predadores: {} vs Presas: {} (Gen. {})".format(contador_predadores,contador_presas,x))
            print(prado_para_str(prado))
            x += 1
        return contador_predadores, contador_presas


# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
# ----------------------------------------------- FIM ----------------------------------------------- #
# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
