import plotly.express as px
import pandas as pd

# Gráfico de gêneros

def build_fig1(df):
    contagem = df["Genero"].value_counts().reset_index()
    contagem.columns = ["Genero", "Contagem"]

    fig1 = px.pie(
        contagem,
        names="Genero",
        values="Contagem",
        title="Distribuição por Gênero"
    )

    fig1.update_traces(
        textinfo="label+percent", 
        textposition="inside",
        marker=dict(colors=["#E74B4C", "#960D0D"])
    )

    fig1.update_layout(
        margin=dict(l=20, r=20, t=100, b=20),
        showlegend=False,
        height=300,
        width=400
    )

    return fig1

# Gráfico de faixas de renda

def build_fig2(df):
    mapa_faixas = {
        "Até 150 dólares": "0-150",
        "Entre 150 e 300 dólares": "150-300",
        "Entre 300 e 600 dólares": "300-600",
        "Entre 600 e 900 dólares": "600-900",
        "Entre 900 e 1200 dólares": "900-1200",
        "Entre 1200 e 1500 dólares": "1200-1500",
        "Entre 1500 e 1800 dólares": "1500-1800",
        "Entre 2100 e 2400 dólares": "2100-2400",
        "Mais do que 2700 dólares": "+2700"
    }

    contagem_renda = df["Renda_Individual"].value_counts().reset_index()
    contagem_renda.columns = ["Faixa_Renda", "Contagem"]

    contagem_renda["Faixa_Renda_Curta"] = pd.Categorical(
        contagem_renda["Faixa_Renda"].map(mapa_faixas),
        categories=list(mapa_faixas.values()),
        ordered=True
    )

    contagem_renda = contagem_renda.sort_values("Faixa_Renda_Curta")

    fig2 = px.bar(
        contagem_renda,
        x="Faixa_Renda_Curta",
        y="Contagem",
        title="Distribuição de Renda Individual",
        text="Contagem"
    )

    fig2.update_traces(textposition="outside", marker_color="#E74B4C")
    fig2.update_layout(
        xaxis_title="Faixa de Renda (em US$)",
        yaxis_title="Número de Pessoas",
        margin=dict(l=20, r=20, t=40, b=20),
        hovermode=False
    )

    return fig2

# Histograma de idades

def build_fig3(df):
    idades = df['Idade'].str.replace(' anos', '', regex=False).astype(int)
    df_idades = idades.reset_index(name="Idade")

    fig3 = px.histogram(
        df_idades,
        x = "Idade",
        title="Distribuição por Idade",
        nbins=None,
    )

    fig3.update_traces(
        xbins=dict(
            start=idades.min() - (idades.min() % 5), 
            end=idades.max() + 5,
            size=5
        ),
        marker=dict(
            line=dict(
                color="black", 
                width=1       
            )
        ),
        marker_color="#E74B4C",
        texttemplate="%{y}",
        textposition="outside"
    )

    fig3.update_layout(
        xaxis_title="Idade",
        yaxis_title="Número de pessoas",
        margin=dict(l=20, r=20, t=40, b=20)
    )

    return fig3

# Gráfico depretencimento à cidade

def build_fig4(df):
    mapa_pertencimento = {0: "Outras cidades", 1: "Buenos Aires"}

    contagem_pertencimento = df["Cidade_é_buenos_aires"].map(mapa_pertencimento).value_counts().reset_index()
    contagem_pertencimento.columns = ["Categoria", "Contagem"]

    fig4 = px.pie(
        contagem_pertencimento,
        names="Categoria",
        values="Contagem",
        title="Mora em Buenos Aires?"
    )

    fig4.update_traces(
        textinfo="label+percent", 
        textposition="inside",
        marker=dict(colors=["#E74B4C", "#960D0D"])
    )

    fig4.update_layout(
        margin=dict(l=20, r=20, t=100, b=20),
        showlegend=False,
        height=300,
        width=400
    )

    return fig4

# Gráfico de filhos

def build_fig5(df):
    mapa_filhos = {
        "Não possuo filhos": 0,
        "1 filho": 1,
        "2 filhos": 2,
        "3 filhos": 3,
        "4 filhos": 4,
        "5 filhos ou mais": 5
    }

    contagem_filhos = df["Filhos"].map(mapa_filhos).value_counts()
    contagem_filhos = contagem_filhos.reindex(list(mapa_filhos.values()), fill_value=0).reset_index()
    contagem_filhos.columns = ["Filhos", "Contagem"]

    fig5 = px.bar(
        contagem_filhos,
        x="Filhos",
        y="Contagem",
        title="Quantidade de filhos do entrevistado",
        text="Contagem"
    )

    fig5.update_traces(textposition="outside", marker_color="#E74B4C")
    fig5.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        hovermode=False,
        xaxis=dict(
            dtick=1,     
            tick0=0       
        )
    )

    return fig5

figuras = [build_fig1, build_fig2, build_fig3, build_fig4, build_fig5]
mostrar_estatisticas = False