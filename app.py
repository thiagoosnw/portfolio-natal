import streamlit as st
import os

st.set_page_config(page_title="Portfólio L.D.M", layout="wide", page_icon="🎅")

arquivo_logo = "logo.png"

col_hdr_esq, col_hdr_dir = st.columns([1, 6])

with col_hdr_esq:
        st.image(arquivo_logo, use_container_width=True)

with col_hdr_dir:
    st.title("L.D.M Personalizados")
    st.markdown("#### Coleção Especial de Natal 🎅")

st.write("---")
st.markdown("### Selecione sua arte preferida")

extensoes_validas = ['.jpg', '.jpeg', '.png', '.webp']
todos_arquivos = os.listdir('.')
imagens = [arq for arq in todos_arquivos if any(arq.lower().endswith(ext) for ext in extensoes_validas) and arq != arquivo_logo]

if not imagens:
    st.info("Aguardando carregamento das imagens na galeria...")
else:
    colunas = st.columns(4)
    for index, arquivo_imagem in enumerate(imagens):
        coluna_atual = colunas[index % 4]
        with coluna_atual:
            with st.container(border=True):
                st.image(arquivo_imagem, use_container_width=True)
                st.markdown(f"<h5 style='text-align: center;'>🎁 Opção {index + 1}</h5>", unsafe_allow_html=True)
                st.caption(f"Ref: {arquivo_imagem}")

st.write("---")
st.markdown("<p style='text-align: center; color: grey;'>© L.D.M Personalizados - Todos os direitos reservados.</p>", unsafe_allow_html=True)