import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CL_Auto_Library-SIEQQC",
    version="0.0.2",
    author="sieqqc",
    author_email="sieqqc@gmail.com",
    description="A custom library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sieqqc/pilotproject",
    project_urls={
        "Bug Tracker": "https://github.com/sieqqc/pilotproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)