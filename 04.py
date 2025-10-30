def verificarSenha(senha):
    if "@" or "!" or "#" or "$" in senha:
        if int in senha:
            if len(senha) >= 10:
                print("Senha válida criada com sucesso!")
                return True
        else:
            print("A senha precisa conter numeros inteiros.")
            return False
    else:
        print("A senha precisa ter algum caractere especial.")
        return False


i = 0

while i < 1:
    try:        
        senhaUser = str(input("Digite uma senha segura: "))

        validated = verificarSenha(senhaUser)

        if validated:
            print("Senha criada com sucesso")

    except:
        print("Houve um erro, tente novamente mais tarde.")





