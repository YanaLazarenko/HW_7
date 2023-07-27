from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1.1',
      description='sort folder into categories according to file"s type',
      url='https://github.com/YanaLazarenko/HW_7.git',
      author='Yana Lazarenko',
      author_email='yana0637007962@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires = 'markdown',
      entry_points = {'console_scripts': ['clean-folder = clean_folder.clean:main']} 
      )
