import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="localhost-on-colab",
    version="0.0.0",
    author="Mayukh Deb", 
    author_email="mayukhmainak2000@gmail.com", 
    description= "Helps you run localhost stuff on colab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mayukhdeb/localhost-on-colab",
    packages=setuptools.find_packages(),
    install_requires= required,
    python_requires='>=3.6',   
    include_package_data=True,
    classifiers=[
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)