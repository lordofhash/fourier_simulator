# [Fourier Series Simulator](https://github.com/lordofhash/fourier_simulator/)

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-green.svg)

An interactive educational tool for visualizing Fourier series approximations of various periodic functions. This simulator helps students and educators understand how Fourier series work by providing real-time visualization of different wave types and their Fourier approximations.

## Features

- **Multiple Wave Types:**
  - Square Wave
  - Sawtooth Wave
  - Triangle Wave
  - Custom Functions
  - Piecewise Functions

- **Interactive Controls:**
  - Adjustable number of terms
  - Amplitude control
  - Custom period settings
  - Real-time updates

- **Visual Feedback:**
  - Side-by-side comparison of original function and Fourier approximation
  - Dynamic equation display
  - Interactive plotting

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lordofhash/fourier_simulator.git
   cd fourier_simulator
   ```

2. **Install required dependencies:**
   ```bash
   pip install numpy matplotlib tk
   ```

3. **Run the simulator:**
   ```bash
   python fouriersimulator[S&S].py
   ```

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- Tkinter (usually comes with Python)
  

## Usage

### Basic Usage

1. Launch the application:
   ```bash
   python fouriersimulator[S&S].py
   ```

2. Select a wave type from the dropdown menu
3. Adjust the number of terms and amplitude
4. Click "Update" to see the changes

### Custom Functions

1. Select "custom" from the wave type dropdown
2. Enter your function using Python/NumPy syntax
3. Set the period (in π units)
4. Examples:
   - `np.sin(2*x)`
   - `np.exp(-x**2)`
   - `x**2`

### Piecewise Functions

1. Select "piecewise" from the wave type dropdown
2. Add pieces using the "Add Piece" button
3. For each piece, specify:
   - The function (e.g., `x`)
   - The condition (e.g., `x < np.pi`)
4. Set the overall period

## Examples

### Square Wave
```python
Wave Type: square
Terms: 5
Amplitude: 1.0
```

### Custom Sine Wave
```python
Wave Type: custom
Function: np.sin(2*x)
Period: 2
Terms: 3
Amplitude: 1.0
```

### Piecewise Linear
```python
Wave Type: piecewise
Piece 1: x, x < np.pi
Piece 2: 2-x, x >= np.pi
Period: 2
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Acknowledgments

- Created by xX[S&S]Xx
- Built using Python's scientific computing libraries
- Inspired by the educational need for interactive Fourier series visualization

## Support

If you encounter any issues or have questions:
1. Check the existing issues or create a new one
2. Review the documentation
3. Contact the maintainers

## Roadmap

- [ ] Add more predefined wave types
- [ ] Implement 2D Fourier transforms
- [ ] Add animation features
- [ ] Include more educational resources
- [ ] Add export capabilities for graphs and equations

---
Made with ❤️ by xX[S&S]Xx

Creators - Shiven Vasan and Suryansh Vikram Singh Kushwaha


