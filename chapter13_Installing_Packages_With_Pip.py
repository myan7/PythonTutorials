from Common import _section_str as sec, _segment_str as seg, _segment_str as sysout
print(f"""{sec}
Chapter 13 Installing Packages With Pip
{sec}
As of Python 3.4,
it is now included with most distributions of the language.
""")


print(f"""{sec}
13.1 Installing Third-Party Packages With Pip
{sec}

Python’s package manager pip is used to install and manage third
party packages.
""")

print(r"""
in the terminal/cmd windown,
type python3 -m pip -V
or python -m pip -V
or python -m pip --version
or pip -V
or pip --version
to check if pip is installed on your laptop and its version.

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip -V
pip 21.2.3 from D:\Program Files\Python39\lib\site-packages\pip (python 3.9)

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ python -m pip -V
pip 21.2.3 from D:\Program Files\Python39\lib\site-packages\pip (python 3.9)


pip usage:

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip -h

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  index                       Inspect information available from package indexes.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --debug                     Let unhandled exceptions propagate outside the main subroutine, instead of logging them to stderr.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --proxy <proxy>             Specify a proxy in the form [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL Certificate Verification' in pip documentation for more information.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.

""")
print(f"""{seg}
Upgrading pip to the Latest Version
{seg}
""")

print(r"""
Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip install --upgrade pip
Requirement already satisfied: pip in d:\program files\python39\lib\site-packages (21.2.3)
Collecting pip
  Downloading pip-21.3.1-py3-none-any.whl (1.7 MB)
     |████████████████████████████████| 1.7 MB 242 kB/s
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.3
    Uninstalling pip-21.2.3:
      Successfully uninstalled pip-21.2.3
ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied: 'D:\\Program Files\\Python39\\~cripts\\pip.exe'
Consider using the `--user` option or check the permissions.


Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip -V
pip 21.3.1 from D:\Program Files\Python39\lib\site-packages\pip (python 3.9)

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip install --upgrade pip
Requirement already satisfied: pip in d:\program files\python39\lib\site-packages (21.3.1)

""")



print(f"""{seg}
Listing All Installed Packages
{seg}
""")

print(r"""
Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip list
Package    Version
---------- -------
pip        21.3.1
setuptools 57.4.0

""")


print(f"""{seg}
Installing a Package
{seg}
""")

