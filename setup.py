from setuptools import setup, find_packages

setup(
    name="dj-pro",
    version="0.0.1",
    description="CLI to create Django projects.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["django>=5.0", "colorama>=0.4.6"],
    entry_points={
        "console_scripts": [
            "dj-pro=core.base:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
