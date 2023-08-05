import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    readme_md = fh.read()

setuptools.setup(
    name="example-pkg-trdlo",  # Replace with your own username
    version="0.0.3",
    author="Anatoliy Novoselov",
    author_email="avnovoselov@gmail.com",
    description="Example package based on packaging python tutorials",
    long_description=readme_md,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/avnovoselov/python-package-example",
    project_urls={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
