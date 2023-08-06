import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="aviv-aws-costexplorer",
    version="0.0.1",
    description="Aviv AWS CostExplorer python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aviv-group/aviv-aws-costexplorer",
    author="Jules Clement",
    author_email="jules.clement@aviv-group.com",
    packages=setuptools.find_packages(),
    install_requires=[
        "boto3>=1.16.51",
        "pandas>=1.1.4",
        "python-dateutil>=2.8",
        "numpy>=1.19.4"
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    extras_require={
        "datastore": [
            "awswrangler>=0.3"
        ]
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Typing :: Typed"
    ],
    use_2to3=False,
    zip_safe=False
)
