# Hiplot
import os
import subprocess

subprocess.call(['hiplot', '--host', '127.0.0.1', 
                 '--port', os.environ['CDSW_APP_PORT']
                ])