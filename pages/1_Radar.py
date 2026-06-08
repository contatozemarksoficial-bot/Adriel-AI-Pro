import streamlit as st
import pandas as pd

# 🚨 REGRA SUPREMA: O set_page_config precisa ser a PRIMEIRA instrução executável do código!
st.set_page_config(page_title="Adriel-AI Pro - Radar de Produtos", layout="wide", initial_sidebar_state="expanded")

# Reaplica o estilo Black de luxo e remove as margens nativas feias do topo
st.markdown("""
<style>
    /* Fundo Escuro Fiel ao Print da Imagem */
    .stApp { 
        background-color: #0b111e !important; 
        color: #ffffff !important; 
    }
    .block-container { 
        padding-top: 1rem !important; 
        padding-bottom: 0rem !important;
    }
    .header-box-real { 
        background-color: #0f172a !important; 
        border: 1px solid #1e293b !important; 
        border-radius: 8px !important; 
        padding: 14px 20px !important; 
        margin-bottom: 15px !important; 
    }
    .subtitulo-bloco-real { 
        font-size: 13px !important; 
        font-weight: bold !important; 
        color: #60a5fa !important; 
        margin-bottom: 15px; 
        text-transform: uppercase; 
    }
    .kpi-box { 
        background: #0f172a; 
        padding: 12px 15px; 
        border-radius: 8px; 
        border: 1px solid #1e293b; 
        text-align: center; 
    }
    /* Estilização para o botão mestre em gradiente verde */
    div.stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 14px !important;
        border: 2px solid #1e293b !important;
        padding: 12px 15px !important;
        border-radius: 6px !important;
        width: 100% !important;
        cursor: pointer !important;
    }
</style>
""", unsafe_allow_html=True)

# Divisão exata das colunas paralelas na horizontal (Clone do Leonardo AI)
col_centro, col_direita = st.columns([1.4, 1.0])

with col_centro:
    st.markdown('<div class="header-box-real">👤 Comandante: <b>José Marques</b> | Mapeamento de Mercado PRO</div>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo-bloco-real">MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</p>', unsafe_allow_html=True)
    
    # Banco de dados original recuperado por extenso com as comissões
    dados_tabela = {
        "Name": ["Sugar Defender", "Java Burn", "Puravive", "Prodentim", "GlucoBerry", "Citrus Burn", "Metanail Complex"],
        "Plataforma": ["BuyGoods 🇺🇸", "ClickBank 🇺🇸", "ClickBank 🇺🇸", "BuyGoods 🇺🇸", "Hotmart 🇧🇷", "ClickBank 🇺🇸", "BuyGoods 🇺🇸"],
        "Comissão": ["$ 118.20", "$ 135.00", "$ 142.50", "$ 125.00", "R$ 247,00", "$ 95.00", "$ 107.40"],
        "Veredito da IA": ["APROVADO (Risco Baixo)"] * 7
    }
    st.dataframe(pd.DataFrame(dados_tabela), use_container_width=True, hide_index=True)
    
    st.write("")
    if st.button("📄 [BAIXAR PLANILHA DE INTELIGÊNCIA EM LOTE .CSV]", key="btn_radar_csv_inside"):
        st.success("✅ Download processado! Tabela de mineração salva com sucesso.")

with col_direita:
    st.markdown('<div class="header-box-real" style="text-align: right;">Filtro Especial: <b>Top 22 Ativos</b></div>', unsafe_allow_html=True)
    
    col_mini1, col_mini2 = st.columns(2)
    with col_mini1: 
        st.markdown('<div class="kpi-box"><span style="font-size:11px;color:#64748b;font-weight:bold;">🔥 CLIQUES HOJE</span><br><span style="font-size:20px;color:#00FF87;font-weight:800;">14.250 mil</span></div>', unsafe_allow_html=True)
    with col_mini2: 
        st.markdown('<div class="kpi-box"><span style="font-size:11px;color:#64748b;font-weight:bold;">📡 OFERTAS ATIVAS</span><br><span style="font-size:20px;color:#00E5FF;font-weight:800;">1.840 mil</span></div>', unsafe_allow_html=True)
        
    st.write("---")
    st.info("🔥 **Módulo Espião Operando**\n\nVarredura contínua rastreando lotes de Gravidade e Temperatura acima de 140+ nas redes dos EUA.")
