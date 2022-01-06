# 1/6/2022
# https://figurl.org/f?v=gs://figurl/volumeview-2&d=747778076c92df4ac817870f6f2ff6864f768962&channel=flatiron1&label=miniwasp_surface_example1

import numpy as np
import kachery_client as kc
import volumeview as vv

def main():
    elements_cone = kc.load_npy('sha1://8cbab88796a3f0ed051d40fb3b62784017f5b341/elements_cone.npy')
    points_cone = kc.load_npy('sha1://47f4a2630b749770c3709299ca788dce506f63ad/points_cone.npy')
    elements_lens = kc.load_npy('sha1://b8fd1eced474f6d980c3c2f61cae06ddcca31223/elements_lens.npy')
    points_lens = kc.load_npy('sha1://ba1b794c88c7975a26759b48c9750d4b62685a7f/points_lens.npy')
    elements_rhabdom = kc.load_npy('sha1://6f3ffb6bfa25c3424455c25bf97a4e6927cb6eaa/elements_rhabdom.npy')
    points_rhabdom = kc.load_npy('sha1://cc643a45264df4a59459b89e63d8fae96dc8af62/points_rhabdom.npy')

    W = vv.Workspace()
    W.add_surface(name='cone', vertices=(points_cone / 1000).astype(np.float32), faces=(elements_cone - 1).astype(np.int32))
    W.add_surface(name='lens', vertices=(points_lens / 1000).astype(np.float32), faces=(elements_lens - 1).astype(np.int32))
    W.add_surface(name='rhabdom', vertices=(points_rhabdom / 1000).astype(np.float32), faces=(elements_rhabdom - 1).astype(np.int32))

    F = W.create_figure()
    url = F.url(label='miniwasp_surface_example1')
    print(url)

if __name__ == '__main__':
    main()