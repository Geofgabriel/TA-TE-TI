# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 13:09:14 2020

@author: Gabriel R. Gelpi
"""
import numpy as np # como se vio el la clase, esta es una libreria recomendada
# para trabajar con matrices.

#====================================
# funciones que necesita el programa
#====================================
""" En esta funcion se define el tablero a medida que avanza el juego. 
tt: tablero
pos: posicion en el tablero elegido por el jugador
jug: jugador 1 o 2""" 
def tablero(jug,pos,tt, marca=True): # Para tener el tablero por pantalla

    if marca == True:  
        if jug == 1:
            tt[pos-1] = 'X' # Jugador 1 con 'X'
        else:
            tt[pos-1] = 'O' # Jugador 2 con 'O'
    else:
        if jug == 1:
            tt[pos-1] = 'O' # Jugador 1 con 'X'
        else:
            tt[pos-1] = 'X' # Jugador 2 con 'O'
        
    print('|',tt[0],'|',tt[1],'|',tt[2],'|')
    print('|',tt[3],'|',tt[4],'|',tt[5],'|')
    print('|',tt[6],'|',tt[7],'|',tt[8],'|')    

""" Para saber quien gana se suman las filas, columnas y diagonales de la matriz.
Cuando la suma de cierto nro gana el jugador 1 o el 2.
j: es el nro de jugador 1 o 2
pos: la posición dentro de la matriz
a: es el arreglo con las posiciones elegidas por cada jugador
"""    
    
def mat(j,pos,a): 

    g1 = 0
    if j == 1:
        a[pos-1] = 1 # Pone un 1 en la matriz aara el jugador 1
    else:
        a[pos-1] = 10 # Pone un 10 en la matriz para el jugador 2
    
    aa = np.reshape(a,(3,3)) #doy forma de matriz al arreglo de numpy
    cont_fil = 0 
    cont_col = 0
    cont_diag = np.trace(aa) # cuenta los valores sobre la diagonal principal
    cont_diag_inv = np.trace(np.flip(aa)) # cuenta los valores sobre la diagonal principal opuesta
    
    for i in range(0,3):

        cont_fil = np.sum(aa[:,i])# cuenta sobre las filas
        cont_col = np.sum(aa[i,:])# cuenta sobre las columnas
        
        if cont_fil == 3 or cont_col ==3 or cont_diag == 3 or cont_diag_inv==3:
           print('Gano jugador 1!')
           g1=20
        elif cont_fil == 30 or cont_col ==30 or cont_diag == 30 or cont_diag_inv ==30:
           print('Gano el jugador 2!')
           g1=20
              
    return a,g1

#=================================================
# comienza el TATETI
#=================================================

print('Bienvenidos al TATETI!') 
print('El tablero para este juego es el siguiente:')
print('|_|_|_|\n|_|_|_| \n|_|_|_|')

print('Por favor jugador 1 elija si quiere jugar con cruz o circulo (tenga en cuenta que empiezan las X!)')
m = str(input()).upper()

if m == 'X':
    marca = True
else:
    marca = False
    
print('La posición en el tablero donde colocar las \'X\' o \'O\' queda definida mediante:')
print('|1|2|3|\n|4|5|6| \n|7|8|9|')



a = np.ones(9)*1000 # Array para guardar las posiciones de los jugadores.
# el 1000 es para no tener problea con la suma de los valores de cada fila,col y diag. 
tt = ['#','#','#','#','#','#','#','#','#'] # Matriz del Tablero.
repetidos = []
i = 0
g = 0
while i < 20: # maximo son 9 movimientos pero puede haber gente que mire mal el tablero
    if marca == True:
        if i % 2 == 0:
        
            print('Ingrege posición en el tablero jugador 1')
            j1 = int(input())
        
            if j1 in repetidos:
                print('Por favor mire el tablero y reingrese posición')
                j1 = int(input())
                
            repetidos.append(j1)  
            tablero(1,j1,tt,marca)
            a,g = mat(1,j1,a)
    
        else:
        
            print('Ingrege posición en el tablero jugador 2')
            j2 = int(input())
            
            if j2 in repetidos:
                print('Por favor mire el tablero y reingrese posición')
                j2 = int(input())
                
            repetidos.append(j2)   
            tablero(2,j2,tt,marca)
            a,g = mat(2,j2,a)
        
        if i == 8 and g != 20:
            print('Empate!')
    else:
        if i % 2 == 0:
        
            print('Ingrege posición en el tablero jugador 2')
            j2 = int(input())
        
            if j2 in repetidos:
                print('Por favor mire el tablero y reingrese posición')
                j2 = int(input())
                
            repetidos.append(j2)  
            tablero(2,j2,tt,marca)
            a,g = mat(2,j2,a)
    
        else:
        
            print('Ingrege posición en el tablero jugador 1')
            j1 = int(input())
            
            if j1 in repetidos:
                print('Por favor mire el tablero y reingrese posición')
                j1 = int(input())
                
            repetidos.append(j1)   
            tablero(1,j1,tt,marca)
            a,g = mat(1,j1,a)
        
        if i == 8 and g != 20:
            print('Empate!')
    i += 1+g
