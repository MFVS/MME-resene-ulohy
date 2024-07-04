from exercise import Exercise
import streamlit as st


class Matematicke_Zaklady(Exercise):
    def chapter_identifier(self):
        return "0"

    def __str__(self) -> str:
        return "Matematické základy"

    def render_body(self):
        st.text("Ukazuje zásadní matematické koncepty v mikroekonomii")


class Teorie_Spotrebitele(Exercise):
    def chapter_identifier(self):
        return "1"

    def __str__(self) -> str:
        return "Teorie spotřebitele"

    def render_body(self):
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


class Teorie_Firmy(Exercise):
    def chapter_identifier(self):
        return "2"

    def __str__(self) -> str:
        return "Teorie Firmy"

    def render_body(self):
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