print(r"""
command can be used:
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org xgboost
or
pip install xgboost

or if you want to install several packages at once.
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pandas jinja2 matplotlib scikit-learn xgboost  matplotlib  pyxlsb
or
pip install pandas jinja2 matplotlib scikit-learn xgboost  matplotlib  pyxlsb

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pandas jinja2 matplotlib scikit-learn xgboost  matplotlib  pyxlsb
Collecting pandas
  Downloading pandas-1.3.5-cp39-cp39-win_amd64.whl (10.2 MB)
     |████████████████████████████████| 10.2 MB 187 kB/s
Collecting jinja2
  Downloading Jinja2-3.0.3-py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 273 kB/s
Collecting matplotlib
  Downloading matplotlib-3.5.1-cp39-cp39-win_amd64.whl (7.2 MB)
     |████████████████████████████████| 7.2 MB 123 kB/s
Collecting scikit-learn
  Downloading scikit_learn-1.0.1-cp39-cp39-win_amd64.whl (7.2 MB)
     |████████████████████████████████| 7.2 MB 81 kB/s
Requirement already satisfied: xgboost in d:\program files\python39\lib\site-packages (1.5.1)
Collecting pyxlsb
  Downloading pyxlsb-1.0.9-py2.py3-none-any.whl (23 kB)
Requirement already satisfied: numpy>=1.17.3 in d:\program files\python39\lib\site-packages (from pandas) (1.21.4)
Collecting python-dateutil>=2.7.3
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     |████████████████████████████████| 247 kB 285 kB/s
Collecting pytz>=2017.3
  Downloading pytz-2021.3-py2.py3-none-any.whl (503 kB)
     |████████████████████████████████| 503 kB 128 kB/s
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.0.1-cp39-cp39-win_amd64.whl (14 kB)
Collecting packaging>=20.0
  Downloading packaging-21.3-py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 325 kB/s
Collecting kiwisolver>=1.0.1
  Downloading kiwisolver-1.3.2-cp39-cp39-win_amd64.whl (52 kB)
     |████████████████████████████████| 52 kB 262 kB/s
Collecting pyparsing>=2.2.1
  Downloading pyparsing-3.0.6-py3-none-any.whl (97 kB)
     |████████████████████████████████| 97 kB 315 kB/s
Collecting cycler>=0.10
  Downloading cycler-0.11.0-py3-none-any.whl (6.4 kB)
Collecting fonttools>=4.22.0
  Downloading fonttools-4.28.4-py3-none-any.whl (885 kB)
     |████████████████████████████████| 885 kB 312 kB/s
Collecting pillow>=6.2.0
  Downloading Pillow-8.4.0-cp39-cp39-win_amd64.whl (3.2 MB)
     |████████████████████████████████| 3.2 MB 89 kB/s
Collecting threadpoolctl>=2.0.0
  Downloading threadpoolctl-3.0.0-py3-none-any.whl (14 kB)
Collecting joblib>=0.11
  Downloading joblib-1.1.0-py2.py3-none-any.whl (306 kB)
     |████████████████████████████████| 306 kB 156 kB/s
Requirement already satisfied: scipy>=1.1.0 in d:\program files\python39\lib\site-packages (from scikit-learn) (1.7.3)
Collecting six>=1.5
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, pyparsing, threadpoolctl, pytz, python-dateutil, pillow, packaging, MarkupSafe, kiwisolver, joblib, fonttools, cycler, scikit-learn, pyxlsb, pandas, matplotlib, jinja2
Successfully installed MarkupSafe-2.0.1 cycler-0.11.0 fonttools-4.28.4 jinja2-3.0.3 joblib-1.1.0 kiwisolver-1.3.2 matplotlib-3.5.1 packaging-21.3 pandas-1.3.5 pillow-8.4.0 pyparsing-3.0.6 python-dateutil-2.8.2 pytz-2021.3 pyxlsb-1.0.9 scikit-learn-1.0.1 six-1.16.0 thread
poolctl-3.0.0
""")
print(f"""{seg}
Show Package Details
{seg}
""")
print(r"""
you can check the installed packages by using pip list

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip list
Package         Version
--------------- -------
cycler          0.11.0
fonttools       4.28.4
Jinja2          3.0.3
joblib          1.1.0
kiwisolver      1.3.2
MarkupSafe      2.0.1
matplotlib      3.5.1
numpy           1.21.4
packaging       21.3
pandas          1.3.5
Pillow          8.4.0
pip             21.3.1
pyparsing       3.0.6
python-dateutil 2.8.2
pytz            2021.3
pyxlsb          1.0.9
scikit-learn    1.0.1
scipy           1.7.3
setuptools      57.4.0
six             1.16.0
threadpoolctl   3.0.0
xgboost         1.5.1

""")

print(f"""{seg}
Show Package Details
{seg}
""")
print(r"""

or for more detailed information of the installed package

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip show scikit-learn
Name: scikit-learn
Version: 1.0.1
Summary: A set of python modules for machine learning and data mining
Home-page: http://scikit-learn.org
Author:
Author-email:
License: new BSD
Location: d:\program files\python39\lib\site-packages
Requires: joblib, numpy, scipy, threadpoolctl
Required-by:

""")

print(f"""{seg}
Installing Speciрc Package Versions With Version Speciрers
{seg}""")

