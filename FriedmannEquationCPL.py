import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class FriedmannEquationCPL:
  """
  Base class describing a model universe using the FLRW metric for specified values of the density parameters and the CPL parameters and containing methods to solve the Friedmann equation for said universe and calculate its age. 

  Parameters:
    Omega_m0 (float): Current-day matter density parameter
    Omega_r0 (float): Current-day radiation density parameter
    Omega_DE0 (float): Current-day dark energy density parameter
    H_0 (float): Current-day Hubble parameter (Hubble's Constant)
    w_0 (float): Current-day dark energy equation of state parameter,first CPL parameter
    w_a (float): Second CPL parameter, negative of the slope of dark energy equation of state parameter as a function of scale factor  

  """
  def __init__(self, Omega_m0=0.31, Omega_r0=9e-5, Omega_DE0=0.685, H_0=67.4, w_0=-1, w_a=0):
    self.Omega_m0 = Omega_m0     # dimensionless
    self.Omega_r0 = Omega_r0     # dimensionless
    self.Omega_DE0 = Omega_DE0   # dimensionless
    self.H_0 = H_0               # km/s/Mpc
    self.w_0 = w_0               # dimensionless
    self.w_a = w_a               # dimensionless

    # 1 km/s/Mpc = 0.00102270 Gyr^-1
    # [H_0] km/s/Mpc = [H_0] * 0.00102270 Gyr^-1
    self.H_0 *= 0.00102270
    # With H_0 implicitly in units of Gyr^-1, our time values will implicitly be in units Gyr.

    self.Omega_0 = self.Omega_m0 + self.Omega_r0 + self.Omega_DE0

  def rhs(self, t, a):
    """
    rhs (da / dt) expression used by solve_ivp.
    """
    r_term = self.Omega_r0 / (a**4)
    m_term = self.Omega_m0 / (a**3)

    # w_DE = self.w_0 + self.w_a*(1-a)
    # DE_term = self.Omega_DE0 / (a**(3 * (1+w_DE))) # --> rho = rho_0 a^{-3(1 + w)} is ONLY true for CONSTANT w. It comes generally from fluid equation.

    DE_term = self.Omega_DE0 * (a**(-3*(1+self.w_0+self.w_a))) * np.exp(-3*self.w_a*(1-a))  # By solving fluid eqn, desi paper

    k_term = (1 - self.Omega_0) / (a**2)

    return a * self.H_0 * np.sqrt(r_term + m_term + DE_term + k_term)

  def rhs_jac(self, t, a):
    """
    Jacobian callable for implicit integration methods. 
    """
    r_term = self.Omega_r0 / (a**4)
    m_term = self.Omega_m0 / (a**3)
    DE_term = self.Omega_DE0 * (a**(-3*(1+self.w_0+self.w_a))) * np.exp(-3*self.w_a*(1-a))  # By solving fluid eqn, see desi paper
    k_term = (1 - self.Omega_0) / (a**2)
    sqrt_factor = np.sqrt(r_term + m_term + DE_term + k_term)

    dr_term_da = -4*self.Omega_r0 / (a**5)
    dm_term_da = -3*self.Omega_m0 / (a**4)
    dDE_term_da = self.Omega_DE0 * ( ( -3*(1+self.w_0+self.w_a)*(a**(-4 - 3*(self.w_0+self.w_a))) * np.exp(-3*self.w_a*(1-a)) ) + ( (a**(-3*(1+self.w_0+self.w_a))) * 3*self.w_a*np.exp(-3*self.w_a*(1-a)) ) )
    dk_term_da = -2*(1 - self.Omega_0) / (a**3)

    prod_rule_term1 = self.H_0 * sqrt_factor
    prod_rule_term2 = a * self.H_0 * (1/(2*sqrt_factor)) * ( dr_term_da + dm_term_da + dDE_term_da + dk_term_da )

    return np.array([prod_rule_term1 * prod_rule_term2])

  def solve(self, t_min=0, t_max=1, nt=1000, method="RK45"):
    """
    Solve the Friedmann equation for the defined model universe

    Parameters:
      t_min (float): time in Gyr to start solution from 
      t_max (float): time in Gyr to end solution at
      nt (float): approximate number of timepoints to calculate solution at
      method (string): method used by solve_ivp to integrate the equation.  

    Returns:
      tpts (np.array[float]): 1D array with all timepoints [Gyr] where solution was found 
      apts (np.array[float]): 1D array with scale factor values for each time listed in tpts (solution) 

    """
    assert t_max > t_min
    # a_0 = 1

    a_almost_zero = lambda t, a: a
    a_almost_zero.terminal = True

    if t_min >= 0:
      tpts = np.linspace(0, t_max, int((t_max / (t_max - t_min))*nt))
      soln = solve_ivp(self.rhs, (0, t_max), np.array([1]), t_eval=tpts, method=method, events=a_almost_zero, jac=self.rhs_jac)

      a_pts_to_return = soln.y[0]
      tpts = tpts[:len(a_pts_to_return)]

      a_pts_to_return = a_pts_to_return[tpts>=t_min]
      return tpts[tpts>=t_min], a_pts_to_return

    elif t_max <= 0:
      tpts = np.linspace(0, t_min, int((np.abs(t_min) / (t_max - t_min))*nt))
      soln = solve_ivp(self.rhs, (0, t_min), np.array([1]), t_eval=tpts, method=method, events=a_almost_zero, jac=self.rhs_jac)

      a_pts_to_return = soln.y[0]
      tpts = tpts[:len(a_pts_to_return)]

      a_pts_to_return = a_pts_to_return[tpts<=t_max]
      return tpts[tpts<=t_max], a_pts_to_return

    else:
      tpts1 = np.linspace(0, t_min, int((np.abs(t_min) / (t_max-t_min))*nt))    #1D array
      tpts2 = np.linspace(0, t_max, int((t_max / (t_max-t_min))*nt))

      soln1 = solve_ivp(self.rhs, (0, t_min), np.array([1]), t_eval=tpts1, method=method, events=a_almost_zero, jac=self.rhs_jac)
      a_pts_to_return1 = soln1.y[0]
      tpts1 = tpts1[:len(a_pts_to_return1)]

      soln2 = solve_ivp(self.rhs, (0, t_max), np.array([1]), t_eval=tpts2, method=method, events=a_almost_zero, jac=self.rhs_jac)
      a_pts_to_return2 = soln2.y[0]
      tpts2 = tpts2[:len(a_pts_to_return2)]

      a_pts_to_return = np.concatenate((a_pts_to_return1[::-1], a_pts_to_return2[1:]))
      return np.concatenate((tpts1[::-1], tpts2[1:])), a_pts_to_return

  def find_universe_age(self, method="RK45"):
    """
    Calculates the age of the model universe from present-day. 

    Parameters:
      method (string): method used by solve_ivp to integrate the Friedmann equation.  

    Returns:
      t (float): age of the model universe in Gyr.

    """
    t, a = self.solve(t_min=-50, t_max=0, nt=100000)
    return -t[-1]
