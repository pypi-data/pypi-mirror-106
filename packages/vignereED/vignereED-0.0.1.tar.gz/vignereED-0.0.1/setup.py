from setuptools import setup
from distutils.core import setup
setup(
      name="vignereED",
      version="0.0.1",
      description="A Demo app for encryption and decryption of messages using vignere cipher",
      author="R.Raja Subramanian",
      author_email="rajasubramanian.r1@gmail.com",
      py_modules=["vignereED"],
      package_dir={"":"src"},
      include_package_data=True,
      )

