from setuptools import setup, find_packages
import os

find_version='2.6.0'
if os.environ.get('CI_COMMIT_TAG'):
    find_version = os.environ['CI_COMMIT_TAG']



setup(
    name='mosaik-influxdb',
    version=find_version,
    author='Ahmad Ahmadi',
    author_email='ahmad.ahmadi0069@gmail.com',
    description=('Stores mosaik simulation data in an InfluxDB database.'),
    long_description=(open('README.rst').read() + '\n\n' +
                      open('CHANGES.txt').read() + '\n\n' +
                      open('AUTHORS.txt').read()),
    url='https://mosaik.offis.de',
    install_requires=[
        'mosaik-api>=2.3',
        'networkx>=2.0',
        'influxdb>=5.3',
        'simpy>=3.0.10,<4.0.0',
        'simpy.io>=0.2.3',

         

    ],
    packages=find_packages(exclude=['tests*']),
    py_modules=['mosaik_influxdb'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'mosaik-influxdb = mosaik_influxdb:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',

    ],
)
