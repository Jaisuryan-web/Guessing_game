import streamlit as st
import random

if 'attempts' not in st.session_state:
  st.session_state['attempts'] = 0
if 'target_number' not in st.session_state:
  st.session_state.target_number = random.randint(1, 100)
#header
st.markdown(
    "<h1 style='text-align: center; color:red ;'>GUESSING GAME</h1>",
    unsafe_allow_html=True)
#subheader
st.write("Guess the number between 1 and 100...")
#input from user
guess = st.number_input("Enter your guess:", min_value=1, max_value=100)
#checking the guessed value
if st.button("SUBMIT"):
  st.session_state.attempts += 1
#checking attempts
if st.session_state.attempts > 5:
  st.write("YOU HAVE EXCEEDED THE ATTEMPT,TRY AGAIN...")
else:
  if guess == st.session_state.target_number:
    st.success(f"CONGRATULATIONS!!! YOU WON...")
    st.session_state.attempts = 0
    st.session_state.target_number = random.randint(1, 100)
  elif guess < st.session_state.target_number:
    st.write("try guessing a bigger number:")
  else:
    st.write("try guessing a small number:")
#remaining attempts
  st.write(f"attempts left: {5-st.session_state.attempts}")
#reset
if st.button("RESET"):
  st.session_state.attempts = 0
  st.session_state.target_number = random.randint(1, 100)
  st.write("GAME HAS BEEN RESETED,START A NEW TRY...")