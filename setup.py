from setuptools import setup, find_packages

setup(
    name='trading212_py',
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    author='Serdar Baran',
    author_email='',
    description='An unofficial Python client for the T212 public API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/serdarbaran/trading212',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
