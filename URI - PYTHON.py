'''# V - Media I *******************************
A = float(input())
B = float(input())
MEDIA = ((3.5*A) + (7.5*B))/2
print('MEDIA = {:.5f}'.format(MEDIA))
'''

'''# VIII - Salario **************************
NUMBER = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())
SALARY = valor_hora * horas_trabalhadas
print('NUMBER = {}'.format(NUMBER))
print('SALARY = U$ {:.2f}'.format(SALARY))'''

'''
myjob = 'hacker'
for i in myjob: print(i, end=' ')

mantra = 'always loock on the bright'
for c in mantra: print (c, end= ' ')


codigo_1 = int(input())
numero_1 = int(input())
valor_unitario = float(input())
print(codigo_1, numero_1, valor_unitario, end=' ')


v = []
while len(v) < 10:
    x = int(input("Escreva um numero: "))
    if x in v:
        print("Nao pode escrever esse numero.")
    else:
        v.append(x)
print(v)
'''

'''# Calculo Simples *******************************
cod_p1, num_p1, v_p1 = input().split(' ')
cod_p1 = int(cod_p1); num_p1 = int(num_p1); v_p1 = float(v_p1)

cod_p2, num_p2, v_p2 = input().split(' ')
cod_p2 = int(cod_p2); num_p2 = int(num_p2); v_p2 = float(v_p2)

pg_pc1 = num_p1 * v_p1
pg_pc2 = num_p2 * v_p2

pg_total = pg_pc1 + pg_pc2
print('VALOR A PAGAR: R$ {:.2f}'.format(pg_total))'''


#LISTA 2 ************************************************
# I - ESFERA
'''
R = float(input())
pi = 3.14159
VOLUME = (4/3.0) * pi * R**3
print('VOLUME = {:.3f}'.format(VOLUME))
'''
# II - Area **********************************
'''A, B, C = input().split(' ')
A = float(A)
B = float(B)
C = float(C)
print('TRIANGULO: {:.3f}'.format((A*C)/2))
print('CIRCULO: {:.3f}'.format(3.14159 * C**2))
print('TRAPEZIO: {:.3f}'.format(C * (A+B)/2))
print('QUADRADO: {:.3f}'.format(B**2))
print('RETANGULO: {:.3f}'.format(A*B))'''

# III - O MAIOR ***********************************
'''a, b, c = input().split(' ')
a = int(a); b = int(b); c = int(c)
MaiorAB = (a + b + abs(a - b))/2
MaiorAB_C = (MaiorAB + c + abs(MaiorAB - c))/2
print('{:.0f} eh o maior'.format(MaiorAB_C))'''

# IV - Consumo - *************************************
'''X = int(input())
Y = float(input())
Media = X + Y
print('{:.3f} km/l'.format(Media))'''

# V - Distancia entre dois pontos ************************
'''x1, y1 = input().split(' ')
x1 = float(x1); y1 = float(y1)

x2, y2 = input().split(' ')
x2 = float(x2); y2 = float(y2)

Distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print('{:.4f}'.format(Distancia))'''

# VI - Distancia ************************************
'''km = int(input())
minutos = (km * 60) // 30
print('{} minutos'.format(minutos))'''

# VII - Gasto de combustivel **************************
'''tempo_gasto =  int(input())
vel_media = int(input())

dist_percorrida = tempo_gasto * vel_media
litros = dist_percorrida / 12

print('{:.3f}'.format(litros))'''

# VIII - Cedulas  *****************************
'''N = int(input())
print(N)

notas_cem = N // 100
N -= (notas_cem * 100)

notas_cin = N // 50
N -= (notas_cin * 50)

notas_vinte = N // 20
N -= (notas_vinte * 20)
notas_dez = N // 10
N -= (notas_dez * 10)
notas_cinco = N // 5
N -= (notas_cinco * 5)
notas_dois = N // 2
N -= (notas_dois * 2)
notas_um = N // 1
N *= N

print('{} nota(s) de R$ 100,00'.format(notas_cem))
print('{} nota(s) de R$ 50,00'.format(notas_cin))
print('{} nota(s) de R$ 20,00'.format(notas_vinte))
print('{} nota(s) de R$ 10,00'.format(notas_dez))
print('{} nota(s) de R$ 5,00'.format(notas_cinco))
print('{} nota(s) de R$ 2,00'.format(notas_dois))
print('{} nota(s) de R$ 1,00'.format(notas_um))'''


