from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name="basic_cowin_api",
    packages=['cowin_api'],
    license='GNU 3.0',
    version="0.0.201",
    description="Python wrapper for Indian CoWin API"
                "https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mayank Johri",
    author_email="mayankjohri@gmail.com",

    url="https://gitlab.com/mayankjohri/cowin_api",
    keywords=["cowin, covid, vaccine"],
    include_package_data=True,
    python_requires=">=3.6",

    install_requires=[
        "pytest",
        "requests"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],

    project_urls={
        "Bug Reports": "https://gitlab.com/mayankjohri/cowin_api/-/issues",
        "Source": "https://gitlab.com/mayankjohri/cowin_api",
    },
)
