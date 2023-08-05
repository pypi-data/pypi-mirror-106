import setuptools
from glob import glob

__package_name__ = "autoserve"
__version__ = "1.0"
__repository_url__ = ""
__download_url__ = ""

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name=__package_name__,
    version=__version__,
    license='MIT',
    author="subhrajit",
    author_email="techbiglover@gmail.com",
    description="Model Serving Automation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__repository_url__,
    download_url = __download_url__,
    packages=setuptools.find_packages(
        exclude=(
            "test.py"
            )
        ),
    include_package_data=True,
    data_files=[
        ('DB', glob('autoserve/meta/*.db')),
    ],
    entry_points={
        "console_scripts": [
            "autoserve=autoserve.__main__:app",
        ],
    },
    python_requires='>=3.7, <4',
    install_requires = required
)