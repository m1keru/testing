from setuptools import setup, find_packages

setup(
    name='tyurhub',
    version='0.1',
    long_description=__doc__,
    include_package_data=True,
    zip_safe=False,
    install_requires=['os'],
    packages=find_packages()
)
