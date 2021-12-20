import os
from seispy.rf import RF
from subprocess import Popen
import pytest
from os.path import exists



def test_download():
    if exists('ex-prf.tar.gz'):
        pytest.skip('Data are downloaded.')
    s = 'wget https://osf.io/dxcfz/download -O ex-prf.tar.gz\n'
    s += 'tar -xzf ex-prf.tar.gz\n'
    proc = Popen(s, shell=True)
    proc.communicate()

def init_RF():
    rf = RF(phase='P', cfg_file='ex-prf/rf.cfg')
    rf.para.datapath = 'ex-prf/Data.CB.NJ2'
    rf.load_stainfo()
    rf.search_eq()
    rf.match_eq()
    rf.detrend()
    rf.filter()
    rf.cal_phase()
    rf.drop_eq_snr()
    return rf
    
def test_sub01():
    rf = init_RF()
    rf.para.decon_method = 'iter'
    rf.para.criterion = 'crust'
    rf.para.rmsgate = 0.2
    rf.rotate()
    rf.trim()
    rf.deconv()
    rf.saverf()

def test_sub02():
    rf = init_RF()
    rf.para.decon_method = 'water'
    rf.para.criterion = 'crust'
    rf.para.rmsgate = None
    rf.rotate()
    rf.trim()
    rf.deconv()
    rf.saverf()

def test_sub03():
    rf = init_RF()
    rf.para.comp = 'lqt'
    rf.para.decon_method = 'water'
    rf.para.criterion = None
    rf.para.rmsgate = None
    rf.rotate()
    rf.trim()
    rf.deconv()
    rf.saverf()
