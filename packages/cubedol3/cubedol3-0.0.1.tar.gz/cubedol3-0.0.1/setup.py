from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'simple demo cube'
LONG_DESCRIPTION = 'simple demo for a cube class for pypi'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="cubedol3", 
        version=VERSION,
        author="David Lignell",
        author_email="<davidlignell@byu.edu>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        py_modules=['cubedol3'],
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'cubedol3'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