# IX - conversao de Tempo **************************
'''N = int(input())
if N >= 3600:
    hours = N // 3600
    N -= (hours * 3600)
    minutes = N // 60
    N -= (minutes * 60)
    seconds = N
    print('{:.0f}:{:.0f}:{:.0f}'.format(hours, minutes, seconds))
else:
    seconds = N % 60
    N -= seconds
    minutes = N / 60
    print('{:.0f}:{:.0f}:{:.0f}'.format(0, minutes, seconds))'''

# X - Idade em dias *************************
'''idade = int(input())

idade_anos = idade // 365
idade -= (idade_anos * 365)

idade_meses = idade // 30
idade -= (idade_meses * 30)

idade_dias = idade % 30

print('{} ano(s)'.format(idade_anos))
print('{} mes(es)'.format(idade_meses))
print('{} dia(s)'.format(idade_dias))'''

# LISTA III **********************************************
# I - Lanche
'''codigo, quantidade = input().split(' ')
cod = int(codigo)
quant = float(quantidade)

#total = 0
preco1 = 4.00
preco2 = 4.50
preco3 = 5.00
preco4 = 2.00
preco5 = 1.50

if cod == 1:
    total = quant * preco1
elif cod == 2:
    total = quant * preco2
elif cod == 3:
    total = quant * preco3
elif cod == 4:
    total = quant * preco4
elif cod == 5:
    total = quant * preco5

print('Total: R$ {:.2f}'.format(total))
'''

# II - Sort Simples - Usando Condiçoes ******************
'''A, B, C = map(int, input().split(' '))

if A >= B and A >= C and B >= C:
    print('{}'.format(C))
    print('{}'.format(B))
    print('{}'.format(A))
elif B >= A and B >= C and A >= C:
    print('{}'.format(C))
    print('{}'.format(A))
    print('{}'.format(B))
elif C >= A and C >= B and A >= B:
    print('{}'.format(B));
    print('{}'.format(A));
    print('{}'.format(C))
elif A >= B and A >= C and C >= B:
    print('{}'.format(B));
    print('{}'.format(C));
    print('{}'.format(A))
elif B >= A and B >= C and C >= A:
    print('{}'.format(A));
    print('{}'.format(C));
    print('{}'.format(B))
elif C >= A and C >= B and B >= A:
    print('{}'.format(A));
    print('{}'.format(B));
    print('{}'.format(C))

print()
print(A)
print(B)
print(C)
'''

# II - Sort Simples - Metodo da Lista *****************
'''A, B, C = map(int, input().split())

lista = [A, B, C]
X = list(lista) # ou X = lista.copy()
X.sort() # .sort = ordena a lista.

for Y in X:
	print(Y)

print()

for Z in lista:
	print(Z)'''


# III - Intervalo *******************************
'''X = float(input())
if X >= 0 and X <= 25:
    print('Intervalo [0,25]')
elif X > 25 and X <= 50:
    print('Intervalo (25,50]')
elif X > 50 and X <= 75:
    print('Intervalo (50,75]')
elif X > 75 and X <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')'''

# IV - Aumento de Salario ************************
'''salario = float(input())
if salario >= 0 and salario <= 400:
    reajuste = salario * (15/100)
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 15 %')

if salario >= 400.01 and salario <= 800:
    reajuste = salario * (12/100)
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 12 %')

if salario >= 800.01 and salario <= 1200.00:
    reajuste = salario * (10/100)
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 10 %')

if salario >= 1200.01 and salario <= 2000.0:
    reajuste = salario * (7/100)
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 7 %')

if salario > 2000:
    reajuste = salario * (4/100)
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 4 %')'''

