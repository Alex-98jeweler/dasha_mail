import re
from setuptools import setup, find_packages


def readme():
    with open('README.rst', 'r') as file:
        content = file.read()
    return content

def get_version():
    with open('src/dasha_mail/__init__.py') as fp:
        version = re.search(r"__version__\s*=\s*'(.*)'", fp.read()).group(1)
    return version


setup(
    name='dasha_mail',
    version=get_version(),
    author='Dashamail',
    author_email='support@dashamail.ru',
    description='Dasha Mail SDK',
    long_description=readme(),
    url='https://github.com/Alex-98jeweler/dasha_mail/',
    packages=find_packages('src'),
    package_dir={"": "src"},
    install_requires=['certifi', 'idna', 'requests', 'urllib3'],
    zip_safe=False,
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires='>=3.8',
)