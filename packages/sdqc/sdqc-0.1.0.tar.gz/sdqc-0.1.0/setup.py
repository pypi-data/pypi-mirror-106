from setuptools import setup, find_packages

exec(open('sdqc/_version.py').read())

long_description = """Project Documentation: http://sdqc.readthedocs.org/"""

setup(
    name='sdqc',
    version=__version__,
    python_requires='>=3.7',
    author='Eneko Martin Martinez',
    author_email='eneko.martin.martinez@gmail.com',
    packages=find_packages(exclude=['docs', 'tests', 'dist', 'build']),
    url='https://gitlab.com/enekomartinmartinez/sdqc',
    license = 'MIT',
    description='System Dynamics Data Quality Check with Python',
    long_description=long_description,
    keywords=['System Dynamics', 'Vensim', 'Quality Check'],
    classifiers=[
    'Development Status :: 3 - Alpha',

    'Topic :: Scientific/Engineering :: Information Analysis',
    'Intended Audience :: Science/Research',

    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'pysd'
    ],
    include_package_data=True
)
