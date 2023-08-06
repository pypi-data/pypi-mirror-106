import setuptools

with open("README.md", "r") as fhandle:
    long_description = fhandle.read() # Your README.md file will be used as the long description!

setuptools.setup(
    name="replitapi", # Put your username here!
    version="0.0.1", # The version of your package!
    author="Finnbar M", # Your name here!
    author_email="xfinnbar@gmail.com", # Your e-mail here!
    description="Tools for interacting with the replit site and database that do not depend on an ancient version of Flask.", # A short description here!
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://replit.com/@xfinnbar/Replit-API", # Link your package website here! (most commonly a GitHub repo)
    packages=setuptools.find_packages(), # A list of all packages for Python to distribute!
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], # Enter meta data into the classifiers list!
    python_requires='>=3.7', # The version requirement for Python to run your package!
    install_requires=[
          'requests',
          'bs4'
    ],
)
