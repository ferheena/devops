import os
import pdb
import shlex
from subprocess import Popen, PIPE

cmd = "curl http://34.93.49.84:5000 | grep -q '<b>Visits:</b>'"
args = shlex.split(cmd)
process = Popen(args, stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
if stdout:
    print "Test Passed!"
else:
    print "Test Failed!"
