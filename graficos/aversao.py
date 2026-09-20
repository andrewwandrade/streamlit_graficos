import plotly.express as px

# Aversão 1

def build_fig6(df):
    contagem_aversao1 = df["Aversao1"].value_counts().reset_index()
    contagem_aversao1.columns = ["Escala", "Contagem"]

    fig6 = px.bar(
        contagem_aversao1,
        x="Escala",
        y="Contagem",
        title="Prefiro comprar/contratar marcas que eu já conheço do que experimentar marcas novas<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig6.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig6.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig6, "Aversao1"

# Aversão 2

def build_fig7(df):
    contagem_aversao2 = df["Aversao2"].value_counts().reset_index()
    contagem_aversao2.columns = ["Escala", "Contagem"]

    fig7 = px.bar(
        contagem_aversao2,
        x="Escala",
        y="Contagem",
        title="Sempre compro/contrato algo que conheço pois assim garanto que não vou errar<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig7.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig7.update_layout(
        margin=dict(l=20, r=20, t=40, b=20)
    )

    return fig7, "Aversao2"

# Aversão 3

def build_fig8(df):
    contagem_aversao3 = df["Aversao3"].value_counts().reset_index()
    contagem_aversao3.columns = ["Escala", "Contagem"]

    fig8 = px.bar(
        contagem_aversao3,
        x="Escala",
        y="Contagem",
        title="Compro/contrato apenas marcas bem estabelecidas<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig8.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig8.update_layout(
        margin=dict(l=20, r=20, t=40, b=20)
    )

    return fig8, "Aversao3"

# Aversão 4

def build_fig9(df):
    contagem_aversao4 = df["Aversao4"].value_counts().reset_index()
    contagem_aversao4.columns = ["Escala", "Contagem"]

    fig9 = px.bar(
        contagem_aversao4,
        x="Escala",
        y="Contagem",
        title="Sou muito cauteloso ao experimentar produtos novos ou diferentes<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig9.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig9.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig9, "Aversao4"

figuras = [build_fig6, build_fig7, build_fig8, build_fig9]
mostrar_estatisticas = True