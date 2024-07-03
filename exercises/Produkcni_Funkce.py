from .exercise import Exercise
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from .styling import latex_style, latex_img, box_style


class Produkcni_Funkce(Exercise):
    def chapter_identifier(self):
        return "2.1"
    def __str__(self) -> str:
        return "Produkční funkce"
    def render_body(self):
        st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)

        left_button, right_button = st.columns([2.098, 1])

        with left_button:
            if st.button("← Domů", key="1"):
                st.session_state.page = "uvod"
                st.rerun()

        with right_button:
            if st.button("2.2 Minimalizace nákladů →", key="2"):
                st.session_state.page = "min_naklady"
                st.rerun()

        st.markdown("---")

        st.subheader("2.1 Produkční funkce firmy")
        st.markdown(
            f"""
            <div style="text-align: justify">
            Produkční funkce firmy udává maximální možný objem výroby při daném množství výrobních faktorů.
            V této kapitole budeme uvažovat dva výrobní faktory: práci <img src="{latex_img}{'L'}" style="{latex_style}" />
            a kapitál <img src="{latex_img}{'K'}" style="{latex_style}" /> (kapitálový statek).
            <br>
            <br>
            Může existovat tzv. neefektivní firma, která se stejným objemem výrobních faktorů vyrobí menší množství zboží než efektivní firma.
            V následujících úlohách budeme ale předpokládat efektivní firmu, pro kterou platí, že hodnota produkční funkce je rovná
            skutečně vyrobenému množství zboží.
            <br>
            <br>
            Dále budeme předpokládat, že firma vyrábí jeden druh finálního produktu a všechny vyrobené kusy jsou homogenní.
            Uvažujeme, že i nakupované výrobní faktory se mezi sebou kvalitativně neliší.
            <br>
            <br>
            </div>
            """,
            unsafe_allow_html=True,
        )

        mrts_definice = f"""
        <div style="{box_style}">
            <b>Definice mezní míry technické substituce</b>: 
            Mezní míra technické substituce (MRTS) udává, o kolik jednotek musí firma zvýšit použití jednoho výrobního faktoru,
            aby zachovala objem výstupu, pokud sníží použití druhého výrobního faktoru. Tato míra je definována vztahem
                <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'MR\\hspace{2pt}TS = -\\frac{MP_L}{MP_K} = -\\frac{\\frac{\\partial Q(L, K)}{\\partial L}}{\\frac{\\partial Q(L, K)}{\\partial K}}'}" style="{latex_style}" /> ,
                </div>
            kde <img src="{latex_img}{'MP_L'}" style="{latex_style}" /> je mezní produktivita práce (tj. o kolik se zvýší zisk, když firma
            zaměstná o jednotku práce více), <img src="{latex_img}{'MP_K'}" style="{latex_style}" /> je mezní produktivita kapitálu
            (tj. o kolik se zvýší zisk, když firma navýší náklady o jednotku kapitálu) a <img src="{latex_img}{'Q(L, K)'}" style="{latex_style}" />
            je produkční funkce firmy.
        </div>
        """

        st.markdown(mrts_definice, unsafe_allow_html=True)

        st.markdown("---")

        st.markdown(
            """<div style="text-align: justify">
                Nyní budeme počítat mezní míru technické substituce s konkrétní produkční funkcí. V bočním panelu si nastavte hodnoty
                vstupních výrobních atributů, tedy práce a kapitálu, a parametry produkční funkce.
                <br>
                <br>
                </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""<div style="text-align: justify">
                    Budeme uvažovat Cobb-Douglasovu produkční funkci ve tvaru
                    <div style="padding: 10px; padding-left: 20px;">
                    <img src="{latex_img}{'Q(L, K) = L^c \\cdot K^d'}" style="{latex_style}" />
                    </div>
                    </div>""",
            unsafe_allow_html=True,
        )

        st.markdown(
            "s parametry $c$ a $d$, přičemž $c+d=1$ a zároveň $c, d > 0$. Zadejte tyto parametry pro produkční funkci dané firmy."
        )

        st.markdown("---")

        # Boční panel pro zadání parametrů
        L = st.sidebar.slider(
            "Množství jednotek práce $L$",
            min_value=1.0,
            max_value=10.0,
            value=5.0,
            step=0.1,
        )

        Q = st.sidebar.slider(
            "Výstup firmy $Q$", min_value=1.0, max_value=10.0, value=5.0, step=0.1
        )

        c = st.sidebar.slider(
            "Parametry $c$ a $d$", min_value=0.01, max_value=0.99, value=0.5, step=0.01
        )
        d = round(1 - c, 2)

        # Dopočítáme množství jednotek kapitálu na základě L a Q
        K = round((Q / L**c) ** (1 / d), 1)

        # Shrnutí zadaných parametrů
        parameters = f"""<div style="{box_style}">
                        <img src="{latex_img}{'L='}{L}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'K='}{K}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'Q='}{Q}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'c='}{c}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'d='}{d}" style="{latex_style}" />
                    </div>"""
        st.sidebar.markdown(parameters, unsafe_allow_html=True)

        # Graf funkcí mezních výrobních faktorů
        st.markdown(
            f"""<div style="text-align: justify">
                    Graf izokvanty pro výstup (produkci) <img src="{latex_img}{'Q'}" style="{latex_style}" /> dané firmy,
                    jež vyznačuje potřebnou kombinaci výrobních faktorů <img src="{latex_img}{'L'}" style="{latex_style}" />
                    a <img src="{latex_img}{'K'}" style="{latex_style}" /> pro dosažení výstupu
                    <img src="{latex_img}{'Q'}" style="{latex_style}" />. Dále je zobrazena tečna pro daný bod
                    <img src="{latex_img}{'(L, K)'}" style="{latex_style}" />, jejíž směrnice je právě
                    <img src="{latex_img}{'MR\\hspace{2pt}TS'}" style="{latex_style}" />, tedy mezní míra technické substituce.
                    <br>
                    <br>
                    </div>""",
            unsafe_allow_html=True,
        )

        # Rozsah grafu
        scope = 30
        x = np.linspace(0.001, scope, 200)

        # Vytvoříme graf
        fig, ax = plt.subplots()

        # Izokvanta pro zadaný výstup firmy
        ax.plot(x, (Q / x**c) ** (1 / d), color="#EE7708")

        # Sklon tečny - MRTS
        m = -(c * K) / (d * L)
        ax.plot(x, m * (x - L) + K, color="#6473AC")

        # Vyznačení daného bodu
        if K < scope / 1.5:
            ax.scatter(L, K, color="red")
            ax.text(L + 0.1 * K, K + 0.1 * L, f"({L:.2f}, {K:.2f})")
        elif scope / 1.5 <= K <= scope:
            ax.scatter(L, K, color="red")
            ax.text(L + 0.08 * K, K - 0.3 * L, f"({L:.2f}, {K:.2f})")

        # Prvky grafu
        font_properties = {
            "fontsize": 12,
            "fontweight": "bold",
            "fontfamily": "sans-serif",
        }

        ax.set_xlabel("L", fontdict=font_properties)
        ax.set_ylabel("K", fontdict=font_properties, rotation=0)
        plt.gca().xaxis.set_label_coords(1, -0.075)
        plt.gca().yaxis.set_label_coords(-0.04, 1.03)
        ax.grid(True)
        ax.set_xlim(0, scope)
        ax.set_ylim(0, scope)

        # Legenda
        handles = [
            plt.Line2D([], [], color="#EE7708", label=f"Izokvanta $Q=${Q}"),
            plt.Line2D([], [], color="#6473AC", label=f"Tečna izokvanty"),
            plt.scatter([], [], color="red", label=f"$MRTS=${round(m, 3)}"),
        ]
        ax.legend(handles=handles, loc="upper right", fontsize=9, facecolor="#0E1117")

        st.pyplot(fig)

        st.markdown("---")

        st.markdown(
            f"""<div style="text-align: justify">
                    V následujících krocích si ukážeme, jak jsme se k tomuto výsledku dostali.
                    <br>
                    <br>
                    <ol>
                    <li>Nejprve pomocí zadaného množství výrobního faktoru <img src="{latex_img}{'L'}" style="{latex_style}" /> (práce)
                    a požadovaného výstupu firmy <img src="{latex_img}{'Q'}" style="{latex_style}" /> dopočítáme množství výrobního
                    faktoru <img src="{latex_img}{'K'}" style="{latex_style}" /> (kapitál):
                    <div style="padding: 10px; padding-left: 20px;">
                    <img src="{latex_img}{'K = \\left( \\frac{Q}{L^c} \\right)^{\\hspace{-1.5pt}\\frac{1}{d}} ='}{K}" style="{latex_style}" />
                    </div>
                    </li>
                    <br>
                    <li>Vypočítáme mezní produktivitu práce <img src="{latex_img}{'MP_L'}" style="{latex_style}" />
                    a mezní produktivitu kapitálu <img src="{latex_img}{'MP_K'}" style="{latex_style}" /> :
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                        <img src="{latex_img}{'MP_L = \\frac{\\partial Q(L, K)}{\\partial L} = c \\cdot \\left( \\frac{K}{L} \\right)^{\\hspace{-1pt}d} ='}{round(c*(K/max(L, 10**-10))**d, 3)}" style="{latex_style}" />
                    <br>
                    <br>
                        <img src="{latex_img}{'MP_K = \\frac{\\partial Q(L, K)}{\\partial K} = d \\cdot \\left( \\frac{L}{K} \\right)^{\\hspace{-1pt}c} ='}{round(d*(L/max(K, 10**-10))**c, 3)}" style="{latex_style}" />
                    </div>
                    </li>
                    <br>
                    <li>Nakonec tyto mezní veličiny vydělíme a získáme mezní míru technické substituce
                    <img src="{latex_img}{'MR\\hspace{2pt}TS'}" style="{latex_style}" /> :
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'MR\\hspace{2pt}TS = -\\frac{MP_L}{MP_K} ='}{round(m, 3)}" style="{latex_style}" />
                    </div>
                    </li>
                    </ol>
                    </div>""",
            unsafe_allow_html=True,
        )

        st.markdown("---")

        st.markdown(
            f"""
            <div style="text-align: justify"> 
            Dalším pojmem souvisejícím s produkční funkcí firmy jsou výnosy z rozsahu. Hodnota výnosů z rozsahu nám může ukázat, do jaké míry
            se firmě vyplatí zvyšovat vstupy (náklady) za účelem zvýšení výstupů (produkce). Podmínkou pro určení výnosů z rozsahu je homogenita
            produkční funkce ve všech proměnných. Pokud máme homogenní funkci <img src="{latex_img}{'n'}" style="{latex_style}" />-tého stupně,
            znamená to, že když argument funkce vynásobíme libovolným kladným koeficientem, pak funkční hodnota se vynásobí
            <img src="{latex_img}{'n'}" style="{latex_style}" />-tou mocninou tohoto koeficientu.
            <br>
            <br>
            </div>
            """,
            unsafe_allow_html=True,
        )

        vynosy_rozsah_definice = f"""
        <div style="{box_style}">
            <b>Určení výnosů z rozsahu</b>:
            Uvažujme produkční funkci homogenní stupně <img src="{latex_img}{'a'}" style="{latex_style}" /> ve všech proměnných.
            Potom výnosy z rozsahu jsou
            <ul style="margin: 0; padding: 0;">
            <li> rostoucí, pokud <img src="{latex_img}{'a > 1'}" style="{latex_style}" /> ,</li>
            <li> klesající, pokud <img src="{latex_img}{'a < 1'}" style="{latex_style}" /> ,</li>
            <li> konstantní, pokud <img src="{latex_img}{'a = 1.'}" style="{latex_style}" /></li>
            </ul>
        </div>
        """

        st.markdown(vynosy_rozsah_definice, unsafe_allow_html=True)

        st.markdown("---")

        st.markdown(
            f"""<div style="text-align: justify">
                    Porovnáme výnosy z rozsahu u tří různých produkčních funkcí (pokud je lze určit):
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                        <img src="{latex_img}{'Q_1(L, K) = L \\cdot K'}" style="{latex_style}" />
                    <br>
                    <br>
                        <img src="{latex_img}{'Q_2(L, K) = L^{\\frac{1}{2}} \\cdot K^{\\frac{1}{2}}'}" style="{latex_style}" />
                    <br>
                    <br>
                        <img src="{latex_img}{'Q_3(L, K) = L^{\\frac{1}{2}} + K^{\\frac{1}{2}}'}" style="{latex_style}" />
                    </div>
                    <br>
                    Násobíme argumenty funkcí konstantou <img src="{latex_img}{'c'}" style="{latex_style}" /> :
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                        <img src="{latex_img}{'Q_1(c \\cdot L, c \\cdot K) = (c \\cdot L) \\cdot (c \\cdot K) = c^2 \\cdot L \\cdot K = c^2 \\cdot Q_1(L, K)'}" style="{latex_style}" />
                    <br>
                    <br>
                        <img src="{latex_img}{'Q_2(c \\cdot L, c \\cdot K) = (c \\cdot L)^{\\frac{1}{2}} \\cdot (c \\cdot K)^{\\frac{1}{2}} = c \\cdot L^{\\frac{1}{2}} \\cdot K^{\\frac{1}{2}} = c \\cdot Q_2(L, K)'}" style="{latex_style}" />
                    <br>
                    <br>
                        <img src="{latex_img}{'Q_3(c \\cdot L, c \\cdot K) = (c \\cdot L)^{\\frac{1}{2}} + (c \\cdot K)^{\\frac{1}{2}} = c^{\\frac{1}{2}} \\cdot \\left( L^{\\frac{1}{2}} + K^{\\frac{1}{2}} \\right) = c^{\\frac{1}{2}} \\cdot Q_3(L, K)'}" style="{latex_style}" />
                    </div>
                    <br>
                    Vidíme, že všechny tři produkční funkce jsou homogenní ve všech proměnných. Funkce
                    <img src="{latex_img}{'Q_1'}" style="{latex_style}" /> je homogenní stupně <img src="{latex_img}{'2'}" style="{latex_style}" /> a
                    funkce <img src="{latex_img}{'Q_2'}" style="{latex_style}" /> je homogenní stupně <img src="{latex_img}{'1'}" style="{latex_style}" /> a
                    funkce <img src="{latex_img}{'Q_3'}" style="{latex_style}" /> je homogenní stupně <img src="{latex_img}{'\\tiny{\\frac{1}{2}}'}" style="{latex_style}" /> .
                    Podle výše uvedených pravidel můžeme tedy určit, že první produkční funkce má rostoucí výnosy z rozsahu, druhá funkce má konstantní
                    výnosy z rozsahu a třetí funkce má klesající výnosy z rozsahu.
                    </div>""",
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # Graf porovnávající produkční funkce
        st.markdown(
            f"""<div style="text-align: justify">
                    Grafické porovnání výnosů z rozsahu u produkčních funkcí <img src="{latex_img}{'Q_1'}" style="{latex_style}" /> ,
                    <img src="{latex_img}{'Q_2'}" style="{latex_style}" /> a <img src="{latex_img}{'Q_3'}" style="{latex_style}" /> :
                    <br>
                    <br>
                    </div>""",
            unsafe_allow_html=True,
        )

        # Rozsah grafu
        x2 = np.linspace(0.001, 8, 200)

        # Vytvoříme graf
        fig2, ax2 = plt.subplots()

        # Q1
        ax2.plot(x2, x2**2, color="#EE7708", label="$Q_1$")
        ax2.text(1.7, 6.7, "$a_1 = 2$", color="#EE7708")

        # Q2
        ax2.plot(x2, x2, color="#6473AC", label="$Q_2$")
        ax2.text(5.7, 6.7, "$a_2 = 1$", color="#6473AC")

        # Q3
        ax2.plot(x2, 2 * x2**0.5, color="#F287D0", label="$Q_3$")
        ax2.text(5.7, 4.3, "$a_3 = \\frac{1}{2}$", color="#F287D0")

        # Prvky grafu
        font_properties = {
            "fontsize": 12,
            "fontweight": "bold",
            "fontfamily": "sans-serif",
        }

        ax2.set_xlabel("L / K", fontdict=font_properties)
        ax2.set_ylabel("Q", fontdict=font_properties, rotation=0)
        plt.gca().xaxis.set_label_coords(0.975, -0.075)
        plt.gca().yaxis.set_label_coords(-0.04, 1.03)
        ax2.grid(True)
        ax2.set_xlim(0, 8)
        ax2.set_ylim(0, 8)

        ax2.legend(loc="lower right", fontsize=12, facecolor="#0E1117")

        st.pyplot(fig2)
