import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="efficient-det",
    version="0.0.11",
    author="Zeynep Boztoprak",
    author_email="zeynep.boztoprak@hhu.de",
    description="Efficient-Det Implementation in Tensorflow Keras",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.hhu.de/zeboz100/efficientdet",
    project_urls={
        "Bug Tracker": "https://git.hhu.de/zeboz100/efficientdet/-/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},

    install_requires=[
        'tensorflow>=2.3.0',
        'tabulate',
        'ray[default]>=1.3.0',
        'ray[tune]',
        'matplotlib',
        'wandb',
        'pillow',
        'progressbar2',
        'pandas',
        'opencv-python'
    ],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

