# P	=	{
# S		® XY,
# X		® XaA
#		XbB	
#		F,	
# Aa	® aA,
# Ab	® bA,
# AY	® Ya,
# Ba	® aB,
# Bb	® bB,
# BY	® Yb,
# Fa	® aF,
# Fb	® bF,
# FY	® e
####
####
### baba = 1,2,7,3,8,10,4,12,11,13
### baba = 0,1,6,2,7,9,3,11,10,12

P = [
 {"S"	:	"XY"	},
 {'X'	:	'XaA'	},
 {'X'	:	'XbB'	},
 {'X'	:	'F'		},
 {'Aa'	:	'aA'	},
 {'Ab'	:	'bA'	},
 {'AY'	:	'Ya'	},
 {'Ba'	:	'aB'	},
 {'Bb'	:	'bB'	},
 {'BY'	:	'Yb'	},
 {'Fa'	:	'aF'	},
 {'Fb'	:	'bF'	},
 {'FY'	:	""		}
 ]

def formar_palavra(P , palavra, instrucoes):
	palavras = list(palavra)
	for i in instrucoes:
		for k,v in P[i].items():
			if k not in palavra:
				return palavra, '{} NOT IN {}'.format(k,palavra), i, palavras
			palavra = palavra.replace(k,v)
			palavras += [palavra]

	return palavra, 'OK', instrucoes[-1], palavras

def get_instructions(instructions):
	return [int(i)-1 for i in instructions if i.isdigit()]

def print_dict(P):
	text = '\ndicionario\n'
	for i in P:
		text += '[{}]\t{}\n'.format(P.index(i)+1,i)
	print(text)

def projeto_01(palavra,instrucoes):

	print_dict(P)
	
	if len(instrucoes) > 0:
		print('instrucoes =      {}'.format([i+1 for i in instrucoes]))
		palavra, msg, instrucao, palavras = formar_palavra(P,palavra,instrucoes)
		print("\n resultado = '{}'\n info = {}\n instrucao {}".format(palavra, msg, instrucao+1))
		print(" palavras = {}".format(palavras))
	
	else:
		print("NOTHING TO DO")
	
def main():
	
	instrucoes = [0,1,6,2,7,9,3,11,10,12]
	palavra = 'S'

	if len(sys.argv) > 1:
		palavra = sys.argv[1]
		instrucoes = get_instructions(sys.argv[2:])
	
	projeto_01(palavra,instrucoes)

import sys
if __name__ == '__main__':
	main()