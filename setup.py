from setuptools import setup, find_packages

setup(
	name="imgcompr",
	version='1.2',
  description='画像圧縮ツール',
  author='Ito Naoki',
  author_email='so30.itonaoki@gmail.com',
  url='https://github.com/ItoNaoki/image-compression',
  packages=find_packages(),
  entry_points={
    'console_scripts':[
      'imgcompr = imgcompr.cli:execute',
    ],
  },
  install_requires=open('requirements.txt').read().splitlines(),
)