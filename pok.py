import random

pokebolas = []
pokedex = ['nada', 'nada', 'nada', 'nada']
pokeFloresta = ['Caterpie', 'Pinsir', 'Pineco', 'Wurmple', 'Wurmple', 'Wurmple', 'Silcoon', 'Silcoon', 'Silcoon', 'Cascoon', 'Volbeat', 'Illumise', 'Kricketot', 'Illumise', 'Caterpie', 'Caterpie', 'Caterpie', 'Pinsir', 'Pineco', 'Pineco']
pokeCaverna = ['Diglett', 'Cubone', 'Nosepass', 'Gigalith', 'Geodude', 'Geodude', 'Geodude', 'Nosepass', 'Nosepass', 'Diglett', 'Diglett']

def escolher_pokemon():
    while True:
        escolha = input("Escolha seu Pokémon inicial:\n1.Charmander \n2.Squirtle \n3.Bulbasaur\nDigite o respectivo número para escolha: ")
        if escolha == "1":
            return "Charmander"
        elif escolha == "2":
            return "Squirtle"
        elif escolha == "3":
            return "Bulbasaur"
        else:
            print("Escolha inválida. Por favor, escolha 1, 2 ou 3.")
        print(f"Você escolheu o {escolher_pokemon()}, parabéns!")

def sorteio_pokebolas():
    return random.randint(0, 2)

def mostrar_pokedex():
    print("Pokédex:")
    for pokemon in pokedex:
        print(pokemon)

def mostrar_pokebolas():
    print(f"Você possui {len(pokebolas)} pokebolas.")

def jogar():
    while True:
        escolha = escolher_pokemon()
        pokedex.pop(0)
        pokedex.append(escolha)
        nome = input("Olá, me chame de Professor Carvalho. Qual é o seu nome?\n")
        print(f"Perfeito, {nome}, sua jornada Pokémon se iniciará agora. Mas antes, você precisará de um equipamento próprio para caçar Pokémon.\n(x4 pokébolas adquiridas)")
        pokebolas.extend(["pokebola"] * 4)

        while True:
            print("Escolha uma ação:")
            print("|1. Ir para floresta |")
            print("|2. Ir para a caverna |")
            print("|3. Pokedex          |")
            print("|4. Reiniciar o jogo |")
            print("|5. Sair do jogo     |")
            print("|6. Pokebolas        |")
            acao = int(input("Selecione uma ação: "))

            if acao < 1 or acao > 6:
                print("Esta função não existe, selecione novamente.")
                continue

            if acao == 1:
                qtd_pokebolas = sorteio_pokebolas()
                print(f"Você encontrou {qtd_pokebolas} pokebolas neste ambiente.")
                pokebolas.extend(['pokebola']*qtd_pokebolas)
                if len(pokebolas) == 0:
                    print("Você não possui pokebolas para caçar Pokémon.")
                    continue
                else:
                    while True:
                        x = random.randint(0, 19)
                        if pokedex[0] == pokeFloresta[x] or pokedex[1] == pokeFloresta[x] or pokedex[2] == pokeFloresta[x]:
                            print(f"Você já capturou o Pokémon {pokeFloresta[x]}. Retornando para casa.")
                            break
                        else:
                            while True:
                                print(f"Um {pokeFloresta[x]} selvagem apareceu. O que você faz?")
                                print("|1. Tentar capturar.|")
                                print("|2. Fugir.           |")
                                acao2 = int(input("Selecione uma ação: "))
                                if acao2 < 1 or acao2 > 2:
                                    print("Ação inválida. Selecione novamente.")
                                    continue
                                elif acao2 == 1:
                                    y = random.randint(1, 2)
                                    if y == 1:
                                        pokedex.pop(0)
                                        pokedex.append(pokeFloresta[x])
                                        print(f"Você capturou o Pokémon {pokeFloresta[x]}. Retornando para casa.")
                                        pokebolas.pop()
                                        break
                                    else:
                                        print(f"O Pokémon {pokeFloresta[x]} fugiu. Retornando para casa.")
                                        pokebolas.pop()
                                        break
                                else:
                                    print("Você volta para casa.")
                                    break
                            break
                continue

            if acao == 2:
                qtd_pokebolas = sorteio_pokebolas()
                print(f"Você encontrou {qtd_pokebolas} pokebolas neste ambiente.")
                pokebolas.extend(['pokebola']*qtd_pokebolas)
                if len(pokebolas) == 0:
                    print("Você não possui pokebolas para caçar Pokémon.")
                    continue
                else:
                    while True:
                        x = random.randint(0, 10)
                        if pokedex[0] == pokeCaverna[x] or pokedex[1] == pokeCaverna[x] or pokedex[2] == pokeCaverna[x]:
                            print(f"Você já capturou o Pokémon {pokeCaverna[x]}. Retornando para casa.")
                            break
                        else:
                            while True:
                                print(f"Um {pokeCaverna[x]} selvagem apareceu. O que você faz?")
                                print("|1. Tentar capturar.|")
                                print("|2. Fugir.           |")
                                acao2 = int(input("Selecione uma ação: "))
                                if acao2 < 1 or acao2 > 2:
                                    print("Ação inválida. Selecione novamente.")
                                    continue
                                elif acao2 == 1:
                                    y = random.randint(1, 100)
                                    if y <= 35:
                                        pokedex.pop(0)
                                        pokedex.append(pokeCaverna[x])
                                        print(f"Você capturou o Pokémon {pokeCaverna[x]}. Retornando para casa.")
                                        pokebolas.pop()
                                        break
                                    else:
                                        print(f"O Pokémon {pokeCaverna[x]} fugiu. Retornando para casa.")
                                        pokebolas.pop()
                                        break
                                else:
                                    print("Você volta para casa.")
                                    break
                            break
                continue

            if acao == 3:
                mostrar_pokedex()
                continue

            if acao == 6:
                mostrar_pokebolas()
                continue

            if acao == 5:
                break

            if acao == 4:
                pokebolas.clear()
                pokedex.clear()
                pokedex.extend(['nada', 'nada', 'nada', 'nada'])
                break

        if acao == 5:
            break
jogar()