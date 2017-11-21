# -*- coding: utf-8 -*-
import re

class Ocorrencia(object):
	def __init__(self, nome, posicao, linha, coluna):
		self.nomeLista = nome
		self.posicaoLista = posicao
		self.linha = linha
		self.coluna = coluna

class Lexico(object):
	def __init__(self):
		self.o = ['<', '>', '=', '!', '|', '&']
		self.o2 = ['=', '|', '&']
		self.listaBuffer = []
		self.listaTokens = {'separadores':[' ', '\n', '\t', '(', ')','{','}',',',';','\r'],
						    'operadores':['+','-','*','/','=','<','<=','>','>=','==','!=','&&','||'],
						    'reservadas':['main','int','float','if','else','while','read','print'],
					    	'inteiro': [], 
							'float': [], 
							'identificadores':[],
							'identificadores1':[],
					  	    'ocorrencias':[],
					  	    'operadores1':[],
					  	    'separadores1':[],
					  	    'reservadas1':[],
					  	    'erros':[],
					  	    'tokens':[],
					  	    'lexema':[],
					  	    'linhas':[]}

		arq = open('teste.txt', 'r')
		self.caracteres = list(arq.read())
		self.linha = 0
		self.TabelaSimbolos = []

	
	def separador(self, token):	
		if (token in self.listaTokens['separadores']):
			return True
				
		return False

	def operador(self, token):						
			if (token in self.listaTokens['operadores'] or (token == '!' and self.caracteres[0] == '=') or 
				(token == '&' and self.caracteres[0] == '&') or (token == '|' and self.caracteres[0] == '|')  ):
				return True
			return False

	def operador2char(self, token):
		result = [False, '']
		if (token in self.listaTokens['operadores'] or token == '!' or token == '&' or token == '|'):
			result = [True, str(token)]
			if (token in self.o and self.caracteres[0] in self.o2):
				result = [True, str(token) + str(self.caracteres[0])]
				self.caracteres.pop(0)

		return result

	def reservadas(self, token):
		if (token in self.listaTokens['reservadas']):
			return True
		return False

	def numeroInt(self, token):
		result = re.match("^-?\\d*(\\d+)?$", token)

		if (result is not None):
			return True
		return False

	def numeroFloat(self, token):
		result = re.match("([0-9]+[.])+[0-9]+", token)
		if (result is not None):
			return True
		return False

	def addToken(self, token, nomeLista):
		self.listaTokens[nomeLista].append(token)

	def identificaToken(self, token):
		nomeLista = ''
		posicaoLista = ''
		linha = ''
		coluna = ''

		
		if (self.operador(token)):
			result = self.operador2char(token)
			if (result[0]):
				token = result[1]

			if (token == "="):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')	
				lexema = token
				lexema = "ATTR"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')	
			if (token == "<"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "LT"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "<="):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "LE"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == ">"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "GT"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == ">="):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "GE"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')	
			if (token == "=="):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "EQ"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')	
			if (token == "!="):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "NE"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "||"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "OR"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "&&"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "AND"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "+"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "PLUS"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "-"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "MINUS"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "*"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "MULT"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "/"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "DIV"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
				
			nomeLista = 'operadores'
			self.addToken(token, 'operadores1')

			if (token != '!'):
				posicaoLista = self.listaTokens[nomeLista].index(token)
				ocorrencia = Ocorrencia(nomeLista, posicaoLista, self.linha, coluna)
			else :
				ocorrencia = Ocorrencia(nomeLista, 10, self.linha, coluna)
			if (token != '&'):
				posicaoLista = self.listaTokens[nomeLista].index(token)
				ocorrencia = Ocorrencia(nomeLista, posicaoLista, self.linha, coluna)
			else :
				ocorrencia = Ocorrencia(nomeLista, 10, self.linha, coluna)	
			if (token != '|'):
				posicaoLista = self.listaTokens[nomeLista].index(token)
				ocorrencia = Ocorrencia(nomeLista, posicaoLista, self.linha, coluna)
			else :
				ocorrencia = Ocorrencia(nomeLista, 10, self.linha, coluna)

		elif (self.separador(token)):
			if(token == '\n'):				
				self.linha +=1;
			if (token == "("):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "LBRACKET"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == ")"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "RBRACKET"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "{"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "LBRACE"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "}"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "RBRACE"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == ","):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "COMMA"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == ";"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "PCOMMA"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')	

			nomeLista = 'separadores'
			self.addToken(token, 'separadores1')
			posicaoLista = self.listaTokens[nomeLista].index(token)
			ocorrencia = Ocorrencia(nomeLista, posicaoLista, self.linha, coluna)
		

		elif(self.reservadas(token)):
			if (token == "int"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "INT"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "main"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "MAIN"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "float"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "FLOAT"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "if"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "IF"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "else"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "ELSE"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "while"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "WHILE"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
			if (token == "read"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "READ"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')	
			if (token == "print"):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "PRINT"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')		
							

			nomeLista = 'reservadas'
			self.addToken(token, 'reservadas1')
			posicaoLista = self.listaTokens[nomeLista].index(token)
			ocorrencia = Ocorrencia(nomeLista, posicaoLista, self.linha, coluna)


		elif(self.numeroFloat(token)):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "FLOAT_CONST"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
				nomeLista = 'float'
				self.addToken(token, nomeLista)
				posicaoLista = self.listaTokens[nomeLista].index(token)
				ocorrencia = Ocorrencia(nomeLista, posicaoLista, self.linha, coluna)

		elif(self.numeroInt(token)):
			self.addToken(token,'lexema')
			self.addToken(self.linha,'linhas')
			lexema = token
			lexema = "INTEGER_CONST"
			#print token, "\t",self.linha,"\t",lexema
			self.addToken(lexema,'tokens')
			nomeLista = 'inteiro'
			self.addToken(token, nomeLista)
			posicaoLista = self.listaTokens[nomeLista].index(token)
			ocorrencia = Ocorrencia(nomeLista, posicaoLista, self.linha, coluna)

		else:
			result = re.match('[A-Za-z]([A-Za-z]|[0-9])*', token)
			if (result is None):
				print "Erro Lexico: ", token, "Linha: ", self.linha
				nomeLista = 'erros'
				self.addToken(token, nomeLista)
				posicaoLista = self.listaTokens[nomeLista].index(token)
				

			nomeLista = 'identificadores1'		
			if(token not in self.listaTokens['erros']):
				self.addToken(token,'lexema')
				self.addToken(self.linha,'linhas')
				lexema = token
				lexema = "ID"
				#print token, "\t",self.linha,"\t",lexema
				self.addToken(lexema,'tokens')
				self.addToken(token, nomeLista)
				posicaoLista = self.listaTokens[nomeLista].index(token)
			

		ocorrencia = Ocorrencia(nomeLista, posicaoLista, self.linha, coluna)
		self.addToken(ocorrencia, 'ocorrencias')


	def run(self):
		while(len(self.caracteres)):
			c = self.caracteres[0]
			self.caracteres.pop(0)

			if(self.separador(c) or self.operador(c)):
				token = ''.join(self.listaBuffer)
				if (token is not ''):
					self.identificaToken(token)

				self.identificaToken(c)
				self.listaBuffer = []
			else:
				self.listaBuffer.append(c)


def main():
	#print "Lexema|Linha|Token"
	lexico = Lexico()
	lexico.run()

	#print "Lexemas \n", lexico.listaTokens['lexema'],'\n'
	#print "Linhas \n" , lexico.listaTokens['linhas'],'\n'
	#print "Operadores \n", lexico.listaTokens['operadores1'],'\n'
	#print "Separadores \n", lexico.listaTokens['separadores1'],'\n'
	#print "Reservadas \n", lexico.listaTokens['reservadas1'],'\n'
	#print "Inteiro\n", lexico.listaTokens['inteiro'], '\n'
	#print "Float\n", lexico.listaTokens['float'], '\n'
	#print "Identificadores\n", lexico.listaTokens['identificadores1'], '\n'
	#print "Erros\n", lexico.listaTokens['erros'], '\n'
	#print "Tokens\n",lexico.listaTokens['tokens'],'\n'

	#print "OCORRENCIAS:\n"
	#for o in lexico.listaTokens['ocorrencias']:
	#	print o.nomeLista, o.posicaoLista, o.linha, o.coluna
	return lexico

#if __name__ == "__main__":
#	main()
lexico = main()