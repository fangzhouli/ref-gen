from setuptools import setup
from setuptools import find_packages

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name                            = 'ref-gen',
    version                         = '1.0.0',
    packages                        = find_packages(),
    entry_points                    = {
        'console_scripts' : ['ref-gen=refgen.cli.run:main']
    },
    description                     = 'Reference genome extraction package',
    author                          = 'Fangzhou Li',
    author_email                    = 'fzli0805@gmail.com',
    url = 'https://github.com/fangzhouli/ref-gen',
    keywords = ['reference-genome', 'ncbi'],
    install_requires                = [
        'pandas'
    ],
    long_description                = long_description,
    long_description_content_type   = 'text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)