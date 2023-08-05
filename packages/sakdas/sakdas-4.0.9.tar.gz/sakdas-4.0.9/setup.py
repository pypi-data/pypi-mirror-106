import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sakdas", # Replace with your own username
    version="4.0.9",
    author="Sakda Loetpipatwanich",
    author_email="sakda.loet@gmail.com",
    description="A data profiling and data quality auditing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sakdaloe/sakdas",
    packages=setuptools.find_packages(),
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)