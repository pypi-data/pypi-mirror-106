from distutils.core import setup

setup(
    name="hypixelBazaar",
    packages=["hypixelBazaar"],
    version="0.1",
    license="MIT",
    description="Unofficial libraries for interacting with the official Hypixel bazaar API",
    author="Ben Snowden",
    author_email="benglensnowden@gmail.com",
    url="https://github.com/BenSnowden/hypixelBazaar.git",  # Provide either the link to your github or to your website
    download_url="https://github.com/BenSnowden/hypixelBazaar/archive/refs/tags/v_0.1.tar.gz",  # I explain this later on
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development" + " :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
)
