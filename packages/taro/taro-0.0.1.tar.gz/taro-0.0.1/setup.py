import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="taro",
    version="0.0.1",
    author="Austin Poor",
    author_email="45295232+a-poor@users.noreply.github.com",
    description="A package for repeatable rectangular data transformations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a-poor/taro",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)

