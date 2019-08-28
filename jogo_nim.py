import random

def main_menu():
	print("""	Bem-vindo ao jogo do NIM! Escolha:

		1 - Para jogar uma partida
		2 - Para jogar um campeonato""")
	try:
		esc = int(input())
	except ValueError:
		esc = 0

	if esc == 1:
		partida()
	elif esc == 2:
		campeonato()
	else :
		print ("Escolha inválida!")

def partida():
	computador_jogou = False
	vencedor = None
	num_pecas = 0
	lim_jog = 1

    #Pede e valida se o jogador colocou um número válido de peças no tabuleiro
	while True:
		try:
			num_pecas = int(input("Quantas peças? "))
			lim_jog = int(input("Limite de peças por jogada? "))
		except ValueError:
			print("Valor inválido!")
		else:
			if num_pecas <= 0 or lim_jog < 1 :
				print ("Valor inválido!")
			else :
				break

	if num_pecas % (lim_jog + 1) == 0:
		print("Você começa")
		num_pecas -= usuario_escolhe_jogada(num_pecas, lim_jog)
		computador_jogou = False
	else:
		num_pecas -= computador_escolhe_jogada(num_pecas, lim_jog)
		computador_jogou = True

	while num_pecas > 0:
		print ("Restam " + str(num_pecas) + " no tabuleiro!")
		if computador_jogou:
			num_pecas -= usuario_escolhe_jogada(num_pecas, lim_jog)
			computador_jogou = False
		else :
			num_pecas -= computador_escolhe_jogada(num_pecas, lim_jog)
			computador_jogou = True

	if computador_jogou:
			vencedor = "Computador"
	elif not computador_jogou:
			vencedor = "Você"

	print (vencedor + " venceu a partida!")
	print()
	return vencedor

def campeonato():
	placar = [0, 0]
	for x in range(3):
		print("Partida " + str(x+1) + "\n")
		venc_part = partida()
		if venc_part == "Você":
			placar[0] += 1
		else:
			placar[1] += 1

		print()
		print ("Placar: Você " + str(placar[0]) + " X " + str(placar[1]) + " Computador")

	print()

	print()

	if placar[0] > placar[1]:
		print ("Você venceu o campeonato!")
	else:
		print ("O computador venceu o campeonato!")

def computador_escolhe_jogada(n, m):
	ret = 1
	while ret < m:
		if ((n - ret) % (m + 1) == 0):
			break
		else :
			ret = ret + 1

	print("O computador tirou " + str(ret) + " peças.")
	return int(ret)

def usuario_escolhe_jogada(n, m):
	while True:
		try:
			ret = int(input("Vai retirar quantas peças? "))
		except ValueError:
			print ("Valor inválido!")
		if ret > n or ret > m or ret < 1:
			print ("Valor inválido!")
		else:
			break

	return int(ret)

main_menu()
