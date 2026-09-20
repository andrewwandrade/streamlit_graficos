import streamlit as st

config_do_plotly = {
    "displayModeBar": True,
    "modeBarButtonsToRemove": ["zoom", "pan", "select", "lasso2d", "zoomIn", "zoomOut", "autoScale", "resetScale"]
}

def plot(fig):
    st.plotly_chart(fig, use_container_width=True, config=config_do_plotly)