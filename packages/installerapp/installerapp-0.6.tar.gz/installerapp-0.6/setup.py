from setuptools import setup
import pathlib

README = (pathlib.Path(__file__).parent / "README.md").read_text()

setup(
  name = 'installerapp',         # How you named your package folder (MyLib)
  packages = ['installerapp'],   # Chose the same as "name"
  version = '0.6',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python module to build installer',   # Give a short description about your library
  long_description=README,
  long_description_content_type="text/markdown",
  author = 'Alex',                   # Type in your name
  author_email = 'alexandre@hachet.com',      # Type in your E-Mail
  url = 'https://github.com/novus-alex/InstallerApp',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/novus-alex/InstallerApp/archive/refs/tags/0.2.tar.gz',    # I explain this later on
  keywords = ['INSTALLER'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'tkinter',
          'threading',
          'requests',
          'urllib',
          'zipfile',
          'PIL',
          'shutil',
          'pythoncom',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)