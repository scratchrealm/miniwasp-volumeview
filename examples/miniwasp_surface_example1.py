# 10/17/2023
# https://figurl.org/f?v=gs://figurl/volumeview-3&d=sha1://e76deec93347d49524c284cab98f099dc2836f2f&label=miniwasp_surface_example1

import numpy as np
import kachery_cloud as kcl
import volumeview as vv

def main():
    elements_cone = kcl.load_npy('sha1://8cbab88796a3f0ed051d40fb3b62784017f5b341?label=elements_cone.npy')
    points_cone = kcl.load_npy('sha1://47f4a2630b749770c3709299ca788dce506f63ad?label=points_cone.npy')
    elements_lens = kcl.load_npy('sha1://b8fd1eced474f6d980c3c2f61cae06ddcca31223?label=elements_lens.npy')
    points_lens = kcl.load_npy('sha1://ba1b794c88c7975a26759b48c9750d4b62685a7f?label=points_lens.npy')
    elements_rhabdom = kcl.load_npy('sha1://6f3ffb6bfa25c3424455c25bf97a4e6927cb6eaa?label=elements_rhabdom.npy')
    points_rhabdom = kcl.load_npy('sha1://cc643a45264df4a59459b89e63d8fae96dc8af62?label=points_rhabdom.npy')

    W = vv.Workspace()
    W.add_surface(name='cone', vertices=(points_cone / 1000).astype(np.float32), faces=(elements_cone - 1).astype(np.int32))
    W.add_surface(name='lens', vertices=(points_lens / 1000).astype(np.float32), faces=(elements_lens - 1).astype(np.int32))
    W.add_surface(name='rhabdom', vertices=(points_rhabdom / 1000).astype(np.float32), faces=(elements_rhabdom - 1).astype(np.int32))

    F = W.create_figure()
    url = F.url(label='miniwasp_surface_example1')
    print(url)

if __name__ == '__main__':
    main()