import setuptools

setuptools.setup(
    name="telethon-session-sqlalchemy-fork",
    version="0.2.16",
    url="https://github.com/tulir/telethon-session-sqlalchemy",

    author="Vitor Daniel",
    author_email="vitor036daniel@gmail.com",

    description="SQLAlchemy backend for Telethon session storage",
    long_description=open("README.rst").read(),

    packages=setuptools.find_packages(),

    install_requires=[
        "SQLAlchemy>=1.2,<2",
    ],

    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires="~=3.5",
)

