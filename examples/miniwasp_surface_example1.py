# 5/6/2022
# https://figurl.org/f?v=gs://figurl/volumeview-3&d=ipfs://bafkreid44axr4eynrctdnaiqywsgmyjcbbolq3ovybapqouaqjl2tbeiuy&label=miniwasp_surface_example1

import numpy as np
import kachery_cloud as kcl
import volumeview as vv

def main():
    elements_cone = kcl.load_npy('ipfs://bafybeic7aeavlfier4ywxengvx3amq4ddn52zmsgn57mu3fy6kzz5ioi7y?label=elements_cone.npy')
    points_cone = kcl.load_npy('ipfs://bafkreifwxujhe5bmfyjgy75kel7xcaxqqqh3c6sywgpqvsjwttsmkhgowm?label=points_cone.npy')
    elements_lens = kcl.load_npy('ipfs://bafkreihzhnmzq7lpmolzbahzbkxpmupqenr4lnv7xweu25jxqpj5t67mwi?label=elements_lens.npy')
    points_lens = kcl.load_npy('ipfs://bafkreigydt5c4fblpgcsz2hqtprpyb2gxf5vnk4q7xyb2k6763rtjupbeq?label=points_lens.npy')
    elements_rhabdom = kcl.load_npy('ipfs://bafybeiarky3jpfgplabcxguswi3brj7zaafqy74zje3hb3x6ye3hxx5hm4?label=elements_rhabdom.npy')
    points_rhabdom = kcl.load_npy('ipfs://bafkreibgae3bo5nhhet6hg6z2im7esstz76omdi2jzn3wdyplz2obkenom?label=points_rhabdom.npy')

    W = vv.Workspace()
    W.add_surface(name='cone', vertices=(points_cone / 1000).astype(np.float32), faces=(elements_cone - 1).astype(np.int32))
    W.add_surface(name='lens', vertices=(points_lens / 1000).astype(np.float32), faces=(elements_lens - 1).astype(np.int32))
    W.add_surface(name='rhabdom', vertices=(points_rhabdom / 1000).astype(np.float32), faces=(elements_rhabdom - 1).astype(np.int32))

    F = W.create_figure()
    url = F.url(label='miniwasp_surface_example1')
    print(url)

if __name__ == '__main__':
    main()