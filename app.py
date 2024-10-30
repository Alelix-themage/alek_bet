import streamlit as st
import banco as bc

st.title("Aposta do Corinthians caindo")
st.image("./assets/funeral.jpeg")


nome = st.text_input("Nome")

st.warning("Coloque a aposta dessa forma, exemplo: '3x0'")
with st.container():
    st.markdown("Curintias X Palmeiras")
    st.image("./assets/jogo1.jpeg")
    jogo1 = st.text_input("Digite o Placar do jogo:", key=1)
    
with st.container():
    st.markdown("Vitória X Curintias")
    st.image("./assets/jogo2.jpeg")
    jogo2 = st.text_input("Digite o Placar do jogo:", key=2)
    
with st.container():
    st.markdown("Curintias X Cruzeiro")
    st.image("./assets/jogo3.jpeg")
    jogo3 = st.text_input("Digite o Placar do jogo:", key=3)
    
with st.container():
    st.markdown("Curintias X Vasco")
    st.image("./assets/jogo4.jpeg")
    jogo4 = st.text_input("Digite o Placar do jogo:", key=4)
    
with st.container():
    st.markdown("Criciuma X Curintias")
    st.image("./assets/jogo5.jpeg")
    jogo5 = st.text_input("Digite o Placar do jogo:", key=5)
    
with st.container():
    st.markdown("Curintias X Bahia")
    st.image("./assets/jogo6.jpeg")
    jogo6 = st.text_input("Digite o Placar do jogo:", key=6)
    
with st.container():
    st.markdown("Gremio X Curintias")
    st.image("./assets/jogo7.jpeg")
    jogo7 = st.text_input("Digite o Placar do jogo:", key=7)


bt = st.button("Validar Aposta")

if bt:
    bc.inserirBanco(nome, jogo1, jogo2, jogo3, jogo4, jogo5, jogo6, jogo7)

st.dataframe(bc.selectBanco())
