from setuptools import setup, find_packages

setup(
    name='bmi_calculator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flake8',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'bmi_calculator=bmi_calculator.main:main',
        ],
    },
)