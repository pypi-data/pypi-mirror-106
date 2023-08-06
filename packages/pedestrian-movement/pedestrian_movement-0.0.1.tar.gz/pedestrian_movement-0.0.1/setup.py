import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pedestrian_movement",
    version="0.0.1",
    author="Michael Hartmann",
    author_email="michael.hartmann@v2c2.at",
    description="Human Locomotion Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "GitHub": "https://github.com/ga74kud/pedestrian_movement.git",
        "Bug Tracker": "https://github.com/ga74kud/pedestrian_movement.git",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)