# 1/12/2022
# https://figurl.org/f?v=gs://figurl/volumeview-2&d=f1309ec6a281bd0be468e6fb7d50adc2ec8b0b59&channel=flatiron1&label=miniwasp_surface_example2

import numpy as np
import kachery_client as kc
import volumeview as vv

def main():
    elements_cone = kc.load_npy('sha1://8cbab88796a3f0ed051d40fb3b62784017f5b341/elements_cone.npy').astype(np.int32)
    elements_lens = kc.load_npy('sha1://b8fd1eced474f6d980c3c2f61cae06ddcca31223/elements_lens.npy').astype(np.int32)
    elements_rhabdom = kc.load_npy('sha1://6f3ffb6bfa25c3424455c25bf97a4e6927cb6eaa/elements_rhabdom.npy').astype(np.int32)

    points_cone = kc.load_npy('sha1://47f4a2630b749770c3709299ca788dce506f63ad/points_cone.npy').astype(np.float32)
    points_lens = kc.load_npy('sha1://ba1b794c88c7975a26759b48c9750d4b62685a7f/points_lens.npy').astype(np.float32)
    points_rhabdom = kc.load_npy('sha1://cc643a45264df4a59459b89e63d8fae96dc8af62/points_rhabdom.npy').astype(np.float32)

    r_cone = kc.load_npy('sha1://5aede6e429a5bdc90e3f96ed017ddec049052156/r_cone.npy').astype(np.float32)
    r_lens = kc.load_npy('sha1://6cf00f5cc0bff3e092ded9dfa2b0982c6725689c/r_lens.npy').astype(np.float32)
    r_rhabdom = kc.load_npy('sha1://8385aad810b303f5a04c3d39ebb68bece7a40d86/r_rhabdom.npy').astype(np.float32)

    x_cone = kc.load_npy('sha1://4147053771ce1e8e9418818d1c1af6751a8e88b1/x_cone.npy').astype(np.float32)
    x_lens = kc.load_npy('sha1://e173b06fc4b7619636d1b026eb53524c5a0e88da/x_lens.npy').astype(np.float32)
    x_rhabdom = kc.load_npy('sha1://cb588c71256cac9647db4ec88a91c8beee387be9/x_rhabdom.npy').astype(np.float32)

    y_cone = kc.load_npy('sha1://d319010049c7d76ace8ff8f52f4ac7b9dbf2278e/y_cone.npy').astype(np.float32)
    y_lens = kc.load_npy('sha1://4ee5c1976f166c8a4fc2c27d576348a20ae39aa1/y_lens.npy').astype(np.float32)
    y_rhabdom = kc.load_npy('sha1://8b6a06a38660c48408bbd10a283804c3a9c42171/y_rhabdom.npy').astype(np.float32)

    z_cone = kc.load_npy('sha1://a242ad02f2a6bf97debc416db16e50daefa45dfb/z_cone.npy').astype(np.float32)
    z_lens = kc.load_npy('sha1://38b3c7dd9f821687ecd834173b741b2b38f6d5b6/z_lens.npy').astype(np.float32)
    z_rhabdom = kc.load_npy('sha1://fc3db80f72d7dae7152e7804936e2848fb171887/z_rhabdom.npy').astype(np.float32)

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

    x = kc.load_pkl('sha1://528f6b30b27dcfb5eb78725c8691a2890227c383/file.pkl')
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
    url = F.url(label='miniwasp_surface_example2')
    print(url)

if __name__ == '__main__':
    main()