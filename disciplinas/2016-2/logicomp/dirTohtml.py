# -*- coding: utf-8 -*-

import os
from os import listdir
from os.path import isfile, join

mypath = os.getcwd() + '/aulas'


#mypathAulas = mypath + '/aulas'
#mypathListas = mypath + '/listas'
#mypathTrabs = mypath + '/trabalhos'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

onlyfiles.sort()

link = 'https://thiagoalvesifce.github.io/disciplinas/2016-2/logicomp/aulas/'

#print link

#print onlyfiles

listRows = []

for name in onlyfiles:
	if name[-3:] == 'pdf' and name[:-1] != '~':
		row = '<tr><td align="center"><a href="' + link + name + '" target="_blank">' + name[:-4] + '</a></td></tr>'
		listRows.append(row)

#print listRows

arq = open('logicomp.html','w')

header = '<HTML><HEAD><TITLE>Lógica para Computação</TITLE>\n'
header = header + '<META content="text/html; charset=utf-8" http-equiv=Content-Type>\n'
header = header + '<META content="MSHTML 5.00.2314.1000" name=GENERATOR></HEAD>\n'
header = header + '<body bgcolor="white" text="#000000" link="#0000A0" vlink="#A000A0" alink="#00A000">\n'
header = header + '<h1>Lógica para Computação</h1>\n'
header = header + '<h2>Aulas</h2>\n' + '<table border="1">\n'# + '<tr><th>Aula</th></tr>\n'

arq.write(header)

for row in listRows:
	arq.write(row + '\n')

arq.write('</table>\n')


arq.write('<h2>Listas</h2>\n<ul>\n')

mypath = os.getcwd() + '/listas'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

onlyfiles.sort()

link = 'https://thiagoalvesifce.github.io/disciplinas/2016-2/logicomp/listas/'

listRows = []

for name in onlyfiles:
	if name[-3:] == 'pdf' and name[:-1] != '~':
		row = '<li><a href="' + link + name + '" target="_blank">' + name[:-4] + '</a></li>'
		listRows.append(row)


for row in listRows:
	arq.write(row + '\n')

arq.write('</ul>\n')

arq.write('<h2>Trabalhos</h2>\n')

#arq.write('<ul>\n<li><a href="https://dl.dropboxusercontent.com/u/4914805/site/disciplinas/2016-1/logicomp/trabalhos/Trabalho1Tableaux.pdf" target="_blank">Trabalho 1 - Tableaux</a></li>\n<li><a href="https://dl.dropboxusercontent.com/u/4914805/site/disciplinas/2016-1/logicomp/trabalhos/Trabalho1Resolu%C3%A7%C3%A3o.pdf" target="_blank">Trabalho 1 - Resolução</a></li>\n<li><a href="https://dl.dropboxusercontent.com/u/4914805/site/disciplinas/2016-1/logicomp/trabalhos/Trabalho1DPLL.pdf" target="_blank">Trabalho 1 - DPLL</a></li>\n<li><a href="https://dl.dropboxusercontent.com/u/4914805/site/disciplinas/2016-1/logicomp/trabalhos/testeSat.cnf" target="_blank">Exemplo Satisfatível</a></li>\n<li><a href="https://dl.dropboxusercontent.com/u/4914805/site/disciplinas/2016-1/logicomp/trabalhos/testeUnsat.cnf">Exemplo Insatisfatível</a></li>\n<li><a href="https://dl.dropboxusercontent.com/u/4914805/site/disciplinas/2016-1/logicomp/trabalhos/Trabalho2Aplicacao.pdf" target="_blank">Temas do Trabalho 2</a></li>\n</ul>\n')

mypath = os.getcwd() + '/trabalhos'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

onlyfiles.sort()

link = 'https://thiagoalvesifce.github.io/disciplinas/2016-2/logicomp/trabalhos/'

listRows = []

for name in onlyfiles:
	if name[-3:] == 'pdf' and name[:-1] != '~':
		row = '<li><a href="' + link + name + '" target="_blank">' + name[:-4] + '</a></li>'
		listRows.append(row)


for row in listRows:
	arq.write(row + '\n')

arq.write('</ul>\n')


arq.write('<h2>Entrega de Trabalhos</h2>\n')
#arq.write('<ul>\n<li><a href="https://www.dropbox.com/request/O9sT4kH65jrmIrgTaTKD" target="_blank">Entrega do Trabalho 01 - Tableaux</a></li>\n<li><a href="https://www.dropbox.com/request/d5iKeXFSqmxszWJmyjBJ" target="_blank">Entrega do Trabalho 01 - Resolução</a></li>\n<li><a href="https://www.dropbox.com/request/x0cwccC9ktnxoqNEJB8q" target="_blank">Entrega do Trabalho 01 - DPLL</a></li></ul>\n')







auxiliar = '<h2>Material Auxiliar</h2>\n<ul>\n<li><a href="http://www.cs.ox.ac.uk/people/bernard.sufrin/personal/jape.org/" target="_blank">JAPE para Dedução Natural</a></li>\n<li><a href="usingjape.html">Utilizando o JAPE</a></li>\n<li><a href="https://dl.dropboxusercontent.com/u/4914805/ifce/2015.2/l%C3%B3gica%20para%20computa%C3%A7%C3%A3o/Regras%20da%20Dedu%C3%A7%C3%A3o%20Natural/Dedu%C3%A7%C3%A3o%20Natural%20-%20Regras.pdf" target="_blank">Regras da Dedução Natural</a></li>\n</ul>\n'


arq.write(auxiliar)

arq.write('<h2>Notas</h2>\n')

arq.write('<ul>\n<li><a href="https://docs.google.com/spreadsheets/d/1uF6hEVtyPw58vKYn9RCn-wUXuhtwy7TA6FD7NbPTvO4" target="_blank">Planilha de Notas</a></li></ul>\n<hr>')

trabsPassados = '<ul>\n<li><a href="logicompstudents.html">Trabalhos Passados</a></li>\n</ul>\n<hr>'

arq.write(trabsPassados)

arq.write('</body>\n</html>')

arq.close()
