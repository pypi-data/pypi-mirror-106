from setuptools import setup, find_packages
import pathlib

README = (pathlib.Path(__file__).parent / "README.md").read_text()

setup(
  name = 'installerapp',
  packages = find_packages(),
  version = '0.9.1', 
  license='MIT',
  description = 'Python module to build installer',
  long_description=README,
  long_description_content_type="text/markdown",
  author = 'Alex',
  author_email = 'alexandre@hachet.com',
  url = 'https://github.com/novus-alex/InstallerApp',
  download_url = 'https://github.com/novus-alex/InstallerApp/archive/refs/tags/0.2.tar.gz',    # I explain this later on
  keywords = ['INSTALLER'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'tk',
          'requests',
          'pillow',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',     #Specify which pyhton versions that you want to support
  ],
)
