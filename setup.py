from setuptools import setup, find_packages

setup(
  name="imgcompr",
  version='1.3',
  description='画像圧縮ツール',
  author='Naoki Ito',
  url='https://github.com/naoki-00-ito/image-compression',
  packages=find_packages(),
  entry_points={
    'console_scripts':[
      'imgcompr = imgcompr.cli:execute',
    ],
  },
  install_requires=open('requirements.txt').read().splitlines(),
)