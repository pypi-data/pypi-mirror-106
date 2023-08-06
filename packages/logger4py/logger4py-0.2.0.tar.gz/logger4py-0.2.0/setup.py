from setuptools import setup


setup(
    name='logger4py',
    version='0.2.0',    
    description='Logging Python Package',
    url='https://gitlab.com/Mahmoudaouinti/logger4py.git',
    author='IoT Team',
    author_email='aouintimahmod@gmail.com',
    packages=['logger4py'],
    install_requires=[ 'watchdog'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',      
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    keywords='sample, setuptools, development',

)