# V - Tempo de Jogo *********************************
'''hora_i, hora_f = map(int, input().split(' '))

if hora_i > hora_f:
    duracao = (24 + hora_f) - hora_i
    print('O JOGO DUROU {} HORA(S)'.format(duracao))
elif hora_i < hora_f:
    duracao = hora_f - hora_i
    print('O JOGO DUROU {} HORA(S)'.format(duracao))
else:
    print('O JOGO DUROU 24 HORA(S)')'''

# VI - Coordenadas de um ponto ************************
'''coord1, coord2 = map(float, input().split())
if coord1 == 0 and coord2 == 0:
    print('Origem')
elif coord1 == 0:
    print('Eixo Y')
elif coord2 == 0:
    print('Eixo X')
elif coord1 > 0 and coord2 > 0:
    print('Q1')
elif coord1 > 0 and coord2 < 0:
    print('Q4')
elif coord1 < 0 and coord2 < 0:
    print('Q3')
else:
    print('Q2')'''

#VII - Triangulo *******************************
'''A, B, C = map(float, input().split())
if A + B > C and B + C > A and A + C > B:
    perimetro = A + B + C
    print('Perimetro = {}'.format(perimetro))
else:
    print('Area = {}'.format((A + B)/2 * C))'''

#VIII - Formula de Bhaskara *************************
'''A, B, C = map(float, input().split())
delta = B**2 - 4*A*C
if A == 0:
    print('Impossivel calcular')
elif delta < 0:
    print('Impossivel calcular')
else:
    R1 = (-B + (delta**0.5))/(2*A)
    R2 = (-B - (delta**0.5))/(2*A)
    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))'''


#IX - Tipos de Triangulos - IF **********************
'''A, B, C = map(float, input().split())
if B > A:
    aux = A
    A = B
    B = aux
if C > B:
    aux = B
    B = C
    C = aux
if B > A:
    aux = A
    A = B
    B = aux

if A >= B + C:
    print('NAO FORMA TRIANGULO')
else:
    if A**2 == B**2 + C**2:
        print('TRIANGULO RETANGULO')
    if A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    if A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or B == C or A == C:
        print('TRIANGULO ISOSCELES')'''

#IX - Tipos de Triangulos - Listas ****************
'''A, B, C = map(float, input().split())
lista = [A, B, C]
lista.sort(reverse = True)
A = lista[0]
B = lista[1]
C = lista[2]

if A >= B + C:
    print('NAO FORMA TRIANGULO')
else:
    if A**2 == B**2 + C**2:
        print('TRIANGULO RETANGULO')
    if A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    if A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or B == C or A == C:
        print('TRIANGULO ISOSCELES')'''

# X - Media 3 *************************************
'''N1, N2, N3, N4 = map(float, input().split())
media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1))/10

if media >= 7:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')
elif media < 5:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
elif media > 5 or media < 6.9:
    nota_exame = float(input())
    nova_media = (media + nota_exame) / 2
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    print('Nota do exame: {:.1f}'.format(nota_exame))
    if nova_media > 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(nova_media))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(nova_media))'''

#************* Lista IV ****************************
# I - Numeros Pares
'''for x in range(2, 102, 2):
    print(x)'''

'''tempo = pa1 = pb1 = 0

t = int(input())

for n in range(0,t):

    tempo = 0

    pa,pb,g1,g2 = input().split()

    pa = int(pa); pb = int(pb); g1 = float(g1); g2 = float(g2)

    while pa <= pb:

        pa1 = (pa * (g1/100)) // 1

        pa += pa1

        pb1  = (pb * (g2/100)) // 1

        pb += pb1

        tempo += 1

        if tempo > 100:

            print('Mais de 1 seculo.')

            break

    if tempo <= 100:

        print('{} anos.'.format(tempo))'''

# II - Numeros positivos *****************************
cont = 0
for x in range(0, 6):
    v = float(input())

    if v > 0:
        cont += 1

print('{} valores positivos'.format(cont))

# III - Seis numeros impares
'''X = int(input())

if X % 2 != 0:
    X += 2
    for C in range(1, 12, 2):
        Y = X + C
        print (Y)
else:
    for C in range(1, 12, 2):
        Y = X + C
        print (Y)'''

