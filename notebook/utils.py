import matplotlib.pyplot as plt
import numpy as np

def pi_multiples_scale():
    return ([0, 0.2, 0.4, 0.6, 0.8, 1.0],
            ['0', '0.2π', '0.4π', '0.6π', '0.8π', 'π'])


def plot_zeros(zeros, legend=False):
    plt.figure(figsize=(6, 5))
    plt.title('Plano Z: Filtro digital')
    plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='tab:blue', label='Zeros')
    plt.plot(np.cos(np.linspace(0, 2 * np.pi, 100)), np.sin(np.linspace(0, 2 * np.pi, 100)), color='black', linestyle='-', label='Círculo Unitário')
    plt.xlabel('$Re$')
    plt.ylabel('$Im$')
    if legend==True:
        plt.legend()
    plt.grid(True)


def plot_impulse_response(N, filter_h):
    plt.figure(figsize=(10, 6))
    plt.stem(range(N), filter_h, basefmt=" ") 
    plt.title('Resposta ao Impulso do Filtro FIR')
    plt.xlabel('Amostra')
    plt.ylabel('Amplitude')
    plt.xlim(0, N)
    # Desativa a grade padrão
    plt.grid(False)
    # Adiciona uma linha de grade manualmente na posição zero
    plt.axhline(0, color='black', linestyle='-', linewidth=0.5)
    plt.show()


def plot_magnitude_response_db(w, h, axs=None, color="black", wc=None, attenuation=None, legend=True, label="Filtro FIR"):
    if axs is None:
        fig, axs = plt.subplots(1, 1, figsize=(6, 8))
    
    axs.plot(w, 20 * np.log10(np.abs(h)), color=color, linewidth=2.0, linestyle='-', label=label)
    axs.set_xlim(0, 1)
    axs.set_title('Magnitude da Resposta em Frequência (dB)')
    axs.set_xlabel(r"Frequência ($\omega$) [rad/s]")
    axs.set_ylabel(r"$|H(e^{j\omega})|$ - Amplitude [dB]")
    axs.grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    axs.set_xticks(*pi_multiples_scale())

    if wc is not None:
        axs.axvline(wc, color='red', linestyle='--', linewidth=2.0, label='Frequência de Corte')
    if attenuation is not None:
        axs.axhline(-attenuation, color='blue', linestyle=':', linewidth=2.0, label=f'Atenuação ({attenuation} dB)')
    
    if legend:
        axs.legend()

def plot_magnitude_response_linear(w, h, axs=None, color="black", wc=None):
    if axs is None:
        fig, axs = plt.subplots(1, 1, figsize=(6, 8))
    
    axs.plot(w, np.abs(h), color=color, linewidth=2.0, linestyle='-')
    axs.set_xlim(0, 1)
    axs.set_title('Magnitude da Resposta em Frequência (Linear)')
    axs.set_xlabel(r"Frequência ($\omega$) [rad/s]")
    axs.set_ylabel(r"$|H(e^{j\omega})|$ - Magnitude")
    axs.grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    axs.set_xticks(*pi_multiples_scale())

    if wc is not None:
        axs.axvline(wc, color='red', linestyle='--', linewidth=2.0, label='Frequência de Corte')


def plot_frequency_response(w, h, wc=None, attenuation=None, axs=None, color="black", legend=True, return_axs=False):
    if axs is None:
        fig, axs = plt.subplots(2, 1, figsize=(6, 8))

    # Plotar a magnitude em dB
    plot_magnitude_response_db(w, h, axs[0], color=color, wc=wc, attenuation=attenuation, legend=legend)

    # Plotar a magnitude linear
    plot_magnitude_response_linear(w, h, axs[1], color=color, wc=wc)

    plt.tight_layout()

    if return_axs:
        return axs


# Função para plotar o erro de aproximação
def plot_approximation_error(w, error, color="black"):
    plt.figure(figsize=(6, 4))
    plt.plot(w, error, linewidth=2.0, color=color)
    plt.title('Erro de Aproximação $E_A(\omega)$')
    plt.xlabel(r'Frequência Normalizada ($\omega$)')
    plt.ylabel(r'$E_A(\omega)$ - Erro de Aproximação')
    plt.grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    plt.xlim(0, 1)
    plt.xticks(*pi_multiples_scale())

    plt.show()


def plot_phase_response(w, h, axs=None, unit='degrees', color="black"):
    if axs is None:
        fig, axs = plt.subplots(figsize=(6, 4))

    # Fase da resposta em frequência
    phase = np.angle(h)
    angles = np.unwrap(phase)
    
    if unit == "degrees":
        angles = np.degrees(angles)
        ylabel = 'Fase [graus]'
    elif unit == "rad":
        ylabel = 'Fase [radianos]'

    axs.plot(w, angles, color=color, linewidth=2.0, linestyle='-')
    axs.set_xlim(0, 1)
    axs.set_title('Resposta em Fase')
    axs.set_xlabel(r"Frequência ($\omega$) [rad/s]")
    axs.set_ylabel(ylabel)
    axs.grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    axs.set_xticks(*pi_multiples_scale())

    plt.tight_layout()
    return axs


def plot_group_delay(M, w):
    # Atraso de grupo constante para um filtro FIR simétrico
    tau_g = M / 2 * np.ones_like(w)

    plt.figure(figsize=(6, 4))
    plt.plot(w, tau_g, color="blue", linewidth=2.0)
    plt.title('Atraso de Grupo $\\tau_g(\\omega)$')
    plt.xlabel(r'Frequência Normalizada ($\omega/\pi$)')
    plt.ylabel('Atraso de Grupo [amostras]')
    plt.ylim([0, M])
    plt.xlim([0, 1])
    plt.grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    plt.xticks(*pi_multiples_scale())
    plt.show()


def plot_frequency_and_phase_response(w, h, wc=None, attenuation=None, color="black", legend=True, return_axs=False):
    fig, axs = plt.subplots(3, 1, figsize=(6, 10))
    
    plot_frequency_response(w, h, wc=wc, attenuation=attenuation, axs=axs, color=color, legend=legend, return_axs=False)

    plot_phase_response(w, h, axs=axs[2], color=color)

    plt.tight_layout()
    plt.show()

    if return_axs == True:
        return axs