print(r"""
------------------------------------------------------------
Version
Specifier   Description
------------------------------------------------------------
<=, >=      Inclusive less than and greater than specifiers
<, >        Exclusive less than and greater than specifiers
==          Exactly equal to specifier
------------------------------------------------------------

for example:
I already installed xgboost 1.5.1,
but I need version 1.4.2

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip install xgboost==1.4.2
Collecting xgboost==1.4.2
  Downloading xgboost-1.4.2-py3-none-win_amd64.whl (97.8 MB)
     |████████████████████████████████| 97.8 MB 11 kB/s
Requirement already satisfied: numpy in d:\program files\python39\lib\site-packages (from xgboost==1.4.2) (1.21.4)
Requirement already satisfied: scipy in d:\program files\python39\lib\site-packages (from xgboost==1.4.2) (1.7.3)
Installing collected packages: xgboost
  Attempting uninstall: xgboost
    Found existing installation: xgboost 1.5.1
    Uninstalling xgboost-1.5.1:
      Successfully uninstalled xgboost-1.5.1
Successfully installed xgboost-1.4.2

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip list
Package         Version
--------------- -------
cycler          0.11.0
fonttools       4.28.4
Jinja2          3.0.3
joblib          1.1.0
kiwisolver      1.3.2
MarkupSafe      2.0.1
matplotlib      3.5.1
numpy           1.21.4
packaging       21.3
pandas          1.3.5
Pillow          8.4.0
pip             21.3.1
pyparsing       3.0.6
python-dateutil 2.8.2
pytz            2021.3
pyxlsb          1.0.9
scikit-learn    1.0.1
scipy           1.7.3
setuptools      57.4.0
six             1.16.0
threadpoolctl   3.0.0
xgboost         1.4.2


""")


print(f"""{seg}
Uninstalling a Package
{seg}""")

print(r"""
Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip install xgboost
Requirement already satisfied: xgboost in d:\program files\python39\lib\site-packages (1.4.2)
Requirement already satisfied: scipy in d:\program files\python39\lib\site-packages (from xgboost) (1.7.3)
Requirement already satisfied: numpy in d:\program files\python39\lib\site-packages (from xgboost) (1.21.4)

Notice I cannot install the 1.5.1 again if I have 1.4.2
I need to uninstall it first and then install it again.

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip uninstall xgboost
Found existing installation: xgboost 1.4.2
Uninstalling xgboost-1.4.2:
  Would remove:
    d:\program files\python39\lib\site-packages\xgboost-1.4.2.dist-info\*
    d:\program files\python39\lib\site-packages\xgboost\*
    d:\program files\python39\xgboost\vcomp140.dll
Proceed (Y/n)? Y
  Successfully uninstalled xgboost-1.4.2

then install it again

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip install xgboost
Collecting xgboost
  Using cached xgboost-1.5.1-py3-none-win_amd64.whl (106.6 MB)
Requirement already satisfied: numpy in d:\program files\python39\lib\site-packages (from xgboost) (1.21.4)
Requirement already satisfied: scipy in d:\program files\python39\lib\site-packages (from xgboost) (1.7.3)
Installing collected packages: xgboost
Successfully installed xgboost-1.5.1

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip list
Package         Version
--------------- -------
cycler          0.11.0
fonttools       4.28.4
Jinja2          3.0.3
joblib          1.1.0
kiwisolver      1.3.2
MarkupSafe      2.0.1
matplotlib      3.5.1
numpy           1.21.4
packaging       21.3
pandas          1.3.5
Pillow          8.4.0
pip             21.3.1
pyparsing       3.0.6
python-dateutil 2.8.2
pytz            2021.3
pyxlsb          1.0.9
scikit-learn    1.0.1
scipy           1.7.3
setuptools      57.4.0
six             1.16.0
threadpoolctl   3.0.0
xgboost         1.5.1

That said, using third-party packages in your code introduces several
concerns that must be addressed with care. You’ll learn about some
of the pitfalls associated with third-party packages in the next section.
""")

print(f"""{sec}
13.1 The Pitfalls of Third-Party Packages
{sec}

By default, pip installs the latest release of a package, so if you distribute your code to someone else and they install a newer version of
a package required by your project, they may not be able to run your
code.

This presents a significant challenge, for both the end user and
yourself. Fortunately, Python comes with a fix for this all-to-common
problem: virtual environments.


""")

