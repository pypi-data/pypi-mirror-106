# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['binarysearchsimulation']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['binarysearchsimulation = '
                     'binarysearchsimulation.command_line:main']}

setup_kwargs = {
    'name': 'binarysearchsimulation',
    'version': '1.0.1',
    'description': 'Python program to visualize the behavior of upper_bound and lower_bound binary searches.',
    'long_description': '# Binary Search Simulation\n\nPython program to visualize the behavior of upper_bound and lower_bound binary searches.\n\n<table>\n  <tr>\n    <th>Upper Bound</th>\n    <th>Lower Bound</th>\n  </tr>\n  <tr>\n    <td>\n      <img src="https://searleser97.github.io/BinarySearchSimulation/upper_bound.png" width="250" height="400" />\n    </td>\n    <td>\n      <img src="https://searleser97.github.io/BinarySearchSimulation/lower_bound.png" width="250" height="400" />\n    </td>\n  </tr>\n</table>\n\n<table>\n<tr>\n<th colspan="2">Intuitive Binary Search</th>\n<tr>\n<tr>\n<th>Upper Bound</th>\n<th>Lower Bound</th>\n</tr>\n<tr>\n<td>\n\n```cpp\nint upperBound(vector<int> &array, int target) {\n  // array should be sorted in non-decreasing\n  // order from left to right\n  int l = 0, r = array.size() - 1;\n  while (l <= r) {\n    int mid = l + (r - l) / 2;\n    if (target < array[mid]) {\n      r = m - 1;\n    } else {\n      l = m + 1;\n    }\n  }\n  return l;\n}\n```\n\n</td>\n<td>\n\n```cpp\nint lowerBound(vector<int> &array, int target) {\n  // array should be sorted in non-decreasing\n  // order from left to right\n  int l = 0, r = array.size() - 1;\n  while (l <= r) {\n    int mid = l + (r - l) / 2;\n    if (target <= array[mid]) {\n      r = m - 1;\n    } else {\n      l = m + 1;\n    }\n  }\n  return l;\n}\n```\n\n</td>\n</tr>\n</table>\n\n<table>\n<tr>\n<th colspan="2">Binary Search Variation (works optimally for non-integer spaces)</th>\n<tr>\n<th>Upper Bound</th>\n<th>Lower Bound</th>\n</tr>\n<tr>\n<td>\n\n```cpp\nint upperBound(vector<int> &array, int target) {\n  // array should be sorted in non-decreasing\n  // order from left to right\n  int l = -1, r = array.size();\n  while (l + 1 < r) {\n    int mid = l + (r - l) / 2;\n    if (target < array[mid]) {\n      r = m;\n    } else {\n      l = m;\n    }\n  }\n  return r;\n}\n```\n\n</td>\n<td>\n\n```cpp\nint lowerBound(vector<int> &array, int target) {\n  // array should be sorted in non-decreasing\n  // order from left to right\n  int l = -1, r = array.size();\n  while (l + 1 < r) {\n    int mid = l + (r - l) / 2;\n    if (target <= array[mid]) {\n      r = m;\n    } else {\n      l = m;\n    }\n  }\n  return r;\n}\n```\n\n</td>\n</tr>\n</table>\n',
    'author': 'searleser97',
    'author_email': 'serchgabriel97@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/searleser97/BinarySearchSimulation',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
