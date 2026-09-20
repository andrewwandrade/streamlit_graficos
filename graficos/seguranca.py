import plotly.express as px

# Segurança 1

def build_fig19(df):
    contagem_seguranca1 = df["Segurança1"].value_counts()
    contagem_seguranca1 = contagem_seguranca1.reindex(range(1, 8), fill_value=0).reset_index() #Necessária para que todas as escalas apareçam
    contagem_seguranca1.columns = ["Escala", "Contagem"]

    fig19 = px.bar(
        contagem_seguranca1,
        x="Escala",
        y="Contagem",
        title="Considerando a segurança geral do app, você diria que ela é boa ou ruim?<br><sup><i>Escala: [1] Totalmente ruim e [7] Totalmente boa</i></sup>"
    )

    fig19.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig19.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig19, "Segurança1"

# Segurança 2

def build_fig20(df):
    contagem_seguranca2 = df["Segurança2"].value_counts().reset_index()
    contagem_seguranca2.columns = ["Escala", "Contagem"]

    fig20 = px.bar(
        contagem_seguranca2,
        x="Escala",
        y="Contagem",
        title="Considerando a segurança geral do app, você diria que ela é consistente?<br><sup><i>Escala: [1] Totalmente inconsistente e [7] Totalmente consistente</i></sup>"
    )

    fig20.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig20.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig20, "Segurança2"

# Segurança 3

def build_fig21(df):
    contagem_seguranca3 = df["Segurança3"].value_counts().reset_index()
    contagem_seguranca3.columns = ["Escala", "Contagem"]

    fig21 = px.bar(
        contagem_seguranca3,
        x="Escala",
        y="Contagem",
        title="Considerando a segurança geral do app, você diria que ela é forte ou fraca?<br><sup><i>Escala: [1] Totalmente forte e [7] Totalmente fraco</i></sup>"
    )

    fig21.update_traces(textposition="outside", texttemplate="%{y}", marker_color="#E74B4C")
    fig21.update_layout(
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig21, "Segurança3"

figuras = [build_fig19, build_fig20, build_fig21]
mostrar_estatisticas = True