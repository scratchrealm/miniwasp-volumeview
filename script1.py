import os
import math
import fmm3dpy
import numpy as np
import mwaspbie as mw
import kachery_client as kc

def main():
    populate_data()

    # Define various components of the geometry and problem 
    # specification
    #

    # 
    # Refinement level of geometry used
    # iref should be 0 or 1
    iref = 0

    #
    #  iomegafrac is a paramater
    #  that defines the wavelength in the
    #  simulation
    #  
    #  omega = 2*pi/(600)/iomegafrac
    #
    #  Currently supported values are 1 and 3
    #
    #
    iomegafrac = 1

    omega = math.pi*2.0/600.0/(iomegafrac+0.0)

    #
    # icase = 2. Denotes the fact that 
    # we are solving a scattering problem 
    # and not an analytic test
    #
    icase = 2

    #
    # idir. Flag for determining 
    # what the direction of the incident field was
    #
    # currently supported value idir = 1
    # for which the incident field is along 
    # smallest principal component of the rhabdom for which
    # direction[0:1] = []
    # 
    #
    #
    idir = 1
    direction = np.zeros(2)
    if (idir == 1):
        direction[0] = -1.530844785708483 
        direction[1] = 1.063728846738649 


    #
    #
    #  ipol. Flag for determining the in plane
    #  polarization directions.
    #  Options for ipol = 1 or 2. 
    #
    #  Currenltly simulations only complete for
    #  ipol = 1
    #
    ipol = 1
    pol = np.zeros(2,dtype='complex')
    if (ipol == 1):
        pol[0] = 1.0

    if (ipol == 2):
        pol[1] = 1.0
    
    # Define geometry and number of components
    string1 = f'data/lens_r0{iref}.go3?data/con_r0{iref}.go3?data/rhabdom_r0{iref}.go3?'

    # string2 = f'{test_data_dir}/geometries/lens_r0'+str(iref)+'.msh?'
    # string2 = string2+f'{test_data_dir}/geometries/con_r0'+str(iref)+'.msh?'
    # string2 = string2+f'{test_data_dir}/geometries/rhabdom_r0'+str(iref)+'.msh?'

    n_components = 3

    fsol = f'data/soln_iref{iref}_iomega{iomegafrac}_icase{icase}_idir{idir}_ipol{ipol}.dat'
    ftarg = f'data/targ_iref{iref}_iomega{iomegafrac}_icase{icase}_idir{idir}_ipol{ipol}.dat'

    # compute number of patches and points
    print('Compute number of patches and points')
    print(string1)
    npatches,npts = mw.em_solver_wrap_mem(string1,n_components)
    print('.')

    # Set translation and scaling of each component
    dP = np.zeros((4,n_components),order="F")
    dP[3,:] = 1.0

    # set wave number of problem, should be consistent with
    # the units of prescribed geometry

    # set material parameters on either side of each component
    contrast_matrix = np.ones((4,n_components),order="F",dtype="complex")
    contrast_matrix[2,0] = 1.452
    contrast_matrix[2,1] = 1.348
    contrast_matrix[2,2] = 1.363

    # set tolerance for quadrature
    eps = 1.0e-3

    # read solution
    xsol = np.loadtxt(fsol)
    soln = xsol[:,0] + 1j*xsol[:,1]

    # Get geometry info
    print('Get geometry info')
    [npatches_vect,npts_vect,norders,ixyzs,iptype,srcvals,srccoefs,wts,
    sorted_vector,exposed_surfaces] = mw.em_solver_open_geom(string1,dP,npatches,
    npts,eps)

    #
    #  Set points per wavelength in each direction 
    #  for target grid
    #
    ppw = 2


    #
    # create target grid
    #

    xmin = np.min(srcvals[0,:])
    xmax = np.max(srcvals[0,:])

    ymin = np.min(srcvals[1,:])
    ymax = np.max(srcvals[1,:])

    zmin = np.min(srcvals[2,:])
    zmax = np.max(srcvals[2,:])

    dx = xmax-xmin
    dy = ymax-ymin
    dz = zmax-zmin

    # determine grid spacing to get the correct 
    # resolution in each dimension of target grid
    nx = int(np.ceil((xmax-xmin)*omega/2/np.pi*ppw))
    ny = int(np.ceil((ymax-ymin)*omega/2/np.pi*ppw))
    nz = int(np.ceil((zmax-zmin)*omega/2/np.pi*ppw))

    print(f'(nx, ny, nz) = ({nx}, {ny}, {nz})')

    xs = np.linspace(xmin+0.1*dx,xmax-0.1*dx,nx)
    ys = np.linspace(ymin+0.1*dy,ymax-0.1*dy,ny)
    zs = np.linspace(zmin+0.1*dz,zmax-0.1*dz,nz)
    xx,yy,zz = np.meshgrid(xs,ys,zs, indexing='ij')

    nt = nx*ny*nz
    targs = np.zeros((3,nt),order="F")
    targs[0,:] = xx.reshape(nt)
    targs[1,:] = yy.reshape(nt)
    targs[2,:] = zz.reshape(nt) 

    #
    # Compute fields at targets using computed surface currents
    #
    E,H = mw.em_solver_wrap_postproc(string1,dP,contrast_matrix,omega,eps,soln,targs)

    uri = kc.store_pkl({
        'Nx': nx,
        'Ny': ny,
        'Nz': nz,
        'dx': dx,
        'dy': dy,
        'dz': dz,
        'x0': xmin,
        'y0': ymin,
        'z0': zmin,
        'E': E.reshape((3, nx, ny, nz)),
        'H': H.reshape((3, nx, ny, nz))
    })
    print(uri)
    # output: sha1://1c71f894e606262dc3cadaef036fc9e94a8337b6/file.pkl

def populate_data():
    if os.path.exists('data'):
        print('NOTE: Directory already exists: data')
        return
    os.mkdir('data')
    kc.load_file('sha1://e7a0d631fb55727732e8f1b55c7dd05243eec56d/lens_r00.go3', dest='data/lens_r00.go3')
    kc.load_file('sha1://f20ff913ebfb3218305a26880d2452b17ab27e7c/con_r00.go3', dest='data/con_r00.go3')
    kc.load_file('sha1://18a1a0e7abf051832655813198d9dd69cb6126ce/rhabdom_r00.go3', dest='data/rhabdom_r00.go3')
    kc.load_file('sha1://ae71ad40126ca89f292e871874aff1c802686bbc/soln_iref0_iomega1_icase2_idir1_ipol1.dat', 'data/soln_iref0_iomega1_icase2_idir1_ipol1.dat')
    kc.load_file('sha1://ef678f51a6c58a47aeccd6a32dd5bcb6bc0d87e8/targ_iref0_iomega1_icase2_idir1_ipol1.dat', 'data/targ_iref0_iomega1_icase2_idir1_ipol1.dat')

if __name__ == '__main__':
    main()