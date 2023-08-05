import setuptools

setuptools.setup(
    name='micropattern',
    version="0.0.5",
    uthor='MicroPattern',
    description="A small helpers for our business",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=['pika==1.2.0', 'requests==2.24.0']
)
