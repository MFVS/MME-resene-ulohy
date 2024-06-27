import streamlit as st
import os
import importlib
from exercises import exercise
import matplotlib.pyplot as plt
from routing import Routing_Context
from homepage import render_topics

st.set_page_config(
    page_title="MME",
    page_icon=":satellite-antenna:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """
st.html(hide_streamlit_style)

st.title("Řešené úlohy z matematiky v mikroekonomii")

ulohy = {}
for file in os.listdir("exercises"):
    if file.endswith(".py"):
        import_name = file.rpartition(".")[0]
        module = importlib.import_module(f"exercises.{import_name}")
        importlib.reload(module)
        classes = [
            getattr(module, x)
            for x in dir(module)
            if isinstance(getattr(module, x), type)
        ]
        for cls in classes:
            if issubclass(cls, exercise.Exercise) and cls != exercise.Exercise:
                ulohy[cls().__str__()] = cls()

ctx = Routing_Context(default="Domů")

for i, u in enumerate(ulohy):
    @ctx.route(str(u))
    def handler():
        ulohy[str(u)].render_body()


@ctx.route("Domů")
def homepage():
    render_topics(ulohy)


ctx.render()

# solved = st.sidebar.radio("Vyber úlohu", ulohy)
st.sidebar.divider()

st.markdown(
    """
    <style>
    a#linkto_top {
        color: white;
        text-decoration: none;
        border: 0.5px solid #41444C;
        padding-top: 7px;
        padding-bottom: 10px;
        padding-left: 12px;
        padding-right: 12px;
        border-radius: 7px;
        background-color: #131720;
    }
    </style>

    <center><a href='#linkto_top' id='linkto_top'>↑ Zpět nahoru</a></center>
""",
    unsafe_allow_html=True,
)
