# 5/6/2022
# https://figurl.org/f?v=gs://figurl/volumeview-3&d=ipfs://bafkreiadl4cdbe5qpl43kk37jiapszgd62l7bmahktomm4aadgqeoht65i&label=miniwasp_surface_example3

import numpy as np
import kachery_cloud as kcl
import volumeview as vv

def main():
    elements_cone = kcl.load_npy('ipfs://bafybeic7aeavlfier4ywxengvx3amq4ddn52zmsgn57mu3fy6kzz5ioi7y?label=elements_cone.npy').astype(np.int32)
    points_cone = kcl.load_npy('ipfs://bafkreifwxujhe5bmfyjgy75kel7xcaxqqqh3c6sywgpqvsjwttsmkhgowm?label=points_cone.npy').astype(np.float32)
    elements_lens = kcl.load_npy('ipfs://bafkreihzhnmzq7lpmolzbahzbkxpmupqenr4lnv7xweu25jxqpj5t67mwi?label=elements_lens.npy').astype(np.int32)
    points_lens = kcl.load_npy('ipfs://bafkreigydt5c4fblpgcsz2hqtprpyb2gxf5vnk4q7xyb2k6763rtjupbeq?label=points_lens.npy').astype(np.float32)
    elements_rhabdom = kcl.load_npy('ipfs://bafybeiarky3jpfgplabcxguswi3brj7zaafqy74zje3hb3x6ye3hxx5hm4?label=elements_rhabdom.npy').astype(np.int32)
    points_rhabdom = kcl.load_npy('ipfs://bafkreibgae3bo5nhhet6hg6z2im7esstz76omdi2jzn3wdyplz2obkenom?label=points_rhabdom.npy').astype(np.float32)
    r_cone = kcl.load_npy('ipfs://bafkreidfbnbfeyx2nniqpvh7znnoflr7r5h44ehezicecfpvu7wbfcsp5u?label=r_cone.npy').astype(np.float32)
    r_lens = kcl.load_npy('ipfs://bafkreiaphntae75cohghw23di7mjmbujocxk5zwjvab7tskvux7rsatemi?label=r_lens.npy').astype(np.float32)
    r_rhabdom = kcl.load_npy('ipfs://bafkreibgo34fxqv32mh5u7724dghzeokxdyhvbq54ce2vyyqzw7a6kpzki?label=r_rhabdom.npy').astype(np.float32)
    x_cone = kcl.load_npy('ipfs://bafkreihrj7j3tl5cqrhprzqjrivnr5vzbxr2jrvswdstcyddygmklizh5y?label=x_cone.npy').astype(np.float32)
    x_lens = kcl.load_npy('ipfs://bafkreicsxfruerkqhas6iqq6oyp46eepv32nmlioyymrzudkrch7h5mrpu?label=x_lens.npy').astype(np.float32)
    x_rhabdom = kcl.load_npy('ipfs://bafkreieaf27tsidttbsv3gmt63dtcfbbhw63uknoqlxhe7bpj6cqqtppky?label=x_rhabdom.npy').astype(np.float32)
    y_cone = kcl.load_npy('ipfs://bafkreiebb72y2sb4kobgllgbhxzyuvzgfymh4oryxbcgeqyud3s7vqujra?label=y_cone.npy').astype(np.float32)
    y_lens = kcl.load_npy('ipfs://bafkreihztvg5yjlwygkg6inj674xnqvg74ozavj6x4x3rhtl6cz5ddz55i?label=y_lens.npy').astype(np.float32)
    y_rhabdom = kcl.load_npy('ipfs://bafkreidk2cwiwaya7a7nerpi6yvetrvdv5emnz53i6ryhmiy4grt65qxay?label=y_rhabdom.npy').astype(np.float32)
    z_cone = kcl.load_npy('ipfs://bafkreidffpghx3omlt3n332tk7vmq47q6h6xo7mwnduyg3xgt6vhrgks4e?label=z_cone.npy').astype(np.float32)
    z_lens = kcl.load_npy('ipfs://bafkreiawx2ha3t7aaltw7x2ahdqusmt2glaskpk6cp3ugd3uy33c6x6cjm?label=z_lens.npy').astype(np.float32)
    z_rhabdom = kcl.load_npy('ipfs://bafkreievmtjcbkouwpz7o6labaqkygiltvt2pqymc2ds2zqcacxxi5q5va?label=z_rhabdom.npy').astype(np.float32)

    W = vv.Workspace()
    S_cone = W.add_surface(name='cone', vertices=points_cone / 1000, faces=elements_cone - 1)
    S_lens = W.add_surface(name='lens', vertices=points_lens / 1000, faces=elements_lens - 1)
    S_rhabdom = W.add_surface(name='rhabdom', vertices=points_rhabdom / 1000, faces=elements_rhabdom - 1)

    W.add_surface_scalar_field(name='x', surface=S_cone, data=x_cone)
    W.add_surface_scalar_field(name='x', surface=S_lens, data=x_lens)
    W.add_surface_scalar_field(name='x', surface=S_rhabdom, data=x_rhabdom)

    W.add_surface_scalar_field(name='y', surface=S_cone, data=y_cone)
    W.add_surface_scalar_field(name='y', surface=S_lens, data=y_lens)
    W.add_surface_scalar_field(name='y', surface=S_rhabdom, data=y_rhabdom)

    W.add_surface_scalar_field(name='z', surface=S_cone, data=z_cone)
    W.add_surface_scalar_field(name='z', surface=S_lens, data=z_lens)
    W.add_surface_scalar_field(name='z', surface=S_rhabdom, data=z_rhabdom)

    W.add_surface_scalar_field(name='r', surface=S_cone, data=r_cone)
    W.add_surface_scalar_field(name='r', surface=S_lens, data=r_lens)
    W.add_surface_scalar_field(name='r', surface=S_rhabdom, data=r_rhabdom)

    x = kcl.load_pkl('ipfs://bafybeieyfjf5d7u6nhcrumbbcpxp57tiiujmu7rccqidk3xk6ghkq7y5aq?label=file.pkl')
    Nx, Ny, Nz = x['Nx'], x['Ny'], x['Nz']
    x0, y0, z0 = x['x0'], x['y0'], x['z0']
    dx, dy, dz = x['dx'], x['dy'], x['dz']
    E = x['E']
    H = x['H']

    grid = W.add_grid(
        name='main',
        Nx=Nx,
        Ny=Ny,
        Nz=Nz,
        x0=x0/1e3,
        y0=y0/1e3,
        z0=z0/1e3,
        dx=dx/1e3,
        dy=dy/1e3,
        dz=dz/1e3
    )
    W.add_grid_vector_field(name='E_real', grid=grid, data=np.real(E).astype(np.float32))
    W.add_grid_vector_field(name='E_imag', grid=grid, data=np.imag(E).astype(np.float32))
    W.add_grid_scalar_field(name='E_mag', grid=grid, data=np.sum(np.abs(E)**2, axis=0).astype(np.float32))
    W.add_grid_vector_field(name='H_real', grid=grid, data=np.real(H).astype(np.float32))
    W.add_grid_vector_field(name='H_imag', grid=grid, data=np.imag(H).astype(np.float32))
    W.add_grid_scalar_field(name='H_mag', grid=grid, data=np.sum(np.abs(H)**2, axis=0).astype(np.float32))

    F = W.create_figure()
    url = F.url(label='miniwasp_surface_example3')
    print(url)

if __name__ == '__main__':
    main()