import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

class LogicaNebulosa:
    def __init__(self):
        # Variáveis fuzzy de entrada
        self.historico = ctrl.Antecedent(np.arange(0, 11, 1), 'historico')
        self.renda = ctrl.Antecedent(np.arange(0, 100001, 1), 'renda')
        self.divida = ctrl.Antecedent(np.arange(0, 100001, 1), 'divida')
        
        # Variável fuzzy de saída
        self.risco = ctrl.Consequent(np.arange(0, 101, 1), 'risco')
        
        # Funções de pertinência para o histórico de crédito
        self.historico['ruim'] = fuzz.trimf(self.historico.universe, [0, 2, 4])
        self.historico['regular'] = fuzz.trimf(self.historico.universe, [2, 4, 6])
        self.historico['bom'] = fuzz.trimf(self.historico.universe, [4, 6, 8])
        self.historico['excelente'] = fuzz.trimf(self.historico.universe, [6, 8, 10])
                
        self.renda['baixa'] = fuzz.trimf(self.renda.universe, [0, 0, 25000])
        self.renda['media'] = fuzz.trimf(self.renda.universe, [20000, 50000, 80000])
        self.renda['alta'] = fuzz.trimf(self.renda.universe, [65000, 100000, 100000])
        
        # Funções de pertinência para a dívida atual
        self.divida['baixa'] = fuzz.trimf(self.divida.universe, [0, 0, 33000])
        self.divida['moderada'] = fuzz.trimf(self.divida.universe, [25000, 50000, 75000])
        self.divida['alta'] = fuzz.trimf(self.divida.universe, [67000, 100000, 100000])
        
        # Funções de pertinência para o risco
        self.risco['baixo'] = fuzz.trimf(self.risco.universe, [0, 0, 33])
        self.risco['medio'] = fuzz.trimf(self.risco.universe, [25, 50, 75])
        self.risco['alto'] = fuzz.trimf(self.risco.universe, [67, 100, 100])
        
        self.regras = [
            # Regras com histórico "ruim"
            ctrl.Rule(self.historico['ruim'] & (self.divida['alta'] | self.renda['baixa']), self.risco['alto']),
            ctrl.Rule(self.historico['ruim'] & (self.divida['moderada'] | self.renda['media']), self.risco['medio']),
            ctrl.Rule(self.historico['ruim'] & self.divida['baixa'] & self.renda['alta'], self.risco['baixo']),

            # Regras com histórico "regular"
            ctrl.Rule(self.historico['regular'] & (self.divida['alta'] | self.renda['baixa']), self.risco['alto']),
            ctrl.Rule(self.historico['regular'] & (self.divida['moderada'] | self.renda['media']), self.risco['medio']),
            ctrl.Rule(self.historico['regular'] & self.divida['baixa'] & self.renda['alta'], self.risco['baixo']),

            # Regras com histórico "bom"
            ctrl.Rule(self.historico['bom'] & (self.divida['alta'] | self.renda['baixa']), self.risco['medio']),
            ctrl.Rule(self.historico['bom'] & (self.divida['moderada'] | self.renda['media']), self.risco['medio']),
            ctrl.Rule(self.historico['bom'] & self.divida['baixa'] & self.renda['alta'], self.risco['baixo']),

            # Regras com histórico "excelente"
            ctrl.Rule(self.historico['excelente'] & (self.divida['alta'] | self.renda['baixa']), self.risco['medio']),
            ctrl.Rule(self.historico['excelente'] & (self.divida['moderada'] | self.renda['media']), self.risco['baixo']),
            ctrl.Rule(self.historico['excelente'] & self.divida['baixa'] & self.renda['alta'], self.risco['baixo']),
        ]

       
        
        # Controle fuzzy
        self.sistema_controle = ctrl.ControlSystem(self.regras)
        self.simulador = ctrl.ControlSystemSimulation(self.sistema_controle)
    
    def calcular_risco(self, historico, renda, divida):
        try:
            # Passando valores para o simulador
            self.simulador.input['historico'] = historico
            self.simulador.input['renda'] = renda
            self.simulador.input['divida'] = divida
            
            # Executando a simulação
            self.simulador.compute()

            # Resultado
            risco_porcentagem = self.simulador.output['risco']
            if risco_porcentagem >= 66:
                tipo_risco = "Alto"
            elif 33 <= risco_porcentagem < 66:
                tipo_risco = "Médio"
            else:
                tipo_risco = "Baixo"

            return risco_porcentagem, tipo_risco
        except Exception as e:
            print(f"Erro ao calcular o risco: {e}")
            return None, None
