import numpy as np
import random

n_boxes = 36#numero de casilas

RED = np.arange(start=1, stop=n_boxes + 1, step=2, dtype=int)#rojas, apuesta!!!
black = np.arange(start=2, stop=n_boxes + 1, step=2, dtype=int)#negras
zero = np.array([0])

budget = 1000#presupuesto
start_bet = 1#apuesta inicial
lose_increment = 2.0#coeficiente de incremento de apuesta si pierdo
win_increment = 2.0#coeficiewnte de ganancia si gano
waiting_time = 30#tiempo de espera
max_consecutive_lose = 16#maximo de perdidas consecutiva

all_boxes = np.arange(start=0, stop=n_boxes + 1, step=1, dtype=int)#todas las casillas
consecutive_lose = np.zeros(max_consecutive_lose, dtype=int)#registro de numero de perdidas maximas consecutivas
balance = budget#balance (variable)
current_bet = start_bet#apuesta en curso (variable)
elapsed_time = 0#tiempo de juego
count_lose = 0

while balance >= 0 and count_lose < max_consecutive_lose:
 balance -= current_bet#deducimos la apuesta en curso
 result = random.randint(0,n_boxes)#resultado

 if result in RED:#si ganamos
  balance += current_bet * win_increment#sumamos la ganancia
  consecutive_lose[count_lose] += 1#registramos el numero de perdidas consecutivas
  current_bet = start_bet#reestablecemos la apuesta en curso a la inicial
  count_lose = 0#reestablecemos el conteo de las perdidas consecutivas
  
 else:#si perdemos
  current_bet *= lose_increment#multiplicamos la apuesta por el factor de incremento
  count_lose += 1#incrementamos el conteo de las perdidas consecutivas
 elapsed_time += waiting_time#agregamos el tiempo que duro la apuesta

 print(f"Tiempo: {round(elapsed_time/3600, 2)}h, Balance:{balance}, Apuesta:{current_bet}, Consecutivas:{consecutive_lose}")

print(32 * "*")
print(f"REGISTRO FINAL")
print(f"Tiempo total transcurrido de juego: {round(elapsed_time/3600, 2)}horas")
print(f"Balance final requerido para continuar:{balance}")
print(f"Ultima apuesta ejecutada/requerida:{current_bet}")
print(f"Ultima racha de perdidas consecutivas (la puntada final):{count_lose}")
consecutive_lose[count_lose] += 1
print(f"Registro de maximos consecutivos perdidos:\n{consecutive_lose}")