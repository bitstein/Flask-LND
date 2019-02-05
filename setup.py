"""
Flask-LND
-------------

Flask-LND initializes an LND gRPC interface that can be used across your app
for communicating with a local or remote LND node.
"""
from setuptools import setup


setup(
    name='Flask-LND',
    version='0.0.1',
    url='https://github.com/bitstein/flask-lnd',
    license='MIT',
    author='Michael Goldstein',
    author_email='michael@bitstein.org',
    description='An LND gRPC interface for Flask',
    long_description=__doc__,
    py_modules=['flask_lnd'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'lnd-grpc'
    ],
    keywords="lnd grpc flask",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
