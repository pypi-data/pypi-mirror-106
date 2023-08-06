from setuptools import setup
import tp24

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'tp24',
  packages = ['tp24'],
  version = tp24.__version__+"",
  license ='gpl-3.0',
  description = 'Python colour library',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = '7d',
  author_email = 'i.third.7d@protonmail.com',
  url = 'https://github.com/iiiii7d/tp24',
  download_url = f'https://github.com/iiiii7d/tp24/archive/refs/tags/v{tp24.__version__}.tar.gz',
  keywords = ['tp24', 'colour', 'color'],
  python_requires='>=3.7',
  package_data={
    'tp24': ['model/*'],
  },
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    'Topic :: Utilities'
  ],
)

#commands for upload in case i forget
#python setup.py sdist
#python setup.py bdist_wheel
#twine upload dist/*