import subprocess
import os
from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

packages = find_packages(exclude=['tests*'])

remote_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

assert "." in remote_version
assert os.path.isfile("it_finance_api/version.py")

with open("it_finance_api/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{remote_version}\n")

setup(
    name='it_finance_api',
    version=remote_version,
    license='LGPLv3',

    author='Telnet Data',
    description='A wrapper for it finance data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/telnet-data/it-finance-api',

    packages=packages,
    package_data={"it_finance_api": ["VERSION"]},
    include_package_data=True,

    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],

    python_requires='>=3.6',
    install_requires=[
        'requests'
    ],
)