import streamlit as st
import os
import importlib
from exercises.exercise import Exercise
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

exercises = {}

# load all exercise classes from the `exercises` folder
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
            if issubclass(cls, Exercise) and cls != Exercise:
                exercises[cls().chapter_identifier()] = cls()

# link nested exercises
linked = {}
for id, exercise in sorted((exercises.items()), key=lambda x: x[0]):
    subchapter_id_list = id.split(".")
    chapter_id = id[-1]
    subchapter_id_list = subchapter_id_list[:-1]
    parent = subchapter_id_list
    for split in subchapter_id_list:
        assert (
            parent.get(split) is not None
        ), f"exercise {exercise.chapter_identifier()} is missing a parent exercise"
        parent = parent.get(split)
    parent[chapter_id] = exercise

# register routes
ctx = Routing_Context(default="Domů")


def register_route_recursively(exercise):
    for child_id, child in exercise.enumerate():
        @ctx.route(child.chapter_identifier())
        def handler():
            st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)
            if st.button("← Domů", key="chapter_move_home"):
                ctx.redirect("Domů")
            left_button, right_button = st.columns([2.4, 1])
            # TODO:
            with left_button:
                if st.button(f"← Předchozí úloha", key="chapter_move_left"):
                    ctx.redirect("Domů")

            with right_button:
                st.empty()
                if st.button(f"Následující úloha →", key="chapter_move_right"):
                    ctx.redirect("Domů")

            st.markdown("---")
            exercises[exercise.chapter_identifier()].render_body()
    # recurse further
    for toplevel_id, child_exercise in exercise.enumerate():
        register_route_recursively(child_exercise)



register_route_recursively(linked)


@ctx.route("Domů")
def homepage():
    render_topics(exercises)


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