# IV - Positivos e Media ************************
'''cont = media = soma = 0
for x in range(0, 6):
    V = float(input())

    if V > 0:
        cont += 1
        soma += V
        media = soma / cont

print('{} valores positivos'.format(cont))
print('{:.1f}'.format(media))'''

# V - Soma de impares consecutivos I *********************
'''X = int(input())
Y = int(input())

S = 0

l = []; l += X, Y
maior = max(l)
menor = min(l)

for C in range(menor+1, maior):    # +1 para não contar com o menor
    if C % 2 != 0:
        S += C
print(S)'''

# VI - Intervalo II *********************************
'''N = int(input())
out = 0; in1 = 0

for x in range(1, N + 1):
    Y = int(input())
    if Y >= 10 and Y <= 20:
        in1 += 1
    else:
        out += 1

print('{} in'.format(in1))
print('{} out'.format(out))'''

# VII - Tabuada ********************************
'''s = 0
N = int(input())

while s < 10:
    s += 1
    print('{} x {} = {}'.format(s, N, (s * N)))'''

# VIII - Maior e posiçao *****************************
'''maior = posicao = 0

for y in range(1,101):
    X = int(input())

    if y == 1:
        maior = X
        posicao == 1
    else:
        if X > maior:
            maior = X
            posicao = y

print('{}'.format(maior))
print('{}'.format(posicao))'''

# IX - Varias notas com validaçao **************************
'''while True:

    n1 = float(input())
    while n1 < 0 or n1 > 10:
        print('nota invalida')
        n1 = float(input())


    n2 = float(input())
    while n2 < 0 or n2 > 10:
        print('nota invalida')
        n2 = float(input())


    print('media = {:.2f}'.format((n1 + n2) / 2))
    print('novo calculo (1-sim 2-nao)')
    X = int(input())

    while X < 1 or X > 2:
        print('novo calculo (1-sim 2-nao)')
        X = int(input())

    if X == 2:
        break'''

# X - Crescimento populacional *****************************
'''Tempo = PA_1 = PB_1 = 0

T = int(input())

for n in range(0, T):
    Tempo = 0

    PA, PB, G1, G2 = input().split()
    PA = int(PA); PB = int(PB); G1 = float(G1); G2 = float(G2)

    while PA <= PB:
        PA_1 = (PA * (G1 / 100)) // 1
        PA += PA_1
        PB_1 = (PB * (G2 / 100)) // 1
        PB += PB_1
        Tempo += 1

        if Tempo > 100:
            print('Mais de 1 seculo.')
            break

    if Tempo <= 100:
        print('{} anos.'.format(Tempo))'''

#*************************LISTA VI****************************
# Matriz quadrada - I
'''while True:
    N = int(input())

    if N == 0 or N < 0:
        break

    resultado = []

    for i in range(N):
        aux = []
        for j in range(N):
            aux.append(1)
        resultado.append(aux)

    valor = 1
    cima = 0
    esq = 0
    baixo = N - 1
    direita = N - 1

    if (N % 2 == 0):
        meio = N / 2

    else:
        meio = (N + 1) / 2

    while (valor <= meio):
        i = esq
        while (i <= direita):
            resultado[cima][i] = valor
            resultado[baixo][i] = valor
            i+=1

        i = (cima + 1)
        while ( i < baixo):
            resultado[i][esq] = valor
            resultado[i][direita] = valor
            i+=1

        valor += 1
        cima += 1
        baixo -= 1
        esq += 1
        direita -= 1

    for i in range(N):
        tx = ''
        for j in range(N):
            tx += " %3d" %resultado[i][j]
        print(tx[1:])
    print()'''

# Preenchimento de vetores - II **************************
'''n = []
V = int(input())
n.append(V)

for i in range(10):
    V *= 2
    n.append(V)

for i in range(10):
    print('N[{}] = {}'.format(i, n[i]))'''

#OU

'''valor = int(input())
print ("N[%d] = %d" % (0, valor))
for i in range(1, 10):
    valor *= 2
    print("N[%d] = %d" %(i, valor))'''

