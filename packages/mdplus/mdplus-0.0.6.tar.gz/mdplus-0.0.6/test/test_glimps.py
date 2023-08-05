import mdtraj as mdt
import os
import numpy as np
import pytest
from mdplus import multiscale
from mdplus.utils import rmsd

rootdir = os.path.dirname(os.path.abspath('__file__'))
ncfile = os.path.join(rootdir, 'examples/test.nc')
pdbfile = os.path.join(rootdir, 'examples/test.pdb')
pczfile = os.path.join(rootdir, 'examples/test.pcz')
pczfile_dm = os.path.join(rootdir, 'examples/test_dm.pcz')

@pytest.fixture(scope="module")
def cg_traj():
    t =  mdt.load(ncfile, top=pdbfile)
    return t.atom_slice(t.topology.select('name CA')).xyz

@pytest.fixture(scope="module")
def fg_traj():
    t = mdt.load(ncfile, top=pdbfile)
    return t.xyz

def test_fit(cg_traj, fg_traj):
    g = multiscale.Glimps()
    g.fit(cg_traj, fg_traj)

def test_fit_nopca(cg_traj, fg_traj):
    g = multiscale.Glimps(pca=False)
    g.fit(cg_traj, fg_traj)

def test_fit_norefine(cg_traj, fg_traj):
    g = multiscale.Glimps(refine=False)
    g.fit(cg_traj, fg_traj)

def test_fit_noshave(cg_traj, fg_traj):
    g = multiscale.Glimps(shave=False)
    g.fit(cg_traj, fg_traj)

def test_fit_transform(cg_traj, fg_traj):
    g = multiscale.Glimps()
    g.fit(cg_traj, fg_traj)
    ref = fg_traj[0]
    cg = cg_traj[0]
    assert len(cg.shape) == 2
    fg = g.transform(cg)
    assert len(fg.shape) == 2
    assert rmsd(ref, fg) < 0.2

def test_fit_transform_nopca(cg_traj, fg_traj):
    g = multiscale.Glimps(pca=False)
    g.fit(cg_traj, fg_traj)
    ref = fg_traj[0]
    cg = cg_traj[0]
    fg = g.transform(cg)
    assert len(fg.shape) == 2
    assert rmsd(ref, fg) < 0.2

def test_fit_transform_noshave(cg_traj, fg_traj):
    g = multiscale.Glimps(shave=False)
    g.fit(cg_traj, fg_traj)
    ref = fg_traj[0]
    cg = cg_traj[0]
    fg = g.transform(cg)
    assert len(fg.shape) == 2
    assert rmsd(ref, fg) < 0.2

def test_fit_transform_norefine(cg_traj, fg_traj):
    g = multiscale.Glimps(refine=False)
    g.fit(cg_traj, fg_traj)
    ref = fg_traj[0]
    cg = cg_traj[0]
    fg = g.transform(cg)
    assert len(fg.shape) == 2
    assert rmsd(ref, fg) < 0.2

def test_fit_inverse_transform(cg_traj, fg_traj):
    g = multiscale.Glimps()
    g.fit(cg_traj, fg_traj)
    cg = cg_traj[0]
    cg[:,0] += 10.0 # big x-shift
    fg = g.transform(cg)
    cg2 = g.inverse_transform(fg)
    assert rmsd(cg, cg2) < 0.1
    diff = cg - cg2
    assert np.abs(diff).max() < 0.03

def test_fit_inverse_transform_nopca(cg_traj, fg_traj):
    g = multiscale.Glimps(pca=False)
    g.fit(cg_traj, fg_traj)
    cg = cg_traj[0]
    cg[:,0] += 10.0 # big x-shift
    fg = g.transform(cg)
    cg2 = g.inverse_transform(fg)
    assert rmsd(cg, cg2) < 0.1
    diff = cg - cg2
    assert np.abs(diff).max() < 0.03

def test_fit_inverse_transform_norefine(cg_traj, fg_traj):
    g = multiscale.Glimps(refine=False)
    g.fit(cg_traj, fg_traj)
    cg = cg_traj[0]
    cg[:,0] += 10.0 # big x-shift
    fg = g.transform(cg)
    cg2 = g.inverse_transform(fg)
    assert rmsd(cg, cg2) < 0.1
    diff = cg - cg2
    assert np.abs(diff).max() < 0.03

def test_fit_inverse_transform_noshave(cg_traj, fg_traj):
    g = multiscale.Glimps(shave=False)
    g.fit(cg_traj, fg_traj)
    cg = cg_traj[0]
    cg[:,0] += 10.0 # big x-shift
    fg = g.transform(cg)
    cg2 = g.inverse_transform(fg)
    assert rmsd(cg, cg2) < 0.1
    diff = cg - cg2
    assert np.abs(diff).max() < 0.05

