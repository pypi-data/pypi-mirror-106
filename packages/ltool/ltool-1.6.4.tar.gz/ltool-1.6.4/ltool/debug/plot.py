#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:20:15 2021

@author: nick
"""

from matplotlib import pyplot as plt
import os
import pandas as pd
import numpy as np

def debug_layers(alt, sig, std, wct, geom, max_alt, snr_factor, prod_ulim, date, 
                 dir_out, dpi_val):
    
    # date = lid.time.values
    # i_d = str(lid.id.values)
    
    if not os.path.exists(dir_out):
        os.makedirs(dir_out)
    
    ulim_y = pd.Series([400., 200., 100., 20., 10., 5., 400., 400., 200., 100., 100., 20., 20., 10., 7., 7.], 
                       index = ['e355', 'e532', 'e1064', 'b355', 'b532', 'b1064', 
                                'e313', 'e351', 'e510', 'e694', 'e817', 'b313', 
                                'b351', 'b510', 'b694', 'b817'])
    
    if len(geom) > 0:
        bases = geom.sel(features = 'base').values
        tops = geom.sel(features = 'top').values
        coms = geom.sel(features = 'center_of_mass').values
    
    # Plots
    plt.figure
    plt.title(f'Product')
    plt.subplot(122)
    xlims = [0, prod_ulim]
    ylims = [0, max_alt]
    plt.title(f'Product')
    if len(geom) > 0:
        for i in range(geom.shape[0]):
            if geom.sel(features='residual_layer_flag').values[i] == 1:
                clrs = ['gray', 'black', 'grey']
            if geom.sel(features='residual_layer_flag').values[i] == 0:
                clrs = ['purple', 'cyan', 'purple']
            plt.plot(xlims, [bases[i], bases[i]], color = clrs[0])
            plt.plot(xlims, [tops[i], tops[i]], color =  clrs[1])
            plt.plot(xlims, [coms[i], coms[i]], '--', color = 'goldenrod')
            plt.axhspan(bases[i], tops[i], facecolor = clrs[2], alpha = 0.2)
    plt.plot(1e6*sig, alt)
    plt.axis(xlims + ylims)
    plt.xlabel('Aerosol Back. Coef. [$Mm^{-1} \cdot sr^{-1}$]')
    plt.ylabel('Altitude [m]')

    plt.subplot(121)
    xlims = [-0.1*prod_ulim, 0.1*prod_ulim]
    ylims = [0, max_alt]
    if len(geom) > 0:
        for i in range(geom.shape[0]):
            if geom.sel(features='residual_layer_flag').values[i] == 1:
                clrs = ['gray', 'black', 'grey']
            if geom.sel(features='residual_layer_flag').values[i] == 0:
                clrs = ['purple', 'cyan', 'purple']
            plt.plot(xlims, [bases[i], bases[i]], color = clrs[0])
            plt.plot(xlims, [tops[i], tops[i]], color =  clrs[1])
            plt.plot(xlims, [coms[i], coms[i]], '--', color = 'goldenrod')
            plt.axhspan(bases[i], tops[i], facecolor = clrs[2], alpha = 0.2)
    plt.plot( 1e6*wct, alt)
    plt.plot( snr_factor*std*1e6, alt, '--', color = 'darkgreen')
    plt.plot(-snr_factor*std*1e6, alt, '--', color = 'lightgreen')
    plt.axis(xlims + ylims)
    plt.xlabel('Wavelet Cov. Transform [$Mm^{-1} sr^{-1}$]')
    plt.ylabel('Altitude [m]')
    
    # ts = pd.to_datetime(str(date)) 
    # date_s = ts.strftime("%Y%m%d_%H%M%S")
    
    plt.tight_layout()
    plt.savefig(os.path.join(dir_out,f'{date}.png'),
                dpi = dpi_val)
    plt.close()
    
    return()