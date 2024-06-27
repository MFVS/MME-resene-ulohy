import streamlit as st
from routing import Routing_Context


class Chapter:
    def __str__(self):
        raise NotImplementedError()

    def description(self):
        raise NotImplementedError()


class Matematicky_Zaklad:
    def __str__(self) -> str:
        return "Matematický základ"

    def description(self):
        st.text("Ukazuje zásadní matematické koncepty v mikroekonomii")


class Teorie_Spotrebitele:
    def __str__(self) -> str:
        return "Teorie spotřebitele"

    def description(self):
        st.markdown(
            """
            <div style="text-align: justify">
            V rámci teorie spotřebitele se zaměříme na zkoumání toho, jak spotřebitelé jednají na trzích s výrobním zbožím a službami. 
            Naše pozornost se bude soustředit na parciální rovnováhu, což znamená, že se budeme snažit najít rovnovážný stav na jednom z trhů.
            Tento rovnovážný stav se nazývá optimum spotřebitele a jedná se o rozložení investic spotřebitele do jednotlivých statků za účelem
            maximalizace užitku nebo minimalizace výdajů. Ke hledání optima spotřebitele slouží následující úlohy.
            </div>
            <br>
            """,
            unsafe_allow_html=True,
        )


class Teorie_Firmy:
    def __str__(self) -> str:
        return "Teorie Firmy"

    def description(self):
        st.markdown(
            """
            <div style="text-align: justify"> 
            V předchozí kapitole jsme zkoumali rozhodování spotřebitele, který je poptávajícím na trzích zboží a služeb.
            Nyní se zaměříme na výrobce, který na těchto trzích své produkty nabízí. V případě teorie firmy budeme mít dva různé typy úloh:
            <ul style="margin-top: 10px; margin-bottom: 10px;">
            <li>minimalizaci nákladů, kdy má firma pevně stanovený objem produkce a řeší, jak tento objem vyrobit s minimálními náklady,</li>
            <li>maximalizaci zisku, kdy firma volí objem vyrobeného zboží a způsob, jak tento objem vyrobit, aby při tom dosáhla
            co nejvyššího zisku.</li>
            </ul> 
            Úloha minimalizace nákladů je významná především z toho důvodu, že její výsledek můžeme dále použít při řešení
            úlohy maximalizace zisku. Nejprve se ale budeme zabývat produkční funkcí firmy, která je základem neoklasického
            popisu firmy a je klíčovou součástí všech následujících úloh.
            </div>
            <br>
            """,
            unsafe_allow_html=True,
        )


topics = [Matematicky_Zaklad(), Teorie_Spotrebitele(), Teorie_Firmy()]


def render_topics(ulohy):
    for chapter_index, chapter in enumerate(topics):
        subchapters = []
        for exercise_index in ulohy:
            u = ulohy.get(exercise_index)
            if u.chapter_name() == str(chapter):
                subchapters.append(u)
        subchapters.sort(key=lambda x: x.subchapter_number())

        st.title(f"{chapter_index} {chapter.__str__()}")
        chapter.description()
        if len(subchapters) == 0:
            st.warning("No subchapters")
            continue
        cols = st.columns(len(subchapters) + 1)
        for [subchapter, col] in zip(subchapters, cols[:-1]):
            print(f"MAYBE REDIRECTING TO {str(subchapter)}")
            if col.button(
                ".".join([str(chapter_index), str(subchapter.subchapter_number())])
                + "\t"
                + str(subchapter),
                "menu_choose_button" + str(chapter_index) + str(subchapter),
            ):
                print(f"ACTUALLY REDIRECTING TO {str(subchapter)}")
                Routing_Context().redirect(str(subchapter))
