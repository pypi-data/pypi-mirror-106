import os

from setuptools import setup, find_packages


pjoin = os.path.join

here = os.path.abspath(os.path.dirname(__file__))

__version__ = None

exec(open(pjoin(here,'jupyter_admin/version.py')).read()) # Load __version__

install_requires = [
    'alembic',
    'jupyterhub>=1.4.1',
    'pluggy',
    'tornado>=6.0.4',
    'traitlets',
]

extras_require = {
}

setup_metadata = dict(
    version = __version__,
    python_requires = '>=3.8',
    author = 'Datalayer',
    author_email = 'eric@datalayer.io',
    license = 'MIT',
    url='',
    # this should be a whitespace separated string of keywords, not a list
    keywords = "jupyter admin",
    classifiers = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    project_urls = {
        'Source': 'https://github.com/datalayer/jupyter-admin',
        'Tracker': 'https://github.com/datalayer/jupyter-admin/issues'
    },
    platforms = "Linux, Mac OS X",
    description = "Jupyter Admin"
    )

# Data files e.g. templates and static js

share_jupyter_admin = pjoin(here, 'share', 'jupyter-admin')

def get_data_files():
    """Get data files in share/jupyter_admin"""
    data_files = []
    ntrim = len(here + os.path.sep)
    for (d, _, filenames) in os.walk(share_jupyter_admin):
        data_files.append((d[ntrim:], [pjoin(d, f)[ntrim:] for f in filenames]))
    return data_files


def get_package_data():
    """Get package data"""
    package_data = {}
    return package_data


setup_metadata.update(dict(
    name = 'jupyter_admin',
    packages = find_packages(),
    package_data = get_package_data(),
    data_files = get_data_files(),
    install_requires = install_requires,
    extras_require = extras_require
))

setup(
    **setup_metadata
)
