import pandas as pd

df = pd.read_csv("ventes.csv")

df["CA_Brut"] = df["Prix"] * df["Quantite"]
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)
df["TVA"] = df["CA_Net"] * 0.20

total = df["CA_Net"].sum()
print("CA total :", total)

id_max = df.loc[df["CA_Net"].idxmax(), "ID"]
print("ID max :", id_max)

df.to_csv("resultats_final.csv", index=False)