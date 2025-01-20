# Wave Function Visualizer

## Overview
The **Wave Function Visualizer** is an interactive web application that simulates and visualizes the evolution of a quantum wave function in a potential field, using concepts from quantum mechanics. The app is built with Streamlit and leverages NumPy, SciPy, and Plotly for computation and visualization.

## Features
- **Interactive Parameter Controls**: Adjust spatial range, number of points, initial wave packet properties, and the potential field in real-time.
- **3D Visualization**: View the wave function's real, imaginary, and magnitude components in an interactive 3D plot.
- **Dynamic Evolution**: Simulate the time evolution of the wave function and observe its behavior step-by-step.
- **Custom Potentials**: Define and apply custom potential fields to observe unique quantum phenomena.

## Error and Known Issue
### Error: Normalization failed
- **Error Message**: `Error: Normalization failed: Wave function norm is zero or invalid.`
- **Cause**: This error occurs if the wave function's norm becomes zero or invalid during initialization or time evolution. This is often caused by extreme parameter values or numerical instability.
- **How to Solve the Error**:
  1. **Verify Parameters**: Ensure that all parameters are within recommended ranges.
  2. **Reduce Time Step (`dt`)**: A smaller time step can improve numerical stability.
  3. **Check Potential Validity**: Confirm that the potential matches the spatial grid size.
  4. **Refine Spatial Grid (`N`)**: A higher resolution can resolve finer details.
  5. **Solve the Issue**: Raise the issue and solve it, i will verify it and approve it ...
  
  ---{ Error Has Been Resolved}---
  

## Requirements
- Python 3.7 or higher
- Required Libraries:
  - NumPy
  - SciPy
  - Matplotlib
  - Plotly
  - Streamlit

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/RohanSai22/wavefunctionvisualizer
   cd wave-function-visualizer
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

## Usage
1. Launch the app by running the command above. The app will open in your default web browser.
2. Use the sidebar to configure simulation parameters:
   - **x_min / x_max**: Define the spatial range for the simulation.
   - **N**: Number of spatial points.
   - **x0 / k0**: Initial position and momentum of the wave packet.
   - **sigma**: Width of the wave packet.
   - **k**: Spring constant for the harmonic potential.
   - **dt**: Time step for the simulation.
3. View the initial wave function and its evolution over time.
4. Optionally, define a custom potential using Python expressions.

## Recommended Parameter Values
- **Spatial Grid (`N`)**: 500 to 1000
- **Wave Packet Width (`sigma`)**: 0.5 to 2.0
- **Time Step (`dt`)**: 0.01 to 0.05
- **Harmonic Spring Constant (`k`)**: 0.1 to 5.0

## Example
Here is an example configuration:
- Spatial range: `x_min = -10`, `x_max = 10`
- Number of points: `N = 500`
- Initial wave packet: `x0 = 0`, `k0 = 5`, `sigma = 1`
- Harmonic potential: `k = 1`
- Time step: `dt = 0.01`

## Troubleshooting
If you encounter the **Normalization failed** error:
1. Verify that the parameters are reasonable.
2. Ensure that the spatial resolution (`dx`) is not too coarse.
3. Decrease the time step (`dt`) if the wave function behaves erratically.
4. Check if the potential function is valid and matches the spatial grid size.
5. Experiment with different initial wave packet parameters to ensure numerical stability.

## Challenge for Contributors
We invite the community to investigate and resolve the `Normalization failed` error under challenging parameter configurations. Can you identify edge cases and propose robust fixes? Submit your solutions via pull requests and contribute to the project!

## Contribution Guidelines
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to the branch:
   ```bash
   git push origin feature-name
   ```
4. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- Quantum mechanics concepts inspired by standard textbooks and online resources.
- Visualization powered by Plotly and Matplotlib.
- UI built with Streamlit.
