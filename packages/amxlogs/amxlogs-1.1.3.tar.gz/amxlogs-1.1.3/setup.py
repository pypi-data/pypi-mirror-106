import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amxlogs",
    version="1.1.3",
    author="Logan Vaughn",
    # author_email="logantv@gmail.com",
    description="finds, downloads, and clears logs from AMX devices using ftp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/logantv/amxlogs",
    project_urls={
        "Bug Tracker": "https://github.com/logantv/amxlogs/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # install_requires=[
    #     "ftplib == *",
    # ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
