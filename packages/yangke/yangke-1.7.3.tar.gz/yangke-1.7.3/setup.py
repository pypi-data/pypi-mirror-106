import setuptools
import os
from gettext import gettext as _

# 国际化：生成语言目录，需要确保相应目录已经创建
# python setup.py extract_messages -k _ --output-file locale/main.pot   # 生成模板，会覆盖已经存在的模板
# python setup.py init_catalog --domain main -l zh_CN -i locale/main.pot -d locale  # 生成po文件
# python setup.py compile_catalog --domain main -l zh_CN -d locale  # 等同上一句

# 发布wheel安装文件
# python setup.py sdist bdist_wheel
from yangke import __version__, extras_require

yangke_version = __version__
with open(os.path.join(os.path.dirname(__file__), 'README.txt'), "r", encoding="utf8") as fh:
    long_description = fh.read()

install_requires = [  # 申明依赖包，安装包时pip会自动安装
                       'pandas>=0.25.3',
                       'pyyaml>=5.2',
                       'json5>=0.8.5',
                       'dill>=0.3.3',  # 储存函数对象
                       'babel>=2.9',
                       'pathlib2',
                       'pillow>=7.0.0',
                       'pywin32',
                   ],

all_lib = []
for v in extras_require.values():
    all_lib.extend(v)
all_lib = list(set(all_lib))
extras_require['All'] = all_lib

setuptools.setup(
    name="yangke",  # 模块名
    version=yangke_version,
    packages=setuptools.find_packages(
        where="lib4python",
        exclude=['StockData', 'yangke..idea', 'yangke..git']),  # 这里输入Mod包文件目录
    # scripts=["main.py"],
    # py_modules: ["main.py"]  # 打包的*.py文件

    package_data={
        "include": ["*.txt", "*.rst", "*.html"],
        "exclude": ["*.msg"],
    },

    python_requires=">=3.6",

    # metadata to display on PyPI
    author="杨可",
    author_email="yangyangyangkekeke@qq.com",
    description=_("个人工具综合平台，包含常用工具，网络爬虫，知识图谱，神经网络预测等工具"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="yangke",
    url="http://localhost",
    project_urls={
        "Bug Tracter": "https://gitee.com/yangke02/lib4python",
        "Documentation": "https://gitee.com/yangke02/lib4python",
        "Source Code": "https://gitee.com/yangke02/lib4python",
        "Funding": "https://gitee.com/yangke02/lib4python",
    },
    classifiers=[  # 给pip工具一些额外的元数据信息，只是用来给pypi提供搜索依据的，对实际项目不做任何限制
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",

        "License :: Freely Distributable",
        "Natural Language :: Chinese (Simplified)",

        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires=install_requires,
    extras_require=extras_require,

    message_extractors={
        'yangke': [
            ('**.py', 'python', None),
            # ('**/templates/**.html', 'genshi', None),
            # ('**/templates/**.txt', 'genshi', {'template_class': 'genshi.template:TextTemplate'})
        ],
    },

)
