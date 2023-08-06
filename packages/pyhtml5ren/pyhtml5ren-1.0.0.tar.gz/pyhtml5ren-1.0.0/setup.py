
from setuptools import setup

setup(
    name='pyhtml5ren',
    version='1.0.0',
    description='A way to render html in python/tk',
    long_description='I will add, but for now, do: \n\nimport html5renderer as h5r; help(h5r)',
    install_requires=["selenium", "pillow"],
    packages=["html5renderer"]
    )

