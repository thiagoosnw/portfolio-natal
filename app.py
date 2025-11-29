import streamlit as st
import os

st.set_page_config(page_title="Portfólio de Natal", layout="wide")

st.title("🎅 Galeria de Artes de Natal")
st.markdown("### Confira abaixo as opções disponíveis para personalização.")
st.write("---")

extensoes_validas = ['.jpg', '.jpeg', '.png', '.webp']

todos_arquivos = os.listdir('.')

imagens = [arq for arq in todos_arquivos if any(arq.lower().endswith(ext) for ext in extensoes_validas)]

if not imagens:
    st.error("Nenhuma imagem encontrada na pasta!")
else:
    colunas = st.columns(3)
    
    for index, arquivo_imagem in enumerate(imagens):
        
        coluna_atual = colunas[index % 3]
        
        with coluna_atual:
            with st.container(border=True):
                st.image(arquivo_imagem, use_container_width=True)
                st.button(f"Opção {index + 1}", key=f"btn_{index}", use_container_width=True)
                st.caption(f"Arquivo: {arquivo_imagem}")

st.write("---")
st.success("Fim da galeria.")