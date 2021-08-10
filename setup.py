from setuptools import setup
from os import path


current_dir = path.abspath(path.dirname(__file__))


with open("README.md", "r") as fh:
    long_description = fh.read()

with open(path.join(current_dir, 'requirements.txt'), 'r') as f:
    install_requires = f.read().split('\n')


setup(
    name='template_multi_level',
    version='0.0.1',
    author='Maryam Bahrami',
    author_email='maryami_66@yahoo.com',
    packages=['template_multi_level'],
    license='MIT',
    description='This is a template multi level python package.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    setup_requires='numpy',
    install_requires=install_requires,
    keywords='template library, template package, multi level library',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)