import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="financeData",
    version="0.0.3",
    author="Berkay Coşkun",
    author_email="berkayreb@gmail.com",
    description="Basic Data Source For Stock,FX,Coin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires  = ['requests'], # List all your dependencies inside the list
    license = 'MIT'
)