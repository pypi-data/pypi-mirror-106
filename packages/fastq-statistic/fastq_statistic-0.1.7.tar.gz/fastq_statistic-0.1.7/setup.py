# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastq_statistic']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.3.3,<4.0.0',
 'numpy>=1.19.5,<2.0.0',
 'pandas>=1.2.1,<2.0.0',
 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['fastq-stat = fastq_statistic.main:app']}

setup_kwargs = {
    'name': 'fastq-statistic',
    'version': '0.1.7',
    'description': '',
    'long_description': 'Fastq Statistic\n===============\nCalculate statistics for Fastq Files.  \n\n# Requirement\nPython: 3.8 or upper  \n\n# Install\nDownload the release whl file.  \n\n```bash\nuser@linux:~$ python3 -m pip install fastq-statistic\n```\n\n# Usage\n```bash\nuser@linux:~$ fastq-stat --help\nUsage: fastq-stat [OPTIONS] READ1 [READ2]\n\nArguments:\n  READ1    Read1 fastq path or fastq path  [required]\n  [READ2]  Read2 filepath or None\n\nOptions:\n  --sampleid TEXT                 SampleID, default is the first item of\n                                  filename splited by underscore(_)\n\n  --result PATH                   Result csv file name, plot with use the same\n                                  name.\n\n  --reserve-data / --no-reserve-data\n                                  Reserve fastq statistic intermediate data.\n                                  [default: False]\n\n  --plot / --no-plot              Plot fastq statistic data.  [default: True]\n  --install-completion [bash|zsh|fish|powershell|pwsh]\n                                  Install completion for the specified shell.\n  --show-completion [bash|zsh|fish|powershell|pwsh]\n                                  Show completion for the specified shell, to\n                                  copy it or customize the installation.\n\n  --help                          Show this message and exit.\n\n```',
    'author': 'Mao Yibo',
    'author_email': 'maoyibo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/maoyibo/fastq_statistic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
