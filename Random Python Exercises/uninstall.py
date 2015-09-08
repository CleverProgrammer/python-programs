import os, shutil
from distutils.sysconfig import *
py2app = os.path.join(get_python_lib(), 'py2app')
import shutil
if os.path.isdir(py2app):
    print "Removing " + py2app
    shutil.rmtree(py2app)

if os.path.exists(py2app + '.pth'):
    print "Removing " + py2app + '.pth'
    os.unlink(py2app + '.pth')

for path in os.environ['PATH'].split(':'):
    script = os.path.join(path, 'py2applet')
    if os.path.exists(script):
        print "Removing " + script
        os.unlink(script)
