import numpy as np
import matplotlib.pyplot as plt


class ConcreteType:

    def __init__(self, fck):
        self.fck = fck

        self.gamma = 1.5
        self.acc = 0.85

        self.eps_cc = -0.002
        self.eps_cu = -0.0035

        self.fcd = self.acc * self.fck / self.gamma

    # definizione diagramma sforzo-deformativo calcestruzzo
    # convenzione dei segni------ negativo di compressione ------positivo di trazione

    def curva_concrete(self, eps):
        self.eps = eps
        n = len(self.eps)
        self.sigma = np.zeros(n)
        for i in range(n):
            if self.eps[i] >= 0:
                # sono nellca zona di traizone non reagente(assunzione)
                self.sigma[i] = 0
            elif 0 > self.eps[i] >= self.eps_cc:
                # sono nellca curva non lineare
                self.sigma[i] = -self.fcd * (2 - self.eps[i] / self.eps_cc) * self.eps[i] / self.eps_cc
            elif self.eps_cc > self.eps[i] >= self.eps_cu:
                # sono nel platau orizzontale del cls
                self.sigma[i] = -self.fcd
            else:
                print("valore di eps_c non valido")
        return self.sigma

    def plot(self):
        eps_prova = np.linspace(-0.0035, 0, 100)
        sigma_prova = self.curva_concrete(eps_prova)
        plt.style.use("seaborn-whitegrid")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(-eps_prova * 1000, -sigma_prova)  # defomrazioni e tensioni cls sono negative perchè di compressione
        plt.show()
