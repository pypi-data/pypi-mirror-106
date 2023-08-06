import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="insertmendoza",
    version="1.0.8",
    author="Insert Mendoza",
    author_email="njavilas@insertmendoza.com.ar",
    description="Cliente para sarys 6.x",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/njavilas2015/sdk-python-v6",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["requests", "python-socketio"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)