import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("resultats_final.csv")

plt.bar(df["ID"], df["CA_Net"])
plt.xlabel("ID")
plt.ylabel("CA Net")
plt.title("CA Net par produit")
plt.show()