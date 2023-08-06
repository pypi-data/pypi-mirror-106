from setuptools import setup, find_packages

setup(
    name = "testindatadev",
    version = "0.0.24",
    keywords = ["云测", "数据集","yuncedata", "testin", "testindatadev"],
    description = "云测数据 数据集管理平台pythonSDK",
    long_description = "file:README.md",
    license = "MIT Licence",

    url = "http://ai.testin.cn/",
    author = "hide-in-code",
    author_email = "hejinlong@testin.cn",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [
        "click",
        "minio",
        "qiniu",
        "requests",
    ]
)
