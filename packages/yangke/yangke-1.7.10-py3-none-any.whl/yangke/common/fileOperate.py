import pandas as pd
import pickle
import re
import os
import time
import datetime

from yangke.base import add_sep_to_csv


def get_last_modified_time(file: str):
    last_change_time = os.stat(file).st_mtime
    last_change_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(last_change_time))
    last_change_time = datetime.datetime.strptime(last_change_time_str, "%Y-%m-%d %H:%M:%S")
    return last_change_time


class re_common:
    """
    常见正则表达式的操作

    Example:
        1. 需要删除括号及括号中的内容，则使用以下语句：

        re = fo.re_common("前者多指对文章（书籍）中某一部分，但为了防止冗杂而把它放在段落之外（文末或页边）")
        result = re.del_char_in_brackets("（", "）")


    """

    def __init__(self, content):
        """
        用需要处理的目标字符串初始化re_common类对象

        :param content: 需要处理的目标字符串
        """
        self.content = content

    def del_char_in_brackets(self, left="(", right=")"):
        """
        如果content中包含括号，则删除括号及括号中的内容。

        :param left: 左括号的字符，如【、{、（、<、<-、《等
        :param right: 右括号的字符
        :return:
        """
        content_ = self.content
        result = re.match(f".*{left}.+{right}.*", content_)  # 判断content中是否存在（）
        while result:
            temp_list = list(re.findall(f"(.*){left}.+{right}(.*)", content_)[0])  # 正则中()中的内容会保留
            temp_list = [item for item in temp_list if item != ""]  # 删掉空字符串
            content_ = "".join(temp_list)  # 拼接起来
            result = re.match(f".*{left}.+{right}.*", content_)  # 判断content中是否存在（），存在就继续去除
        self.content = content_
        return self.content


def read_data(file, encoding="utf8"):
    """
    读取股票数据的csv文件内容到
    :param file:
    :param encoding:
    :return:
    """
    f = open(file)
    df = pd.read_csv(f, encoding=encoding)
    data_local = df.iloc[:, 1:6]
    return data_local.values


def writeLine(file: str, line: str, encoding="utf8", append=False):
    """
    将字符串line内容写入文件，如果文件不存在则创建，如果文件存在，默认覆盖原文件，可以通过设置append=True实现追加文本
    """
    mode = 'a' if append else 'w'
    with open(file, encoding=encoding, mode=mode) as f:
        f.write(line)


def writeLines(file: str, lines: list, encoding="utf8", append=False):
    """
    将字符串列表写入文件，每个列表项为单独一行
    """
    import os
    mode = 'a' if append else 'w'
    lines = os.linesep.join(lines)  # 列表项之间添加换行符
    with open(file, encoding=encoding, mode=mode) as f:
        f.writelines(lines)


def readLines(file: str, encoding="utf8"):
    with open(file, encoding=encoding, mode='r')as f:
        f.readlines()


def readPoints(file: str, split=',', return_type='[x][y][z]'):
    """
    从txt文件中读取点坐标

    :param file:
    :param split:
    :param return_type: '[x][y][z]'则返回x,y,z三个列表，如果是'[xyz]'则返回[x,y,z]形式的点坐标列表
    :return:
    """
    points = []
    x, y, z = [], [], []
    with open(file, mode='r')as f:
        for line in f.readlines():
            coor = line.split(split)
            px = float(coor[0])
            py = float(coor[1])
            pz = float(coor[2])
            points.append([px, py, pz])
            x.append(px)
            y.append(py)
            z.append(pz)

    if return_type == '[xyz]':
        return points
    else:
        return x, y, z


def writeAsPickle(file: str, obj: object):
    """
    保存任意对象到硬盘文件，obj是函数对象时，保存的是函数的名称和地址，无法在应用重启后加载原函数。
    如果需要保存函数，请使用write_func(file: str, func: object)

    :param file:
    :param obj:
    :return:
    """
    with open(file, 'wb') as f:
        pickle.dump(obj, f)


def readFromPickle(file: str, auto_create=True):
    """
    从硬盘文件加载pickle对象，obj是函数对象时，请使用read_func(file: str, func: object)

    :param file: 硬盘文件
    :param auto_create: 文件不存在时返回空
    :return:
    """
    if not os.path.exists(file):  # 文件不存在，返回None
        return None
    with open(file, 'rb') as f:
        obj = pickle.load(f)
    return obj


def write_func(file: str, func: object):
    """
    保存python函数或方法到硬盘，以便应用重启后直接加载

    :param file: 保存到的文件名
    :param func: 需要保存的函数名
    :return:
    """
    import dill
    writeAsPickle(file, dill.dumps(func))


def read_func(file: str):
    """
    从硬盘文件中加载函数对象

    :param file:
    :return:
    """
    import dill
    return dill.loads(readFromPickle(file))


def readFromYAML(file: str, encoding="utf8"):
    import yaml
    if not os.path.exists(file):  # 文件不存在，返回空字典
        return {}
    with open(file, 'r', encoding=encoding) as f:
        content = f.read()
    """
    Loader的几种加载方式 
    BaseLoader--仅加载最基本的YAML 
    SafeLoader--安全地加载YAML语言的子集。建议用于加载不受信任的输入。 
    FullLoader--加载完整的YAML语言。避免任意代码执行。这是当前（PyYAML 5.1）默认加载器调用 
            yaml.load(input)（发出警告后）。
    UnsafeLoader--（也称为Loader向后兼容性）原始的Loader代码，可以通过不受信任的数据输入轻松利用。"""
    obj = yaml.load(content, Loader=yaml.FullLoader)
    return obj


def read_csv_ex(file, sep=",", header="infer", skiprows=None, error_bad_lines=True, nrows=None, index_col=None):
    """
    pandas增强版的read_csv()方法，可以自动匹配任何文件编码
    :param file:
    :param sep:
    :param header:
    :param error_bad_lines:
    :return:
    """
    encoding_csv = "utf-8"
    try:
        data = pd.read_csv(file, sep=sep, header=header, error_bad_lines=error_bad_lines, encoding=encoding_csv,
                           skiprows=skiprows, nrows=nrows, index_col=index_col)
    except UnicodeDecodeError:
        encoding_csv = "gb18030"
        try:
            data = pd.read_csv(file, sep=sep, header=header, error_bad_lines=error_bad_lines, encoding=encoding_csv,
                               skiprows=skiprows, nrows=nrows, index_col=index_col)
        except UnicodeDecodeError:
            encoding_csv = "utf-16"
            data = pd.read_csv(file, sep=sep, header=header, error_bad_lines=error_bad_lines, encoding=encoding_csv,
                               skiprows=skiprows, nrows=nrows, index_col=index_col)
    except pd.errors.ParserError:
        # 说明pandas发现列数不一致，导致报错
        to_file = os.path.join(os.path.dirname(file), f"{os.path.basename(file).split('.')[0]}_add_sep.csv")
        add_sep_to_csv(file, sep, to_file=to_file)
        data = read_csv_ex(file=to_file, sep=sep, header=header, skiprows=skiprows, error_bad_lines=error_bad_lines,
                           nrows=nrows, index_col=index_col)
        os.remove(to_file)
    return data
