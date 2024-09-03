import matplotlib.pyplot as plt
import numpy as np

def plot_impulse_response(M, h):
    # Resposta impulsiva do filtro
    n = np.arange(len(h))

    # Resposta impulsiva do filtro
    plt.figure(figsize=(8, 5))
    plt.stem(n - (M - 1) // 2, h, basefmt='b-')
    plt.xlabel("n", fontsize=16)
    plt.ylabel("Amplitude", fontsize=16)
    plt.title("Resposta Impulsiva do Filtro", fontsize=18)



def plot_frequency_response(w, h, wc=None, attenuation=None, fig=None, axs=None, color="black", legend=True, return_axs=False):
    
    if fig is None or axs is None:
        fig, axs = plt.subplots(2, 1, figsize=(6, 8))
    
    # Magnitude da resposta em frequência (em dB)
    axs[0].plot(w, 20 * np.log10(np.abs(h)), color=color, linewidth=2.0, linestyle='-', label="Filtro FIR")
    axs[0].set_xlim(0, 1)

    axs[0].set_title('Magnitude da Resposta em Frequência (dB)')
    axs[0].set_xlabel(r"Frequência ($\omega$) [rad/s]")
    axs[0].set_ylabel(r"$|H(e^{j\omega})|$ - Amplitude [dB]")
    axs[0].grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    
    # Configurações do eixo x para mostrar múltiplos de pi
    axs[0].set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], 
                      ['0', '0.2π', '0.4π', '0.6π', '0.8π', 'π'])


    # Magnitude da resposta em frequência (linear)
    axs[1].plot(w, np.abs(h), color=color, linewidth=2.0, linestyle='-')
    axs[1].set_xlim(0, 1)
    axs[1].set_title('Magnitude da Resposta em Frequência (Linear)')
    axs[1].set_xlabel(r"Frequência ($\omega$) [rad/s]")
    axs[1].set_ylabel('Magnitude')
    axs[1].set_ylabel(r"$|H(e^{j\omega})|$ - Magnitude")
    axs[1].grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    axs[1].set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], 
                      ['0', '0.2π', '0.4π', '0.6π', '0.8π', 'π'])

    
    # Se wc foi fornecido, desenhe a linha de frequência de corte
    if wc is not None:
        axs[0].axvline(wc, color='red', linestyle='--', linewidth=2.0, label='Frequência de Corte')
        axs[1].axvline(wc, color='red', linestyle='--', linewidth=2.0, label='Frequência de Corte')

    # Se attenuation foi fornecido, desenhe a linha de atenuação
    if attenuation is not None:
        axs[0].axhline(-attenuation, color='blue', linestyle=':', linewidth=2.0, label=f'Atenuação ({attenuation} dB)')

    if legend == True:
        axs[0].legend() 
    
    plt.tight_layout()

    if return_axs == True:
        return axs
    else: 
        return None 


# Função para plotar o erro de aproximação
def plot_approximation_error(w, error, color="black"):
    plt.figure(figsize=(6, 4))
    plt.plot(w, error, linewidth=2.0, color=color)
    plt.title('Erro de Aproximação $E_A(\omega)$')
    plt.xlabel(r'Frequência Normalizada ($\omega/\pi$)')
    plt.ylabel(r'$E_A(\omega)$ - Erro de Aproximação')
    plt.grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    plt.show()


def plot_phase_response(w, h, fig=None, axs=None, unit='degrees', color="black"):
    if fig is None or axs is None:
        fig, axs = plt.subplots(figsize=(6, 4))

    # Fase da resposta em frequência
    phase = np.angle(h)
    angles = np.unwrap(phase)
    
    if unit == 'degrees':
        angles = np.degrees(angles)
        ylabel = 'Fase [degraus]'
    else:
        angles = angles
        ylabel = 'Fase [radianos]'

    axs.plot(w, angles, color=color, linewidth=2.0, linestyle='-')
    axs.set_xlim(0, 1)
    axs.set_title('Resposta em Fase')
    axs.set_xlabel(r"Frequência ($\omega/) [rad/s]")
    axs.set_ylabel(ylabel)
    axs.grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    axs.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], 
                   ['0', '0.2π', '0.4π', '0.6π', '0.8π', 'π'])

    plt.tight_layout()
    return axs


def plot_group_delay(w, group_delay, fig=None, axs=None, color="black"):
    if fig is None or axs is None:
        fig, axs = plt.subplots(figsize=(6, 4))

    axs.plot(w / np.pi, group_delay, color=color, linewidth=2.0, linestyle='-')
    axs.set_xlim(0, 1)
    axs.set_title('Atraso de Grupo')
    axs.set_xlabel(r"Frequência ($\omega$) [rad/s]")
    axs.set_ylabel('Atraso de Grupo [s]')
    axs.grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    axs.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], 
                   ['0', '0.2π', '0.4π', '0.6π', '0.8π', 'π'])

    plt.tight_layout()
    return axs
