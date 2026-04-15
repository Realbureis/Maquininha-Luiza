import streamlit as st

# Configuração da página com o nome da clínica
st.set_page_config(page_title="Luiza Pérola - Estética Avançada", page_icon="💎")

st.title("💎 Luiza Pérola - Estética Avançada")
st.subheader("Calculadora de Repasse de Taxas (Ton)")
st.markdown("---")

# 1. Entrada do valor que ela quer receber líquido (Preço do procedimento)
valor_liquido = st.number_input("Quanto você quer receber (Líquido)?", min_value=0.0, value=1000.0, step=50.0)

# 2. Dicionário completo com os DIVISORES (Plano R$ 6k - R$ 10k)
# Lógica: Valor / Divisor = Valor com taxa embutida
divisores = {
    "Débito (1,34%)": 0.9866,
    "Crédito 1x (3,31%)": 0.9669,
    "Crédito 2x (7,18%)": 0.9282,
    "Crédito 3x (8,56%)": 0.9144,
    "Crédito 4x (9,44%)": 0.9056,
    "Crédito 5x (10,31%)": 0.8969,
    "Crédito 6x (11,17%)": 0.8883,
    "Crédito 7x (12,02%)": 0.8798,
    "Crédito 8x (12,88%)": 0.8712,
    "Crédito 9x (13,74%)": 0.8626,
    "Crédito 10x (14,58%)": 0.8542,
    "Crédito 11x (15,44%)": 0.8456,
    "Crédito 12x (16,30%)": 0.8370,
    "Crédito 18x (17,90%)": 0.8210
}

# 3. Seleção da forma de pagamento
opcao = st.selectbox("Selecione a forma de pagamento:", list(divisores.keys()))

# 4. Cálculos automáticos
divisor_selecionado = divisores[opcao]
valor_venda = valor_liquido / divisor_selecionado
custo_maquininha = valor_venda - valor_liquido

# 5. Exibição dos resultados com destaque
st.markdown("---")
st.write("### Resultado para passar na máquina:")
st.metric(label="VALOR TOTAL A COBRAR", value=f"R$ {valor_venda:,.2f}")

with st.expander("Detalhamento Financeiro"):
    st.write(f"**Valor para a Luiza:** R$ {valor_liquido:,.2f}")
    st.write(f"**Taxa da Ton (Desconto):** R$ {custo_maquininha:,.2f}")
    st.info("Dinheiro disponível na conta na mesma hora!")

st.caption("Fórmulas baseadas nas taxas Ton 2026 - Configuração para recebimento imediato.")
