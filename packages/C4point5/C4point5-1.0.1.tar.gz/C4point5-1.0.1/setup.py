import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="C4point5", # Replace with your own username
    version="1.0.1",
    author="Abdullah Al Noman",
    author_email="nomancseku@gmail.com",
    description="An implementation of C4.5 Algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nomancseku/C4point5",
    project_urls={
        "Bug Tracker": "https://github.com/nomancseku/C4point5/issues",
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