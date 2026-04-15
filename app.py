import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora Clínica Luiza", page_icon="💉")

st.title("💉 Calculadora de Taxas - Ton")
st.markdown("---")

# 1. Entrada do valor que ela quer receber líquido
valor_desejado = st.number_input("Quanto você quer receber (Líquido)?", min_value=0.0, value=1000.0, step=50.0)

# 2. Dicionário com as taxas e os divisores (Plano R$ 6k - R$ 10k)
# Lógica: divisor = (1 - taxa_decimal)
taxas_config = {
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
opcao = st.selectbox("Forma de Pagamento:", list(taxas_config.keys()))

# 4. Cálculo do valor a cobrar
divisor = taxas_config[opcao]
valor_a_cobrar = valor_desejado / divisor
custo_taxa = valor_a_cobrar - valor_desejado

# 5. Exibição dos resultados
st.markdown("---")
st.subheader("Resultado para passar na máquina:")
st.metric(label="Valor a Cobrar da Cliente", value=f"R$ {valor_a_cobrar:,.2f}")

with st.expander("Ver detalhes da transação"):
    st.write(f"**Valor que cairá na sua conta:** R$ {valor_desejado:,.2f}")
    st.write(f"**Custo da taxa da Ton:** R$ {custo_taxa:,.2f}")
    st.info("O dinheiro cai na sua conta na mesma hora!")

# Rodapé simples
st.caption("Taxas baseadas no Plano Ton (R$ 6k a R$ 10k) - Atualizado 2026")
