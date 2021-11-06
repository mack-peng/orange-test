import os
import json

class DataHandler:
    _DATABASE_DIR = ""
    _DATABASE_NAME = 'app.json'
    _FILE_PATH = ""
    _json_data = {}

    def __init__(self, database_name='app'):
        self._DATABASE_NAME = database_name + '.json'

        current_dir = os.path.dirname(os.path.abspath(__file__))
        self._DATABASE_DIR = os.path.join(current_dir, 'database')
        file_path = os.path.join(self._DATABASE_DIR, self._DATABASE_NAME)
        self._FILE_PATH = file_path
        # 如果文件不存在，创建并写入{}
        if not os.path.exists(file_path):
            self.clear()
        self._json_data = self._read(file_path)

    # 清空数据库
    def clear(self):
        # 初始化类中管理的数据和文件数据
        self._json_data = {}
        self._write(self._FILE_PATH, {})

    # 查询
    def select(self, name):
        if name in self._json_data:
            return self._json_data[name]
        else:
            return 'None'

    def select_all(self):
        return self._json_data

    # 更新数组
    def insert_arr(self, name, value):
        json_data = self._json_data
        if name not in json_data:
            json_data[name] = []
        json_data[name].append(value)

    # 更新字符串
    def update(self, name, value):
        self._json_data[name] = value

    # 数字值自增
    def setInc(self, name):
        json_data = self._json_data
        if name not in json_data:
            json_data[name] = 0
        num = json_data[name]
        json_data[name] = num + 1

    # 数字值自减
    def setDec(self, name):
        json_data = self._json_data
        if name not in json_data:
            json_data[name] = 0
        num = json_data[name]
        json_data[name] = num - 1

    # 删除dict对象
    def delete(self, name):
        self._json_data.pop(name)

    # 数据写入文件，持久化。
    def write(self):
        self._write(self._FILE_PATH, self._json_data)

    def _read(self, file_path):
        with open(file_path, 'r') as load_f:
            load_dict = json.load(load_f)

        return load_dict

    def _write(self, file_path, json_data):
        with open(file_path, 'w') as dump_f:
            json.dump(json_data, dump_f)

# 单例模式
app_data_handler = DataHandler('app')
user_data_handler = DataHandler('user')
