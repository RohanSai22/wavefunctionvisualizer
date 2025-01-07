import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar
from scipy.linalg import expm
import streamlit as st
import plotly.graph_objects as go

# Define constants
mass = 1.0  # Mass of the particle

def normalize_wave_function(psi, dx):
    norm = np.sqrt(np.sum(np.abs(psi)**2) * dx)
    return psi / norm

def initialize_wave_packet(x, x0, k0, sigma):
    norm = (1 / (np.sqrt(sigma * np.sqrt(np.pi))))
    wave_packet = norm * np.exp(-((x - x0) ** 2) / (2 * sigma ** 2)) * np.exp(1j * k0 * x)
    return wave_packet

def hamiltonian(x, V):
    dx = x[1] - x[0]
    N = len(x)
    kinetic = -(hbar**2 / (2 * mass)) * (
        np.diag(np.ones(N - 1), -1) - 2 * np.diag(np.ones(N)) + np.diag(np.ones(N - 1), 1)
    ) / dx**2
    potential = np.diag(V)
    return kinetic + potential

def evolve_wave_function(psi, H, dt):
    U = expm(-1j * H * dt / hbar)
    return U @ psi

def plot_wave_function(x, psi, title):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, psi.real, label="Real Part", color="blue")
    ax.plot(x, psi.imag, label="Imaginary Part", color="red")
    ax.plot(x, np.abs(psi), label="Magnitude", color="green")
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(-1, 1)
    ax.set_title(title)
    ax.legend()
    ax.set_xlabel("x")
    ax.set_ylabel("Wave Function")
    st.pyplot(fig)

def interactive_3d_visualization(x, psi):
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=x, y=np.zeros_like(x), z=psi.real, mode='lines', name='Real Part'))
    fig.add_trace(go.Scatter3d(x=x, y=np.ones_like(x), z=psi.imag, mode='lines', name='Imaginary Part'))
    fig.add_trace(go.Scatter3d(x=x, y=2 * np.ones_like(x), z=np.abs(psi), mode='lines', name='Magnitude'))
    fig.update_layout(
        title="3D Wave Function Visualization",
        scene=dict(
            xaxis_title="x",
            yaxis_title="Components",
            zaxis_title="Amplitude"
        )
    )
    st.plotly_chart(fig)

# Streamlit App
st.title("Wave Function Visualizer in Quantum Computing")
st.sidebar.title("Simulation Parameters")

# Simulation parameters
x_min = st.sidebar.number_input("x_min", value=-10.0, step=1.0)
x_max = st.sidebar.number_input("x_max", value=10.0, step=1.0)
N = st.sidebar.number_input("Number of spatial points (N)", value=500, step=10)
x = np.linspace(x_min, x_max, int(N))

default_x0 = (x_min + x_max) / 2
x0 = st.sidebar.slider("Initial position (x0)", min_value=float(x_min), max_value=float(x_max), value=default_x0)
k0 = st.sidebar.slider("Initial momentum (k0)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
sigma = st.sidebar.slider("Wave packet width (sigma)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

k = st.sidebar.slider("Spring constant (k) for harmonic potential", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
V = 0.5 * k * x**2  # Harmonic potential

dx = x[1] - x[0]
time_steps = st.sidebar.number_input("Number of time steps", value=200, step=10)
dt = st.sidebar.number_input("Time step (dt)", value=0.01, step=0.001, format="%.3f")

# Initialize wave packet and Hamiltonian
psi = initialize_wave_packet(x, x0, k0, sigma)
psi = normalize_wave_function(psi, dx)
H = hamiltonian(x, V)

# Display initial wave function
st.header("Initial Wave Function")
plot_wave_function(x, psi, "Initial Wave Function")
interactive_3d_visualization(x, psi)

# Time evolution
st.header("Wave Function Dynamics")
progress_bar = st.progress(0)
psi_evolved = psi.copy()
for t in range(time_steps):
    psi_evolved = evolve_wave_function(psi_evolved, H, dt)
    psi_evolved = normalize_wave_function(psi_evolved, dx)
    progress_bar.progress((t + 1) / time_steps)

if not np.any(psi_evolved):
    st.error("Final wave function is empty. Please check the parameters and try again.")
else:
    st.subheader("Final Wave Function After Evolution")
    plot_wave_function(x, psi_evolved, "Final Wave Function")
    interactive_3d_visualization(x, psi_evolved)

# Additional feature: Custom potential
st.sidebar.subheader("Custom Potential")
use_custom_potential = st.sidebar.checkbox("Use custom potential")
if use_custom_potential:
    V_custom = st.sidebar.text_area("Enter custom potential as a Python expression (e.g., 0.5 * x**2)", value="0.5 * x**2")
    try:
        V = eval(V_custom)
        if len(V) == len(x):
            H = hamiltonian(x, V)
            st.success("Custom potential applied successfully.")
        else:
            st.error("Custom potential must match the spatial grid size.")
    except Exception as e:
        st.error(f"Error in custom potential: {e}")

# Conclusion
st.header("Summary")
st.write("This app demonstrates the evolution of a quantum wave function in a harmonic potential. You can modify parameters such as the initial wave packet, potential, and time evolution settings to explore different scenarios. Use the sidebar to adjust these settings and see the results dynamically.")
