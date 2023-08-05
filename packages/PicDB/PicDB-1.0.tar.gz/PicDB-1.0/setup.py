from setuptools import setup


long_description = """
https://github.com/Ma-Mush/PicDB/
"""


setup(
    name="PicDB",
    version="1.0",
    description="DataBase in picture!?!?!??!?!!!",
    packages=["PicDB"],
    author_email="ma_mush@mail.ru",
    zip_safe=False,
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["Pillow==8.2.0", "numpy==1.20.3"]
)
