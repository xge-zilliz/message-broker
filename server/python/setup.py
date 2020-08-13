from setuptools import find_packages, setup

setup(
    name="server_client",
    author="Zilliz",
    author_email="support@zilliz.com",
    description="server python client",
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=['pulsar'],
)
