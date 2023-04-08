import matplotlib.pyplot as plt
import seaborn as sns

orneklem1 = [188, 188, 189, 195, 198, 202, 203, 207, 208, 209, 209, 209, 212, 214, 216, 219, 225, 228, 228, 236]
orneklem2 = [151, 155, 157, 173, 176, 182, 185, 191, 192, 192, 198, 209, 213, 214, 218, 219, 219, 251, 258, 259]

# Verileri bir DataFrame içinde birleştirelim
import pandas as pd
df1 = pd.DataFrame({'Örneklem': '1', 'Değer': orneklem1})
df2 = pd.DataFrame({'Örneklem': '2', 'Değer': orneklem2})
df = pd.concat([df1, df2])

# Box-plot diyagramını çizdirelim
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.boxplot(x="Örneklem", y="Değer", data=df)
plt.title("Örneklem 1 ve Örneklem 2 Box-Plot Karşılaştırması")
plt.show()
