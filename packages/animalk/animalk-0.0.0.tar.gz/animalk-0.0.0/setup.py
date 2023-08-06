import setuptools
import animals

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='animalk',
    version=animals.__version__,
    description='Please describe this',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CamiloCastellanos/PrimeraLibreriaPY',
    packages=setuptools.find_packages(
        exclude=['sphinx_docs', 'docs', 'tests']),
    python_requires='~=3.5',
    install_requires=[
        i.replace('\n', '')
        for i in open('requirements.txt', 'r').readlines()
    ],
    extras_require={
        'dev': ['setuptools', 'wheel', 'twine', 'Sphinx'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
