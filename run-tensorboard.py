# Tensorboard
import os
import subprocess

subprocess.call(
  [
    "tensorboard", 
    "--logdir", "logs/fit", 
    "--host", "127.0.0.1", 
    "--port", os.environ["CDSW_APP_PORT"], 
    "serve"
  ]
) 
