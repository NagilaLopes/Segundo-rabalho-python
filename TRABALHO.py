q=("A opcao 2 nao pode ser correspondida no momento") 
nom=[]
c=[]
tel=[] 
e=[] 
s=[] 
dice = 0 
print("Seja-Bem vindo ao site do 1º ano B")
print("-------------------------------------------------------------")
i=0 
while i!=5:
	print("\n1-Cadastrar")
	print("2-Ler") 			
	print("3-Deletar") 		
	print("4-Atualizar") 			
	print("5-Sair")
	o=int(input("Escolha uma opção:"))
	if o==1:
	 y=int(input("digite qt cadastros quer fazer:"))
	 x=0
	 while x<y:
	 	nome=input("Digite seu nome:")
	 	ce=input("Digite seu cpf:") 
	 	tele=input("Digite seu telefone:")   
	 	ee=input("Digite seu email:") 					
	 	se=input("Crie uma senha:")
	 	b=0
	 	x+=1
	 	while b==0:
	 		print(" \nVocê deseja confirmar seus dados acima: \n") 						
	 		print("1- Sim,confirmo meus dados cadastrados.") 						
	 		print("2-Não,desejo refazer novamente. \n")
	 		esc=int(input("Escolha as opção  acima:"))
	 		if esc==1:
	 			print("Dados salvos \n")
	 			b=1
	 			nom.append(nome) 							
	 			c.append(ce) 							
	 			tel.append(tele) 							
	 			e.append(ee) 							
	 			s.append(se) 						
	 			if esc>2:
	 				print("Sem função")
	 				b=0 						
	 			elif esc==2:
	 				b=0							
	 				x=0
	if o==2:
	 	w=0
	 	r=1
	 	while w<y:
	 					print("###Cadastro %d###"%r)
	 					print("nome: ",nom[w])
	 					print("cpf:" ,c[w]) 						
	 					print("telefone:" ,tel[w])
	 					print("email:" ,e[w]) 						
	 					print("senha: " ,s[w])
	 					w=w+1
	 					r=r+1
	
	if o==3:
	 						d=nom+c+tel+e+s 						
	 						print("1-nome: ",nom)
	 						print("2-cpf:" ,c) 						
	 						print("3-telefone:" ,tel)
	 						print("4-email:" ,e) 						
	 						print("5-senha: " ,s ) 						
	 						print("6-deletar tudo:" ,d)
	 						k=0
	 						while k==0:
	 							dele=int(input("escolha uma opção: "))
	 							indice = int(input("escolha o cadastro: 0 = primeiro cadastro 1 = segundo cadastro etc. 100 = todos"))
	 							if dele==1:
	 								print("nome deletado")
	 								nom[indice]=("nome não encontrado")
	 								k=1
	 							if dele==2:
	 								print("cpf deletado")
	 								c[indice]=("cpf não encontrado")
	 								k=1 							
	 							if dele==3:
	 								print("telefone deletado")
	 								tel[indice]=("telefone não encontrado")
	 								k=1 							
	 							if dele==4:
	 								print("email deletado")
	 								e[indice]=("email não encontrado")
	 								k=1 							
	 							if dele==5:
	 								print("senha deletado")
	 								s[indice]=("senha não encontrada")
	 								k=1
	 							if dele==6:
	 								nom[indice]=("Nome não encontrado")
	 								c[indice]=("Cpf deletado")
	 								tel[indice]=("Telefone deletado")
	 								print("Telefone não encontrado")
	 								e[indice]=("Email não encontrado")
	 								s[indice]=("Senha não encomtrado")
	 								print("------------------------------------")
	 								print("Tudo apagado.")
	 								print("Voltar pro começo\nDigite 1:")
	 							if dele>6:
	 								print("Sem função")
	 								k=1
	if o==4: 				
		z=0
		while z==0:
			at=int(input("Deseja atualizar alguma coisa?\n1 - Sim\n2 - Não\n"))
			o=1
			if at==2:
				print("--Começo--")
				z=1
			if at==1:
				indice = int(input("escolha o cadastro: 0 = primeiro cadastro 1 = segundo cadastro etc. 100 = todos"))
				atu=int(input("Qual deseja atualizar?\n1 - Nome\n2 - CPF\n3 - Telefone\n4 - Email\n5 - Senha\n6 - Todas as opções\n7 - Voltar\nEscolha:"))
				print("1 - Nome")
				print("2 - CPF") 			
				print("3 - Telefone") 	
				print("4 - Email") 			
				print("5 - Senha")
				print("6 - Todas as opções")
				print("7- Voltar")
				
				if atu==1:
					print("Mude o nome")
					for names in nom:
						names=input("Nome:")
						print(names)
				if atu==2:
					print("Mude o cpf")
					for cpff in c:
																cpff=input("CPF:")
																print(cpff)
				if atu == 3:
																tel[indice]
																input("telefone:")
																print(tel[indice])
				if atu == 4:
																	e[indice] = input("email:")
																	print(e[indice])
				if atu == 5:
																		s[indice]=input("senha:")
																		print(s[indice])
				if atu == 6:
																	nom[indice] = input("nome:")
																	print(nom[indice])
																	c[indice] = input("CPF:")
																	print(nom[indice])
																	tel[indice] = input("telefone:")
																	print(tel[indice])
																	e[indice] = input("email:")
																	print(e[indice])
																	s[indice] = input("senha:")
																	print(s[indice])
																	print("mudança concluida")
	if o==5:
		v=0
		while v==0:
			sa=int(input("Você deseja sair do programa?\n1 - Sim\n2 - Não\n"))
			if sa==1:
				print("Programa finalizado.")
				i=5
				v=1
			if sa==2:
				print("Operação cancelada.")
				v=1 
				i=0