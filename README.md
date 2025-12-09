# Universe Expansion Simulation with CPL Parameterization

**Project Description:**
The geometry and evolution of the Universe is determined by a set of components: matter, radiation, dark energy and curvature. The equation of state parameter for dark energy (according to the currently accepted $\Lambda$-CDM model) is a constant of $w_{DE}=-1$. However, it has been proposed that the equation of state parameter may vary with the scale factor of the Universe, $a(t)$, and hence with time. We intend to use the CPL parameterization (a certain description of a non-constant dark energy equation of state parameter) to model how the Universe would expand with such time-evolving dark energy. 

The Friedmann equation is the ODE that determines the time evolution of the scale factor $a(t)$ for a universe given certain values of the present energy densities of the universe's components $\Omega_m, \Omega_r, \Omega_{DE}$, and their equation of state parameters $w_m=0,w_r=\frac{1}{3},w_{DE}$. The CPL parameteriztion for $w_{DE}$ is given by $w_{DE}(a)=w_0+w_a(1-a)$ where $w_0$ and $w_a$ are some constant parameters.  

We will create a program which can solve a version of the Friedmann equation implementing the CPL parameterization given any specified values of the present density parameters $\Omega_m, \Omega_r, \Omega_{DE}$ and the CPL parameters $w_0$ and $w_a$, and make plots of the scale factor $a(t)$ and Hubble parameter (expansion rate) $H(t)=\frac{\dot{a}}{a}$ (among others) as functions of time. 

We will investigate how the end-time behavior of the universe changes as we vary the parameters of the Friedmann equation, particularly the CPL parameters $w_0,w_a$ which model the nature of dark energy. We will attempt to map out the $w_a,w_0$ phase space into regions where the universe would expand indefinitely over infinite time ("Big Chill" or "Heat Death"), where the universe would collapse back to a point in finite time ("Big Crunch"), where the universe's scale factor would blow up to infinity in finite time ("Big Rip") and any other behaviors we may observe. <-- We should probably remove this.

We will also compare the performance of using a standard vs an implicit ODE solver for this equation.   

**Directory Structure:**
Everything required to run the program is in the top-level directory. 
- Demo.ipynb: Example of the project running. Interactive visualizer allowing user to explore CPL parameter space and visualize the resulting cosmic dynamics as per the Friedmann Equation.
- FriedmannEquationCPL.py: Defines FriedmannEquationCPL class which contains parameters and setup for model universe, as well as solvers for the Friedmann Equation and universe age. To be called in Demo.ipynb to create visualizations from the solutions.

## Scientific Background

### History
In the 1920s, Edwin Hubble observed the light from numerous distant galaxies and found that they were all redshifted away from us, and further galaxies appeared to be moving faster. The conclusion was that every single galaxy was moving away from every other galaxy, regardless of location. This observation implies that the Universe must be expanding.

More recent observations regarding the CMB, supernovae, and the distribution of galaxy clusters has shown that the expansion rate has not been uniform over time - in the early universe, it was slowing down, but today it is accelerating.

Now, the latest experiments are starting to show hints that even the nature of this acceleration - modelled as dark energy - is not constant in time either.  

