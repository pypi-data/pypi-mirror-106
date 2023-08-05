from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="encrypter_fernet_dr",
    version="0.0.1",
    description="Encrypt file using fernet",
    py_modules=["encrypter_fernet_dr"],
    package_dir={"":"src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require = {
        "dev": [
            "pytest>=3.7",
        ],
    },
    url="https://github.com/dav-rs/PythonPackage/tree/main/Encrypter",
    author="David Rios",
    author_email="hdavidrios@hotmail.com",
    # install_requires=["blessings ~= 1.7"] e.g. if blessings was required for the installation
)