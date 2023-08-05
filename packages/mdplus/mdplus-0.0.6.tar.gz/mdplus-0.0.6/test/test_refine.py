import mdtraj as mdt
import os
import numpy as np
import pytest
from mdplus import refinement
from mdplus.utils import rmsd

rootdir = os.path.dirname(os.path.abspath('__file__'))
ncfile = os.path.join(rootdir, 'examples/test.nc')
pdbfile = os.path.join(rootdir, 'examples/test.pdb')
pczfile = os.path.join(rootdir, 'examples/test.pcz')
pczfile_dm = os.path.join(rootdir, 'examples/test_dm.pcz')

@pytest.fixture(scope="module")
def traj():
    t =  mdt.load(ncfile, top=pdbfile)
    return t.atom_slice(t.topology.select('name CA')).xyz


def test_optimize_fit(traj):
    r = refinement.ENM()
    r.fit(traj)
    assert r.n_atoms == 58
    assert len(r.restraints) == 113

def test_optimize_transform(traj):
    r = refinement.ENM()
    r.fit(traj)
    ref = traj[0]
    crude = ref + (np.random.random(ref.shape) * 0.02) - 0.01 
    refined = r.transform(crude)

def test_fix_bumps():
    t = mdt.load(pdbfile)
    x = t.xyz[0]
    x2 = x + np.random.random((x.shape)) * 0.1 - 0.5
    x3 = refinement.fix_bumps(x2, 0.1, 0.15)

