# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:18:06 2022

@author: Manuela
"""

# Parameters for normal distributions
import scipy.stats as stats
params = [(0,0.2,'blue'), (0, 1.0, 'red'), (0, 5.0, 'orange'), (-2,0.5,'green')]

for mean, variance, color in params:
    x = np.linspace(mean - 3*math.sqrt(variance), mean + 3*math.sqrt(variance), 100)
    sigma = math.sqrt(variance)
    label = '$\mu = %.1f, \ \sigma^2=%.1f$' %(mean, variance)
    y_norm = stats.norm.pdf(x, mean, sigma)
    plt.plot(x, y_norm, label=label, c = color)
plt.xlim(-5,5)
plt.ylim(0,1)
plt.xlabel('X')
plt.ylabel('$φ_{μ,σ^2}(X)$')
plt.title('Distribución Normal')
plt.legend(title = "Parámetros")
plt.show()
