from setuptools import setup, find_packages

setup(
    name="hypogenai",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pdfplumber",
        "pandas"
    ],
    python_requires=">=3.8"
)
