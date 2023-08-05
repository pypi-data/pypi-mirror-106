import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pandasguard", # Replace with your own username
    version="0.1",
    author="Josh Anish",
    author_email="josh.anish1@gmail.com",
    description="pandas utilities",
    long_description="pandas utilities",
    long_description_content_type="text/markdown",
    url="https://github.com/anish9/pandas_guard",
    project_urls={
        "Bug Tracker": "https://github.com/anish9/pandas_guard/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas","tqdm"],
    package_dir={"": "src"},

    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",include_package_data=True
)