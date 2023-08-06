# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['numpickle']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.2,<2.0.0', 'pandas>=1.2.4,<2.0.0']

setup_kwargs = {
    'name': 'numpickle',
    'version': '0.1.2.post6',
    'description': 'Faster loading of pandas data frames by saving them as numpy arrays and pickling their meta info (row+column names, column dtype info).',
    'long_description': '\n# numpickle\n\nFaster loading of pandas data frames by saving them as numpy arrays and pickling their meta info (row+column names, column dtype info).\n\n## Install\n\n```pip install numpickle```\n\n## Usage\n\n```\nimport pandas as pd\nimport numpickle as npl\n\n\n# create example data frame with non-numeric and numeric columns\ndf = pd.DataFrame([[1, 2,\'a\'], [3, 4, \'b\']])\ndf.columns = ["A", "B", "C"]\ndf.index = ["row1", "row2"]\n\ndf\n#       A  B  C\n# row1  1  2  a\n# row2  3  4  b\n\ndf.dtypes\n# A     int64\n# B     int64\n# C    object\n# dtype: object\n\n\n\n\n# save data frame as numpy array and pickle row and column names\n# into helper pickle file "/home/user/test.npy.pckl"\nnpl.save_numpickle(df, "/home/user/test.npy")\n\n# load the saved data\ndf_ = npl.load_numpickle("/home/user/test.npy")\n\ndf_\n#       A  B  C\n# row1  1  2  a\n# row2  3  4  b\n\n\ndf_.dtypes\n# A     int64\n# B     int64\n# C    object\n# dtype: object\n\nall(df == df_)\n# True\n\n```\n\n\n',
    'author': 'Gwang-Jin Kim',
    'author_email': 'gwang.jin.kim.phd@gmail.com',
    'maintainer': 'Gwang-Jin Kim',
    'maintainer_email': 'gwang.jin.kim.phd@gmail.com',
    'url': 'https://github.com/gwangjinkim/numpickle',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