# Números pares - III *************************************
'''for i in range(1, 101):
    if i % 2 == 0 and i > 0:
        print(i)'''

# Maior e posicao - IV ***********************************
'''maior = posicao = 0

for y in range(1,101):
    X = int(input())

    if y == 1:
        maior = X
        posicao == 1
    else:
        if X > maior:
            maior = X
            posicao = y

print('{}'.format(maior))
print('{}'.format(posicao))

# COM LISTAS e INPUT

maior =  0
lista = {}
posicao =  0
enquanto posicao <  100 :
    valor =  int ( input ())
    se (valor > maior):
        maior = valor
        lista [valor] = posicao
    posicao + =  1
imprimir (maior)
print (lista [maior] + 1 )'''

# Substituição em Vetor I - V *********************
'''X = []
for i in range(10):
    V = int(input())
    X.append(V)

    if X[i] < 1:
        X[i] = 1

for i in range(10):
    print('X[{}] = {}'.format(i, X[i]))

# OU

for i in range(10):
    valor = int(input())

    if valor < 1:
        valor = 1

    print('X[{}] = {}'.format(i, valor))'''

# Pedra, Papel, Ataque aéreo - VI ***************************
'''N = int(input())
for i in range(0, N):
    i += 1
    n1 = input()
    n2 = input()

    if n1 == 'ataque' and n2 == 'pedra':
        print('Jogador 1 venceu')

    elif n1 == 'pedra' and n2 == 'papel':
	    print('Jogador 1 venceu')

    elif n1 == 'papel' and n2 == 'ataque':
	    print('Jogador 2 venceu')

    elif n1 == 'papel' and n2 == 'papel':
	    printf('Ambos venceram')

    elif n1 == 'pedra' and n2 == 'pedra':
	    print('Sem ganhador')

    elif n1 == 'ataque' and n2 == 'ataque':
	    print('Aniquilacao mutua')

    elif n1 == 'ataque' and n2 == 'papel':
        print('Jogador 1 venceu')

    elif n1 == 'papel' and n2 == 'pedra':
        print('Jogador 2 venceu')

    elif n1 == 'pedra' and n2 == 'ataque':
        print('Jogador 2 venceu')'''
# MESMA QUESTÃO, SÓ QUE EM C, POIS O CÓDIGO ACIMA APRESENTA RUNTIME ERROR
#include <stdio.h>
'''int main (){
	int t, i;
	char n1[10], n2[10];

	scanf("%d", &t);

	for (i=0; i<t; i++){
		//fflush(stdin)
		scanf("%s", n1);
		scanf("%s", n2);

		if ((strcmp(n1,"papel") == 0) && (strcmp(n2,"papel") == 0)) {
			printf("Ambos venceram\n");
		}
                else if ((strcmp(n1,"ataque") == 0) && (strcmp(n2,"ataque")==0)) {
			printf("Aniquilacao mutua\n");
		}
                else if ((strcmp(n1,"pedra") == 0) && (strcmp(n2,"pedra") == 0)) {
			printf("Sem ganhador\n");

		}
                else if ((strcmp(n1,"ataque") == 0) && (strcmp(n2,"pedra") == 0)) {
			printf("Jogador 1 venceu\n");
		}
                else if ((strcmp(n1,"pedra") == 0) && (strcmp(n2,"ataque") == 0)) {
			printf("Jogador 2 venceu\n");
		}
                else if ((strcmp(n1,"pedra") == 0) && (strcmp(n2,"papel") == 0)) {
			printf("Jogador 1 venceu\n");
		}
                else if ((strcmp(n1,"papel") == 0) && (strcmp(n2,"pedra") == 0)) {
			printf("Jogador 2 venceu\n");
		}
                else if ((strcmp(n1,"ataque") == 0) && (strcmp(n2,"papel") == 0)) {
			printf("Jogador 1 venceu\n");
		}
                else if ((strcmp(n1,"papel") == 0) && (strcmp(n2,"ataque") == 0)) {
			printf("Jogador 2 venceu\n");
		}
	}
	return 0;
}'''

