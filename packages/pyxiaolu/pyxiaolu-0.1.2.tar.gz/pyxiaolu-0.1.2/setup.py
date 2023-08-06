import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyxiaolu",
    version="0.1.2",
    author="krishuang",
    author_email="huangzikun2008@hotmail.com",
    description="python库以在小陆同学上执行代码 | python library to execute code on 'xiaolu'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krishuang2008/pyxiaolu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=['requests'],
)