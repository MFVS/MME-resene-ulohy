import streamlit as st
import os
import importlib
from exercise import Exercise
from routing import Routing_Context

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
found_classes = []
for file in os.listdir("exercises"):
    if not file.endswith(".py"):
        continue
    import_name = file.rpartition(".")[0]

    module = importlib.import_module(f"exercises.{import_name}")
    importlib.reload(module)
    found_classes.extend([
        getattr(module, x)
        for x in dir(module)
        if isinstance(getattr(module, x), type)
    ])
removed_classes = []
for cls in reversed(found_classes): # removes classes that aren't exercises
    if not issubclass(cls, Exercise) or cls is Exercise:
        found_classes.remove(cls)
        removed_classes.append(cls)
        continue
    # st.warning(f"chapter identifier: {cls().chapter_identifier()}")
    exercise = cls()
    exercises[exercise.chapter_identifier()] = exercise
# TODO: detect duplicate exercise classnames

# st.info(f"removed classes {removed_classes}")

# link nested exercises
top_level_chapters = {}
sorted_chapter_ids = sorted(exercises.keys())
# st.info(f"list {sorted_chapters}")
for chapter_id in sorted_chapter_ids:
    parent = top_level_chapters
    exercise = exercises.get(chapter_id)
    assert isinstance(exercise, Exercise), f"cannot use {exercise} because an Exercise subclass is expected"
    id = exercise.chapter_identifier()
    # st.info(f"exercise {exercise}")
    subchapter_id_list = id.split(".")
    assert len(subchapter_id_list) > 0, f"invalid chapter identifier {id}"
    if len(subchapter_id_list) == 1:
        top_level_chapters[id] = exercise
        continue
    assert isinstance(parent, Exercise) or parent is top_level_chapters, f"cannot use {parent} because an Exercise subclass is expected"
    for id_part in subchapter_id_list[:-1]:
        parent = parent.get(id_part)
        assert parent is not None
        assert isinstance(parent, Exercise) or parent is top_level_chapters, f"cannot use {parent} because an Exercise subclass is expected"
        # st.info(f"{id_part}:{parent}")
    last_id_part = id[-1]
    # st.info(f"{type(last_id_part)} : {parent}")
    assert (
        parent is not top_level_chapters
    ), f"exercise {exercise.chapter_identifier()} is missing a parent exercise"
    assert isinstance(exercise, Exercise), f"cannot use {exercise} because an Exercise subclass is expected"
    if parent is exercise:
        continue
    parent[last_id_part] = exercise

# register routes
ctx = Routing_Context(default="Domů")

# def register_route_recursively(exercise):
#     for child_id in exercise.keys():
#         child = exercise.get(child_id)
#         @ctx.route(child.chapter_identifier())
#         def handler():
#             st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)
#             if st.button("← Domů", key="chapter_move_home"):
#                 ctx.redirect("Domů")
#             left_button, right_button = st.columns([2.4, 1])
#             # TODO:
#             with left_button:
#                 if st.button(f"← Předchozí úloha", key="chapter_move_left"):
#                     ctx.redirect("Domů")

#             with right_button:
#                 st.empty()
#                 if st.button(f"Následující úloha →", key="chapter_move_right"):
#                     ctx.redirect("Domů")

#             st.markdown("---")
#             exercises[exercise.chapter_identifier()].render_body()
#     # recurse further
#     for toplevel_id in exercise.keys():
#         child_exercise = exercise.get(toplevel_id)
#         register_route_recursively(child_exercise)

def register_routes(exercise):
    @ctx.route(exercise.chapter_identifier())
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
        exercise.render_body()
    for child_id in exercise.keys():
        st.info(f"{exercise.__str__()} {child_id}")
        register_routes(exercises.get(child_id))

# TODO: this doesn't work at all
for id in exercises:
    exercise = exercises.get(id)
    @ctx.route(exercise.chapter_identifier())
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
        exercises.get(id).render_body()
    # register_routes(top_level_chapters.get(id))
# register_route_recursively(top_level_chapters)

# st.info(f"total {len(top_level_chapters)} top level chapters")

@ctx.route("Domů")
def homepage():
    for top_level_chapter in top_level_chapters:
        chapter = top_level_chapters[top_level_chapter]
        st.title(f"{chapter.chapter_identifier()} {chapter}")
        chapter.render_body()
        cols = st.columns(4)
        for i, subchapter_id in enumerate(chapter.subchapters):
            subchapter = chapter.subchapters[subchapter_id]
            btn_text = f"{subchapter.chapter_identifier()} {subchapter}"
            index = i%4
            col = cols[index]
            with col:
                if st.button(btn_text, key=btn_text):
                    ctx.redirect(subchapter.chapter_identifier())


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