# Fuso Horário! - VII ***************************************
'''lista = input().split()
a = int(lista[0]); b = int(lista[1]); c = int(lista[2])

hora_chegada = a + b + c

if hora_chegada >= 24:
    hora_chegada = hora_chegada - 24

elif hora_chegada < 0:
    hora_chegada = hora_chegada + 24

print("{}".format(abs(hora_chegada)))'''

# I am Toorg! - VIII ******************************************
'''N = int(input())
for i in range(0, N):
    input()
    print('I am Toorg!')'''

# Notação científica - IX *************************************
'''n = input()
num = float(n)

if n[0] == "-":
    print('%.4E' % num)

else:
    print("+%.4E" % num)'''

# Numeração romana para números de página - X *****************
# Presentation error
'''numero = int(input())
if numero >= 500:
    if numero >= 900:
        print("CM", end='')
        numero -= 900
    else:
        print("D", end='')
        numero -= 500

if numero < 500 and numero >= 100:
    while numero >= 100:
        if numero >= 400:
            print("CD", end='')
            numero -= 400
        else:
            print("C", end='')
            numero -= 100

if numero < 100 and numero >= 50:
    if numero >= 90:
        print("XC", end='')
        numero -= 90
    else:
        print("L", end='')
        numero -= 50

if numero < 50 and numero >= 10:
    while numero >= 10:
        if numero >= 40:
            print("XL", end='')
            numero -= 40
        else:
            print("X", end='')
            numero -= 10

if numero < 10 and numero >= 5:
    while numero >= 5:
        if numero >= 9:
            print("IX", end='')
            numero -= 9
        else:
            print("V", end='')
            numero -= 5

if numero < 5 and numero >= 1:
    while numero >= 1:
        if numero >= 4:
            print("IV", end='')
            numero -= 4
        else:
            print("I", end='')
            numero -= 1

# Em C

#include <stdio.h>
int main() {

    int numero;

    scanf("%d", &numero);
    if (numero >= 500) {
        if (numero >= 900) {
            printf("CM");
            numero -= 900;
        }
        else {
            printf("D");
            numero -= 500;
        }
    }
    if (numero < 500 && numero >= 100) {
        while (numero >= 100) {
            if (numero >= 400) {
                printf("CD");
                numero -= 400;
            }
            else {
                printf("C");
                numero -= 100;
            }
        }
    }
    if (numero < 100 && numero >= 50) {
        if (numero >= 90) {
            printf("XC");
            numero -= 90;
        }
        else {
            printf("L");
            numero -= 50;
        }
    }
    if (numero < 50 && numero >= 10) {
        while (numero >= 10) {
            if (numero >= 40) {
                printf("XL");
                numero -= 40;
            }
            else {
                printf("X");
                numero -= 10;
            }
        }
    }
    if (numero < 10 && numero >= 5) {
        while (numero >= 5) {
            if (numero >= 9) {
                printf("IX");
                numero -= 9;
            }
            else {
                printf("V");
                numero -= 5;
            }
        }
    }
    if (numero < 5 && numero >= 1) {
        while (numero >= 1) {
            if (numero >= 4) {
                printf("IV");
                numero -= 4;
            }
            else {
                printf("I");
                numero -= 1;
            }
        }
    }
    printf("\n");
    return 0;
}'''

################## LISTA V ################################################
# Seleção em vetor I - III
'''for i in range(100):
    numero = float(input())
    if numero <= 10:
        print('A[{}] = {}'.format(i, numero))'''

# Menor e posicao - IV *********************************
'''pos = cont = 0
valor = int(input())
lista = list(map(int, input().split()))
menor = lista[0]

for i in lista:
    if i < menor:
        menor = i
        pos = cont
    cont += 1

print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(pos))'''

# Preenchimento de Vetor IV - V **************************
'''par = []
impar = []

for i in range(15):
    valor = int(input())
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

    if len(par) == 5:
        outros = 0
        for j in par:
            print('par[{}] = {}'.format(outros, j))
            outros += 1
        par = []

    if len(impar) == 5:
        outros = 0
        for j in impar:
            print('impar[{}] = {}'.format(outros, j))
            outros += 1
        impar = []

if len(impar) > 0:
    outros = 0
    for c in impar:
        print('impar[{}] = {}'.format(outros, c))
        outros += 1

if len(par) > 0:
    outros = 0
    for c in par:
        print('par[{}] = {}'.format(outros, c))
        outros += 1'''

