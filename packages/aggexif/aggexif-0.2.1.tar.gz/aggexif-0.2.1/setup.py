# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aggexif']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['aggexif = aggexif.main:main']}

setup_kwargs = {
    'name': 'aggexif',
    'version': '0.2.1',
    'description': "Aggregate Image's EXIF Tool",
    'long_description': '## Required\n- exiftool\n- poetry\n\n## Usage\n```\n$ poetry run main ~/dir/*.NEF\n---- CAMERA LIST ----\nNIKON Z 7: 276▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\nNIKON Z 6: 69▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n---- LENS LIST ----\nAF-S VR Zoom-Nikkor 70-300mm f/4.5-5.6G IF-ED: 213▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n                       NIKKOR Z 14-30mm f/4 S: 69▇▇▇▇▇▇▇▇\n                        NIKKOR Z 50mm f/1.8 S: 48▇▇▇▇▇\n       AF-S Zoom-Nikkor 80-200mm f/2.8D IF-ED: 13\n---- FOCAL LENGTH ----\n  10-15: 19▇▇▇▇▇▇▇▇▇▇▇\n  15-20: 7▇▇▇\n  20-24: 9▇▇▇▇▇\n  28-35: 34▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n  45-50: 48▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n  60-70: 54▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n  70-85: 30▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n 85-105: 13▇▇▇▇▇▇▇\n105-135: 11▇▇▇▇▇\n135-200: 18▇▇▇▇▇▇▇▇▇▇\n200-300: 100▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n```\n\n## Help\n```\n$ poetry run main -h\nusage: Aggregate EXIF [-h] [-w WIDTH] [-l [LENS ...]] [-c [CAMERA ...]]\n                      [paths ...]\n\npositional arguments:\n  paths                 images paths\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -w WIDTH, --width WIDTH\n                        print width\n  -l [LENS ...], --lens [LENS ...]\n                        select lens\n  -c [CAMERA ...], --camera [CAMERA ...]\n                        select camera\n```\n\n## Tested Camera\n- Nikon Z6/Z7(+FTZ)\n- SONY A7C/A7III\n- OLYMPUS E-PL10\n- Panasonic GX7MK3(GX9)\n- Canon EOS-RP\n',
    'author': 'ponkotuy',
    'author_email': 'web@ponkotuy.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ponkotuy/python-exif',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
