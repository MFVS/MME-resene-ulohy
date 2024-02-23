from .exercise import Exercise
import streamlit as st

class Uloha_Trapny_Grafy(Exercise):
    def render_navbar(self, sidebar):
        sidebar.write("Tady budou parametry")
    def render_body(self):
        st.write("Tady bude tvoje řešení")
    def __str__(self) -> str:
        return "Trapný grafy"

class Uloha_Dalsi_Grafy(Exercise):
    def render_navbar(self, sidebar):
        sidebar.write("Tady budou jiné parametry")
    def render_body(self):
        st.write("Tady bude tvoje další řešení")
    def __str__(self) -> str:
        return "Další grafy"