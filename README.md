# Universe Expansion Simulation with CPL Parameterization

**Project Description:**
The geometry and evolution of the Universe is determined by a set of components: matter, radiation, dark energy and curvature. The equation of state parameter for dark energy (according to the currently accepted $\Lambda$-CDM model) is a constant of $w_{DE}=-1$. However, it has been proposed that the equation of state parameter may vary with the scale factor of the Universe, $a(t)$, and hence with time. We intend to use the CPL parameterization (a certain description of a non-constant dark energy equation of state parameter) to model how the Universe would expand with such time-evolving dark energy. 

The Friedmann equation is the ODE that determines the time evolution of the scale factor $a(t)$ for a universe given certain values of the present energy densities of the universe's components $\Omega_m, \Omega_r, \Omega_{DE}$, and their equation of state parameters $w_m=0,w_r=\frac{1}{3},w_{DE}$. The CPL parameteriztion for $w_{DE}$ is given by $w_{DE}(a)=w_0+w_a(1-a)$ where $w_0$ and $w_a$ are some constant parameters.  

We will create a program which can solve a version of the Friedmann equation implementing the CPL parameterization given any specified values of the present density parameters $\Omega_m, \Omega_r, \Omega_{DE}$ and the CPL parameters $w_0$ and $w_a$, and make plots of the scale factor $a(t)$ and Hubble parameter (expansion rate) $H(z)=\frac{\dot{a}}{a}$ as functions of time. 

We will investigate how the end-time behavior of the universe changes as we vary the parameters of the Friedmann equation, particularly the CPL parameters $w_0,w_a$ which model the nature of dark energy. We will attempt to map out the $w_a,w_0$ phase space into regions where the universe would expand indefinitely over infinite time ("Big Chill" or "Heat Death"), where the universe would collapse back to a point in finite time ("Big Crunch"), where the universe's scale factor would blow up to infinity in finite time ("Big Rip") and any other behaviors we may observe.   

We will also compare the performance of using a standard vs an implicit ODE solver for this equation.   

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
5) Perform parameter sweeps and explore the impacts on the solution behavior.

**Member Contributions**
- Christa: Visualization of simulation results (plots, sliders, maps, etc)
- Sanskar: Creating functions for equations needed to solve/aid in solving
- Gautam: Produce solutions of main differential equation
- Saurav: Implement variation of values of $w(z)$ to find range of diffeq solutions.

**Additional equations, references, and info:**

The energy density of a component of the universe as a function of scale factor is $\rho_i(a)=\rho_{i,0}a^{-3(1+w_i)}$ where $w_i$ is the equation of state parameter for that component. The total energy density of the universe $\rho(a) = \sum_i \rho_i(a)$

The total density parameter $\Omega(t) = \frac{\rho(t)}{\rho_c(t)}$, where $\rho_c(t)=\frac{3c^2 H(t)^2}{8\pi G}$ is the critical density of the universe at time t.

The density parameter of a component $\Omega_i(t) = \frac{\rho_i(t)}{\rho_c(t)}$

$H=\frac{\dot{a}}{a}=H_0\left[ \sum \left(\Omega_{i,0}a^{-3(1+w_i)}\right) + \frac{1-\Omega_0}{a^2}  \right]^{1/2}$ is the Friedmann equation. 
$H_0$ is the Hubble constant i.e. the modern-day expansion rate.

So,
$\dot{a}=aH_0\left[ \frac{\Omega_{r,0}}{a^4} + \frac{\Omega_{m,0}}{a^3} + \Omega_{\Lambda,0} + \frac{1-\Omega_0}{a^2} \right]^{1/2}$ in $\Lambda$-CDM

Because in $\Lambda$-CDM, $w_{DE}=-1 \Rightarrow \Omega_{DE}(a)=\Omega_{DE,0}a^{-3(1+(-1))}=\Omega_{DE,0}$ constant


Now, we are using the CPL parameterization $w(a)=w_0+w_a(1-a)$. Which makes $\rho_{DE} = \rho_{DE,0}a^{-3(1 + w_0+w_a(1-a))} = \rho_{DE,0}a^{-3(1 + w_0+w_a)}e^{-3w_a(1-a)}$

$\dot{a}=aH_0\left[ \frac{\Omega_{r,0}}{a^4} + \frac{\Omega_{m,0}}{a^3} + \Omega_{DE,0}a^{-3(1 + w_0+w_a)}e^{-3w_a(1-a)} + \frac{1-\Omega_0}{a^2} \right]^{1/2}$ using CPL.
