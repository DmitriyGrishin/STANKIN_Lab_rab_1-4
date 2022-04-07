from setuptools import setup, find_packages

setup(
    name='elecwriter',
    version='0.1.0',
    py_modules=['elecwriter'],
    install_requires=[
        'pycryptodome'
    ],
    entry_points={
        'console_scripts': [
            'elecwriter = elecwriter:cli',
        ],
    },
)
