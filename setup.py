import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ziim",
    version="0.0.9.2",
    scripts=['./scripts/ziim'],
    author="Sanix-darker",
    author_email="s4nixd@gmail.com",
    description="Let your CLI find available solutions for errors/exceptions in your code for you, "
                "no need open a Browser. and do something yourself, you just have to select the forum",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sanix-darker/ziim",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
