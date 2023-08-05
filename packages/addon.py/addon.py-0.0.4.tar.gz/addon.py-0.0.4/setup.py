import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="addon.py",
    version="0.0.4",
    author="svenskithesource, shizo",
    author_email="",
    description="An API Wrapper for addon.to's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/svenskithesource/addon.py",
    packages=["addon"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["requests", "python-dateutil"]
)
