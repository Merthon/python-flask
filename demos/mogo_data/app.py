from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# 连接到 MongoDB 数据库（假设 MongoDB 运行在默认的 localhost:27017）
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]  # 使用名为 "mydatabase" 的数据库
collection = db["mycollection"]  # 使用名为 "mycollection" 的集合

# 插入数据
@app.route('/add', methods=['POST'])
def add_data():
    data = request.json  # 从请求中获取 JSON 数据
    result = collection.insert_one(data)  # 插入数据到 MongoDB
    return jsonify({"message": "Data added", "id": str(result.inserted_id)}), 201

# 获取数据
@app.route('/get', methods=['GET'])
def get_data():
    data = list(collection.find())  # 获取所有数据
    for item in data:
        item["_id"] = str(item["_id"])  # 将 ObjectId 转换为字符串
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