print(r"""
for more information please refer to:
https://www.youtube.com/watch?v=zDYL22QNiWk&ab_channel=CoreySchafer

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip install pipenv
Collecting pipenv
  Downloading pipenv-2021.11.23-py2.py3-none-any.whl (3.6 MB)
     |████████████████████████████████| 3.6 MB 327 kB/s
Requirement already satisfied: pip>=18.0 in d:\program files\python39\lib\site-packages (from pipenv) (21.3.1)
Requirement already satisfied: setuptools>=36.2.1 in d:\program files\python39\lib\site-packages (from pipenv) (57.4.0)
Collecting virtualenv
  Downloading virtualenv-20.10.0-py2.py3-none-any.whl (5.6 MB)
     |████████████████████████████████| 5.6 MB 56 kB/s
Collecting certifi
  Downloading certifi-2021.10.8-py2.py3-none-any.whl (149 kB)
     |████████████████████████████████| 149 kB 344 kB/s
Collecting virtualenv-clone>=0.2.5
  Downloading virtualenv_clone-0.5.7-py3-none-any.whl (6.6 kB)
Collecting backports.entry-points-selectable>=1.0.4
  Downloading backports.entry_points_selectable-1.1.1-py2.py3-none-any.whl (6.2 kB)
Collecting distlib<1,>=0.3.1
  Downloading distlib-0.3.4-py2.py3-none-any.whl (461 kB)
     |████████████████████████████████| 461 kB 48 kB/s
Collecting filelock<4,>=3.2
  Downloading filelock-3.4.0-py3-none-any.whl (9.8 kB)
Requirement already satisfied: six<2,>=1.9.0 in d:\program files\python39\lib\site-packages (from virtualenv->pipenv) (1.16.0)
Collecting platformdirs<3,>=2
  Downloading platformdirs-2.4.0-py3-none-any.whl (14 kB)
Installing collected packages: platformdirs, filelock, distlib, backports.entry-points-selectable, virtualenv-clone, virtualenv, certifi, pipenv
Successfully installed backports.entry-points-selectable-1.1.1 certifi-2021.10.8 distlib-0.3.4 filelock-3.4.0 pipenv-2021.11.23 platformdirs-2.4.0 virtualenv-20.10.0 virtualenv-clone-0.5.7

""")

print(r"""
you can use pipenv install to install packages and it will install them
specifically for this project.

what I did was to create a new folder called pipEnvProject and cd to it in cygwin
run pipenv install requests there

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ mkdir pipEnvProject

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ cd pipEnvProject/

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials/pipEnvProject
$ pipenv install requests
Creating a virtualenv for this project...
Pipfile: E:\pythonProject\PythonTutorials\pipEnvProject\Pipfile
Using D:/Program Files/Python39/python.exe (3.9.7) to create virtualenv...
[====] Creating virtual environment...created virtual environment CPython3.9.7.final.0-64 in 12984ms
  creator CPython3Windows(dest=C:\Users\Administrator\.virtualenvs\pipEnvProject--hroJYAi, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Administrator\AppData\Local\pypa\virtualenv)
    added seed packages: pip==21.3.1, setuptools==58.3.0, wheel==0.37.0
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

Successfully created virtual environment!
Virtualenv location: C:\Users\Administrator\.virtualenvs\pipEnvProject--hroJYAi
Creating a Pipfile for this project...
Installing requests...
Adding requests to Pipfile's [packages]...
Installation Succeeded
Pipfile.lock not found, creating...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
           Building requirements...
Resolving dependencies...
Success!
Updated Pipfile.lock (fe5a22)!
Installing dependencies from Pipfile.lock (fe5a22)...
  ================================ 0/0 - 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.

just noticed that I cannot activate the pipenv thru cygwin...
now this is the cmd window

C:\Users\Administrator>e:

E:\>cd pythonProject\PythonTutorials\pipEnvProject

E:\pythonProject\PythonTutorials\pipEnvProject>pipenv shell
Launching subshell in virtual environment...
Microsoft Windows [Version 10.0.19042.1415]
(c) Microsoft Corporation. All rights reserved.

(pipEnvProject--hroJYAi) E:\pythonProject\PythonTutorials\pipEnvProject>python
Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.executable
'C:\\Users\\Administrator\\.virtualenvs\\pipEnvProject--hroJYAi\\Scripts\\python.exe'
>>> import requests
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> exit()

(pipEnvProject--hroJYAi) E:\pythonProject\PythonTutorials\pipEnvProject>exit

E:\pythonProject\PythonTutorials\pipEnvProject>

or you can use this way to run the virtual environment

E:\pythonProject\PythonTutorials\pipEnvProject>pipenv run python
Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.executable
'C:\\Users\\Administrator\\.virtualenvs\\pipEnvProject--hroJYAi\\Scripts\\python.EXE'

""")
