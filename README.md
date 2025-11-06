# Universe Expansion Simulation with CPL Parameterization

**Project Description:**
The geometry and evolution of the Universe is determined by a set of components, matter, radiation, dark energy and curvature. The equation of state parameter for dark energy (according to the currently accepted $\Lambda$-CDM model) is a constant of $w=-1$. However, it has been proposed that the equation of state parameter may vary with the scale factor of the Universe, $a(t)$, and hence with time. We intend to use the CPL parameterization (a certain description of a non-constant dark energy equation of state parameter) to model how the Universe would expand with such time-evolving dark energy. 

**Planned Directory Structure:**

Top level file: demo.py - Example of the project running

Subdirectory files:
1) visualization.py - Runs the visualizations which display the parameter sliders and resulting plots.
2) num_solver.py - Includes all of the numerical calculations needed for the simulation

**Steps to Complete Project**

1) Conceptualize the math and equations involved
2) Express the scale factor (or other functions that we intend to study) as a function of the equation of state parameter $w(z)$
3) Identify numerical methods to solve the resulting differential equation and solve using varying values of the $w(z)$
4) Plot solutions

**Member Contributions**
- Christa: 
- Sanskar: 
- Gautam: 
- Saurav: 

**Additional equations, references, and info:**

$\rho_i(a)=\rho_{i,0}a^{-3(1+w_i)}$

$\Omega(t) = \frac{\rho(t)}{\rho_c(t)}$, where $\rho_c(t)=\frac{3c^2 H(t)^2}{8\pi G}$ is the critical density of the universe at time t.

$\Omega_i(t) = \frac{\rho_i(t)}{\rho_c(t)}$

$\frac{\dot{a}}{a}=H_0\left[ \sum \left(\Omega_{i,0}a^{-3(1+w_i)}\right) + \frac{1-\Omega_0}{a^2}  \right]^{1/2}$

$\dot{a}=aH_0\left[ \frac{\Omega_{r,0}}{a^4} + \frac{\Omega_{m,0}}{a^3} + \Omega_{\Lambda,0} + \frac{1-\Omega_0}{a^2} \right]^{1/2}$ in $\Lambda$-CDM

Because in $\Lambda$-CDM, $w_{DE}=-1 \Rightarrow \Omega_{DE}(a)=\Omega_{DE,0}a^{-3(1+(-1))}=\Omega_{DE,0}$ constant

Now, we are using the CPL parameterization $w(a)=w_0+w_a(1-a)$. Which makes $\rho_{DE} = \rho_{DE,0}a^{-3(1 + w_0+w_a(1-a))} = \rho_{DE,0}a^{-3(1 + w_0+w_a)}e^{-3w_a(1-a)}$

$\dot{a}=aH_0\left[ \frac{\Omega_{r,0}}{a^4} + \frac{\Omega_{m,0}}{a^3} + \Omega_{DE,0}a^{-3(1 + w_0+w_a)}e^{-3w_a(1-a)} + \frac{1-\Omega_0}{a^2} \right]^{1/2}$ using CPL.
