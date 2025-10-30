numsTentativas = 0

loginUser = "vini@gmail.com"
senhaUser = "vini123"

def validacaoDeUsuario(login, senha):
    if (len(login) < 10 or len(senha) < 5):
        print("Login ou senha muito curtas. Tente novamente mais tarde.")
        return False
    elif (login != loginUser or senha != senhaUser):
        print("Login ou senha incorretos. Tente novamente mais tarde.")
        return False
    else:
        return True

while numsTentativas < 3:
    try:
        login = str(input("Digite seu login: "))
        senha = str(input("Digite sua senha: "))

        validated = validacaoDeUsuario(login, senha)

        if validated:
            print("Usuario logado com sucesso.")
            break
        else:
            numsTentativas += 1
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        numsTentativas += 1

if numsTentativas == 3:
    print("Você atingiu o número máximo de tentativas")















