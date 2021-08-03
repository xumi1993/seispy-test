#!/bin/bash

wget https://osf.io/dxcfz/download -O ex-prf.tar.gz
tar -xzf ex-prf.tar.gz
cd ex-prf

# TRZ, iter, crust, 0.2
setpar rf.cfg decon decon_method iter
setpar rf.cfg save criterion crust
setpar rf.cfg save rmsgate 0.2
prf rf.cfg

# TRZ, water, crust, 
setpar rf.cfg decon decon_method water
setpar rf.cfg save criterion crust
setpar rf.cfg save rmsgate ""
prf rf.cfg

# LQT, iter, , 0.2
setpar rf.cfg rotation comp lqt
setpar rf.cfg decon decon_method iter
setpar rf.cfg save criterion ""
setpar rf.cfg save rmsgate 0.2
prf rf.cfg

# LQT, water, ,
setpar rf.cfg rotation comp lqt
setpar rf.cfg decon decon_method water
setpar rf.cfg save criterion ""
setpar rf.cfg save rmsgate ""
prf rf.cfg

# Hk stacking
hk hk.cfg

cd ..