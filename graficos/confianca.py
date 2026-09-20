import plotly.express as px

# Confiança 1

def build_fig10(df):
    contagem_confianca1 = df["Confianca1"].value_counts().reset_index()
    contagem_confianca1.columns = ["Escala", "Contagem"]

    fig10 = px.bar(
        contagem_confianca1,
        x="Escala",
        y="Contagem",
        title="O app cumpre o que promete<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig10.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig10.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig10, "Confianca1"

# Confiança 2

def build_fig11(df):
    contagem_confianca2 = df["Confianca2"].value_counts().reset_index()
    contagem_confianca2.columns = ["Escala", "Contagem"]

    fig11 = px.bar(
        contagem_confianca2,
        x="Escala",
        y="Contagem",
        title="Os motoristas do app são confiáveis<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig11.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig11.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig11, "Confianca2"

# Confiança 3

def build_fig12(df):
    contagem_confianca3 = df["Confianca3"].value_counts().reset_index()
    contagem_confianca3.columns = ["Escala", "Contagem"]

    fig12 = px.bar(
        contagem_confianca3,
        x="Escala",
        y="Contagem",
        title="O app tem um nome em que se pode confiar<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig12.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig12.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig12, "Confianca3"

# Confiança 4

def build_fig13(df):
    contagem_confianca4 = df["Confianca4"].value_counts().reset_index()
    contagem_confianca4.columns = ["Escala", "Contagem"]

    fig13 = px.bar(
        contagem_confianca4,
        x="Escala",
        y="Contagem",
        title="O app não finge ser algo que não é<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig13.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig13.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig13, "Confianca4"

# Confiança 5

def build_fig14(df):
    contagem_confianca5 = df["Confianca5"].value_counts().reset_index()
    contagem_confianca5.columns = ["Escala", "Contagem"]

    fig14 = px.bar(
        contagem_confianca5,
        x="Escala",
        y="Contagem",
        title="O app oferece carros com um nível de qualidade constante<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig14.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig14.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig14, "Confianca5"

# Confiança 6

def build_fig15(df):
    contagem_confianca6 = df["Confianca6"].value_counts().reset_index()
    contagem_confianca6.columns = ["Escala", "Contagem"]

    fig15 = px.bar(
        contagem_confianca6,
        x="Escala",
        y="Contagem",
        title="O app ajuda a resolver qualquer problema que se possa ter com as viagens<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig15.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig15.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig15, "Confianca6"

# Confiança 7

def build_fig16(df):
    contagem_confianca7 = df["Confianca7"].value_counts().reset_index()
    contagem_confianca7.columns = ["Escala", "Contagem"]

    fig16 = px.bar(
        contagem_confianca7,
        x="Escala",
        y="Contagem",
        title="O app está interessado na satisfação dos clientes<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig16.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig16.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig16, "Confianca7"

# Confiança 8

def build_fig17(df):
    contagem_confianca8 = df["Confianca8"].value_counts().reset_index()
    contagem_confianca8.columns = ["Escala", "Contagem"]

    fig17 = px.bar(
        contagem_confianca8,
        x="Escala",
        y="Contagem",
        title="O app valoriza os clientes<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig17.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig17.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig17, "Confianca8"

# Confiança 9

def build_fig18(df):
    contagem_confianca9 = df["Confianca9"].value_counts().reset_index()
    contagem_confianca9.columns = ["Escala", "Contagem"]

    fig18 = px.bar(
        contagem_confianca9,
        x="Escala",
        y="Contagem",
        title="O app é um app confiável<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig18.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig18.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig18, "Confianca9"

figuras = [build_fig10, build_fig11, build_fig12, build_fig13, build_fig14, build_fig15, build_fig16, build_fig17, build_fig18]
mostrar_estatisticas = True