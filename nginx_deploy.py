import apt
import sys
import shutil
import os
from pystemd.systemd1 import Unit
import time

def install_pkg(pkg_name):
    cache = apt.cache.Cache()
    cache.update()
    cache.open()

    pkg = cache[pkg_name]
    if pkg.is_installed:
        print ("{pkg_name} already installed".format(pkg_name=pkg_name))
    else:
        pkg.mark_install()
        try:
            cache.commit()
        except Exception(arg):
            print('Sorry, package installation failed [{err}]'.format(err=str(arg)), file=sys.stderr)

   

pkg_name = "nginx"
install_pkg(pkg_name)
shutil.copyfile('nginx.conf', '/etc/nginx/nginx.conf')

unit = Unit(b'nginx.service')
unit.load()
print ('Try to restart')
unit.Unit.Restart(b'replace')
time.sleep(5)
if unit.Unit.ActiveState != b'active':
    print ('Service is not active')
    exit(1)
else:
    print ('Service is active')
