from setuptools import setup, find_packages

setup(
    name='datachat',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'datachat=datachat.cli:main',
        ],
    },
)
