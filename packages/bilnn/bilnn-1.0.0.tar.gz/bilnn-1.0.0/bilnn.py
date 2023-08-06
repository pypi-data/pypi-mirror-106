#coding:utf-8
"""
本SDK由 异想之旅（比邻云盘用户 异想之旅王子） 基于官方SDK重写而成
https://www.bilnn.com/
"""

import base64
import os

import requests
import urllib
import xmltodict


class Bilnn:
    def __init__(self, username, password, show=True):
        self.username = username
        self.password = password
        self.secret_key = base64.encodebytes(
            ("%s:%s" % (username, password)).encode()).decode()[:-1]
        self.sdk_header = headers = {
            "Authorization": "Basic " + self.secret_key
        }
        if show:
            print("初始化成功！")
            print("本程序基于https://www.bilnn.com/官方接口，由异想之旅开发，源码地址https://github.com/Danny-Yxzl/bilnn-python-sdk")
            print("所有的云端路径都必须加前导的“/”！所有的本地路径必须是绝对路径！")
            print("若不希望看到此提示，请传入参数show=False")
        return

    def upload(self, local_path, cloud_path):
        if not os.path.isfile(local_path):
            return {
                "success": False,
                "code": 404,
                "msg": "本地文件不存在",
                "backdata": {
                    "localpath": local_path
                }
            }
        try:
            requests.put("https://pan.bilnn.com/dav" + cloud_path,
                         headers=self.sdk_header,
                         data=open(local_path, "rb"))
            return {
                "success": True,
                "code": 200,
                "msg": "文件上传成功",
                "backdata": {
                    "localpath": local_path,
                    "cloudpath": cloud_path
                }
            }
        except:
            return {
                "success": False,
                "code": 500,
                "msg": "文件上传失败",
                "backdata": {
                    "localpath": local_path,
                    "cloudpath": cloud_path
                }
            }

    def get_url(self, cloud_path):
        data = {"secret_key": self.secret_key, "filePath": cloud_path}
        try:
            r = requests.post(
                "https://pan.bilnn.com/app/index.php?c=api&a=getDownLoadUrl",
                data=data,
                headers=self.sdk_header)
            return {
                "success": True,
                "code": 500,
                "msg": "外链获取成功",
                "backdata": {
                    "cloudpath": cloud_path,
                    "url":
                    "https://pan.bilnn.com" + r.json()["backdata"]["url"]
                }
            }
        except:
            return {
                "success": False,
                "code": 200,
                "msg": "外链获取失败",
                "backdata": {
                    "cloudpath": cloud_path
                }
            }

    def delete(self, cloud_path):
        try:
            r = requests.delete("https://pan.bilnn.com/dav" + cloud_path,
                            headers=self.sdk_header)
            if r.text == "Not Found":
                return {
                    "success": False,
                    "code": 404,
                    "msg": "文件或文件夹不存在",
                    "backdata": {
                        "cloudpath": cloud_path
                    }
                }
            else:
                return {
                    "success": True,
                    "code": 200,
                    "msg": "删除文件或文件夹成功",
                    "backdata": {
                        "cloudpath": cloud_path
                    }
                }
        except:
            return {
                "success": False,
                "code": 500,
                "msg": "删除文件或文件夹失败",
                "backdata": {
                    "cloudpath": cloud_path
                }
            }

    def list_dir(self, cloud_path="/"):
        try:
            r = requests.request("propfind",
                                 "https://pan.bilnn.com/dav" + cloud_path,
                                 headers=self.sdk_header)
            result = []
            data = dict(
                xmltodict.parse(urllib.parse.unquote(r.text),
                                process_namespaces=True))
            data = dict(data["DAV::multistatus"])["DAV::response"]
            for i in data:
                temp = dict(i)
                filesize = dict(dict(i["DAV::propstat"])["DAV::prop"]).get(
                    "DAV::getcontentlength")
                result.append({
                    "filename":
                    i["DAV::href"],
                    "is_folder":
                    False if filesize else True,
                    "filesize":
                    filesize or 0,
                    "lastmodified":
                    dict(dict(i["DAV::propstat"])["DAV::prop"])
                    ["DAV::getlastmodified"]
                })
            return {
                "success": True,
                "code": 200,
                "msg": "文件目录获取成功",
                "backdata": {
                    "cloudpath": cloud_path,
                    "list": result
                }
            }
        except:
            return {
                "success": False,
                "code": 401,
                "msg": "请检查账号、密码或路径是否正确",
                "backdata": {
                    "cloudpath": cloud_path,
                }
            }

    def make_dir(self, cloud_path):
        try:
            r = requests.request("mkcol",
                                "https://pan.bilnn.com/dav" + cloud_path,
                                headers=self.sdk_header)
            if r.text == "Created":
                return {
                    "success": True,
                    "code": 200,
                    "msg": "文件夹创建成功",
                    "backdata": {
                        "cloudpath": cloud_path
                    }
                }
            else:
                return {
                    "success": False,
                    "code": 500,
                    "msg": "文件夹创建失败，可能已存在",
                    "backdata": {
                        "cloudpath": cloud_path
                    }
                }
        except:
            return {
                "success": False,
                "code": 500,
                "msg": "文件夹创建失败",
                "backdata": {
                    "cloudpath": cloud_path
                }
            }

    def move(self, cloud_path, new_cloud_path):
        try:
            headers = self.sdk_header.copy()
            headers[
                "Destination"] = "https://pan.bilnn.com/dav" + urllib.parse.quote(
                    new_cloud_path)
            r = requests.request("move",
                                "https://pan.bilnn.com/dav" + cloud_path,
                                headers=headers)
            if r.text == "Not Found":
                return {
                    "success": False,
                    "code": 404,
                    "msg": "文件不存在",
                    "backdata": {
                        "oldcloudpath": cloud_path
                    }
                }
            elif r.text == "Bad Request":
                return {
                    "success": False,
                    "code": 500,
                    "msg": "文件操作失败",
                    "backdata": {
                        "oldcloudpath": cloud_path,
                        "newcloudpath": new_cloud_path
                    }
                }
            return {
                "success": True,
                "code": 200,
                "msg": "文件操作成功",
                "backdata": {
                    "oldcloudpath": cloud_path
                }
            }
        except:
            return {
                "success": False,
                "code": 500,
                "msg": "文件操作错误",
                "backdata": {
                    "oldcloudpath": cloud_path,
                    "newcloudpath": new_cloud_path
                }
            }


if __name__ == "__main__":
    pan = Bilnn("abc@example.com", "PASSWORD")  # Bilnn("你的WebDav账号", "你的WebDav密码")
    print(pan.upload("D:/1.txt", "/1.txt"))  # pan.upload("本地文件路径", "云端保存路径"))
    print(pan.get_url("/1.txt"))  # pan.get_url("云端文件路径")
    print(pan.list_dir("/"))  # pan.list_dir("云端目录路径")
    print(pan.move("/1.txt", "/2.txt"))  # pan.move("云端原始文件或文件夹名", "云端更改后的文件或文件夹名")
    print(pan.delete("/2.txt"))  # pan.delete("云端文件路径")
