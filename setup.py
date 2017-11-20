from distutils.core import setup

setup(
    name="pdfOffnen",
    version='0.1.0',
    author="VulcanoAhab",
    packages=["pdfOffnen"],
    url="https://github.com/VulcanoAhab/pdfOffner.git",
    description="Browsers Utils",
    install_requires=[
        "pdfminer.six==20170720",
        ]
)
