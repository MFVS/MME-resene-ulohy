import matplotlib.pyplot as plt

# Kosmetika rámečků
box_style = """
    border: 0.5px solid #41444C;
    padding: 10px;
    border-radius: 5px;
    text-align: justify;
    background-color: #131720;
"""

# Renderování LaTeXu
latex_img = 'https://latex.codecogs.com/svg.latex?'
latex_style = 'filter: invert(100%);'

# Kosmetika grafů
plt.rcParams.update({
    'figure.facecolor': 'none',
    'axes.facecolor': 'none',
    'axes.edgecolor': 'white',
    'axes.labelcolor': 'white',
    'xtick.color': 'white',
    'ytick.color': 'white',
    'text.color': 'white',
    'grid.color': '#2C2C2B',
    'grid.linestyle': '--',
    'grid.linewidth': 0.5,
})