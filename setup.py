from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in secure_customer_app/__init__.py
from secure_customer_app import __version__ as version

setup(
	name="secure_customer_app",
	version=version,
	description="encryption of customer details in customer doctype",
	author="omar hatem",
	author_email="omarhatem9182@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
