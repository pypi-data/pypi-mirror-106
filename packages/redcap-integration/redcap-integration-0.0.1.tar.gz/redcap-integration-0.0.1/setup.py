import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redcap-integration",  # Replace with your own username
    version="0.0.1",
    author="Mehran Zolghadr",
    author_email="mehran@keyleadhealth.com",
    description="Redcap Integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IOMehran/redcap-integration",
    download_url="https://github.com/IOMehran/redcap-integration/archive/refs/tags/v0.0.1.tar.gz",
    project_urls={
        "Bug Tracker": "https://github.com/IOMehran/redcap-integration/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",

    install_requires=[
        "certifi==2020.12.5",
        "chardet==4.0.0",
        "idna==2.10",
        "PyCap==1.1.3",
        "python-dotenv==0.17.1",
        "requests==2.25.1",
        "semantic-version==2.8.5",
        "urllib3==1.26.4",
    ],
)
