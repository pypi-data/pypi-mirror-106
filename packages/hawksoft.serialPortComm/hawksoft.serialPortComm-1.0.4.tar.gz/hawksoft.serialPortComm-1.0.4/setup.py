from setuptools import setup, find_packages

setup(name='hawksoft.serialPortComm',
      version='1.0.4',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # 多文件模块写法
      author="xingyongkang",
      author_email="xingyongkang@cqu.edu.cn",
      description="Provides many useful command lines in python",
      long_description=open('./README.md', encoding='utf-8').read(),
      long_description_content_type = "text/markdown",
      #long_description="http://gitee.comg/xingyongkang",
      license="MIT",
      url = "https://gitee.com/xingyongkang/serialportcomm",
      include_package_data=True,
      platforms="any",
      #install_requires=['pyserial','pykonw'],
      install_requires=['pykonw'],
      keywords='serial port comm',
       entry_points={
          'console_scripts': [
              'traffic=hawksoft.trafficSign:main'
          ]
      },
)