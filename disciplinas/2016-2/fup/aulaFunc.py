def soma(primeiro, segundo):
	primeiro = primeiro + segundo
	return primeiro

def media(x1, x2):
	return soma(x1,x2)/2.0



primeiro, segundo = raw_input().split()
primeiro = int(primeiro)
segundo = int(segundo)
print soma(primeiro, segundo)
print primeiro
