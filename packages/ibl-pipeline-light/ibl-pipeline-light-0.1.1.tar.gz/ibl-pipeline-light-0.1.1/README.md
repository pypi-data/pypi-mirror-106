# IBL-pipeline-light
A light version of IBL pipeline that allows users to access datajoint tables.



## Modules
A user connecting to the public IBL database could use the following modules:

`reference`, `subject`, `action`, `acquisition`, `data`, `behavior`, `ephys`, `histology`, and `analyses.behavior`.

In addition to the above modules, an IBL internal user connecting to the internal IBL database could use the following modules as well:

`qc`


## Install package
The package is released on PyPI and could be installed with the following command:

```bash
pip install ibl-pipeline-light
```

If you would like to run the notebooks provided with this repository, instead of pip install from PyPI, we recommend you to fork, clone and install locally instead, with the following steps:


1. Fork the repository to your own GitHub account
2. Clone your fork to local computer
3. Create a conda environment with a name (for example, `ibl-pipeline-light`) and activate it.
4. Change the directory to the root of the cloned repository
5. Run `pip install -e .`
6. Add the conda evironment to the ipython kernel by: `python -m ipykernel install --user --name=ibl-pipeline-light`
7. Start Jupyter server and run notebooks


## Set up the configuration to connect to the IBL database.
To connect to the database for the first time, you will need to set up the DataJoint config within python.

```python
import datajoint as dj
dj.config['database.host'] = {host_name}
dj.config['database.user'] = {user_name}
dj.config['database.password'] = {password}
dj.config.save_local()
```

+ For **internal users**:

    + host name: 'datajoint.internationalbrainlab.org'
    + user and pass: Contact Shan Shen for the username and password if you are new to IBL

+ For **external users**:

    + host name: 'datajoint-public.internationalbrainlab.org'
    + user and pass: currently there are two approaches to get username and password for external users:

        + For **NeuroMatch Academy users**: fill in [a form](https://datajoint.io/events/nma-ibl-public) to get an email containing the credentials.
        + For **general users**: visit our [public JupyterHub](https://jupyterhub.internationalbrainlab.org) and sign up with your GitHub account. The notebook `public_notebooks/05-Access the database locally.ipynb` gives instructions on the username and password information.


`dj.config.save_local()` saves the config file `dj_local_conf.json` in the local directory, which allows direct connection to the database in this directory. The next time if the python kernel starts from the directory containing `dj_local_conf.json`, DataJoint will be pre-configured while importing.

If you need the global config that allows direct connection from any directory, use `dj.config.save_global()` instead.

After these, you will be able to import the modules:

```python
from ibl_pipeline import reference, subject, action, acquisition, behavior
```
