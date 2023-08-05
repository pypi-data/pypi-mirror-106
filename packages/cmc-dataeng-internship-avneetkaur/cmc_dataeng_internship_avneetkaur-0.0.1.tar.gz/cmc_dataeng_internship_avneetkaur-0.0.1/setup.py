from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Package for Excercise 13'
LONG_DESCRIPTION = 'Package for Excercise 13'

# Setting up
setup(
       
        name="cmc_dataeng_internship_avneetkaur", 
        version=VERSION,
        author="Avneet Kaur",
        author_email="<avneet14027@iiitd.ac.in>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)