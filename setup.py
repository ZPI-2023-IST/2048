# setup.py
import setuptools

setuptools.setup(
    name="game2048",
    version="0.0.1",
    author="Mateusz",
    description="2048 game",
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
    py_modules=["code2048"],
    install_requires=open("requirements.txt").read().splitlines(),
    package_dir={"": "."},
)