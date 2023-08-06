from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
      name='diagnet',
      version='0.0.4',
      description='A python network diagnosis tool',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Joey Kennedy',
      author_email='joey.s.k.kennedy@gmail.com',
      url='https://github.com/slowpoke1214/Diagnet',
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      install_requires=[
            'scapy>=2.4.3',
            'prettytable>=2.1.0'
      ],
      package_dir={'': 'src'},
      packages=find_packages(where='src'),
      python_requires=">=3.6",
      entry_points={
            'console_scripts': [
                  'diagnet=src.__main__:main',
            ],
      }
     )
