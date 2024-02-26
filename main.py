import streamlit as st
import os
import importlib
from exercises import exercise

st.set_page_config(
    page_title="MME",
    page_icon=":satellite-antenna:",
    layout="centered",
    initial_sidebar_state="expanded",
)
st.title("řešené úlohy matematika v mikroekonomii")


ulohy = []
for file in os.listdir('exercises'):
    if file.endswith('.py'):
        import_name = file.rpartition('.')[0]
        module = importlib.import_module(f'exercises.{import_name}')
        classes = [getattr(module, x) for x in dir(module) if isinstance(getattr(module, x), type)]
        for cls in classes:
            if issubclass(cls, exercise.Exercise) and cls != exercise.Exercise:
                ulohy.append(cls())

solved = st.sidebar.radio("Vyber úlohu", ulohy)
st.sidebar.divider()

solved.render_navbar(st.sidebar)
solved.render_body()