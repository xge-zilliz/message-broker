from setuptools import find_packages, setup

setup(
    name="milvus_client",
    author="Zilliz",
    author_email="support@zilliz.com",
    description="milvus python client",
    packages=find_packages(),
    python_requires='>=3.6',
)
