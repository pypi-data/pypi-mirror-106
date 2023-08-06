# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()


setup_args = dict(
    name='eeg-preprocessing',
    version='0.2.1',
    description='Semiautomatic framework for preprocessing EEG data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Szonja Weigl',
    author_email='weigl.anna.szonja@gmail.com',
    url='https://github.com/weiglszonja/eeg-preprocessing',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['mne', 'PyQt5', 'scipy', 'pandas', 'autoreject', 'jupyter',
                      'joblib', 'sklearn', 'matplotlib', 'ipyfilechooser'],
)


if __name__ == '__main__':
    setup(**setup_args)
