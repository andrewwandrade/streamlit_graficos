import plotly.express as px

# Inteção 1

def build_fig22(df):
    contagem_intencao1 = df["Intenção1"].value_counts().reset_index()
    contagem_intencao1.columns = ["Escala", "Contagem"]

    fig22 = px.bar(
        contagem_intencao1,
        x="Escala",
        y="Contagem",
        title="Eu gostaria de viajar usando o app<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig22.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig22.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig22, "Intenção1"

# Inteção 2

def build_fig23(df):
    contagem_intencao2 = df["Intenção2"].value_counts().reset_index()
    contagem_intencao2.columns = ["Escala", "Contagem"]

    fig23 = px.bar(
        contagem_intencao2,
        x="Escala",
        y="Contagem",
        title="O app é um bom jeito de se locomover pela cidade<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig23.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig23.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig23, "Intenção2"

# Inteção 3

def build_fig24(df):
    contagem_intencao3 = df["Intenção3"].value_counts().reset_index()
    contagem_intencao3.columns = ["Escala", "Contagem"]

    fig24 = px.bar(
        contagem_intencao3,
        x="Escala",
        y="Contagem",
        title="Eu pretendo usar o app nos próximos 7 dias<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig24.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig24.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig24, "Intenção3"

figuras = [build_fig22, build_fig23, build_fig24]
mostrar_estatisticas = True