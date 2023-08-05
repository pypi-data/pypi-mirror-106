from setuptools import setup

setup(
    name='sunnybeamtool',
    version='0.0.1',    
    description='SMA Sunny Beam Tool',
    url='https://github.com/dannerph/SunnyBeamToolPython',
    author='Philipp Danner',
    author_email='philipp@danner-web.de',
    license='LGPL',
    packages=['sunnybeamtool'],
    install_requires=['crcmod>=1.7',
                      'pyusb>=1.1.1',                    
                      ],

    classifiers=[
    ],
)
