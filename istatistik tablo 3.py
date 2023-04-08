import matplotlib.pyplot as plt

tip1 = [350, 350, 350, 358, 370, 370, 370, 371, 371, 372, 372, 384, 391, 391, 392]
tip2 = [350, 354, 359, 363, 365, 368, 369, 371, 373, 374, 376, 380, 383, 388, 392]
tip3 = [350, 361, 362, 364, 364, 365, 366, 371, 377, 377, 377, 379, 380, 380, 392]

def dot_plot(veriler, etiket, renk, y_pos):
    plt.scatter(veriler, [y_pos] * len(veriler), label=etiket, color=renk, alpha=0.7)

plt.figure(figsize=(10, 5))
dot_plot(tip1, "Tip 1", "red", 1)
dot_plot(tip2, "Tip 2", "blue", 2)
dot_plot(tip3, "Tip 3", "green", 3)

plt.yticks([1, 2, 3], ["Tip 1", "Tip 2", "Tip 3"])
plt.xlabel("Yorulma Limiti (Mpa)")
plt.ylabel("Halat Teli Numunesi")
plt.title("Halat Teli Numuneleri için Yorulma Limitleri")
plt.legend()
plt.grid(axis="y")
plt.show()
