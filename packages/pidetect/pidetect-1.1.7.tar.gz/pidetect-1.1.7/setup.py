import setuptools

setuptools.setup(
    name="pidetect",
    version="1.1.7",
    description="python image detect lib",
    packages=['pidetect'],
    package_data={'pidetect': ['so/*']},
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)

