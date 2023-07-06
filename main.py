def descriptografar (cipher, prikey) :
		o,i = prikey
		msg = [c**o%i for c in cipher]
		msg = [chr(m) for m in msg]
		message = ''.join(msg)
		return message

def criptografar(message, pubkey) :
		msg = [ord(char) for char in message]
		l,i = pubkey
		c = [m**l%i for m in msg]
		return c



p, q = 47, 71
i = p*q
l = 79
o = 1019

pubkey = (l, i)
prikey = (o, i)

opcao = 0
while opcao !=3:
		
		print("")
		print("Insira uma opção")
		print("1- Criptografar")
		print("2- Descriptografar")
		print("3- Finalizar o programa")
		print("")
		opcao =int(input("opção "))
		
		if opcao == 1:
				msg = input("Insira a mensagem que irá ser criptografada: ")
				cipher = criptografar(msg, pubkey)
				for c in cipher : print (c)
				
		elif opcao == 2:
				decipher = descriptografar(cipher, prikey)
				decipher : print (decipher)
				
		elif opcao == 3:
				print("Fim do codigo!")
				
		else:
				print("Opção não existente!")