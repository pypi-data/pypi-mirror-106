from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'MyPy1989 Python package'
LONG_DESCRIPTION = 'MyPy1989 Python package - dummy'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="mypy1989", 
        version=VERSION,
        author="saibabanadh konda",
        author_email="<saibabanadh@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'mypy1989 package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)