import numpy as np
import csv


#NÃO CALCULEI AS MEDIAS DE TODAS AS PESSOAS JUNTAS

def average_timestamps(filename):
	#ELE TAMBÉM QUER QUE USEMOS O TEMPO DO ACELEROMETRO
	data = []
	#just throw in all the cells of the file, row by row
	for row in csv.reader(open(filename + '.csv', 'rb'))
    	#FALTA TIRAR A MÉDIA ENTRE TODOS OS CRONOMETROS DA POSIÇÃO "i" E COLOCAR EM DATA[]
    	#QUERO A POSIÇÃO 0 COM O TEMPO MÉDIO PRA IR DE 0M A 10M, A POSIÇÃO 2 COM O TEMPO MÉDIO PRA IR DE 10M A 20M...
    	data.append(row)
    return data;

def MRU_velocity(time):
	#cada posição de velocity_array vai ter a distância percorrida (10m) dividida pelo tempo gasto (time_array[i]),
	#que é a velocidade desenvolvida em cada posição (espera-se que seja constante)
    time_array = time
    velocity_array = []
    for i in range(time_array.len()):
        velocity_array.append(10/time_array[i])
    return velocity_array

def MRU_plot(velocity):


def MRUV_velocity(time):
	#cada posição de velocity_array vai ter a distância percorrida (10m) dividida pelo tempo gasto (time_array[i]),
	#que é a velocidade desenvolvida em cada posição (nao é constante)
	time_array = time
    velocity_array = []
    #coloquei esse zero pra conseguir calcular delta_v para os primeiros 10m 
    velocty_array.append(0)
    for i in range(time_array.len()):
        velocity_array.append(10/time_array[i])
    return velocity_array

def MRUV_accel(velocity):
	#cada posição de accel_array vai ter (vf - vo)/tf - to, isso é a aceleração em cada ponto (10, 20, 30)
	#(espera-se constante)
	#..."Assim, precisa calcular acelera¸c˜ao apessoa de cada pessoa, a acelera¸c˜ao m´edia de todas
	#as pessoas usando os dados. A partir disso, deve-se calcular a velocidade e a posi¸c˜ao
	#simuladas usando as equa¸c˜oes do movimento"
	#NAO ENTENDI ISSO. PRA TER A ACELERAÇÃO PRA CALCULAR A VELOCIDADE, NÉ?
	velocity_array = velocity
    accel_array = []
    for i in range(1, velocity_array.len()):
        accel_array.append((velocity_array[i] - velocity_array[i-1])/time_array[i])
    return accel_array


def MRUV_plot(accel):

def main():
	#chamar average timestamps e calcular MRU_velocity e MRU_plot pra cada pessoa
	#chamar average_timestamps e calcular MRUV_velocity e MRUV_accel pra cada pessoa
main()





