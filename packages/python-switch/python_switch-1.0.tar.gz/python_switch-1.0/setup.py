from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'python_switch',
  packages = ['python_switch'],
  version = '1.0',
  license='MIT',
  description = 'Python Switch Like JavaScript Switch Statement',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'isacolak',
  author_email = 'isacolak04@gmail.com',
  url = 'https://github.com/isacolak/python_switch',
  download_url = 'https://github.com/isacolak/python_switch/archive/python_switch_v_1.tar.gz',
  keywords = ["switch","python js switch","python javascript switch","python switch"],
  classifiers=[
    'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta", "5 - Production/Stable"
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ]
)