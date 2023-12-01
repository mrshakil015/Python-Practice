import numpy as np
import matplotlib.pyplot as plt

def generate_ecg(duration, fs):
    t = np.arange(0, duration, 1 / fs)
    ecg_signal = np.zeros_like(t)

    # Generate individual components of the ECG signal
    p_wave = np.sin(2 * np.pi * 0.5 * t)  # P-wave
    qrs_complex = np.sin(2 * np.pi * 1.0 * t)  # QRS complex
    t_wave = np.sin(2 * np.pi * 0.2 * t)  # T-wave

    # Combine the components
    ecg_signal += p_wave + qrs_complex + t_wave

    return ecg_signal, p_wave, qrs_complex, t_wave

# Set the duration (seconds) and sampling frequency (Hz)
duration = 5.0
fs = 1000

# Generate the ECG signal and components
ecg, p_wave, qrs_complex, t_wave = generate_ecg(duration, fs)

# Create the time axis for plotting
t = np.arange(0, duration, 1 / fs)

# Plot the ECG signal
plt.plot(t, ecg, label='ECG Signal')
plt.plot(t, p_wave, label='P-wave')
plt.plot(t, qrs_complex, label='QRS complex')
plt.plot(t, t_wave, label='T-wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('ECG Signal with P, Q, R, S, T Points')
plt.legend()
plt.grid(True)
plt.show()
