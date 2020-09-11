import numpy as np
from scipy.special import iv

def bunch_length_m_to_rad(L, clight, f_RF):
    phi = L*(2*np.pi*f_RF)/clight
    return phi

def cmpt_bunch_length_correction_factor(sigma_phi, noise_type):
    '''
    This function computes the correction factor, C, due to the bunch length, sigma_phi, assuming a 2D gaussian longitudinal distribution.
    - phase_noise = True (False): computes C for phase (amplitude) noise case
    - sigma_phi: in radians at the CC frequency
    
    - Io, I2l: Modified Bessel functions of the first kind. 
    - I2l: It converges to zero for larger orders. Therefore, a summation up to a large integer, here 10000 is used,  gives us trustworthy resutls.
    
    Note: Possibility to compute the factors for a pillbox distribution which is the other extreme (email from Themis). 
    '''

    if noise_type == 'PN':
        Io = iv(0, sigma_phi**2) # The first argument is the order
        I2l_sum = 0
        for order in range(2, 10000, 2):
            I2l_sum = I2l_sum + iv(order, sigma_phi**2)
         
        C = np.exp(-sigma_phi**2)*(Io+2*I2l_sum)
        
    if noise_type == 'AN':
        I2ll_sum = 0
        for order in range(0, 10000, 2):
            I2ll_sum = I2ll_sum + iv(order+1, sigma_phi**2)
        
        C = np.exp(-sigma_phi**2)*I2ll_sum
        
    return C

def emit_growth_phase_noise(betay, Vcc, frev, Eb, CDeltaPhi, PSD_phi):
    ey_rate = betay*(Vcc*frev/(2*Eb))**2*CDeltaPhi*PSD_phi
    return 2*ey_rate # the factor of 2 corresponds to the number of betatron sidebands we "see"

def emit_growth_amplitude_noise(betay, Vcc, frev, Eb, CDeltaA, PSD_A):
    ey_rate = betay*(Vcc*frev/(2*Eb))**2*CDeltaA*PSD_A
    return 4*ey_rate # the factor of 4 corresponds to the number of betatron and synchrobetatron sidebands we "see"

