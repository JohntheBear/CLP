#! /usr/bin/env python

# Part of CLP
# A universal command line plotting script
#
# John Novak

# This sub-file just holds a global dictionary

# written for Python 2.6. Requires Scipy, Numpy, and Matplotlib

dic = {'formats': [],
       'outputs': [],
       'TYPE': 'pdf',
       'MULTIT': None,
       'MULTIP': None,
       'layout': None,
       'columnsfirst': False,
       'Ucolor': [],
       'Ustyle': [],
       'Messy': False,
       'remnants': [],
       'remnanterrors': [],
       'x_range': None,
       'y_range': None,
       'x_label': None,
       'y_label': None,
       'x_log': False,
       'y_log': False,
       'currentfile': None,
       'numbered': None,
       'Numbering': None,
       'multicounttile': 0,
       'multicountpile': 0,
       'currentoutput': None,
       'files': [],
       'legend': False,
       'labels': [],
       'columnlabel': [],
       'currentstruct': 0,
       'colorstyle': [],
       'errorbands': False,
       'fontsize': 20,
       'grid': False,
       'sys_err_default': 0,
       'default_marker_size': 5,
       'sys_err': 0,
       'plot_sys_err': False,
       'yscaled': 1,
       'xscaled': 1,
       'alpha': 0.25,
       'norm': False,
       'EmbedData': True}


if __name__ == '__main__':
    print "This code is part of CLP"
