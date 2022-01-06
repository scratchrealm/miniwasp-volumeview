import numpy as np
import kachery_client as kc
import volumeview as vv

def main():
    x = kc.load_pkl('sha1://1c71f894e606262dc3cadaef036fc9e94a8337b6/file.pkl')
    Nx, Ny, Nz = x['Nx'], x['Ny'], x['Nz']
    x0, y0, z0 = x['x0'], x['y0'], x['z0']
    dx, dy, dz = x['dx'], x['dy'], x['dz']
    E = x['E']
    H = x['H']
    print(E.shape, H.shape)

    W = vv.Workspace()
    print(Nx, Ny, Nz, x0, y0, z0, dx, dy, dz)
    grid = W.add_grid(name='main', Nx=Nx, Ny=Ny, Nz=Nz, x0=x0/1e3, y0=y0/1e3, z0=z0/1e3, dx=dx/1e3, dy=dy/1e3, dz=dz/1e3)
    # grid = W.add_grid(name='main', Nx=Nx, Ny=Ny, Nz=Nz, x0=0, y0=0, z0=0, dx=1, dy=1, dz=1)
    W.add_grid_vector_field(name='E_real', grid=grid, data=np.real(E).astype(np.float32))
    W.add_grid_vector_field(name='E_imag', grid=grid, data=np.imag(E).astype(np.float32))
    W.add_grid_scalar_field(name='E_magnitude', grid=grid, data=np.sum(np.abs(E)**2, axis=0).astype(np.float32))
    W.add_grid_vector_field(name='H_real', grid=grid, data=np.real(H).astype(np.float32))
    W.add_grid_vector_field(name='H_imag', grid=grid, data=np.imag(H).astype(np.float32))
    W.add_grid_scalar_field(name='H_magnitude', grid=grid, data=np.sum(np.abs(H)**2, axis=0).astype(np.float32))

    F = W.create_figure()
    url = F.url(label='test miniwasp')
    print(url)
    # https://figurl.org/f?v=gs://figurl/volumeview-2&d=4218893dbd648ac274ab83d27a77336bc216ffe0&channel=flatiron1&label=test%20miniwasp

if __name__ == '__main__':
    main()