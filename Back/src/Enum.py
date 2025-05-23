from enum import Enum

class Types_Products(Enum):
    PULA_PULA_MEDIO = 'Pula Pula Médio'
    PULA_PULA_GRANDE = 'Pula Pula Grande'
    CASA_BOLINHA_PEQUENA = 'Casa de Bolinha Pequena'
    CASA_BOLINHA_GRANDE = 'Casa de Bolinha Grande'
    TOBOGA_INFLAVEL = 'Tobogã Inflável'
    FUTEBOL_SABAO_INFLAVEL = 'Futebol de Sabão Inflável'
    GUERRA_COTONETE_INFLAVEL = 'Guerra de Cotonete Inflável'
    CASTELINHO_INFLAVEL = 'Castelinho Inflável '
    PEBOLIM = 'Pebolim'
    FLIPERAMA = 'Fliperama'
    TORO_MECANICO = 'Toro Mecânico'


    # Implementar uma forma de automatizar o Enum -> Talvez criar uma lista vazia e um método para fazer push nela através do flask admin. 
    # Criar uma tabela nova para poder add um brinquedo -> name, quantity, id (primary_key, autoincrement), type parecido com o que já tem.
    