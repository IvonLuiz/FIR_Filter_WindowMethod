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


def plot_frequency_response_direct(w, H):
    # Plotando a resposta em frequência do filtro
    plt.figure(figsize=(6, 6))

    # Magnitude da resposta em frequência
    plt.subplot(2, 1, 1)
    plt.plot(w / np.pi, 20 * np.log10(np.abs(H)), 'b')
    plt.title('Resposta em Frequência do Filtro FIR utilizando Janela de Kaiser')
    plt.xlabel('Frequência Normalizada (π radianos)')
    plt.ylabel('Amplitude (dB)')
    plt.grid()

    # Resposta em frequência em amplitude linear
    plt.subplot(2, 1, 2)
    plt.plot(w / np.pi, np.abs(H), 'b')
    plt.xlabel('Frequência Normalizada (π radianos)')
    plt.ylabel('Amplitude')
    plt.grid()

    plt.tight_layout()
    plt.show()


def plot_frequency_response_cascade(w_cascade, wc, H_cascade, H):
    fig, axs = plt.subplots(2, 1, figsize=(8, 12))
    plt.subplots_adjust(hspace=0.8)
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
    ax.vlines([wc], -60, 5, color='g', lw=2., linestyle='--')
    ax.hlines(0, -np.pi, np.pi, color='g', lw=2., linestyle='--')
    ax.set_xlabel(r"$\omega$", fontsize=22)
    ax.set_ylabel(r"$20\log_{10}|H(\omega)|$", fontsize=18)
    ax.set_title("Resposta em Frequência em dB", fontsize=18)
    ax.grid()
    ax.legend()

    plt.show()