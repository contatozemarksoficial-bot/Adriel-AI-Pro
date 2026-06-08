import streamlit as st

# Configuração premium de layout amplo (Força a barra lateral nativa a nascer fechada)
st.set_page_config(page_title="Adriel-AI Pro - Core Dashboard", layout="wide", initial_sidebar_state="collapsed")

# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ PRO FALA AO ENTRAR NA HOME)
texto_boas_vindas = "Olá, Comandante José Marques da Silva! O núcleo de Inteligência Artificial tridimensional está ativo nos servidores do Adriel A I Pro. Selecione os módulos numerados na barra lateral."

st.markdown(f"""
<script>
    document.addEventListener('click', function() {{
        if (!window.audioDisparado) {{
            var msg = new SpeechSynthesisUtterance();
            msg.text = "{texto_boas_vindas}";
            msg.lang = "pt-BR";
            msg.rate = 1.0;
            msg.pitch = 0.92;
            window.speechSynthesis.speak(msg);
            window.audioDisparado = true;
        }}
    }});
</script>
""", unsafe_allow_html=True)

# INJEÇÃO DE CSS DE ALTO LUXO (ESTILO BLACK E SINAL PISCANTE HOVER NO MENU LATERAL)
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Fiel ao Print do Leonardo AI */
    .stApp { background-color: #0b111e !important; color: #ffffff !important; }
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    
    /* 🚨 FORÇA A OCULTAÇÃO ABSOLUTA DA BARRA LATERAL CINZA NATIVA DO STREAMLIT */
    [data-testid="stSidebar"] {
        display: none !important;
        width: 0px !important;
    }
    [data-testid="stHeader"] { display: none !important; }
    
    /* Recorta o contêiner principal para usar 100% do monitor livremente */
    .stMainBlockContainer {
        max-width: 100% !important;
        width: 100% !important;
    }

    /* Caixas centrais */
    .header-box-real { background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 8px !important; padding: 12px 18px !important; margin-bottom: 15px !important; }
    .kpi-box { background: #0f172a; padding: 10px 15px; border-radius: 8px; border: 1px solid #1e293b; text-align: center; }
</style>
""", unsafe_allow_html=True)

# Interface do Painel Central Geral em 2 Colunas Livres de amarras lógicas
col_centro, col_direita = st.columns([1.4, 1.0])

with col_centro:
    st.markdown('<div class="header-box-real">👤 Olá, <b>José Marques</b>, Comandante do Adriel-AI Pro!</div>', unsafe_allow_html=True)
    st.markdown("### 🎛️ CENTRAL OPERACIONAL SAAS MASTER")
    st.write("Sua nova infraestrutura modular está 100% ativa e limpa de travas cinzas. Use o menu do seu navegador ou as chaves síncronas para operar o tráfego.")
    
with col_direita:
    st.markdown('<div class="header-box-real" style="text-align: right;">🟢 Licença PRO: <span style="color:#00FF87; font-weight:bold;">Ativa e Vitalícia</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="kpi-box"><span style="font-size:11px;color:#64748b;font-weight:bold;">🔥 STATUS DO LEILÃO</span><br><span style="font-size:20px;color:#00FF87;font-weight:800;">SÍNCRONO 🟢</span></div>', unsafe_allow_html=True)
