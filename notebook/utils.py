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



def plot_frequency_response(w, h, wc=None, attenuation=None, fig=None, axs=None, color="black", legend=True):
    
    figure_input = True
    if fig is None or axs is None:
        figure_input = False
        fig, axs = plt.subplots(2, 1, figsize=(6, 8))
    
    # Magnitude da resposta em frequência (em dB)
    axs[0].plot(w / np.pi, 20 * np.log10(np.abs(h)), color=color, linewidth=2.0, linestyle='-', label="Filtro FIR")
    axs[0].set_xlim(0, 1)

    axs[0].set_title('Magnitude da Resposta em Frequência (dB)')
    axs[0].set_xlabel(r"Frequência ($\omega$) [rad/s]")
    axs[0].set_ylabel(r"$|H(e^{j\omega})|$ - Amplitude [dB]")
    axs[0].grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    
    # Configurações do eixo x para mostrar múltiplos de pi
    axs[0].set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], 
                      ['0', '0.2π', '0.4π', '0.6π', '0.8π', 'π'])


    # Magnitude da resposta em frequência (linear)
    axs[1].plot(w / np.pi, np.abs(h), color=color, linewidth=2.0, linestyle='-')
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
        axs[0].axvline(wc / np.pi, color='red', linestyle='--', linewidth=2.0, label='Frequência de Corte')
        axs[1].axvline(wc / np.pi, color='red', linestyle='--', linewidth=2.0, label='Frequência de Corte')

    # Se attenuation foi fornecido, desenhe a linha de atenuação
    if attenuation is not None:
        axs[0].axhline(-attenuation, color='blue', linestyle=':', linewidth=2.0, label=f'Atenuação ({attenuation} dB)')

    if legend == True:
        axs[0].legend() 
    
    plt.tight_layout()

    if figure_input == True:
        return axs
    else: 
        return None 

def plot_approximation_error(w, h, desired_response, fig=None, axs=None, color="black", legend=None):
    if fig is None or axs is None:
        fig, axs = plt.subplots(figsize=(6, 4))

    # Calculando o erro de aproximação
    error = 20 * np.log10(np.abs(desired_response - h))
    
    axs.plot(w / np.pi, error, color=color, linewidth=2.0, linestyle='-', label=legend)
    axs.set_xlim(0, 1)
    axs.set_title('Erro de Aproximação')
    axs.set_xlabel(r"Frequência Normalizada ($\omega$) [$\pi$ rad/s]")
    axs.set_ylabel('Erro [dB]')
    axs.grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    axs.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], ['0', '0.2π', '0.4π', '0.6π', '0.8π', 'π'])

    if legend is not None:
        axs.legend()

    plt.tight_layout()
    return axs


def plot_phase_response(w, h, fig=None, axs=None, color="black", legend=None):
    if fig is None or axs is None:
        fig, axs = plt.subplots(figsize=(6, 4))

    # Fase da resposta em frequência
    phase = np.angle(h)
    
    axs.plot(w / np.pi, phase, color=color, linewidth=2.0, linestyle='-', label=legend)
    axs.set_xlim(0, 1)
    axs.set_title('Resposta em Fase')
    axs.set_xlabel(r"Frequência Normalizada ($\omega$) [$\pi$ rad/s]")
    axs.set_ylabel('Fase [rad]')
    axs.grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    axs.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], ['0', '0.2π', '0.4π', '0.6π', '0.8π', 'π'])

    if legend is not None:
        axs.legend()

    plt.tight_layout()
    return axs

def plot_group_delay(w, h, fig=None, axs=None, color="black", legend=None):
    if fig is None or axs is None:
        fig, axs = plt.subplots(figsize=(6, 4))

    # Calculando o atraso de grupo
    phase = np.angle(h)
    group_delay = -np.diff(phase) / np.diff(w)
    
    # Ajustar o eixo x para corresponder ao comprimento de group_delay
    w_group_delay = (w[:-1] + w[1:]) / 2 / np.pi
    
    axs.plot(w_group_delay, group_delay, color=color, linewidth=2.0, linestyle='-', label=legend)
    axs.set_xlim(0, 1)
    axs.set_title('Atraso de Grupo')
    axs.set_xlabel(r"Frequência Normalizada ($\omega$) [$\pi$ rad/s]")
    axs.set_ylabel('Atraso de Grupo [s]')
    axs.grid(True, which='both', linestyle='-', linewidth=0.2, alpha=0.6, color='black')
    axs.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], ['0', '0.2π', '0.4π', '0.6π', '0.8π', 'π'])

    if legend is not None:
        axs.legend()

    plt.tight_layout()
    return axs

def plot_frequency_response_direct(w, h, wc, fig=None, axs=None, color='b'):
    # Agora, plotando a fase da resposta em frequência
    plt.figure()

    # Gráfico de fase
    plt.plot(w, np.angle(h), color='black', linewidth=2.0, linestyle='-')

    # Linha tracejada vermelha para a frequência de corte
    plt.axvline(x=wc, color='red', linestyle='--', linewidth=2.0, label='Frequência de Corte')

    # Ajustes no estilo do gráfico
    plt.xlabel('Frequência em radianos ($\omega$)')
    plt.ylabel('Radianos')

    # Configurações do eixo x para mostrar múltiplos de pi de 0 a π
    plt.xticks([0, np.pi/2, np.pi], ['0', '$\\frac{\\pi}{2}$', '$\pi$'])

    # Ajustando o eixo y para mostrar a fase em radianos
    plt.yticks(np.arange(-4, 5, 2))

    # Exibir a legenda
    plt.legend()

    # Grid e display
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='black')
    plt.show()