import streamlit as st
import pandas as pd
from graficos import perfil, aversao, confianca, seguranca, intencao_uso, comunicacao
from streamlit_option_menu import option_menu
from utils.plot_config import plot
from utils.estatistica import calcular_estatisticas

SECOES = {
    "Perfil do entrevistado": perfil,
    "Aversão": aversao,
    "Confiança": confianca,
    "Segurança": seguranca,
    "Intenção de uso": intencao_uso,
    "Comunicação": comunicacao,
}

def render_page(df):
    with st.sidebar:
        st.markdown("# Visualização de Dados")
        st.markdown("## ")
        secao_escolhida = option_menu(
            menu_title="Categorias",
            options=list(SECOES.keys()),
            icons=[
                "person",
                "shield-exclamation",
                "heart",
                "lock",
                "cursor",
                "megaphone",
            ],
            menu_icon="caret-right-fill",
            default_index=0,
        )

    modulo = SECOES[secao_escolhida]
    mostrar_stats = getattr(modulo, "mostrar_estatisticas")

    st.header(secao_escolhida)
    st.markdown("---")

    # Lista para acumular as estatísticas do módulo
    lista_stats = []

    for build_fig in modulo.figuras:
        if mostrar_stats:
            fig, coluna = build_fig(df)
            plot(fig)

            stats = calcular_estatisticas(df, coluna)
            lista_stats.append(stats)

            # Formata apenas na hora de exibir a tabela individual
            df_stats_exibicao = pd.DataFrame(
                [{"Estatística": k, "Valor": f"{v:.2f}"} for k, v in stats.items()]
            )
            st.table(df_stats_exibicao)

            st.write("")
            st.write("")
        else:
            fig = build_fig(df)
            plot(fig)
            st.write("")
            st.write("")

    # Exibe a média das estatísticas no final da página
    if mostrar_stats and lista_stats:
        st.write("")
        st.write("")
        st.markdown("## Média Geral das Estatísticas da Seção")

        df_todas_stats = pd.DataFrame(lista_stats)
        medias_finais = df_todas_stats.mean()

        df_media_exibicao = pd.DataFrame(
            {
                "Estatística": medias_finais.index,
                "Média das Colunas": medias_finais.values,
            }
        )

        # Formata os valores para 2 casas decimais na exibição
        df_media_exibicao["Média das Colunas"] = df_media_exibicao[
            "Média das Colunas"
        ].apply(lambda x: f"{x:.2f}")

        st.table(df_media_exibicao)
    
    st.markdown("---")
    st.caption("Painel desenvolvido como parte da entrega do Case Técnico - Okiar Intelligence")
    st.caption("Andrew de Andrade")