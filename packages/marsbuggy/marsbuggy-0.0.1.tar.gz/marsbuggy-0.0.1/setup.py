from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="marsbuggy",
    version="0.0.1",
    py_modules=["intro"],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[  # versions should be relaxed
        "numpy~=1.16.6",
    ],
    extras_require={  # versions should be specific
        "dev": [
            "pytest>=3.7",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
