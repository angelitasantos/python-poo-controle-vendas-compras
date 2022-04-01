from classValidacoes import *
from classInterface import *
from classArquivos import *
from classCompras import *
import csv


class ContasPagar:

    def __init__(self, arquivo, compra, parcela, valor, vencimento):
        self.arquivo = arquivo
        self.compra = compra
        self.parcela = parcela
        self.valor = valor
        self.vencimento = vencimento


    def ler_arquivo_contas_pagar(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            Interface.apresentar_cabecalho_interno(self, 'CONTAS A PAGAR')
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            
            lista = list(leitor)
            lista_ordenada = sorted (lista[1:], key = lambda dado: str(dado[1]))

            print(f'{bgCor[4]}{lista[0][0]:<14} {lista[0][2]:<35}{lista[0][6]:<10}{lista[0][7]:<15}{lista[0][8]:<11}{lista[0][10]:<14}{bgCor[0]}')
            print(Interface.incrementar_linha(self, tamanho, '~'))

            if len(lista) != 1:
                for linha in lista_ordenada:
                    valor = Validacoes.formatar_valor_real(float((linha[7])))
                    print(f'{linha[0]:>14} {linha[2]:<35}{linha[6]:<9} R$ {valor:.>11} {linha[8]:<11}{linha[10]:<14}')
                print(Interface.incrementar_linha(self, tamanho, '~'))
            else:
                print(f'\n{fontCor[1]}Não existe nenhum parcela registrada no sistema.\n{fontCor[0]}')
        finally:
            arquivo.close()


    def cadastrar_contas_pagar(self, nome):
        try:
            arquivo = open(nome, 'a')
        except:
            print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao abrir o arquivo.{bgCor[0]}\n')
        else:
            try:
                escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')
                Interface.apresentar_cabecalho_interno(self, 'CADASTRAR UMA NOVA PARCELA')

                resposta = str(input(f'\nQuer consultar o número da compra? [S/N] '))
                if resposta == 'S' or resposta == 's':
                    Compras.buscar_compras_fornecedor(self, arquivo_vendas)

                busca_movimento = Compras.buscar_compras(self, arquivo_vendas)

                while busca_movimento == None:
                    print(f'\n{fontCor[1]}Você não digitou um número válido.{fontCor[0]}')
                    busca_movimento = Compras.buscar_compras(self, arquivo_vendas)

                if busca_movimento != None:
                    numero = busca_movimento[0]
                    cod_contato = busca_movimento[1]
                    nome_contato = busca_movimento[2]
                    cidade = busca_movimento[3]
                    estado = busca_movimento[4]
                    tipo_fornecedor = busca_movimento[5]
                    print(f'{numero}-{nome_contato}-{cidade}/{estado}')
                    
                parcela = str(input(f'{"Digite a parcela ":.<35} '))
                valor = Validacoes.digitar_numero_real(self)
                vencimento = str(input(f'{"Digite o vencimento ":.<35} '))
                numparc = f'{cod_contato}{numero}{parcela}'
                status = 'EM ABERTO'

                tabela = [  numero, cod_contato, nome_contato, cidade, estado, tipo_fornecedor,
                                    parcela, valor, vencimento, numparc, status]
                escritor.writerow(tabela)
            except:
                print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao incluir os dados.{bgCor[0]}\n')
            else:
                print(f'\n{bgCor[2]}Parcela registrada com sucesso.{bgCor[0]}\n')
                arquivo.close()


    def buscar_contas_pagar(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            
            lista = list(leitor)
            lista_ordenada = sorted (lista[1:], key = lambda dado: str(dado[9]))

            if len(lista) == 1:
                print(f'\n{fontCor[1]}Não existe nenhum parcela registrada no sistema.\n{fontCor[0]}')
            elif len(lista) != 1:
                numero = str(input(f'\n{"Digite o número da parcela":.<35} ')).strip().upper()
                for linha in lista_ordenada: 
                    if linha[9].upper() == numero:
                        return [linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],linha[7],linha[8],linha[9],linha[10]]
        finally:
            arquivo.close()


    def buscar_contas_pagar_fornecedor(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            
            lista = list(leitor)
            lista_ordenada = sorted (lista[1:], key = lambda dado: str(dado[2]))

            if len(lista) == 1:
                print(f'\n{fontCor[1]}Não existe nenhum produto cadastrado no sistema.\n{fontCor[0]}')
            elif len(lista) != 1:
                Interface.apresentar_cabecalho_interno(self, 'PESQUISAR CONTAS A PAGAR POR FORNECEDOR')

                descricao = str(input(f'\n{"Digite o nome do fornecedor ":.<35} ')).strip().upper()
                palavra = descricao
                print(f'\n{bgCor[4]}{lista[0][0]:<14} {lista[0][2]:<35}{lista[0][6]:<10}{lista[0][7]:<15}{lista[0][8]:<11}{lista[0][10]:<14}{bgCor[0]}')
                print(Interface.incrementar_linha(self, tamanho, '~'))

                for linha in lista_ordenada: 
                    if palavra in linha[2] and linha[0] != 'NUMERO':
                        valor = Validacoes.formatar_valor_real(float((linha[7])))
                        print(f'{linha[0]:>14} {linha[2]:<35}{linha[6]:<9} R$ {valor:.>11} {linha[8]:<11}{linha[10]:<14}')
                print(Interface.incrementar_linha(self, tamanho, '~'))
        finally:
            arquivo.close()

    
    def buscar_contas_pagar_compra(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            
            lista = list(leitor)
            lista_ordenada = sorted (lista[1:], key = lambda dado: str(dado[2]))

            if len(lista) == 1:
                print(f'\n{fontCor[1]}Não existe nenhum produto cadastrado no sistema.\n{fontCor[0]}')
            elif len(lista) != 1:
                Interface.apresentar_cabecalho_interno(self, 'PESQUISAR CONTAS A PAGAR POR NUMERO DA COMPRA')

                descricao = str(input(f'\n{"Digite o número da compra ":.<35} ')).strip().upper()
                palavra = descricao
                print(f'\n{bgCor[4]}{lista[0][0]:<14} {lista[0][2]:<35}{lista[0][6]:<10}{lista[0][7]:<15}{lista[0][8]:<11}{lista[0][10]:<14}{bgCor[0]}')
                print(Interface.incrementar_linha(self, tamanho, '~'))

                for linha in lista_ordenada: 
                    if palavra in linha[0] and linha[0] != 'NUMERO':
                        valor = Validacoes.formatar_valor_real(float((linha[7])))
                        print(f'{linha[0]:>14} {linha[2]:<35}{linha[6]:<9} R$ {valor:.>11} {linha[8]:<11}{linha[10]:<14}')
                print(Interface.incrementar_linha(self, tamanho, '~'))
        finally:
            arquivo.close()


'''
self = 'self'
ContasPagar.ler_arquivo_contas_pagar(self, arquivo_pagar)
busca = ContasPagar.buscar_contas_pagar(self, arquivo_pagar)
print(busca)
ContasPagar.buscar_contas_pagar_fornecedor(self, arquivo_pagar)
ContasPagar.cadastrar_contas_pagar(self, arquivo_pagar)
ContasPagar.buscar_contas_pagar_compra(self, arquivo_pagar)
'''
