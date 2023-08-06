from setuptools import setup
with open('Readme.md', 'r') as op:
    data = op.read()
setup(
    name = 'csvreader',
    version = '0.0.2',
    description = 'A Library that Reads and Writes CSV Files Quickly.',
    long_description = data,
    long_description_type = 'text/markdown',
    author = 'SF Publishing',
    install_requires = ['pip','setuptools','wheel','virtualenv'],
    packages = ['csvreader']
)