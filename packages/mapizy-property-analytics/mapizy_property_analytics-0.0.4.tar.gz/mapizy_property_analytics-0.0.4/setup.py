from setuptools import setup
from setuptools import find_packages, setup

setup(
    name='mapizy_property_analytics',
    version='0.0.4',    
    description='A example Python package',
    url='https://mapizy-studio.com',
    author='Milad Ghorbani',
    author_email='mi.ghorbani.g@gmail.com',
    license='MIT',
    packages=find_packages(include=['mapizy_property_analytics']),
    install_requires=['requests',
                      'datetime'                  
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)