import pandas as pd
import matplotlib.pyplot as plt

liquid_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
liquid_header = ["Alcohol", "Acido Malico", "Cenizas", "Alcanilidad de las Cenizas", "Magnesio", "Fenoles Totales", "Flavonoides", "Fenoles no Flavonoides", "Proanticianinas", "Intensidad de Color", "Matiz", "OD280/OD315 de Sustancia Diluida", "Prolina"]
liquid_df = pd.read_csv(liquid_url, names=liquid_header)

fig, axis1 = plt.subplots()
fig.set_size_inches(13, 10)

axis1.set_xlabel("Alcohol")
axis1.set_ylabel("Intensidad de Color")
axis1.set_title("Relacion Intesidad de Color ~ Cantidad de Alcohol")

c = liquid_df["Intensidad de Color"]

plt.scatter(liquid_df["Alcohol"], liquid_df["Intensidad de Color"], c=c, cmap="RdPu", s=liquid_df["Prolina"]*.3, alpha=0.9)
