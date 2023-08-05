from setuptools import setup, find_packages

with open("README.md", "r") as rd:
    long_description = rd.read()
with open("requirements.txt", "r") as req:
    requirements = req.readlines()
    print(requirements)
setup(
    name="github-info.py",
    version="1.0.0",
    description="A GitHub API wrapper that allows you to get info on users and organisations",
    url="https://github.com/cxllm/github-info.py",
    author="Callum",
    author_email="me@cxllm.xyz",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    keywords=["github", "api", "git", "github api"],
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests>=2.25.1", "python-dateutil>=2.8.1"],
)
