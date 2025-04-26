class Ativo:
    def __init__(self, nome, valor_inicial, valor_residual, vida_util):
        self.nome = nome
        self.valor_inicial = valor_inicial
        self.valor_residual = valor_residual
        self.vida_util = vida_util
        self.depreciacao_anual = self.calcular_depreciacao()

    def calcular_depreciacao(self):
        return (self.valor_inicial - self.valor_residual) / self.vida_util

    def exibir_info(self):
        print(f"\nAtivo: {self.nome}")
        print(f"Valor Inicial: R$ {self.valor_inicial:.2f}")
        print(f"Valor Residual: R$ {self.valor_residual:.2f}")
        print(f"Vida Útil: {self.vida_util} anos")
        print(f"Depreciação Anual: R$ {self.depreciacao_anual:.2f}")


class RelatorioContabil:
    def __init__(self):
        self.ativos = []

    def adicionar_ativo(self, ativo):
        self.ativos.append(ativo)

    def gerar_relatorio(self):
        print("\n=== Relatório Contábil ===")
        total_depreciacao = 0
        for ativo in self.ativos:
            ativo.exibir_info()
            total_depreciacao += ativo.depreciacao_anual
        print(f"\nTotal de Depreciação Anual: R$ {total_depreciacao:.2f}")


# Criando ativos
ativo1 = Ativo("Computador", 5000, 500, 5)
ativo2 = Ativo("Veículo", 40000, 8000, 10)

# Gerando relatório contábil
relatorio = RelatorioContabil()
relatorio.adicionar_ativo(ativo1)
relatorio.adicionar_ativo(ativo2)
relatorio.gerar_relatorio()