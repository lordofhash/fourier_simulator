import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class FourierSeriesSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Fourier Series Simulator")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Controls
        controls_frame = ttk.Frame(main_frame)
        controls_frame.grid(row=0, column=0, pady=5)
        
        # Wave function selector
        ttk.Label(controls_frame, text="Wave Function:").grid(row=0, column=0, padx=5)
        self.wave_var = tk.StringVar(value="square")
        wave_menu = ttk.Combobox(controls_frame, textvariable=self.wave_var)
        wave_menu['values'] = ('square', 'sawtooth', 'triangle', 'custom', 'piecewise')
        wave_menu.grid(row=0, column=1, padx=5)
        wave_menu.bind('<<ComboboxSelected>>', self.on_wave_select)
        
        # Custom function frame
        self.custom_frame = ttk.LabelFrame(main_frame, text="Custom Function", padding="5")
        self.custom_frame.grid(row=1, column=0, pady=5, sticky=(tk.W, tk.E))
        self.custom_frame.grid_remove()  # Initially hidden
        
        # Custom function input
        ttk.Label(self.custom_frame, text="f(x) =").grid(row=0, column=0, padx=5)
        self.custom_func_var = tk.StringVar(value="np.sin(2*x)")
        custom_entry = ttk.Entry(self.custom_frame, textvariable=self.custom_func_var, width=40)
        custom_entry.grid(row=0, column=1, padx=5)
        
        ttk.Label(self.custom_frame, text="Period (in π units):").grid(row=0, column=2, padx=5)
        self.period_var = tk.StringVar(value="2")
        period_entry = ttk.Entry(self.custom_frame, textvariable=self.period_var, width=5)
        period_entry.grid(row=0, column=3, padx=5)





         # Piecewise function frame
        self.piecewise_frame = ttk.LabelFrame(main_frame, text="Piecewise Function", padding="5")
        self.piecewise_frame.grid(row=1, column=0, pady=5, sticky=(tk.W, tk.E))
        self.piecewise_frame.grid_remove()  # Initially hidden
        
        # Piecewise function entries
        self.piece_entries = []
        self.add_piece_button = ttk.Button(self.piecewise_frame, text="Add Piece", command=self.add_piece)
        self.add_piece_button.grid(row=0, column=0, padx=5, pady=5)
        
        ttk.Label(self.piecewise_frame, text="Period (in π units):").grid(row=0, column=1, padx=5)
        self.piecewise_period_var = tk.StringVar(value="2")
        piecewise_period_entry = ttk.Entry(self.piecewise_frame, textvariable=self.piecewise_period_var, width=5)
        piecewise_period_entry.grid(row=0, column=2, padx=5)





        
        # Help buttons
        help_button = ttk.Button(self.custom_frame, text="?", width=2, command=self.show_help)
        help_button.grid(row=0, column=4, padx=5)
        
        piecewise_help_button = ttk.Button(self.piecewise_frame, text="?", width=2, command=self.show_piecewise_help)
        piecewise_help_button.grid(row=0, column=3, padx=5)
        
        # Add initial piece
        self.add_piece()
        
        # Number of terms control
        ttk.Label(controls_frame, text="Number of Terms:").grid(row=0, column=2, padx=5)
        self.terms_var = tk.StringVar(value="5")
        terms_entry = ttk.Entry(controls_frame, textvariable=self.terms_var, width=5)
        terms_entry.grid(row=0, column=3, padx=5)
        
        # Amplitude control
        ttk.Label(controls_frame, text="Amplitude:").grid(row=0, column=4, padx=5)
        self.amplitude_var = tk.StringVar(value="1.0")
        amplitude_entry = ttk.Entry(controls_frame, textvariable=self.amplitude_var, width=5)
        amplitude_entry.grid(row=0, column=5, padx=5)

        
        
        # Update button
        update_button = ttk.Button(controls_frame, text="Update", command=self.update_plot)
        update_button.grid(row=0, column=6, padx=5)
        
        # Create figure and canvas for plotting
        self.fig = Figure(figsize=(8, 6))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=main_frame)
        self.canvas.get_tk_widget().grid(row=2, column=0, pady=5)
        
        # Equation label
        self.equation_var = tk.StringVar()
        equation_label = ttk.Label(main_frame, textvariable=self.equation_var, wraplength=600)
        equation_label.grid(row=3, column=0, pady=5)
        
        # Initial plot
        self.update_plot()





    
    def add_piece(self):
        """Add a new piece to the piecewise function."""
        index = len(self.piece_entries)
        frame = ttk.Frame(self.piecewise_frame)
        frame.grid(row=index+1, column=0, columnspan=4, pady=2, sticky='w')
        
        # Function entry
        ttk.Label(frame, text=f"f{index+1}(x) =").grid(row=0, column=0, padx=5)
        func_var = tk.StringVar(value="x")
        func_entry = ttk.Entry(frame, textvariable=func_var, width=20)
        func_entry.grid(row=0, column=1, padx=5)
        
        # Condition entry
        ttk.Label(frame, text="for").grid(row=0, column=2, padx=5)
        cond_var = tk.StringVar(value=f"x < {index+1}*np.pi")
        cond_entry = ttk.Entry(frame, textvariable=cond_var, width=20)
        cond_entry.grid(row=0, column=3, padx=5)
        
        # Remove button
        remove_button = ttk.Button(frame, text="×", width=2,
                                 command=lambda: self.remove_piece(frame))
        remove_button.grid(row=0, column=4, padx=5)
        
        self.piece_entries.append((frame, func_var, cond_var))
    
    def remove_piece(self, frame):
        """Remove a piece from the piecewise function."""
        if len(self.piece_entries) > 1:  # Keep at least one piece
            for i, (f, _, _) in enumerate(self.piece_entries):
                if f == frame:
                    self.piece_entries.pop(i)
                    frame.destroy()
                    break
    
    def show_help(self):
        help_text = """Custom Function Help:
        
1. Use numpy functions with 'np.' prefix:
   - np.sin(x), np.cos(x), np.exp(x)
   - np.sqrt(x), np.abs(x)
   
2. Example functions:
   - np.sin(2*x)
   - np.exp(-x**2)
   - x**2
   - np.where(x < np.pi, 1, -1)
   
3. Period should be in π units:
   - For functions like sin(x): period = 2
   - For custom periods, adjust accordingly
   
Variables available: x, np (numpy)

Made by xX[S&S]Xx"""
        messagebox.showinfo("Custom Function Help", help_text)
    
    def show_piecewise_help(self):
        help_text = """Piecewise Function Help:

1. Each piece consists of:
   - A function f(x)
   - A condition when to use it

2. Example:
   Function: x
   Condition: x < np.pi
   Function: 2*x
   Condition: x >= np.pi

3. Use numpy functions with 'np.' prefix
4. Conditions must use comparison operators
   (<, >, <=, >=, ==)
5. Last condition is used as default

Note: Ensure conditions cover the entire period
and functions connect smoothly.

Made by xX[S&S]Xx"""
        messagebox.showinfo("Piecewise Function Help", help_text)
    
    def on_wave_select(self, event=None):
        """Handle wave type selection."""
        wave_type = self.wave_var.get()
        self.custom_frame.grid_remove()
        self.piecewise_frame.grid_remove()
        
        if wave_type == 'custom':
            self.custom_frame.grid()
        elif wave_type == 'piecewise':
            self.piecewise_frame.grid()



            
    
    def square_wave(self, x, n, amplitude):
        """Generate square wave term."""
        return (4 * amplitude / (n * np.pi)) * np.sin(n * x)
    
    def sawtooth_wave(self, x, n, amplitude):
        """Generate sawtooth wave term."""
        return (2 * amplitude / (n * np.pi)) * np.sin(n * x)
    
    def triangle_wave(self, x, n, amplitude):
        """Generate triangle wave term."""
        return (8 * amplitude / (np.pi * np.pi * n * n)) * np.sin(n * x)
    
    def square_wave_original(self, x):
        """Generate original square wave."""
        return self.amplitude * np.where(np.sin(x) >= 0, 1, -1)
    
    def sawtooth_wave_original(self, x):
        """Generate original sawtooth wave."""
        return self.amplitude * ((x % (2 * np.pi)) / np.pi - 1)
    
    def triangle_wave_original(self, x):
        """Generate original triangle wave."""
        x = x % (2 * np.pi)
        return self.amplitude * (2 * abs(2 * (x - np.pi) / (2 * np.pi) - 1) - 1)

    def compute_fourier_coefficients(self, func, n, period):
        """Compute Fourier coefficients for custom function."""
        T = period * np.pi
        x = np.linspace(0, T, 1000)
        dx = x[1] - x[0]
        
        # Compute an (cosine) coefficient
        an = (2/T) * np.sum(func(x) * np.cos(2*np.pi*n*x/T)) * dx
        
        # Compute bn (sine) coefficient
        bn = (2/T) * np.sum(func(x) * np.sin(2*np.pi*n*x/T)) * dx
        
        return an, bn


    def generate_piecewise_function(self):
        """Generate a lambda function from piecewise entries."""
        pieces = []
        conditions = []
        
        # Build the piecewise function string
        for _, func_var, cond_var in self.piece_entries[:-1]:
            pieces.append(func_var.get())
            conditions.append(cond_var.get())
        
        # Add the last piece as default
        pieces.append(self.piece_entries[-1][1].get())
        
        # Build the nested where expression
        expr = pieces[-1]  # Start with the default case
        for piece, condition in zip(pieces[:-1][::-1], conditions[::-1]):
            expr = f"np.where({condition}, {piece}, {expr})"
        
        return lambda x: eval(expr)

    


    def generate_fourier_series(self, wave_function, terms, amplitude, x):
        """Generate Fourier series data points."""
        self.amplitude = amplitude
        y = np.zeros_like(x)
        
        if wave_function in ['custom', 'piecewise']:
            try:
                # Create function from string
                period = float(self.period_var.get() if wave_function == 'custom' 
                             else self.piecewise_period_var.get())
                
                if wave_function == 'custom':
                    custom_func = lambda x: eval(self.custom_func_var.get())
                else:
                    custom_func = self.generate_piecewise_function()
                
                # Compute Fourier coefficients and series
                a0 = np.mean(custom_func(x))
                y += a0
                
                for n in range(1, terms + 1):
                    an, bn = self.compute_fourier_coefficients(custom_func, n, period)
                    y += amplitude * (an * np.cos(2*np.pi*n*x/(period*np.pi)) + 
                                   bn * np.sin(2*np.pi*n*x/(period*np.pi)))
                
                # Plot original function for comparison
                self.ax.plot(x, custom_func(x), '--', alpha=0.5, label='Original')
                
            except Exception as e:
                messagebox.showerror("Error", f"Error in function: {str(e)}")
                return np.zeros_like(x)

        else:
            # Plot original function based on wave type
            if wave_function == 'square':
                original = self.square_wave_original(x)
                self.ax.plot(x, original, '--', alpha=0.5, label='Original')
                for n in range(1, terms + 1):
                    if n % 2 != 0:
                        y += self.square_wave(x, n, amplitude)
            elif wave_function == 'sawtooth':
                original = self.sawtooth_wave_original(x)
                self.ax.plot(x, original, '--', alpha=0.5, label='Original')
                for n in range(1, terms + 1):
                    y += self.sawtooth_wave(x, n, amplitude)
            elif wave_function == 'triangle':
                original = self.triangle_wave_original(x)
                self.ax.plot(x, original, '--', alpha=0.5, label='Original')
                for n in range(1, terms + 1):
                    if n % 2 != 0:
                        y += self.triangle_wave(x, n, amplitude)

            pass
        
        return y
    
    def generate_equation(self, wave_function, terms, amplitude):
        """Generate equation string."""
        if wave_function == 'custom':
            return f"f(x) = {self.custom_func_var.get()} (Original)\nFourier approximation with {terms} terms"
            
        equation = f"f(x) = {amplitude} × ("
        terms_added = 0
        
        for n in range(1, terms + 1):
            if wave_function == 'square':
                if n % 2 != 0:
                    equation += f"{' + ' if terms_added > 0 else ''}4/(({n}π)) × sin({n}x)"
                    terms_added += 1
            elif wave_function == 'sawtooth':
                equation += f"{' + ' if terms_added > 0 else ''}2/(({n}π)) × sin({n}x)"
                terms_added += 1
            elif wave_function == 'triangle':
                if n % 2 != 0:
                    equation += f"{' + ' if terms_added > 0 else ''}8/({n}²π²) × sin({n}x)"
                    terms_added += 1
        
        equation += ")"
        return equation
    
    def update_plot(self):
        """Update the plot with current parameters."""
        try:
            wave_function = self.wave_var.get()
            terms = int(self.terms_var.get())
            amplitude = float(self.amplitude_var.get())
            
            # Generate x values
            x = np.linspace(0, 2 * np.pi, 1000)
            
            # Generate y values
            self.ax.clear()
            y = self.generate_fourier_series(wave_function, terms, amplitude, x)
            
            # Update plot
            self.ax.plot(x, y, label='Fourier Series')
            self.ax.set_xlabel('x')
            self.ax.set_ylabel('f(x)')
            self.ax.set_title(f'Fourier Series: {wave_function.capitalize()} Wave')
            self.ax.grid(True)
            self.ax.legend()
            
            # Update equation
            equation = self.generate_equation(wave_function, terms, amplitude)
            self.equation_var.set(f"Equation: {equation}")
            
            # Refresh canvas
            self.canvas.draw()
            
        except ValueError:
            self.equation_var.set("Error: Please enter valid numbers for terms and amplitude")

def main():
    root = tk.Tk()
    app = FourierSeriesSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
