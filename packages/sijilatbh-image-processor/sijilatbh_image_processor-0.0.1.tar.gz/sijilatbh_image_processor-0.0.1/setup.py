from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Image Processor Function'
LONG_DESCRIPTION = 'The Functionality offers to process SearchCR images gathered via sijilat.bh'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="sijilatbh_image_processor",
    version=VERSION,
    author="Ayhan Dis",
    author_email="<disayhan@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python','pytesseract','pandas','numpy'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=['python', 'image processor for sijilat.bh'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)