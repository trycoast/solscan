from setuptools import setup

import solscan


def readme():
    '''Read README file'''
    with open('README.rst') as file:
        return file.read()


setup(
    name='solscan',
    version=solscan.__version__,
    description='Simple python API wrapper for https://solscan.io',
    long_description=readme().strip(),
    author='',
    author_email='',
    url='https://github.com/trycoast/solscan',
    license='MIT',
    packages=['solscan'],
    install_requires=['requests', 'tenacity', 'ratelimit @ git+https://github.com/trycoast/ratelimit.git'],
    keywords=[
        'api',
        'solana',
        'solscan',
        'crypto'
    ],
    include_package_data=True,
    zip_safe=False
)
