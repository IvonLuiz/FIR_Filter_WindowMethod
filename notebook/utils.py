import matplotlib.pyplot as plt
import numpy as np

def plot_impulse_response(M, h):
    # Resposta impulsiva do filtro
    n = np.arange(len(h))

    # Resposta impulsiva do filtro
    plt.figure(figsize=(10, 5))
    plt.stem(n - (M - 1) // 2, h, basefmt='b-')
    plt.xlabel("n", fontsize=16)
    plt.ylabel("Amplitude", fontsize=16)
    plt.title("Resposta Impulsiva do Filtro", fontsize=18)

    plt.show()


def plot_frequency_response_direct(w, H, fig=None, axs=None, color='b'):
    # Criando a figura e os subplots caso não tenham sido passados
    if fig is None or axs is None:
        fig,axs = plt.subplots(2, 1, figsize=(10, 8))
    
    # Magnitude da resposta em frequência (em dB)
    axs[0].plot(w / np.pi, 20 * np.log10(np.abs(H)), color, label="Filtro FIR")
    axs[0].set_xlim(0, 1)

    axs[0].set_title('Magnitude da Resposta em Frequência (dB)')
    axs[0].set_xlabel(r"$\omega$ [$\pi$ * rad / s] - Frequência Normalizada (π radianos)")
    axs[0].set_ylabel(r"$|H(e^{j\omega})|$ - Amplitude [dB]")
    axs[0].grid()

    # Resposta em frequência em amplitude linear
    axs[1].plot(w / np.pi, np.abs(H), color)
    axs[1].set_xlim(0, 1)

    axs[1].set_title('Magnitude da Resposta em Frequência (Linear)')
    axs[1].set_xlabel(r"$\omega$ [$\pi$ * rad / s] - Frequência Normalizada (π radianos)")
    axs[1].set_ylabel(r"$|H(e^{j\omega})|$ - Amplitude")
    axs[1].grid()

    # Ajustando o layout
    plt.tight_layout()

    return axs


def plot_frequency_response_cascade(w_cascade, wc, H_cascade, H, fig=None, axs=None, color='g'):
    if fig is None or axs is None:
        fig, axs = plt.subplots(2, 1, figsize=(10, 10))
    
    # plt.subplots_adjust(hspace=0.8)
    
    # Magnitude da resposta em frequência
    ax = axs[0]
    ax.plot(w_cascade * np.pi, abs(H_cascade))
    ax.vlines([wc], 0, 1.2 * max(np.max(abs(H)), np.max(abs(H_cascade))), color='g', lw=2., linestyle='--')
    ax.hlines(1, -np.pi, np.pi, color='g', lw=2., linestyle='--')
    ax.set_xlabel(r"$\omega$", fontsize=22)
    ax.set_ylabel(r"$|H(\omega)|$", fontsize=22)
    ax.set_title("Magnitude de Resposta em Frequência", fontsize=18)
    ax.grid()
    ax.legend()

    # Resposta em frequência em dB
    ax = axs[1]
    ax.plot(w_cascade * np.pi, 20 * np.log10(abs(H_cascade)))
    ax.vlines([wc], -60, 5, color=color, lw=2., linestyle='--')
    ax.hlines(0, -np.pi, np.pi, color=color, lw=2., linestyle='--')
    ax.set_xlabel(r"$\omega$", fontsize=22)
    ax.set_ylabel(r"$20\log_{10}|H(\omega)|$", fontsize=18)
    ax.set_title("Resposta em Frequência em dB", fontsize=18)
    ax.grid()
    ax.legend()

    plt.show()