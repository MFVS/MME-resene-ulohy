from .exercise import Exercise
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from .styling import latex_style, latex_img, box_style


class Produkcni_Funkce(Exercise):
    def subchapter_number(self):
        return 3

    def chapter_name(self):
        return "Teorie Firmy"

    def __str__(self) -> str:
        return "Maximalizace zisku"

    def render_body(self):
        st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)

        left_button, right_button = st.columns([7.07, 1])

        with left_button:
            if st.button("← 2.2 Minimalizace nákladů", key="1"):
                st.session_state.page = "min_naklady"
                st.rerun()

        with right_button:
            if st.button("Domů →", key="2"):
                st.session_state.page = "uvod"
                st.rerun()

        st.markdown("---")

        st.subheader("2.3 Maximalizace zisku")
        st.markdown(
            """
            <div style="text-align: justify"> 
            Při úloze maximalizace zisku musíme o vyráběném objemu zboží rozhodnout. Stále
            však máme na paměti naše úvahy o minimalizaci nákladů a tento objem zboží chceme
            vyrobit co nejlevněji.
            <br>
            <br>
            </div>
            """,
            unsafe_allow_html=True,
        )

        funkce_zisk_definice = f"""
        <div style="{box_style}">
            <b>Definice funkce zisku</b>: 
            Funkce zisku <img src="{latex_img}{'\\pi'}" style="{latex_style}" /> udává zisk firmy v závislosti na
            ceně práce <img src="{latex_img}{'w'}" style="{latex_style}" />, ceně kapitálu
            <img src="{latex_img}{'r'}" style="{latex_style}" /> a prodejní ceně zboží <img src="{latex_img}{'P'}" style="{latex_style}" /> .           
        </div>
        """

        st.markdown(funkce_zisk_definice, unsafe_allow_html=True)

        st.markdown(
            """
            <div style="text-align: justify">
            <br>
            Existují dva způsoby, jak řešit úlohu maximalizace zisku:
            </div>
            """,
            unsafe_allow_html=True,
        )

        metoda = st.radio(
            "x", ["Dvoustupňová metoda", "Přímá metoda"], label_visibility="hidden"
        )

        st.markdown(
            f"""
            <div style="text-align: justify">
            Dvoustupňová metoda předpokládá, že nejprve budeme řešit úlohu minimalizace nákladů (nebo využijeme již existující řešení této úlohy)
            a teprve potom se zaměříme na maximalizaci zisku. Naopak přímá metoda předpokládá, že při řešení maximalizace zisku se přímo
            řídíme produkční funkcí. Dvoustupňová metoda je tedy náročnější výpočetně, ale přímá metoda nám neposkytne informace o
            nákladové funkci <img src="{latex_img}{'LTC(w, r, Q)'}" style="{latex_style}" />. Probereme obě metody.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # Boční panel pro zadání parametrů
        if metoda == "Dvoustupňová metoda":
            P = st.sidebar.slider(
                "Prodejní cena $P$", min_value=500, max_value=5000, value=2500, step=1
            )

            LFC = st.sidebar.slider(
                "Fixní náklady $LFC$", min_value=10, max_value=1000, value=500, step=1
            )

            LVC = st.sidebar.slider(
                "Variabilní náklady $LVC$", min_value=10, max_value=1000, value=500, step=1
            )

            c = st.sidebar.slider(
                "Parametr $c$", min_value=2.0, max_value=5.0, value=3.0, step=0.01
            )

            # Shrnutí zadaných parametrů
            parameters = f"""<div style="{box_style}">
                            <img src="{latex_img}{'P='}{P}" style="{latex_style}" />
                            <br>
                            <img src="{latex_img}{'LFC='}{LFC}" style="{latex_style}" />
                            <br>
                            <img src="{latex_img}{'LVC='}{LVC}" style="{latex_style}" />
                            <br>
                            <img src="{latex_img}{'c='}{c}" style="{latex_style}" />
                        </div>"""
            st.sidebar.markdown(parameters, unsafe_allow_html=True)

            metoda2_definice = f"""
            <div style="{box_style}">
                <b>Definice dvoustupňové metody</b>:
                Dvoustupňová metoda maximalizace zisku firmy předpokládá nejprve minimalizaci nákladů (tj. odvození funkce
                <img src="{latex_img}{'LTC'}" style="{latex_style}" />). Poté řešíme úlohu
                    <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'\\max_Q   \\pi = P \\cdot Q - LTC(w, r, Q)'}" style="{latex_style}" />
                    </div>
                za podmínky
                    <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'Q \\geq 0'}" style="{latex_style}" /> ,
                    </div>
                kde <img src="{latex_img}{'\\pi'}" style="{latex_style}" /> je funkce zisku, <img src="{latex_img}{'P'}" style="{latex_style}" />
                je prodejní cena zboží, <img src="{latex_img}{'Q'}" style="{latex_style}" /> je výstup (produkce) a
                <img src="{latex_img}{'LTC(w, r, Q)'}" style="{latex_style}" /> je nákladová funkce určená ještě pomocí cen výrobních faktorů
                <img src="{latex_img}{'w, '}" style="{latex_style}" /> .
            </div>
            """

            st.markdown(metoda2_definice, unsafe_allow_html=True)

            zisk = round(
                P * (P / (c * LVC)) ** (1 / (c - 1))
                - LFC
                - LVC * (P / (c * LVC)) ** (c / (c - 1)),
                2,
            )
            st.markdown(
                f"""<div style="text-align: justify">
                        <br>
                        Budeme uvažovat jednoduchou nákladovou funkci
                        <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'LTC = LFC + LVC \\cdot Q^c'}" style="{latex_style}" /> ,
                        </div>
                        kde <img src="{latex_img}{'LFC'}" style="{latex_style}" /> jsou fixní náklady,
                        <img src="{latex_img}{'LVC'}" style="{latex_style}" /> jsou variabilní náklady na jednotku zboží a
                        <img src="{latex_img}{'c'}" style="{latex_style}" /> je parametr produkce.
                        Po dosazení tedy máme funkci zisku v tomto tvaru
                        <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'\\pi(Q) = P \\cdot Q - LFC - LVC \\cdot Q^c'}" style="{latex_style}" /> .
                        </div>
                        V bočním panelu si nastavte prodejní cenu, parametr <img src="{latex_img}{'c'}" style="{latex_style}" />,
                        fixní náklady a variabilní náklady. Následně hledáme optimální vyráběné množství <img src="{latex_img}{'Q'}" style="{latex_style}" />.
                        Určíme první derivaci funkce zisku a položíme ji rovnou <img src="{latex_img}{'0'}" style="{latex_style}" />
                        <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'\\frac{\\partial \\pi}{\\partial Q} = P - c \\cdot LVC \\cdot Q^{c-1} = 0'}" style="{latex_style}" /> ,
                        </div>
                        potom vyjádříme <img src="{latex_img}{'Q'}" style="{latex_style}" />
                        <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'Q = \\left( \\frac{P}{c \\cdot LVC} \\right)^{\\frac{1}{c-1}}'}" style="{latex_style}" /> ,
                        </div>
                        dosadíme optimální množství vyrobeného zboží do funkce zisku a vypočítáme zisk firmy
                        <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'\\pi(Q) = P \\cdot \\left( \\frac{P}{c \\cdot LVC} \\right)^{\\frac{1}{c-1}} - LFC - LVC \\cdot \\left( \\frac{P}{c \\cdot LVC} \\right)^{\\frac{c}{c-1}} ='}{zisk}" style="{latex_style}" />
                        </div>
                        </div>""",
                unsafe_allow_html=True,
            )

        else:
            P = st.sidebar.slider(
                "Prodejní cena $P$", min_value=500, max_value=5000, value=2500, step=1
            )

            w = st.sidebar.slider(
                "Cena práce $w$", min_value=10, max_value=1000, value=500, step=1
            )

            r = st.sidebar.slider(
                "Cena kapitálu $r$", min_value=10, max_value=1000, value=500, step=1
            )

            c = st.sidebar.slider(
                "Parametry $c$ a $d$", min_value=0.01, max_value=0.99, value=0.5, step=0.01
            )
            d = round(1 - c, 2)

            # Shrnutí zadaných parametrů
            parameters = f"""<div style="{box_style}">
                            <img src="{latex_img}{'P='}{P}" style="{latex_style}" />
                            <br>
                            <img src="{latex_img}{'w='}{w}" style="{latex_style}" />
                            <br>
                            <img src="{latex_img}{'r='}{r}" style="{latex_style}" />
                            <br>
                            <img src="{latex_img}{'c='}{c}" style="{latex_style}" />
                            <br>
                            <img src="{latex_img}{'d='}{d}" style="{latex_style}" />
                        </div>"""
            st.sidebar.markdown(parameters, unsafe_allow_html=True)

            metoda1_definice = f"""
            <div style="{box_style}">
                <b>Definice přímé metody</b>: 
                Přímou metodou při maximalizaci zisku firmy máme na mysli řešení následující úlohy
                    <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'\\max_{K, L}   \\pi = P \\cdot Q(L, K) - w \\cdot L - r \\cdot K'}" style="{latex_style}" />
                    </div>
                za podmínek
                    <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'L \\geq 0'}" style="{latex_style}" /> , <img src="{latex_img}{'K \\geq 0'}" style="{latex_style}" /> ,
                    </div>
                kde <img src="{latex_img}{'\\pi'}" style="{latex_style}" /> je funkce zisku, <img src="{latex_img}{'P'}" style="{latex_style}" />
                je prodejní cena zboží, <img src="{latex_img}{'Q'}" style="{latex_style}" /> je produkční funkce,
                <img src="{latex_img}{'L'}" style="{latex_style}" /> je práce, <img src="{latex_img}{'K'}" style="{latex_style}" /> je kapitál,
                <img src="{latex_img}{'w'}" style="{latex_style}" /> a <img src="{latex_img}{'r'}" style="{latex_style}" /> jsou ceny těchto výrobních faktorů.
            </div>
            """

            st.markdown(metoda1_definice, unsafe_allow_html=True)

            zisk = round(P - w * ((c * r) / (d * w)) ** d - r * ((d * w) / (c * r)) ** c, 2)
            st.markdown(
                f"""<div style="text-align: justify">
                        <br>
                        Budeme uvažovat jednoduchou Cobb-Douglasovu produkční funkci
                        <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'Q(L, K) = L^c \\cdot K^d'}" style="{latex_style}" /> ,
                        </div>
                        </div>""",
                unsafe_allow_html=True,
            )

            st.markdown("""s parametry $c$ a $d$, přičemž $c+d=1$ a $c, d > 0$.""")
            st.markdown(
                f"""<div style="text-align: justify">
                        Po dosazení tedy máme funkci zisku v tomto tvaru
                        <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'\\pi(L, K) = P \\cdot L^c \\cdot K^d - w \\cdot L - r \\cdot K'}" style="{latex_style}" /> .
                        </div>
                        V bočním panelu si nastavte prodejní cenu, ceny výrobních faktorů a parametry
                        <img src="{latex_img}{'c'}" style="{latex_style}" /> a <img src="{latex_img}{'d'}" style="{latex_style}" />. Následně
                        hledáme optimální množství jednotek práce a optimální množství jednotek kapitálu.
                        Určíme parciální derivace funkce zisku a položíme je rovny <img src="{latex_img}{'0'}" style="{latex_style}" />
                        <div style="padding: 15px; padding-left: 20px;">
                            <img src="{latex_img}{'\\frac{\\partial \\pi(L, K)}{\\partial L} = c \\cdot P \\cdot \\left( \\frac{K}{L} \\right)^d - w = 0'}" style="{latex_style}" />
                        <br>
                        <br>
                            <img src="{latex_img}{'\\frac{\\partial \\pi(L, K)}{\\partial K} = d \\cdot P \\cdot \\left( \\frac{L}{K} \\right)^c - r = 0'}" style="{latex_style}" /> ,
                        </div>
                        potom vyjádříme <img src="{latex_img}{'P'}" style="{latex_style}" />
                        <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'P = \\frac{w}{c} \\cdot \\left( \\frac{L}{K} \\right)^d = \\frac{r}{d} \\cdot \\left( \\frac{K}{L} \\right)^c'}" style="{latex_style}" /> ,
                        </div>
                        vyjádříme <img src="{latex_img}{'K'}" style="{latex_style}" />
                        <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'K = \\frac{L \\cdot d \\cdot w}{c \\cdot r}'}" style="{latex_style}" /> ,
                        </div>
                        dosadíme do produkční funkce a vyjádříme <img src="{latex_img}{'L'}" style="{latex_style}" />
                        <div style="padding: 15px; padding-left: 20px;">
                            <img src="{latex_img}{'Q(L, K) = L^c \\cdot \\left( \\frac{L \\cdot d \\cdot w}{c \\cdot r} \\right)^d'}" style="{latex_style}" />
                        <br>
                        <br>
                            <img src="{latex_img}{'L = \\left( \\frac{c \\cdot r}{d \\cdot w} \\right)^d'}" style="{latex_style}" /> ,
                        </div>
                        dopočítáme <img src="{latex_img}{'K'}" style="{latex_style}" />
                        <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'K = \\left( \\frac{d \\cdot w}{c \\cdot r} \\right)^c'}" style="{latex_style}" /> ,
                        </div>
                        dosadíme optimální výrobní faktory do funkce zisku a vypočítáme zisk firmy
                        <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'\\pi(L, K) = P \\cdot \\left( \\frac{c \\cdot r}{d \\cdot w} \\right)^{d \\cdot c} \\cdot \\left( \\frac{d \\cdot w}{c \\cdot r} \\right)^{c \\cdot d} - w \\cdot \\left( \\frac{c \\cdot r}{d \\cdot w} \\right)^d - r \\cdot \\left( \\frac{d \\cdot w}{c \\cdot r} \\right)^c ='}{zisk}" style="{latex_style}" />
                        </div>
                        </div>""",
                unsafe_allow_html=True,
            )
