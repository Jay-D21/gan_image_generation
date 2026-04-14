from setuptools import setup, find_packages

setup(
    name='gan_image_generation',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    author='Jay',
    description='A production-ready ML pipeline',
)
