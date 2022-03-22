import random


bgCor = (
    '\033[m',               # 0 - sem cor
    '\033[0;30;41m',        # 1 - vermelho
    '\033[0;30;42m',        # 2 - verde
    '\033[0;30;43m',        # 3 - amarelo
    '\033[0;30;44m',        # 4 - azul
    '\033[0;30;45m',        # 5 - roxo
    '\033[7;30m',           # 6 - branco
)

fontCor = (
    '\033[m',               # 0 - sem cor
    '\033[31m',             # 1 - vermelho
    '\033[32m',             # 2 - verde
    '\033[33m',             # 3 - amarelo
    '\033[34m',             # 4 - azul
    '\033[35m',             # 5 - roxo
    '\033[30m',             # 6 - branco
)


class Validacoes:

    def __init__(self, validacao):
        self.validacao = validacao


    def validar_numero_inteiro(self, mensagem=''):
        while True:
            try:
                numero = int(input(mensagem))
            except (ValueError, TypeError):
                print(f'{bgCor[1]}ERRO: Por favor, digite um valor inteiro!{bgCor[0]}')
                continue
            except (KeyboardInterrupt):
                print(f'{bgCor[1]}ERRO: Usuário não digitou um valor válido.{bgCor[0]}')
                return 0
            else:
                return numero


    def validar_numero_real(self, mensagem=''):
        while True:
            try:
                numero = float(input(mensagem))
            except (ValueError, TypeError):
                print(f'{bgCor[1]}ERRO: Por favor, digite um valor real!{bgCor[0]}')
                continue
            except (KeyboardInterrupt):
                print(f'{bgCor[1]}ERRO: Usuário não digitou um valor válido.{bgCor[0]}')
                return 0
            else:
                return numero


    def formatar_valor_real(valor):
        a = "{:,.2f}".format(float(valor))
        b = a.replace(',','v')
        c = b.replace('.',',')
        return c.replace('v','.')

    
    def formatar_quantidade(valor):
        a = "{:,.3f}".format(float(valor))
        b = a.replace(',','v')
        c = b.replace('.',',')
        return c.replace('v','.')


    def gerar_identificador(self):
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'
        qnt = 8
        qntInt = int(qnt)
        length = qntInt
        all = lower + upper + digits
        id = "".join(random.sample(all, length))
        return id


    ''' # criar um método para validar se o campo está vazio
    def validar_campo_vazio(self, mensagem=''):
        return validar
    '''
 
    ''' # criar um método para validar o tamanho dos campos
    def validar_tamanho_campo(self, mensagem=''):
        return validar    
    '''