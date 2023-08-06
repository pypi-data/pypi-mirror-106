import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="guess_number-atalay",
    version="1.2",
    author="Atalay Denknalbant",
    author_email="atalaydenknalbant@hotmail.com",
    description="Guess the number game",
    long_description=long_description,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    license_files = ('LICENSE.txt'),
)
