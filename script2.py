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
    grid = W.add_grid()

if __name__ == '__main__':
    main()