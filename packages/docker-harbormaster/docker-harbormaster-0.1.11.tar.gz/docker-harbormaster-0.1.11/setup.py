# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['docker_harbormaster']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0', 'click>=7.1.2,<8.0.0', 'docker-compose>=1.29.1,<2.0.0']

entry_points = \
{'console_scripts': ['harbormaster = docker_harbormaster.cli:cli']}

setup_kwargs = {
    'name': 'docker-harbormaster',
    'version': '0.1.11',
    'description': 'A supervisor for docker-compose apps.',
    'long_description': 'Harbormaster\n============\n\nHarbormaster is a small utility that lets you easily deploy multiple\nDocker-Compose applications.\n\n\n## Installation\n\nInstalling Harbormaster is simple. You can use `pipx` (recommended):\n\n```\n$ pipx install docker-harbormaster\n```\n\nOr `pip` (less recommended):\n\n```\n$ pip install docker-harbormaster\n```\n\nYou need to also make sure you have `git` installed on your system.\n\n\n## Usage\n\nHarbormaster uses a single YAML configuration file that\'s basically a list of\nrepositories containing `docker-compose.yml` files/apps to deploy:\n\n```yaml\napps:\n  myapp:\n    # The git repository URL to clone.\n    url: https://github.com/someuser/somerepo.git\n    # Which branch to deploy.\n    branch: main\n    # The environment variables to run Compose with.\n    environment:\n      FOO: bar\n      MYVAR: 1\n    # A file to load environment variables from. The file must consist of lines\n    # in the form of key=value. The filename is relative to the Harbormaster\n    # config file (this file).\n    # Variables in the `environment` key above take precedence over variables\n    # in the file.\n    environment_file: "somefile.txt"\n  otherapp:\n    url: https://gitlab.com/otheruser/otherrepo.git\n    # The Compose config filename, if it\'s not docker-compose.yml.\n    compose_filename: mydocker-compose.yml\n    # A dictionary of replacements (see below).\n    replacements:\n      MYVOLUMENAME: volume\n    # A file containing replacements. Works in the exact same way as the\n    # `environment_file` above.\n    replacements_file: "otherfile.txt"\n  oldapp:\n    # This is an old app, so it shouldn\'t be run.\n    enabled: false\n    # Two apps can use the same repo.\n    url: https://gitlab.com/otheruser/otherrepo.git\n```\n\nThen, just run Harbormaster in the same directory as that configuration file.\nHarbormaster will parse the file, automatically download the repositories\nmentioned in it (and keep them up to date).\n\nHarbormaster only ever writes to the working directory you specify, and nowhere\nelse. All the data for each Compose app is under `<workdir>/data/<appname>`, so\nyou can easily back up the entire data directory in one go.\n\n**WARNING:** Make sure the Compose config in each of the repos does not use\n`container_name`, otherwise Harbormaster might not always be able to terminate\nyour apps when necessary.\n\n\n## Handling data directories\n\nDue to the way Compose files work, you need to do some extra work to properly\ntell Harbormaster about your volumes.\n\nHarbormaster provides two kinds of directories: Data and cache.\n\nData is anything that you want to keep. Data directories will never be deleted,\nif you remove an app later on, its corresponding data directory will be moved\nunder the `archives/` directory and renamed to `<appname>-<deletion date>`.\n\nCache is anything you don\'t care about. When you remove an app from the config,\nthe cache dir is deleted.\n\nHarbormaster will look for a file called `docker-compose.yml` at the root of the\nrepo, and look for the specific strings `{{ HM_DATA_DIR }}` and\n`{{ HM_CACHE_DIR }}` in it. It will replace those strings with the proper\ndirectories (without trailing slashes), so the `volumes` section of your\nCompose file in your repository needs to look something like this:\n\n```yaml\nvolumes:\n  - {{ HM_DATA_DIR }}/my_data:/some_data_dir\n  - {{ HM_DATA_DIR }}/foo:/home/foo\n  - {{ HM_CACHE_DIR }}/my_cache:/some_cache_dir\n```\n\n\n### Replacements\n\nSometimes, the user needs to give access to paths that already exist on their\nsystem, or specify more parameters in the Dockerfile. This is where replacements\ncome in.\n\nReplacements are basically custom replacement strings (like the data directory\nstrings) that you can specify yourself.\n\nFor example, if the user needs to specify a directory with their media, you can\nask them to include a replacement called `MEDIA_DIR` in their Harbormaster\nconfig file, and then use the string `{{ HM_MEDIA_DIR }}` in your Compose file\nto mount the volume, like so:\n\n```yaml\nvolumes:\n  - {{ HM_MEDIA_DIR }}:/some_container_dir\n```\n\nHarbormaster will replace that string wherever in the file it finds it (not\njust the `volumes` section, and the user can specify it in their Harbormaster\nconfig like so:\n\n\n```yaml\nsomeapp:\n  url: https://gitlab.com/otheruser/otherrepo.git\n  replacements:\n    MEDIA_DIR: /media/my_media\n```\n\nKeep in mind that if the variable is called `VARNAME`, the string that will end\nup being replaced is `{{ HM_VARNAME }}`. If the variable is not found, it will\nnot be replaced or touched at all. This is to avoid messing with any unrelated\ntemplates in the Compose file.\n\nAlso, note that replacements will be written on disk, in the Compose config\nfile. If, for some reason, you want to avoid that (e.g. if you have secrets you\ndon\'t want exposed), try to use environment variables instead.\n',
    'author': 'Stavros Korokithakis',
    'author_email': 'hi@stavros.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/stavros/harbormaster',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