# Linha na Matriz - VI **********************************
'''linha = int(input())
oper = input()
soma = 0

for i in range(12):
    for j in range(12):
        numero = float(input())
        if i == linha:
            soma += numero

if oper == 'S':
    print('{:.1f}'.format(soma))

else:
    print('{:.1f}'.format(soma / 12))'''

# Acima da Diagonal principal - VII *********************
'''oper = input()
soma = numero = 0
c_out = 1
c_in = 11
nao_entra = c_out
entra = c_in

for i in range(144):
	valor = float(input())

	if nao_entra + entra == 0:
		c_out += 1
		c_in -= 1
		nao_entra = c_out
		entra = c_in

	if nao_entra > 0:
		nao_entra -= 1
		continue

	if entra > 0:
		entra -= 1
		soma += valor
		numero += 1
		continue

if(oper == 'S'):
	print('{:.1f}'.format(soma))
else:
	print('{:.1f}'.format(soma / float(numero)))'''

# Acima da diagonal secundária - VIII **************
'''oper = input()
soma = numero = 0
c_out = 0
c_in = 11
nao_entra = c_out
entra = c_in

for i in range(144):
	valor = float(input())

	if entra > 0:
		entra -= 1
		soma += valor
		numero += 1
		continue

	if nao_entra > 0:
		nao_entra -= 1
		continue

	if nao_entra + entra == 0:
		c_out += 1
		c_in -= 1
		nao_entra = c_out
		entra = c_in

if(oper == 'S'):
	print('{:.1f}'.format(soma)
else:
	print('{:.1f}'.format(soma / float(numero)))'''

# area superior - IX
'''oper = input()
soma = numero = 0
c_out = 1
c_in = 10
nao_entra = c_out
entra = c_in

for i in range(144):
	valor = float(input())

	if nao_entra + entra == 0:
		c_out += 2
		c_in -= 2
		nao_entra = c_out
		entra = c_in

	if nao_entra > 0:
		nao_entra -= 1
		continue

	if entra > 0:
		entra -= 1
		soma += valor
		numero += 1
		continue

if oper == 'S':
	print('{:.1f}'.format(soma))
else:
	print('{:.1f}'.format(soma / float(numero)))'''

# Desafio PYTHON *********************************
# Notas e moedas - III
'''valor = float(input())
real = int(valor)
centavos = int((valor - real) * 100)

n100 = real // 100
real = real - (n100 * 100)
n50 = real // 50
real = real - (n50 * 50)
n20 = real // 20
real = real - (n20 * 20)
n10 = real // 10
real = real - (n10 * 10)
n5 = real // 5
real = real - (n5 * 5)
n2 = real // 2
real = real - (n2 * 2)

m1 = 0
if real:
    m1 = 1

m50 = centavos // 50
centavos = centavos - (m50 * 50)
m25 = centavos // 25
centavos = centavos - (m25 * 25)
m10 = centavos // 10
centavos = centavos - (m10 * 10)
m05 = centavos // 5
centavos = centavos - (m05 * 5)
m01 = centavos

print('NOTAS:')
print(n100, 'nota(s) de R$ 100.00')
print(n50, 'nota(s) de R$ 50.00')
print(n20, 'nota(s) de R$ 20.00')
print(n10, 'nota(s) de R$ 10.00')
print(n5, 'nota(s) de R$ 5.00')
print(n2, 'nota(s) de R$ 2.00')
print('MOEDAS:')
print(m1, 'moeda(s) de R$ 1.00')
print(m50, 'moeda(s) de R$ 0.50')
print(m25, 'moeda(s) de R$ 0.25')
print(m10, 'moeda(s) de R$ 0.10')
print(m05, 'moeda(s) de R$ 0.05')
print(m01, 'moeda(s) de R$ 0.01')'''
