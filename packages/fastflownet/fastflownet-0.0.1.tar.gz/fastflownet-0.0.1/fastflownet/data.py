import os.path as osp

import gdown


download_dir = osp.expanduser('~/.fastflownet')

base_url = 'https://github.com/ltkong218/FastFlowNet/raw/main/checkpoints/'


def get_pretrained_model():
    """Return grasp type recognition pretrained model path.

    Returns
    -------
    dst_path : str
        pretrained model path.
    """
    dst_path = osp.join(download_dir, 'fastflownet_ft_mix.pth')
    url = osp.join(base_url, 'fastflownet_ft_mix.pth')
    if not osp.exists(dst_path):
        gdown.cached_download(
            url=url,
            path=dst_path,
            md5='4493ddcc093e97b682f2e548757059c2',
            quiet=True,
        )
    return dst_path
