"""
python-cbfeeds
"""

from setuptools import setup

setup(
    name='cbfeeds-fork',
    version='1.0.1',
    url='https://github.com/mlodic/cbfeeds',
    license='MIT',
    author='Matteo Lodi',
    description='Carbon Black Alliance Feeds Forked',
    long_description=__doc__,
    packages=['cbfeeds', ],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ], requires=['requests']
)
