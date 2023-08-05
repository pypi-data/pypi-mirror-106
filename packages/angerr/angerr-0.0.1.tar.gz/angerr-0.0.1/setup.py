from setuptools import setup

with open("README.md", "r") as f:
  long_description = f.read()

setup(
  name='angerr',
  version='0.0.1',
  description="When your coding doesn't work, simply call the rage function with the amount of your rage and you will feel much, much better.",
  py_modules=["anger"],
  package_dir={"": "src"},
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/MasterCoder21/anger",
  author="minecraftpr03",
  author_email=None,
  classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
  ]
)