from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="SearchFile",
      version="0.0.1",
      long_description=long_description,
      long_description_content_type="text/markdown",
      description="Search for files by the specified path.",
      author="Prudnikov Artem",
      author_email="artem_prudnikov_2002@mail.ru",
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3.9",
          "License :: OSI Approved :: MIT License",
      ],
      python_requires='>=3.9')
