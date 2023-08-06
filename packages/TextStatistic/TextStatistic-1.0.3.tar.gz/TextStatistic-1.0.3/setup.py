import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TextStatistic",
    version="1.0.3",
    author="Andrew Puchkov",
    author_email="andr1502puch@gmail.com",
    description="Text statistics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShadowStalker13/TextStatistics",
    classifiers=[
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3.9",
    ],
    package_dir={"": "scr"},
    packages=setuptools.find_packages(where="scr"),
)
