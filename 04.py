def verificarSenha(senha):

    if any(c in senha for c in ["@", "!", "#", "$"]):
        if len(senha) >= 10:
            print("Senha válida criada com sucesso.")
            return True
        else:
            print("A senha precisa ter pelo menos 10 caracteres.")
            return False
    else:
        print("A senha precisa ter pelo menos um caractere especial (@, !, # ou $).")
        return False


i = 0

while i < 1:
    try:        
        senhaUser = str(input("Digite uma senha segura: "))

        validated = verificarSenha(senhaUser)

        if validated:
            i += 1

    except Exception as e:
        print(f"Houve um erro: {e}")
