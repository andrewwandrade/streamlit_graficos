import plotly.express as px

# Comunicação 1
def build_fig25(df):
    contagem_comunicacao1 = df["Comunicação1"].value_counts().reset_index()
    contagem_comunicacao1.columns = ["Escala", "Contagem"]

    fig25 = px.bar(
        contagem_comunicacao1,
        x="Escala",
        y="Contagem",
        title="Vejo muitas propagandas do app<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig25.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig25.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig25, "Comunicação1"

# Comunicação 2
def build_fig26(df):
    contagem_comunicacao2 = df["Comunicação2"].value_counts().reset_index()
    contagem_comunicacao2.columns = ["Escala", "Contagem"]

    fig26 = px.bar(
        contagem_comunicacao2,
        x="Escala",
        y="Contagem",
        title="Vejo muitas propagandas do app na TV<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig26.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig26.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig26, "Comunicação2"


# Comunicação 3
def build_fig27(df):
    contagem_comunicacao3 = df["Comunicação3"].value_counts().reset_index()
    contagem_comunicacao3.columns = ["Escala", "Contagem"]

    fig27 = px.bar(
        contagem_comunicacao3,
        x="Escala",
        y="Contagem",
        title="Leio muitas notícias sobre o app nos principais jornais do país<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig27.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig27.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig27, "Comunicação3"


# Comunicação 4
def build_fig28(df):
    contagem_comunicacao4 = df["Comunicação4"].value_counts().reset_index()
    contagem_comunicacao4.columns = ["Escala", "Contagem"]

    fig28 = px.bar(
        contagem_comunicacao4,
        x="Escala",
        y="Contagem",
        title="Com frequência, vejo o app nas minhas redes sociais<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig28.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig28.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig28, "Comunicação4"


# Comunicação 5
def build_fig29(df):
    contagem_comunicacao5 = df["Comunicação5"].value_counts().reset_index()
    contagem_comunicacao5.columns = ["Escala", "Contagem"]

    fig29 = px.bar(
        contagem_comunicacao5,
        x="Escala",
        y="Contagem",
        title="Interajo bastante com o app nas minhas redes sociais<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig29.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig29.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig29, "Comunicação5"


# Comunicação 6
def build_fig30(df):
    contagem_comunicacao6 = df["Comunicação6"].value_counts().reset_index()
    contagem_comunicacao6.columns = ["Escala", "Contagem"]

    fig30 = px.bar(
        contagem_comunicacao6,
        x="Escala",
        y="Contagem",
        title="Meus amigos me recomendam o app com frequência<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig30.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig30.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig30, "Comunicação6"


# Comunicação 7
def build_fig31(df):
    contagem_comunicacao7 = df["Comunicação7"].value_counts().reset_index()
    contagem_comunicacao7.columns = ["Escala", "Contagem"]

    fig31 = px.bar(
        contagem_comunicacao7,
        x="Escala",
        y="Contagem",
        title="Pessoas que sigo nas redes sociais recomendam o app<br><sup><i>Escala: [1] Discordo totalmente e [7] Concordo totalmente</i></sup>"
    )

    fig31.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig31.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig31, "Comunicação7"


figuras = [build_fig25, build_fig26, build_fig27, build_fig28, build_fig29, build_fig30, build_fig31]
mostrar_estatisticas = True