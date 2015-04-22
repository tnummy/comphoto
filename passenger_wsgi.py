import sys, os
INTERP = os.path.join(os.environ['HOME'], 'comphoto.timnummyphotography.com', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

sys.path.append('comphoto')
from comphoto.app import app as application