# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 11:26:50 2024

@author: Daniel
"""
import time
import streamlit as st
import random

def obtener_jugada_usuario():
    jugada = st.radio('Elige', ('Piedra :fist:', "Papel :hand:", "Tijera :v:"))
    return jugada

def obtener_jugada_computadora():
    return random.choice(['Piedra :fist:', "Papel :hand:", "Tijera :v:"])

def determinar_ganador(jugada_usuario, jugada_computadora):
    if jugada_usuario == jugada_computadora:
        return "Empate"
    elif (jugada_usuario == 'Piedra :fist:' and jugada_computadora == "Tijera :v:") or (jugada_usuario == "Papel :hand:" and jugada_computadora == 'Piedra :fist:') or (jugada_usuario == "Tijera :v:" and jugada_computadora == "Papel :hand:"):
        return "¡Ganaste!"
    else:
        return "La computadora gana"

jugada = 'elige tu jugada'

resultado = 'haz tu elección'

col1, col2, col3 = st.columns(3)

with col1:
   b_1 = st.button(":fist:")
   if b_1:
       jugada = 'Piedra :fist:'

with col2:
   b_2 = st.button(":hand:")
   if b_2:
       jugada = "Papel :hand:"


with col3:
   b_3 = st.button(":v:")
   if b_3:
       jugada = "Tijera :v:"
computadora = obtener_jugada_computadora()

col1, col2, col3 = st.columns(3)
with col2:

    if jugada == 'elige tu jugada':
        resultado = 'Empieza a jugar'
    else:
        gestos = [':fist:',':hand:',':v:',computadora]
        placeholder = st.empty()
        for i in gestos:
            with placeholder.container():
                placeholder.empty()
                placeholder.write(i)
            time.sleep(0.5)
        st.write('Has sacado: '+ jugada )
        st.write('y Computadora sacó: ' + computadora)
        if jugada == computadora:
            resultado = "Empate :crossed_swords:"
        elif (jugada == 'Piedra :fist:' and computadora == "Tijera :v:") or (jugada == "Papel :hand:" and computadora == 'Piedra :fist:') or (jugada == "Tijera :v:" and computadora == "Papel :hand:"):
            resultado = "Ganaste :trophy:"
        else:
            resultado = "La computadora gana :shit:"
           
    st.header(resultado)

