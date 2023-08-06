from setuptools import setup


setup(
    name="pymd5search",
    version="0.0.1",
    description="pymd5search loops and tries to find a string which equals to itself when encoded with the md5 hash function",
    long_description="The complete description/installation/use/FAQ is available at : https://github.com/thib1984/pymd5search#readme",
    url="https://github.com/thib1984/pymd5search",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="MIT",
    packages=["pymd5search"],
    install_requires=[],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "pymd5search=pymd5search.__init__:pymd5search"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
