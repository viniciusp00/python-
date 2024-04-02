def exibir_opcoes():    
    print('1 Cadastrar restaurante')
    print('2 listar restaurante')
    print('3 ativar restaurante')
    print('4 sair')

opcao_escolhida = int(input('escolha uma opcao'))
print(f'Você escolheu a opção {opcao_escolhida}')

def finalizar_app():
    os.system('cls')
    print('finalizando o app')

if opcao_escolhida ==1:
    print('cadastrar restaurante')
elif opcao_escolhida ==2:
    print('listar restaurante')
elif opcao_escolhida ==3:
    print('ativar restaurante')
else: 
    print('encerrrando o programa')

def main():
    exibir_opcoes()    
    finalizar_app()

