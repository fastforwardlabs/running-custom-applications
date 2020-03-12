# Running custom applications in CDSW/CML

With the recent addition of [Analytical Applications](https://docs.cloudera.com/documentation/data-science-workbench/1-7-x/topics/cdsw_analytical_applications.html), data scientists and data engineers can now deploy their own custom applications and share them with other users.

Whilst simple applications may have all necessary code already baked into one script file more complicated applications may require: custom launchers, run flags that are set on execution and parameters that maybe instance specific. In order to run these sorts of applications we can leverage the Python `subprocess` module to run the commands that we would normally have manually entered into the terminal.

# Getting Started

For this demonstration, I will show how to run [Tensorboard](https://www.tensorflow.org/tensorboard) and [Hiplot](https://facebookresearch.github.io/hiplot/index.html) which both allow for the visualisation of parameters from multiple runs of deep learning models.

Both applications rely on a custom command to trigger them as standalone applications: `tensorboard` for Tensorboard and `hiplot` for Hiplot.

## Requirements

- CDSW 1.7.1 or later
- Python 3 engines with web access available (for installing libraries)

## Setup

Click Create Project:

![Create Project][CreateProject]

Git clone from: https://github.com/fastforwardlabs/running-custom-applications

Click Open Workbench:

![Open Workbench][OpenWorkbench]


Launch New Python Session:

![Start Session][StartingSession]

First we need to make sure that all the required libraries are installed. From the CML/CDSW IDE run:

```bash
!pip3 install -r requirements.txt
```

![Install Packages][InstallPackages]

Packages that are installed in a session will be preserved for use by the project across all sessions

I have created two run scripts to start the apps: 

For Hiplot:

```python

# Hiplot
import os
import subprocess

subprocess.call(['hiplot', '--host', '127.0.0.1', 
                 '--port', os.environ['CDSW_APP_PORT']
                ])

```

I save this out in the `run-hiplot.py` script.

The `os.environ["CDSW_APP_PORT]` command calls the environment variable `CDSW_APP_PORT` which specifies which port the application must use in order to run successfully.

For Tensorboard:

```python

# Tensorboard
import os
import subprocess

subprocess.call(["tensorboard", " --logdir=logs/fit", "--host", "127.0.0.1",
               "--port", os.environ["CDSW_APP_PORT"]]) 

```
I save this out in the `run-tensorboard.py` script.

Notice that adding a flag is as simple as adding the flag and its settings in as a part of the comma separated list within the `subprocess.call([ ... ])` command.

For this demonstration, I will generate some data to populate tensorboard first.

Run `test_runs_tensorflow.py` in the CDSW/CML Session by opening the py file then clicking the play arrow in the coding window.

![GenreateData][PopulateWithData]


# Running applications that require flags

Now that we have the script, we can go ahead and trigger it as an application:

Go the applications screen:

![Applications Button][ApplicationsMenu]

Create New Application:

![New Applications][NewApplications]

Fill in the form:

![Application Form][ApplicationsForm]

Note the option to `Set Environment Variables` just before the `Create Application` button. Leveraging `os.environ['']` and the ability to set environment variables from the `New Application` screen, it is still possible to edit run flags without editing the `run` script.

Click Create:

![Application Created][ApplicationCreated]


To access the application, click the box with the arrow.

![Application Running][ApplicationRun]

# Conclusion

The new Analytical Applications function, rolled out in [CDSW 1.7.x](https://docs.cloudera.com/documentation/data-science-workbench/1-7-x/topics/cdsw_analytical_applications.html#cdsw_overview) and availabe in [CML - Public Cloud](https://docs.cloudera.com/machine-learning/cloud/applications/topics/ml-applications.html) enables the deployment of third party and custom applications on Cloudera Machine Learning infrastructure.

Through the use of the python `subprocess` module it is possible to execute arbitrary code and set runtime flags for applications as well. Happy Coding!

[CreateProject]: screenshots/CreateProject.png
[OpenWorkbench]: screenshots/OpenWorkbench.png
[StartingSession]: screenshots/StartingSession.png
[InstallPackages]: screenshots/InstallPackages.png
[ApplicationsMenu]: screenshots/ApplicationsButton.png
[NewApplications]: screenshots/NewApplications.png
[ApplicationsForm]: screenshots/ApplicationForm.png
[ApplicationCreated]: screenshots/ApplicationCreated.png
[ApplicationRun]: screenshots/ApplicationScreen.png
[PopulateWithData]: screenshots/PopulateWithData.png
