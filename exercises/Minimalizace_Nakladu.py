from exercise import Exercise
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from .styling import latex_style, latex_img, box_style


class Minimalizace_Nakladu(Exercise):
    def chapter_identifier(self):
        return "2.2"

    def __str__(self) -> str:
        return "Minimalizace Nákladů"

    def render_body(self):
        st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)

        left_button, center_button, right_button = st.columns([1.5, 0.82, 1])

        with left_button:
            if st.button("← 2.1 Produkční funkce firmy", key="1"):
                st.session_state.page = "prod_fun"
                st.rerun()

        with center_button:
            if st.button("↑ Domů", key="2"):
                st.session_state.page = "uvod"
                st.rerun()

        with right_button:
            if st.button("2.3 Maximalizace zisku →", key="3"):
                st.session_state.page = "max_zisk"
                st.rerun()

        st.markdown("---")

        st.subheader("2.2 Minimalizace nákladů")
        st.markdown(
            """
            <div style="text-align: justify"> 
            Každá efektivní firma se snaží minimalizovat své náklady. Nejprve si definujeme úlohu minimalizace nákladů a následně se podíváme
            na další pojmy související s minimalizací nákladů.
            <br>
            <br>
            </div>
            """,
            unsafe_allow_html=True,
        )

        min_naklady_definice = f"""
        <div style="{box_style}">
            <b>Definice úlohy minimalizace nákladů firmy</b>: 
            Úloha minimalizace nákladů firmy znamená nalezení
                <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'\\min_{L, K}   w \\cdot L + r \\cdot K'}" style="{latex_style}" />
                </div>
            za podmínky
                <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'Q(L, K) = Q_0'}" style="{latex_style}" /> ,
                </div>
            kde <img src="{latex_img}{'w'}" style="{latex_style}" /> je cena práce, <img src="{latex_img}{'r'}" style="{latex_style}" />
            je cena kapitálu, <img src="{latex_img}{'Q(L, K)'}" style="{latex_style}" /> je produkční funkce firmy a
            <img src="{latex_img}{'Q_0'}" style="{latex_style}" /> je dané množství zboží, které má firma vyrobit (tj. požadovaná produkce).
        </div>
        """

        st.markdown(min_naklady_definice, unsafe_allow_html=True)

        st.markdown(
            """
            <div style="text-align: justify">
            <br>
            Můžeme pozorovat, že z matematického hlediska se jedná o stejnou úlohu, jako je Hicksova úloha. Pouze zde figurují jiné
            proměnné, které se týkají firmy a ne spotřebitele. Firma minimalizuje své náklady a maximalizuje produkci, zatímco spotřebitel
            minimalizuje své výdaje a maximalizuje užitek. Optimální kombinaci množství výrobních faktorů lze tedy nalézt obdobně
            jako u Hicksovy úlohy pomocí metody Lagrangeových multiplikátorů. Zopakujeme stejný postup, jenom nahradíme proměnné a místo
            užitkové funkce použijeme produkční funkci.
            <br>
            <br>
            </div>
            """,
            unsafe_allow_html=True,
        )

        min_naklady_veta = f"""
        <div style="{box_style}">
            <b>Věta</b>: 
            Firma minimalizuje náklady na výrobu, jestliže se poměr cen
            výrobních faktorů rovná poměru mezních produktivit výrobních faktorů, tj. musí platit
                <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'\\frac{MP_L}{MP_K} = \\frac{w}{r}'}" style="{latex_style}" /> ,
                </div>
            přičemž do této rovnosti lze zakomponovat i mezní míru technické substituce
                <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'MR\\hspace{2pt}TS = -\\frac{MP_L}{MP_K} = -\\frac{w}{r}'}" style="{latex_style}" /> .
                </div>
        </div>
        """

        st.markdown(min_naklady_veta, unsafe_allow_html=True)

        st.markdown("---")

        # Boční panel pro zadání parametrů
        w = st.sidebar.slider(
            "Cena práce $w$", min_value=1.0, max_value=10.0, value=5.0, step=0.1
        )

        r = st.sidebar.slider(
            "Cena kapitálu $r$", min_value=1.0, max_value=10.0, value=5.0, step=0.1
        )

        Q_0 = st.sidebar.slider(
            "Výstup firmy $Q_0$", min_value=1.0, max_value=10.0, value=5.0, step=0.1
        )

        c = st.sidebar.slider(
            "Parametry $c$ a $d$", min_value=0.01, max_value=0.99, value=0.5, step=0.01
        )
        d = round(1 - c, 2)

        # Shrnutí zadaných parametrů
        parameters = f"""<div style="{box_style}">
                        <img src="{latex_img}{'w='}{w}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'r='}{r}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'Q_0='}{Q_0}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'c='}{c}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'d='}{d}" style="{latex_style}" />
                    </div>"""
        st.sidebar.markdown(parameters, unsafe_allow_html=True)

        # Graf produkční funkce
        st.markdown(
            f"""<div style="text-align: justify">
                    V bočním panelu si nastavte ceny výrobních faktorů, požadovanou produkci firmy a parametry produkční funkce.
                    Graf produkční funkce firmy, na němž je zobrazena optimální kombinace výrobních faktorů
                    <img src="{latex_img}{'L'}" style="{latex_style}" /> a <img src="{latex_img}{'K'}" style="{latex_style}" />
                    pro minimalizaci nákladů při pevně stanovených cenách práce a kapitálu –  <img src="{latex_img}{'w'}" style="{latex_style}" />,
                    <img src="{latex_img}{'r'}" style="{latex_style}" /> :
                    <br>
                    <br>
                    </div>""",
            unsafe_allow_html=True,
        )

        # Rozsah grafu
        scope = int(round((22 / (w * r)) * Q_0 * np.mean([w, r]), 0))
        x = np.linspace(0.001, scope, scope * 50)

        # Vytvoříme graf
        fig, ax = plt.subplots()

        # Cobb-Douglasova produkční funkce
        ax.plot(x, (Q_0 / x**c) ** (1 / d), color="#EE7708", label="$Q_1$")

        # Kombinace výrobních faktorů minimalizující náklady
        L_optimal = Q_0 * ((c * r) / (d * w)) ** d
        K_optimal = Q_0 * ((d * w) / (c * r)) ** c

        # Tečna produkční funkce
        slope = -w / r
        line_equation = lambda x: slope * (x - L_optimal) + K_optimal
        ax.plot(x, line_equation(x), color="#6473AC")

        # Vyznačení optima
        C_min = w * L_optimal + r * K_optimal
        ax.scatter(L_optimal, K_optimal, color="red")
        ax.text(
            L_optimal + 0.1 * K_optimal,
            K_optimal + 0.1 * L_optimal,
            f"({L_optimal:.2f}, {K_optimal:.2f})",
            color="white",
            fontsize=10,
        )

        # Prvky grafu
        font_properties = {
            "fontsize": 12,
            "fontweight": "bold",
            "fontfamily": "sans-serif",
        }

        ax.set_xlabel("L", fontdict=font_properties)
        ax.set_ylabel("K", fontdict=font_properties, rotation=0)
        plt.gca().xaxis.set_label_coords(1, -0.075)
        plt.gca().yaxis.set_label_coords(-0.05, 1.02)
        ax.grid(True)
        ax.set_xlim(0, scope)
        ax.set_ylim(0, scope)

        handles = [
            plt.Line2D([], [], color="#EE7708", label="$Q(L, K) = L^c \\cdot K^d$"),
            plt.Line2D(
                [],
                [],
                color="#6473AC",
                label="$w \\cdot L + r \\cdot K = TC$",
            ),
            plt.scatter(
                [],
                [],
                color="red",
                label=f"Minimální náklady\n{'min $TC$'} = {round(C_min, 2)}",
            ),
        ]
        ax.legend(handles=handles, loc="upper right", fontsize=9, facecolor="#0E1117")

        st.pyplot(fig)

        st.markdown("---")

        podmin_poptavka_definice = f"""
        <div style="{box_style}">
            <b>Definice podmíněné poptávky</b>:
            Podmíněná poptávka firmy po výrobním faktoru <img src="{latex_img}{'X'}" style="{latex_style}" />
            udává množství výrobního faktoru <img src="{latex_img}{'X'}" style="{latex_style}" /> nakupovaného firmou v závislosti na
            ceně všech výrobních faktorů firmy a požadovaném objemu produkce. 
        </div>
        """

        st.markdown(podmin_poptavka_definice, unsafe_allow_html=True)

        st.markdown(
            f"""
            <div style="text-align: justify">
            <br>
            Na základě této definice vidíme, že podmíněná poptávka je obdobou Hicksovy poptávky, přičemž se jedná o poptávku z pohledu firmy,
            nikoliv spotřebitele.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        st.markdown(
            f"""
            <div style="text-align: justify">
            Na základě údajů nastavených v bočním panelu si nyní spočítáme podmíněné poptávky po výrobních faktorech
            <img src="{latex_img}{'K'}" style="{latex_style}" /> a <img src="{latex_img}{'L'}" style="{latex_style}" /> .
            <br>
            <br>
            Budeme opět uvažovat Cobb-Douglasovu produkční funkci ve tvaru
            <div style="padding: 10px; padding-left: 20px;">
            <img src="{latex_img}{'Q(L, K) = L^c \\cdot K^d'}" style="{latex_style}" />
            </div>
            </div>""",
            unsafe_allow_html=True,
        )

        st.markdown("s parametry $c$ a $d$, přičemž $c+d=1$ a zároveň $c, d > 0$.")

        st.markdown("---")

        st.markdown(
            f"""<div style="text-align: justify">
                    V následujících krocích si ukážeme, jak probíhá výpočet podmíněných poptávek.
                    <br>
                    <br>
                    <ol>
                    <li>Nejprve sestavíme Langrangeovu funkci, jež má tvar
                    <div style="padding: 10px; padding-left: 20px;">
                    <img src="{latex_img}{'\\mathcal{L} = w \\cdot L + r \\cdot K + \\lambda(L^c \\cdot K^d - Q_0)'}" style="{latex_style}" /> .
                    </div>
                    </li>
                    <br>
                    <li>Určíme si parciální derivace této funkce a položíme je rovny nule
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                        <img src="{latex_img}{'\\frac{\\partial \\mathcal{L} (L, K, \\lambda)}{\\partial L} = w + \\frac{\\lambda \\cdot c \\cdot K^d}{L^d} = 0'}" style="{latex_style}" />
                    <br>
                    <br>
                        <img src="{latex_img}{'\\frac{\\partial \\mathcal{L} (L, K, \\lambda)}{\\partial K} = r + \\frac{\\lambda \\cdot d \\cdot L^c}{K^c} = 0'}" style="{latex_style}" />
                    <br>
                    <br>
                        <img src="{latex_img}{'\\frac{\\partial \\mathcal{L} (L, K, \\lambda)}{\\partial \\lambda} = L^c \\cdot K^d - Q_0 = 0'}" style="{latex_style}" /> .
                    </div>
                    </li>
                    <br>
                    <li>Vyjádříme Lagrangeův multiplikátor
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                    <img src="{latex_img}{'\\lambda = -\\frac{w \\cdot L^d}{c \\cdot K^d} = -\\frac{r \\cdot K^c}{d \\cdot L^c}'}" style="{latex_style}" />
                    </div>
                    a z této rovnosti vyjádříme
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'K = \\frac{d \\cdot w \\cdot L}{c \\cdot r}'}" style="{latex_style}" /> .
                    </div>
                    </li>
                    <br>
                    <li>Dosadíme do užitkové funkce
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                    <img src="{latex_img}{'L^c \\cdot \\left( \\frac{d \\cdot w \\cdot L}{c \\cdot r} \\right)^d = Q_0'}" style="{latex_style}" />
                    </div>
                    a vyjádříme
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                        <img src="{latex_img}{'L = Q_0 \\cdot \\left( \\frac{c \\cdot r}{d \\cdot w} \\right)^d ='}{round(L_optimal, 2)}" style="{latex_style}" />
                    <br>
                    <br>
                        <img src="{latex_img}{'K = Q_0 \\cdot \\left( \\frac{d \\cdot w}{c \\cdot r} \\right)^c ='}{round(K_optimal, 2)}" style="{latex_style}" />
                    </div>
                    </li>
                    <br>
                    <li> Podmíněná poptávka po práci je <img src="{latex_img}{round(L_optimal, 2)}" style="{latex_style}" />
                    a podmíněná poptávka po kapitálu je <img src="{latex_img}{round(K_optimal, 2)}" style="{latex_style}" /> pro danou firmu.
                    </li>
                    </ol>
                    </div>""",
            unsafe_allow_html=True,
        )

        st.markdown("---")

        stezka_produktu_definice = f"""
        <div style="{box_style}">
            <b>Definice dlouhodobé stezky expanze produktu</b>:
            Dlouhodobá stezka expanze produktu je množina optimálních kombinací výrobních faktorů firmy při jejich
            konstantních cenách a při různých úrovních výstupu.
        </div>
        """

        st.markdown(stezka_produktu_definice, unsafe_allow_html=True)

        st.markdown(
            f"""
            <div style="text-align: justify">
            <br>
            Expanze produktu znamená, že se zvyšuje vyráběné množství tohoto produktu (tj. produkce). Jednotlivé úrovně produkce můžeme znázornit
            jako izokvanty v grafu, přičemž izokvanta je křivka zahrnující všechny možné kombinace množství výrobních faktorů pro konkrétní
            úroveň produkce neboli požadovaný výstup firmy. Dlouhodobá stezka expanze produktu je tedy přímka procházející všemi optimálními
            kombinacemi množství výrobních faktorů na každé izokvantě.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # Graf dlouhodobé stezky expanze produktu
        st.markdown(
            f"""<div style="text-align: justify">
                    V bočním panelu si nastavte ceny výrobních faktorů, jednu konkrétní úroveň produkce firmy a parametry
                    Cobb-Douglasovy produkční funkce.
                    Graf dlouhodobé stezky expanze produktu, na němž jsou zobrazeny optimální kombinace výrobních faktorů
                    <img src="{latex_img}{'L'}" style="{latex_style}" /> a <img src="{latex_img}{'K'}" style="{latex_style}" />
                    pro minimalizaci nákladů při pevně stanovených cenách práce a kapitálu –  <img src="{latex_img}{'w'}" style="{latex_style}" />,
                    <img src="{latex_img}{'r'}" style="{latex_style}" /> – pro různé úrovně produkce:
                    <br>
                    <br>
                    </div>""",
            unsafe_allow_html=True,
        )

        # Vypnutí a zapnutí popisků
        _, align_switch = st.columns([3.5, 1])
        with align_switch:
            labels_switch = st.toggle("Zobrazit údaje")

        y = np.linspace(0, scope, scope * 20)

        # Vytvoříme graf
        fig2, ax2 = plt.subplots()

        # Cobb-Douglasova produkční funkce
        L, K = np.meshgrid(x, y)
        Q = L**c * K**d

        # Izokvanty
        izo = [Q_0 + x * (scope / 9) for x in range(-8, 9)]
        ax2.contour(
            L, K, Q, levels=izo, colors="#7A7A7A", linestyles="dashed", alpha=0.75
        )

        # Optimální kombinace výrobních faktorů pro různé izokvanty
        L_optimals = np.array(izo) * ((c * r) / (d * w)) ** d
        K_optimals = np.array(izo) * ((d * w) / (c * r)) ** c

        # Dlouhodobá stezka expanze produktu
        slope2 = (d * w) / (c * r)
        ax2.plot(x, slope2 * x, color="#6473AC")

        # Vyznačení optima
        Q_levels = w * L_optimals + r * K_optimals
        ax2.scatter(L_optimals, K_optimals, color="red")

        for i, C_min in enumerate(Q_levels):
            if (
                C_min >= 0
                and L_optimals[i] < scope
                and K_optimals[i] < scope
                and labels_switch
            ):
                add_label = f"({round(L_optimals[i], 2)}, {round(K_optimals[i], 2)})\n$Q=${round(L_optimals[i]**c * K_optimals[i]**d, 2)}\n$TC=${round(C_min, 2)}"
                ax2.text(
                    L_optimals[i],
                    K_optimals[i],
                    add_label,
                    color="white",
                    fontsize=5.5,
                    bbox=dict(
                        facecolor="#0E1117", edgecolor="grey", linewidth=0.3, alpha=0.6
                    ),
                )

        # Prvky grafu
        font_properties = {
            "fontsize": 12,
            "fontweight": "bold",
            "fontfamily": "sans-serif",
        }

        ax2.set_xlabel("L", fontdict=font_properties)
        ax2.set_ylabel("K", fontdict=font_properties, rotation=0)
        plt.gca().xaxis.set_label_coords(1, -0.075)
        plt.gca().yaxis.set_label_coords(-0.05, 1.02)
        ax2.grid(True)
        ax2.set_xlim(0, scope)
        ax2.set_ylim(0, scope)

        handles = [
            plt.Line2D(
                [], [], color="#6473AC", label="Dlouhodobá stezka\nexpanze produktu"
            ),
            plt.Line2D(
                [],
                [],
                linestyle="dashed",
                color="#7A7A7A",
                alpha=0.75,
                label="Izokvanty pro $Q \\in \\mathbb{R}^{+}_0$",
            ),
            plt.scatter(
                [],
                [],
                color="red",
                label=f"Minimální náklady\nmin {'$w \\cdot L + r \\cdot K$'} pro {'$Q \\in \\mathbb{R}^{+}_0$'}",
            ),
        ]
        legend_pos = "upper left" if slope2 < 1.5 else "lower right"
        ax2.legend(handles=handles, loc=legend_pos, fontsize=9, facecolor="#0E1117")

        st.pyplot(fig2)

        st.markdown("---")

        st.markdown(
            f"""<div style="text-align: justify">
                    Rovnici dlouhodobé stezky expanze produktu pro danou firmu určíme následujícím způsobem:
                    <br>
                    <br>
                    <ol>
                    <li>Využijeme již odvozené podmíněné poptávky po výrobních faktorech
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                        <img src="{latex_img}{'L = Q_0 \\cdot \\left( \\frac{c \\cdot r}{d \\cdot w} \\right)^d'}" style="{latex_style}" />
                    <br>
                    <br>
                        <img src="{latex_img}{'K = Q_0 \\cdot \\left( \\frac{d \\cdot w}{c \\cdot r} \\right)^c'}" style="{latex_style}" /> .
                    </div>
                    </li>
                    <br>
                    <li>Vyjádříme z obou rovnic produkci <img src="{latex_img}{'Q_0'}" style="{latex_style}" />
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                        <img src="{latex_img}{'Q_0 = L \\cdot \\left( \\frac{d \\cdot w}{c \\cdot r} \\right)^d'}" style="{latex_style}" />
                    <br>
                    <br>
                        <img src="{latex_img}{'Q_0 = K \\cdot \\left( \\frac{c \\cdot r}{d \\cdot w} \\right)^c'}" style="{latex_style}" /> .
                    </div>
                    </li>
                    <br>
                    <li>Máme rovnost
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                    <img src="{latex_img}{'L \\cdot \\left( \\frac{d \\cdot w}{c \\cdot r} \\right)^d = K \\cdot \\left( \\frac{c \\cdot r}{d \\cdot w} \\right)^c'}" style="{latex_style}" />
                    </div>
                    a z této rovnosti vyjádříme <img src="{latex_img}{'K'}" style="{latex_style}" />
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'K = L \\cdot \\left( \\frac{d \\cdot w}{c \\cdot r} \\right)^{d+c} = \\frac{L \\cdot d \\cdot w}{c \\cdot r}'}" style="{latex_style}" /> .
                    </div>
                    </li>
                    <br>
                    <li>Získali jsme rovnici dlouhodobé stezky expanze produktu
                    <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'K = \\frac{L \\cdot d \\cdot w}{c \\cdot r}'}" style="{latex_style}" /> .
                    </div>
                    </li>
                    </ol>
                    </div>""",
            unsafe_allow_html=True,
        )

        st.markdown("---")

        LAC_definice = f"""
        <div style="{box_style}">
            <b>Definice funkce průměrných nákladů</b>:
            Funkci průměrných nákladů určíme ze vztahu
            <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
            <img src="{latex_img}{'LAC(w, r, Q) = \\frac{LTC(w, r, Q)}{Q}'}" style="{latex_style}" /> ,
            </div>
            kde <img src="{latex_img}{'Q'}" style="{latex_style}" /> je objem produkce a
            <img src="{latex_img}{'LTC(w, r, Q)'}" style="{latex_style}" /> jsou celkové náklady.
        </div>
        """

        st.markdown(LAC_definice, unsafe_allow_html=True)

        st.html("<br>")

        LMC_definice = f"""
        <div style="{box_style}">
            <b>Definice funkce mezních nákladů</b>:
            Funkci mezních nákladů určíme ze vztahu
            <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
            <img src="{latex_img}{'LMC(w, r, Q) = \\frac{\\partial LTC(w, r, Q)}{\\partial Q}'}" style="{latex_style}" /> ,
            </div>
            kde <img src="{latex_img}{'Q'}" style="{latex_style}" /> je objem produkce a
            <img src="{latex_img}{'LTC(w, r, Q)'}" style="{latex_style}" /> jsou celkové náklady.
        </div>
        """

        st.markdown(LMC_definice, unsafe_allow_html=True)
