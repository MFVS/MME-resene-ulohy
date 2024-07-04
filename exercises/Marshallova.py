from exercise import Exercise
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from .styling import latex_style, latex_img, box_style


class Marshalls_Exercise(Exercise):
    def chapter_identifier(self):
        return "1.1"

    def __str__(self) -> str:
        return "Marshallova úloha"

    def render_body(self):
        st.markdown(
            f"""
            <div style="text-align: justify">
            Základním problémem, který budeme v rámci teorie spotřebitele řešit, je Marshallova
            úloha. Při této úloze uvažujeme spotřebitele, který má určité (konstantní a exogenně
            dané) množství peněžních prostředků a ty chce utratit za zboží a služby.
            <br>
            <br>
            Pro zjednodušení budeme pracovat s předpokladem, že spotřebitel se rozhoduje mezi
            dvěma druhy zboží neboli statků – statkem <img src="{latex_img}{'X'}" style="{latex_style}" />
            a statkem <img src="{latex_img}{'Y'}" style="{latex_style}" />.
            <br>
            <br>
            </div>
            """,
            unsafe_allow_html=True,
        )

        marshall_definice = f"""
        <div style="{box_style}">
            <b>Definice Marshallovy úlohy</b>: Marshallovou úlohou myslíme maximalizaci spotřebitelova užitku při konstantním
            a pevně daném důchodu (jehož výši označujeme jako
            <img src="{latex_img}{'I'}" style="{latex_style}" />), tj.
                <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'\\max_{X, Y} U(X, Y)'}" style="{latex_style}" />
                </div>
            za podmínky
                <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'P_X\\cdot X + P_Y\\cdot Y = I'}" style="{latex_style}" />,
                </div>
            kde <img src="{latex_img}{'X'}" style="{latex_style}" /> a <img src="{latex_img}{'Y'}" style="{latex_style}" />
            jsou množství poptávaných statků, <img src="{latex_img}{'P_X'}" style="{latex_style}" /> a <img src="{latex_img}{'P_Y'}" style="{latex_style}" />
            jsou jejich ceny, <img src="{latex_img}{'U'}" style="{latex_style}" /> je spotřebitelova užitková funkce a
            <img src="{latex_img}{'I'}" style="{latex_style}" /> je spotřebitelův důchod.
        </div>
        """

        st.markdown(marshall_definice, unsafe_allow_html=True)

        st.html("<br>")

        marshall_poptavka = f"""<div style="{box_style}">
                            <b>Definice Marshallovy poptávky</b>: Marshallova poptávka spotřebitele po
                            statku <img src="{latex_img}{'X'}" style="{latex_style}" /> je množství peněžních prostředků
                            spotřebitele a cen <img src="{latex_img}{'P_X'}" style="{latex_style}" /> a
                            <img src="{latex_img}{'P_Y'}" style="{latex_style}" /> a udává množství
                            statku <img src="{latex_img}{'X'}" style="{latex_style}" />, které spotřebitel poptává,
                            jestliže minimalizuje své peněžní výdaje.
                            </div>"""

        st.markdown(marshall_poptavka, unsafe_allow_html=True)

        st.markdown("---")

        st.markdown(
            f"""<div style="text-align: justify">
                    Nyní budeme optimalizovat užitek spotřebitele s konkrétní užitkovou funkcí. V bočním panelu si nastavte
                    ceny poptávaných statků, důchod spotřebitele a jeho preference (parametry užitkové funkce). Budeme zjišťovat, jaká
                    množství statků <img src="{latex_img}{'X'}" style="{latex_style}" /> a <img src="{latex_img}{'Y'}" style="{latex_style}" />
                    by měl spotřebitel zvolit, aby maximalizoval svůj užitek.
                    <br>
                    <br>
                    </div>""",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""<div style="text-align: justify">
                    Budeme uvažovat Cobb-Douglasovu užitkovou funkci ve tvaru
                    <div style="padding: 10px; padding-left: 20px;">
                    <img src="{latex_img}{'U(X, Y) = X^c \\cdot Y^d'}" style="{latex_style}" />
                    </div>
                    </div>""",
            unsafe_allow_html=True,
        )

        st.markdown(
            "s parametry $c$ a $d$, přičemž $c+d=1$ a zároveň $c, d > 0$. Zadejte tyto parametry pro užitkovou funkci daného spotřebitele."
        )

        st.markdown("---")

        # Boční panel pro zadání parametrů
        P_x = st.sidebar.slider(
            "Cena statku $P_X$", min_value=1.0, max_value=10.0, value=5.0, step=0.1
        )

        P_y = st.sidebar.slider(
            "Cena statku $P_Y$", min_value=1.0, max_value=10.0, value=5.0, step=0.1
        )

        capital_i = st.sidebar.slider(
            "Důchod spotřebitele $I$", min_value=100, max_value=1000, value=500, step=1
        )

        c = st.sidebar.slider(
            "Parametry $c$ a $d$", min_value=0.01, max_value=0.99, value=0.5, step=0.01
        )
        d = round(1 - c, 2)

        # Shrnutí zadaných parametrů
        parameters = f"""<div style="{box_style}">
                        <img src="{latex_img}{'P_X='}{P_x}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'P_Y='}{P_y}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'I='}{capital_i}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'c='}{c}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'d='}{d}" style="{latex_style}" />
                    </div>"""
        st.sidebar.markdown(parameters, unsafe_allow_html=True)

        # Graf užitkové funkce
        st.markdown(
            f"""<div style="text-align: justify">
                    Graf užitkové funkce s indiferenční křivkou <img src="{latex_img}{'U'}" style="{latex_style}" />, jež označuje optimum
                    spotřebitele vypočítané na základě zadaných parametrů:
                    <br>
                    <br>
                    </div>""",
            unsafe_allow_html=True,
        )

        # Rozsah grafu
        scope = int(round(capital_i / min(P_x, P_y), 0))
        x = np.linspace(0, scope * 1.5, scope * 5)
        y = np.linspace(0, scope * 1.5, scope * 5)

        # Vytvoříme graf
        fig, ax = plt.subplots()

        # Funkce Marshallovy poptávky
        ax.plot(x, (capital_i - P_x * x) / P_y, color="#6473AC")

        # Cobb-Douglasova užitková funkce
        X, Y = np.meshgrid(x, y)
        U = X**c * Y**d

        # Optimum spotřebitele
        X_optimal = (c * capital_i) / P_x
        Y_optimal = (d * capital_i) / P_y
        U_optimal = X_optimal**c * Y_optimal**d

        # Indiferenční křivka
        ax.contour(X, Y, U, levels=[U_optimal], colors="white", linestyles="dashed")
        ax.contour(
            X,
            Y,
            U,
            levels=[U_optimal + x * (scope / 6) for x in range(-8, 9) if x != 0],
            colors="#4D4D4D",
            linestyles="dashed",
            alpha=0.75,
        )

        # Vyznačení optima
        if c == 0:
            text_fix_x = 0
            text_fix_y = 0.1 * Y_optimal
        elif d == 0:
            text_fix_x = 0.05 * X_optimal
            text_fix_y = 0
        else:
            text_fix_x = 0
            text_fix_y = 0
        ax.scatter(X_optimal, Y_optimal, color="red")
        ax.text(
            X_optimal + 0.1 * Y_optimal + text_fix_x,
            Y_optimal + 0.1 * X_optimal + text_fix_y,
            f"({X_optimal:.2f}, {Y_optimal:.2f})",
            color="white",
            fontsize=10,
        )

        # Prvky grafu
        font_properties = {
            "fontsize": 12,
            "fontweight": "bold",
            "fontfamily": "sans-serif",
        }

        ax.set_xlabel("X", fontdict=font_properties)
        ax.set_ylabel("Y", fontdict=font_properties, rotation=0)
        plt.gca().xaxis.set_label_coords(1, -0.075)
        plt.gca().yaxis.set_label_coords(-0.05, 1.02)
        ax.grid(True)
        ax.set_xlim(0, scope * 1.5)
        ax.set_ylim(0, scope * 1.5)

        handles = [
            plt.Line2D(
                [], [], color="#6473AC", label="$P_X \\cdot X + P_Y \\cdot Y = I$"
            ),
            plt.Line2D(
                [],
                [],
                linestyle="dashed",
                color="white",
                label="$U(X, Y) = X^c \\cdot Y^d$",
            ),
            plt.scatter(
                [],
                [],
                color="red",
                label=f"Optimum spotřebitele\nmax $U(X, Y)$ = {round(U_optimal, 2)}",
            ),
        ]
        ax.legend(handles=handles, loc="upper right", fontsize=9, facecolor="#0E1117")

        st.pyplot(fig)

        st.markdown("---")

        st.markdown(
            f"""
            <div style="text-align: justify">
                V následujících krocích si ukážeme, jak jsme se k tomuto výsledku dostali.
                <br>
                <br>
                <ol>
                <li>Nejprve sestavíme Langrangeovu funkci, jež má tvar
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{'\\mathcal{L} = U(X, Y) + \\lambda(P_X \\cdot X + P_Y \\cdot Y - I)'}" style="{latex_style}" /> ,
                </div>
                přičemž <img src="{latex_img}{'\\lambda'}" style="{latex_style}" /> je Lagrangeův multiplikátor.
                </li>
                <br>
                <li>Uvažujeme Cobb-Douglasovu užitkovou funkci, kterou můžeme zapsat tímto způsobem
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{'U(X, Y) = X^c \\cdot Y^d'}" style="{latex_style}" />
                </div>
                a dále ji zlogaritmovat, což úlohu zjednoduší:
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{'\\ln U(X, Y) = c \\cdot \\ln X + d \\cdot \\ln Y'}" style="{latex_style}" />.
                </div>
                </li>
                <br>
                <li>Lagrangeovu funkci pro tuto úlohu tedy můžeme zapsat jako
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{'\\mathcal{L} = c \\cdot \\ln X + d \\cdot \\ln Y + \\lambda(P_X \\cdot X + P_Y \\cdot Y - I)'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Určíme si parciální derivace této funkce a položíme je rovny nule
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'\\frac{\\partial \\mathcal{L} (X, Y, \\lambda)}{\\partial X} = \\frac{c}{X} + \\lambda \\cdot P_X = 0'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'\\frac{\\partial \\mathcal{L} (X, Y, \\lambda)}{\\partial Y} = \\frac{d}{Y} + \\lambda \\cdot P_Y = 0'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'\\frac{\\partial \\mathcal{L} (X, Y, \\lambda)}{\\partial \\lambda} = P_X \\cdot X + P_Y \\cdot Y - I = 0'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Vyjádříme Lagrangeův multiplikátor
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                <img src="{latex_img}{'\\lambda = -\\frac{d}{P_Y \\cdot Y} = -\\frac{c}{P_X \\cdot X}'}" style="{latex_style}" />
                </div>
                a z této rovnosti vyjádříme
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                <img src="{latex_img}{'Y = \\frac{d \\cdot P_X \\cdot X}{c \\cdot P_Y}'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Dosadíme do rozpočtové rovnice
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                <img src="{latex_img}{'P_X \\cdot X + P_Y \\cdot \\frac{d \\cdot P_X \\cdot X}{c \\cdot P_Y} = I'}" style="{latex_style}" />
                </div>
                a vyjádříme
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'X = \\frac{c \\cdot I}{P_X \\cdot (c + d)} = \\frac{c \\cdot I}{P_X}'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'Y = \\frac{I - c \\cdot I}{P_Y} = \\frac{d \\cdot I}{P_Y}'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Nyní pouze dosadíme zadané hodnoty, vypočítáme optimální množství <img src="{latex_img}{'X'}" style="{latex_style}" /> a 
                optimální množství <img src="{latex_img}{'Y'}" style="{latex_style}" /> (optimum spotřebitele) a nakonec i maximalizovaný
                užitek pomocí užitkové funkce.
                </li>
                </ol>
                </div>
            """,
            unsafe_allow_html=True,
        )
