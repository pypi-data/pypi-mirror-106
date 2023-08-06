# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['usn', 'usn.tests']

package_data = \
{'': ['*'], 'usn.tests': ['data/*']}

entry_points = \
{'console_scripts': ['ubuntu-server-netboot = usn.usn:ubuntu_server_netboot']}

setup_kwargs = {
    'name': 'ubuntu-server-netboot',
    'version': '0.1.1rc4',
    'description': 'This utility generates a netboot directory tree from an Ubuntu Server Live ISO image, an image based on the subiquity installer.',
    'long_description': '# ubuntu-server-netboot\nThis utility generates a netboot directory tree from an Ubuntu Server Live ISO image, an image based on the `subiquity` installer. The tree contents are similar to the contents of the `netboot.tar.gz` file that debian-installer builds provide. Example:\n\n```\n$ ./ubuntu-server-netboot --url http://releases.ubuntu.com/focal/ubuntu-20.04.2-live-server-amd64.iso\nINFO: Downloading http://releases.ubuntu.com/focal/ubuntu-20.04.2-live-server-amd64.iso\nINFO: Attempting to download http://archive.ubuntu.com/ubuntu/dists/focal-updates/main/uefi/grub2-amd64/current/grubx64.efi.signed\nINFO: Netboot generation complete: /tmp/tmpo54145m2/ubuntu-installer\n```\n\nThe `--url` parameter is used for 2 reasons:\n\n1. `ubuntu-server-netboot` will download the image at runtime to extract the necessary files from it.\n1. Subiquity-based installs need to download an image at install-time. `ubuntu-server-netboot` will generate configuration files that point the installer to this URL.\n\nIf you have a local copy of the ISO, you can point to it with the `--iso` parameter to avoid having `ubuntu-server-netboot` download an extra copy. Just be sure that `--iso` and `--url` point to the same version of the ISO.\n\nOptionally, you can place `--autoinstall-url` to tell the netbooting process to enable subiquity automation. See [our autoinstall example](./autoinstall/README.md) and [the autoinstall and Automated Server Installs\nIntroduction of Ubuntu Server guide](Automated Server Installs Introduction) for more details.\n\nYou can also add additional kernel command line arguments (e.g. `"console=ttyS0"`) to the generated configuration files using the `--extra-args` parameter.\n\n## Usage of the Generated Files\nCopy the files generated under the interim folder `/tmp/tmpxxx/ubuntu-installer/`\nto your tftp root folder for netboot, for example `/srv/tftp` or `/var/lib/tftpboot`.\nYou may check your tftpd configuration of the root directory, for instance, tftpd-hpa is `/etc/default/tftpd-hpa`. Let\'s copy:\n\n```\n$ sudo cp -r /tmp/tmpxxx/ubuntu-installer/* /srv/tftp\n```\n\nThen your netboot server is ready to go if the corresponding DHCP is set up.\n\n## Troubleshooting\nFor more details on setting up a PXE environment for x86 systems using a legacy BIOS, see [this discourse post](https://discourse.ubuntu.com/t/netbooting-the-server-installer-on-amd64/16620).\n\nFor more details on setting up a PXE environment for UEFI-based systems, see [this discourse post](https://discourse.ubuntu.com/t/netbooting-the-live-server-installer-via-uefi-pxe-on-arm-aarch64-arm64-and-x86-64-amd64/19240).\n\n## Dependencies\nToday `ubuntu-server-netboot` needs to run on Ubuntu or another Debian derivative with the following packages installed:\n\n - genisoimage\n - mtools\n - python3-distro-info\n - pxelinux (x86-only)\n - syslinux-common (x86-only)\n\nThis script is tested with Ubuntu 18.04 ("bionic beaver") and above.\n\n## Contribution and Development\n\nPlease report bugs to [this github issue tracker](https://github.com/dannf/ubuntu-server-netboot/issues). The github templates including "Issue" and "Pull requests" are originally forked from [this "cookiecutter" templates for python](https://github.com/Lee-W/cookiecutter-python-template).\n\nPlace `pytest` to cover the basic test sets.\n',
    'author': 'dann frazier',
    'author_email': 'dannf@ubuntu.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6.5,<4.0.0',
}


setup(**setup_kwargs)
