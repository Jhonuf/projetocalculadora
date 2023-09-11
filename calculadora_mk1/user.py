class User:
    def __init__(self, login=None, senha=None):
        self.login = login
        self.senha = senha

        
    def adicionar_usuario(self, nome_usuario, senha):
        # Verifica se o usuário já existe
        for usuario in self.usuario:
            if usuario['nome'] == nome_usuario:
                return "Usuário já existe. Escolha outro nome de usuário."
        
        # Se o usuário não existe, adiciona à lista
        self.usuario.append({'nome': nome_usuario, 'senha': senha})
        return "Usuário cadastrado com sucesso."
    

    
# Exemplo de uso:
    
# Adicionar um usuário
#resultado = gerenciador.adicionar_usuario("joao", "senha123")
#print(resultado)  # Deve imprimir "Usuário cadastrado com sucesso."

# Verificar o login
#resultado = gerenciador.verificar_login("joao", "senha123")
#print(resultado)  # Deve imprimir "Login bem-sucedido."