![](https://newscenter.lbl.gov/wp-content/uploads/2025/03/Newscenter_featured_1190px_DESI_BAO_iotw2025a.jpg)

### Theory
Expansion depends on the energy content of the Universe, described by the total energy density $\rho$. This total can be broken into constituent parts $\rho_i$ based on the components of the Universe - radiation, matter, and dark energy. (Note that matter contains DM and baryonic).

How these components contribute to the universe's expansion is described by the Friedmann Equation:

$\frac{\dot{a}}{a}=H_0\left[ \sum \left(\Omega_{i,0}\frac{\rho_i}{\rho_{i,0}}\right) + \frac{1-\Omega_0}{a^2}  \right]^{1/2}$

The variable 'a' is the scale factor, which describes the size of the Universe. Conventionally, we let a = 1 today. If two galaxies are a distance $r$ apart today $t=t_0$, they were a distance $a(t)r$ at a different time.

In general, the '0' subscript refers to the value of a quantity today. The $\Omega$ variables are known as density parameters - they dimensionlessly represent energy density quantities. $\Omega_{i,0}=\frac{\rho_{i,0}}{\rho_{c,0}}$, where $\rho_{c,0}$ is the total energy density the universe would need today for it to have zero net curvature (flat).

![](https://vickyscowcroft.github.io/PH40112_rmd/Images/compo-pie-chart.jpg)

The universe's expansion in turn affects the components' density, according to the fluid equation

$\frac{d\rho_i}{\rho_i}=-3(1+w_i)\frac{da}{a}$

As we can see, the equation accounts for the domination of different components of the Universe as 'a' varies, which explains the variation of the expansion rate. The equation of state parameter, $w=P/\rho$, tells us how 'repulsive' the component is, and conventionally ($\Lambda$CDM) these values are taken to be

$w_m = 0$, $w_r = 1/3$, and $w_{DE} = -1$.


---


Solving the fluid equation with these values gives us that

$\rho_m=\rho_{m,0}a^{-3}$

$\rho_r=\rho_{r,0}a^{-4}$

$\rho_{DE}=\rho_{DE,0}$ constant.


---


So, we can obtain the completed Friedmann equation.

$\dot{a}=aH_0\left[ \frac{\Omega_{r,0}}{a^4} + \frac{\Omega_{m,0}}{a^3} + \Omega_{\Lambda,0} + \frac{1-\Omega_0}{a^2} \right]^{1/2}$

The dominant factor today is dark energy. The idea that $w_{DE} = -1$ comes from Einstein's cosmological constant, a factor that simply 'makes everything work'. However, this isn't an observationally determined value. Our project proposes that this value is in fact inaccurate, and instead the true nature of dark energy varies with time.


---


The Chevallier–Polarski–Linder (CPL) Parameterization is a common method of representing a time-varying equation of state parameter, as follows:

$w(a)=w_0​+w_a​(1−a)$

where $w_0$ is the value of the parameter today, and $w_a$ is a constant controlling how the overall parameter varies with time (or in this case, scale factor, which is analogous).


---


Substituting this intto the fluid equation, we can find that the density of this variable dark energy would change with scale factor as:

$\rho_{DE} = \rho_{DE,0}a^{-3(1 + w_0+w_a)}e^{-3w_a(1-a)}$

So, our Friedmann Equation describing the evolution of the universe with time-varying dark energy as described by CPL is

$\dot{a}=aH_0\left[ \frac{\Omega_{r,0}}{a^4} + \frac{\Omega_{m,0}}{a^3} + \Omega_{DE,0}a^{-3(1 + w_0+w_a)}e^{-3w_a(1-a)} + \frac{1-\Omega_0}{a^2} \right]^{1/2}$


### Summary

If dark energy changes over time, even slightly, it affects the expansion rate of the universe at different stages of its history. The CPL model introduces two parameters, $w_0$ and $w_a$, which control the behavior of dark energy. The value $w_0$ sets the strength of dark energy today, so changing $w_0$ shifts the current expansion rate and the predicted distances to nearby supernovae and galaxies. The parameter $w_a$ describes how dark energy evolves with time. Even small changes in $w_a$ modify the expansion rate in the early and mid-Universe and influence how large-scale structures grow. Because modern observations measure distances and growth rates with very high precision, variations in either $w_0$ or $w_a$ can leave detectable signatures. This is why studying a time-varying form of dark energy in the CPL framework is important.

![Probable values of w_0 and w_a from DESI Data Release 2 results](https://newscenter.lbl.gov/wp-content/uploads/2025/03/1389px_DR2-cosmo-christhian-890x665.jpg)

Understanding the nature of dark energy is important in many ways - it can tell us the age of the universe, the timing of domination between radiation, matter, and dark energy in our universe's history, and help us predict how our universe will end up.

In this project, we explore how changing the values of $w_0$ and $w_a$ affects the universe’s expansion. We write a program that solves the Friedmann equation numerically to find how the scale factor $a(t)$ evolves for any choice of parameters. We create an interactive visualization allowing us to easily adjust $w_0$ and $w_a$ and immediately see the change in the universe's age, universe's expansion and the component densities' evolution. We also compute important moments in cosmic history, such as when radiation and matter become equal in energy density and when matter and dark energy became equal. By scanning over many combinations of $w_0$ and $w_a$, we create a heatmap that shows how the predicted age of the Universe depends on these parameters.
