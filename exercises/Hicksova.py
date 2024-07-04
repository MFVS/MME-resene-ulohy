import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from exercise import Exercise
from .styling import box_style, latex_img, latex_style


class Hicksova_Uloha(Exercise):
    def chapter_identifier(self):
        return "1.2"

    def __str__(self) -> str:
        return "Hicksova úloha"

    def render_body(self):
        st.markdown(
            """
            <div style="text-align: justify">
            Alternativou k Marshallově úloze je Hicksova úloha. Přesněji řečeno, Hicksova úloha
            je duální úlohou k Marshallově úloze. Zatímco v případě Marshallovy úlohy jsme maximalizovali
            užitek spotřebitele při daném fixním příjmu, u Hicksovy úlohy minimalizujeme výdaje
            spotřebitele na dosažení určité požadované (a fixní) hodnoty užitku.
            <br>
            <br>
            </div>
            """,
            unsafe_allow_html=True,
        )

        hicks_definice = f"""
        <div style="{box_style}">
            <b>Definice Hicksovy úlohy</b>: Hicksovou úlohou myslíme minimalizaci výdajů na nákup zboží při
            dané požadované úrovni užitku, tj.
                <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'\\min_{X, Y}   P_X \\cdot X + P_Y \\cdot Y'}" style="{latex_style}" />
                </div>
            za podmínky
                <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'U(X, Y) = C'}" style="{latex_style}" />,
                </div>
            kde <img src="{latex_img}{'X'}" style="{latex_style}" /> a <img src="{latex_img}{'Y'}" style="{latex_style}" />
            jsou množství poptávaných statků, <img src="{latex_img}{'P_X'}" style="{latex_style}" /> a <img src="{latex_img}{'P_Y'}" style="{latex_style}" />
            jsou jejich ceny, <img src="{latex_img}{'U'}" style="{latex_style}" /> je spotřebitelova užitková funkce a
            <img src="{latex_img}{'C'}" style="{latex_style}" /> je spotřebitelův užitek.
        </div>
        """

        st.markdown(hicks_definice, unsafe_allow_html=True)

        st.html("<br>")

        hicks_poptavka = f"""<div style="{box_style}">
                            <b>Definice Hicksovy poptávky</b>: Hicksova poptávka spotřebitele po
                            statku <img src="{latex_img}{'X'}" style="{latex_style}" /> je funkcí požadované
                            úrovně užitku spotřebitele a cen <img src="{latex_img}{'P_X'}" style="{latex_style}" /> a
                            <img src="{latex_img}{'P_Y'}" style="{latex_style}" /> a udává množství
                            statku <img src="{latex_img}{'X'}" style="{latex_style}" />, které spotřebitel poptává,
                            jestliže minimalizuje své peněžní výdaje.
                            </div>"""

        st.markdown(hicks_poptavka, unsafe_allow_html=True)

        st.markdown("---")

        st.markdown(
            f"""<div style="text-align: justify">
                    Nyní budeme minimalizovat výdaje spotřebitele s konkrétní užitkovou funkcí. V bočním panelu si nastavte
                    ceny poptávaných statků, požadovaný užitek spotřebitele a jeho preference (parametry užitkové funkce). Budeme zjišťovat, jaká
                    množství statků <img src="{latex_img}{'X'}" style="{latex_style}" /> a <img src="{latex_img}{'Y'}" style="{latex_style}" />
                    by měl spotřebitel zvolit, aby minimalizoval své výdaje při zachování požadovaného užitku.
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

        C = st.sidebar.slider(
            "Užitek spotřebitele $C$",
            min_value=1.0,
            max_value=10.0,
            value=5.0,
            step=0.1,
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
                        <img src="{latex_img}{'C='}{C}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'c='}{c}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'d='}{d}" style="{latex_style}" />
                    </div>"""
        st.sidebar.markdown(parameters, unsafe_allow_html=True)

        # Graf užitkové funkce
        st.markdown(
            f"""<div style="text-align: justify">
                    Graf Hicksovy poptávkové funkce s indiferenční křivkou <img src="{latex_img}{'U'}" style="{latex_style}" />, jež označuje
                    zadaný užitek, jehož se snažíme dosáhnout s minimálními výdaji:
                    <br>
                    <br>
                    </div>""",
            unsafe_allow_html=True,
        )

        # Rozsah grafu
        scope = int(round((22 / (P_x * P_y)) * C * np.mean([P_x, P_y]), 0))
        x = np.linspace(0, scope, scope * 20)
        y = np.linspace(0, scope, scope * 20)

        # Vytvoříme graf
        fig, ax = plt.subplots()

        # Cobb-Douglasova užitková funkce
        X, Y = np.meshgrid(x, y)
        U = X**c * Y**d

        # Indiferenční křivka
        ax.contour(X, Y, U, levels=[C], colors="white", linestyles="dashed")
        ax.contour(
            X,
            Y,
            U,
            levels=[C + x * (scope / 9) for x in range(-8, 9) if x != 0],
            colors="#4D4D4D",
            linestyles="dashed",
            alpha=0.75,
        )

        # Optimum spotřebitele
        X_optimal = C * ((c * P_y) / (d * P_x)) ** d
        Y_optimal = C * ((d * P_x) / (c * P_y)) ** c

        # Funkce Hicksovy poptávky
        slope = -P_x / P_y

        def line_equation(x):
            return slope * (x - X_optimal) + Y_optimal

        ax.plot(x, line_equation(x), color="#EE7708")

        # Vyznačení optima
        capital_i = P_x * X_optimal + P_y * Y_optimal
        ax.scatter(X_optimal, Y_optimal, color="red")
        ax.text(
            X_optimal + 0.1 * Y_optimal,
            Y_optimal + 0.1 * X_optimal,
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
        ax.set_xlim(0, scope)
        ax.set_ylim(0, scope)

        handles = [
            plt.Line2D(
                [],
                [],
                color="#EE7708",
                label="$P_X \\cdot X + P_Y \\cdot Y = I$",
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
                label=f"Minimální výdaje\n{'min $P_X \\cdot X + P_Y \\cdot Y$'} = {round(capital_i, 2)}",
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
                <img src="{latex_img}{'\\mathcal{L} = P_X \\cdot X + P_Y \\cdot Y + \\lambda(U(X, Y) - C)'}" style="{latex_style}" /> ,
                </div>
                přičemž <img src="{latex_img}{'\\lambda'}" style="{latex_style}" /> je Lagrangeův multiplikátor.
                </li>
                <br>
                <li>Uvažujeme Cobb-Douglasovu užitkovou funkci, kterou můžeme zapsat tímto způsobem
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{'U(X, Y) = X^c \\cdot Y^d'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Lagrangeovu funkci pro tuto úlohu tedy můžeme zapsat jako
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{'\\mathcal{L} = P_X \\cdot X + P_Y \\cdot Y + \\lambda(X^c \\cdot Y^d - C)'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Určíme si parciální derivace této funkce a položíme je rovny nule
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'\\frac{\\partial \\mathcal{L} (X, Y, \\lambda)}{\\partial X} = P_X + \\frac{\\lambda \\cdot c \\cdot Y^d}{X^d} = 0'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'\\frac{\\partial \\mathcal{L} (X, Y, \\lambda)}{\\partial Y} = P_Y + \\frac{\\lambda \\cdot d \\cdot X^c}{Y^c} = 0'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'\\frac{\\partial \\mathcal{L} (X, Y, \\lambda)}{\\partial \\lambda} = X^c \\cdot Y^d - C = 0'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Vyjádříme Lagrangeův multiplikátor
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                <img src="{latex_img}{'\\lambda = -\\frac{P_X \\cdot X^d}{c \\cdot Y^d} = -\\frac{P_Y \\cdot Y^c}{d \\cdot X^c}'}" style="{latex_style}" />
                </div>
                a z této rovnosti vyjádříme
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                <img src="{latex_img}{'Y = \\frac{d \\cdot P_X \\cdot X}{c \\cdot P_Y}'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Dosadíme do užitkové funkce
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                <img src="{latex_img}{'X^c \\cdot \\left( \\frac{d \\cdot P_X \\cdot X}{c \\cdot P_Y} \\right)^d = C'}" style="{latex_style}" />
                </div>
                a vyjádříme
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'X = C \\cdot \\left( \\frac{c \\cdot P_Y}{d \\cdot P_X} \\right)^d'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'Y = C \\cdot \\left( \\frac{d \\cdot P_X}{c \\cdot P_Y} \\right)^c'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Nyní pouze dosadíme zadané hodnoty, vypočítáme optimální množství <img src="{latex_img}{'X'}" style="{latex_style}" /> a 
                optimální množství <img src="{latex_img}{'Y'}" style="{latex_style}" /> a nakonec i minimální výdaje spotřebitele
                potřebné pro dosažení požadovaného užitku.
                </li>
                </ol>
                </div>
            """,
            unsafe_allow_html=True,
        )
