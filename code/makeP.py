import numpy as np
import os

def makeP(n_layers, p_top, p_bottom, filename, log=True): 
    '''
    Make a logarithmic or linearly equi-spaced pressure array and store
    in filename.  It is called by BART_config.py.
  
    Parameters:
    -----------
    n_layers: Integer
       Number of layers in the atmosphere.
    p_top: Float
       Pressure at the top of the atmosphere (in bars).
    p_bottom: Float
       Pressure at the bottom of the atmopshere (in bars).
    filename: String
       Name of the file to be produced.
    log: Boolean
       If True, logarithmic sampling of the pressure range is choosen,
       else linear.

    Returns:
    --------
    None

    Developers:
    -----------
    Jasmina Blecic      jasmina@physics.ucf.edu
    Patricio Cubillos   pcubillos@fulbrightmail.org

    Revisions
    ---------
    2014-06-22  Jasmina   Initial version.
    2014-08-15  Patricio  Complemented doc-string and updated string formatting
    '''

    # Make logarithmic or linearly equispaced array:
    if log:
      pres = np.logspace(np.log10(p_top), np.log10(p_bottom), n_layers)   
    else:
      pres = np.linspace(p_top, p_bottom, n_layers)   

    # Header line:
    header = "Layer  P (bar)\n"

    # Open file to write:
    f = open(str(filename), 'w')
    f.write(header)

    # Write layer index number and pressure:
    for i in np.arange(n_layers):
      f.write("{:5d}  {:.4e}\n".format(i+1, pres[i]))
    f.close()

