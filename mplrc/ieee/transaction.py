#       transaction.py
#       
#       Copyright 2011 alex arsenovic <arsenovic@virginia.edu>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#

import matplotlib.pyplot as plt


params ={\
    'backend': 'GTKAgg',
    
    'font.family': 'serif',
    'font.serif': ['Times', 'Palatino', 'New Century Schoolbook', 'Bookman', 'Computer Modern Roman'],
    'font.sans-serif' : ['Helvetica', 'Avant Garde', 'Computer Modern Sans serif'],
#font.cursive       : Zapf Chancery
#font.monospace     : Courier, Computer Modern Typewriter
    'text.usetex': True,
    
    'axes.labelsize': 9,
    'axes.linewidth': .75,
    
    'figure.figsize': (3.5, 2.5),
    'figure.subplot.left' : 0.175,
    'figure.subplot.right': 0.95,
    'figure.subplot.bottom': 0.15,
    'figure.subplot.top': .95,
    
    'figure.dpi':150,
    
    'text.fontsize': 9,
    'legend.fontsize': 7,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    
    'lines.linewidth':.75,
    'savefig.dpi':600,
    }

plt.rcParams.update(params)
