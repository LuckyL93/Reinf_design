import numpy as np
import matplotlib.pyplot as plt


class SteelType:

    def __init__(self, fyk):
        self.fyk = fyk
        self.Es = 200000  # Gpa
        self.gamma = 1.15
        self.fyd = self.fyk / self.gamma

        self.eps_su = 0.01
        self.eps_y = self.fyd / self.Es

    def curva_steel(self, eps):
        self.eps = eps
        n = len(self.eps)
        self.sigma = np.zeros(n)
        for i in range(n):
            if -self.eps_su <= self.eps[i] <= -self.eps_y:
                # sono nella zona di compresisone dell'acciaio
                self.sigma[i] = -self.fyd
            elif -self.eps_y < self.eps[i] <= self.eps_y:
                # zona lineare dell'acciao prima di snervem
                self.sigma[i] = self.eps[i] * self.Es
            elif self.eps_y < self.eps[i] <= self.eps_su:
                # zona tesa dell'acciaio positiva
                self.sigma[i] = self.fyd
            else:
                print("valore di eps_s non valido")
        return self.sigma

    def plot(self):
        eps_prova = np.linspace(-0.01, 0.01, 100)
        sigma_prova = self.curva_steel(eps_prova)
        plt.style.use("seaborn-whitegrid")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(-eps_prova * 1000, -sigma_prova)
        plt.show()
