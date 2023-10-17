# 10/17/2023
# https://figurl.org/f?v=gs://figurl/volumeview-3&d=sha1://8831daf585d661f1c3f1701b63a0d17a935303c2&label=miniwasp_surface_example2

import numpy as np
import kachery_cloud as kcl
import volumeview as vv

def main():
    elements_cone = kcl.load_npy('sha1://8cbab88796a3f0ed051d40fb3b62784017f5b341?label=elements_cone.npy').astype(np.int32)
    points_cone = kcl.load_npy('sha1://47f4a2630b749770c3709299ca788dce506f63ad?label=points_cone.npy').astype(np.float32)
    elements_lens = kcl.load_npy('sha1://b8fd1eced474f6d980c3c2f61cae06ddcca31223?label=elements_lens.npy').astype(np.int32)
    points_lens = kcl.load_npy('sha1://ba1b794c88c7975a26759b48c9750d4b62685a7f?label=points_lens.npy').astype(np.float32)
    elements_rhabdom = kcl.load_npy('sha1://6f3ffb6bfa25c3424455c25bf97a4e6927cb6eaa?label=elements_rhabdom.npy').astype(np.int32)
    points_rhabdom = kcl.load_npy('sha1://cc643a45264df4a59459b89e63d8fae96dc8af62?label=points_rhabdom.npy').astype(np.float32)
    r_cone = kcl.load_npy('sha1://5aede6e429a5bdc90e3f96ed017ddec049052156?label=r_cone.npy').astype(np.float32)
    r_lens = kcl.load_npy('sha1://6cf00f5cc0bff3e092ded9dfa2b0982c6725689c?label=r_lens.npy').astype(np.float32)
    r_rhabdom = kcl.load_npy('sha1://8385aad810b303f5a04c3d39ebb68bece7a40d86?label=r_rhabdom.npy').astype(np.float32)
    x_cone = kcl.load_npy('sha1://4147053771ce1e8e9418818d1c1af6751a8e88b1?label=x_cone.npy').astype(np.float32)
    x_lens = kcl.load_npy('sha1://e173b06fc4b7619636d1b026eb53524c5a0e88da?label=x_lens.npy').astype(np.float32)
    x_rhabdom = kcl.load_npy('sha1://cb588c71256cac9647db4ec88a91c8beee387be9?label=x_rhabdom.npy').astype(np.float32)
    y_cone = kcl.load_npy('sha1://d319010049c7d76ace8ff8f52f4ac7b9dbf2278e?label=y_cone.npy').astype(np.float32)
    y_lens = kcl.load_npy('sha1://4ee5c1976f166c8a4fc2c27d576348a20ae39aa1?label=y_lens.npy').astype(np.float32)
    y_rhabdom = kcl.load_npy('sha1://8b6a06a38660c48408bbd10a283804c3a9c42171?label=y_rhabdom.npy').astype(np.float32)
    z_cone = kcl.load_npy('sha1://a242ad02f2a6bf97debc416db16e50daefa45dfb?label=z_cone.npy').astype(np.float32)
    z_lens = kcl.load_npy('sha1://38b3c7dd9f821687ecd834173b741b2b38f6d5b6?label=z_lens.npy').astype(np.float32)
    z_rhabdom = kcl.load_npy('sha1://fc3db80f72d7dae7152e7804936e2848fb171887?label=z_rhabdom.npy').astype(np.float32)

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

    F = W.create_figure()
    url = F.url(label='miniwasp_surface_example2')
    print(url)

if __name__ == '__main__':
    main()