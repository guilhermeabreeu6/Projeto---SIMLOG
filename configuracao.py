# Arquivo: configuracao.py

class ConfiguracaoSistema:
    # Atributo de classe para armazenar a instância única
    _instancia = None

    def __new__(cls, *args, **kwargs):
        """
        Sobrescreve o método de criação da instância para garantir que apenas
        uma seja criada (Singleton Pattern).
        """
        # Verifica se a instância já existe
        if cls._instancia is None:
            # Se não existe, chama o __new__ da classe pai, para criar a instância real
            cls._instancia = super(ConfiguracaoSistema, cls).__new__(cls)
        return cls._instancia
        
    def __init__(self):
        """
        Inicializa os atributos da instância, mas garante que a inicialização
        (ex: leitura de arquivo) só ocorra uma vez.
        """
        if not hasattr(self, '_inicializado'):
            print("SIMLOG System: Carregando configurações iniciais...")

            # Parâmetros de configuração
            self.TAXA_KM_VAN = 0.50
            self.CAPACIDADE_MAX_VAN = 150
            self.TAXA_TONELADA_CAMINHAO = 10.00
            self.CAPACIDADE_MAX_CAMINHAO = 5000

            self._inicializado = True
        
    def exibir_config(self):
        """Método simples para verificar os valores"""
        print(f"--- Configurações Ativas ---")
        print(f"Taxa KM Van: R$ {self.TAXA_KM_VAN}")
        print(f"Capacidade Máx. Van: {self.CAPACIDADE_MAX_VAN}kg")
        print(f"Taxa Tonelada Caminhão: R$ {self.TAXA_TONELADA_CAMINHAO}")
        print(f"Capacidade Máx. Caminhão: {self.CAPACIDADE_MAX_CAMINHAO}kg")
        print("-----------------------------------------")


config1 = ConfiguracaoSistema()
config2 = ConfiguracaoSistema()

config1.exibir_config()

print(f"\nconfig1 é config2? {config1 is config2}")