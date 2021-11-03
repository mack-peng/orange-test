import os
import json

class DataHandler:
    _DATABASE_DIR = ""
    _DATABASE_NAME = 'app.json'
    _FILE_PATH = ""
    _json_data = {}

    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self._DATABASE_DIR = os.path.join(current_dir, 'database')
        file_path = os.path.join(self._DATABASE_DIR, self._DATABASE_NAME)
        self._FILE_PATH = file_path
        self._json_data = self._read(file_path)

    # 清空数据库
    def clear(self):
        self._write(self._FILE_PATH, {})

    # 查询
    def select(self, name):
        return self._json_data[name]

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

    # 执行完对数据的修改/新增/删除后需要执行close结束操作
    def close(self):
        self._write(self._FILE_PATH, self._json_data)

    def _read(self, file_path):
        with open(file_path, 'r') as load_f:
            load_dict = json.load(load_f)

        return load_dict

    def _write(self, file_path, json_data):
        with open(file_path, 'w') as dump_f:
            json.dump(json_data, dump_f)

