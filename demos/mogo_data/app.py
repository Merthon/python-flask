from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# 配置 MongoDB URI
app.config["MONGO_URI"] = "mongodb://admin:admin@localhost:27017/mydatabase"

# 初始化 PyMongo
mongo = PyMongo(app)

@app.route('/')
def index():
    # 获取 MongoDB 集合（collection）
    users = mongo.db.users  # 假设有一个名为 users 的集合
    # 查询集合中的所有文档
    all_users = users.find()
    return str([user for user in all_users])

# 向 users 集合插入数据
@app.route('/add_user')
def add_user():
    users = mongo.db.users
    user_data = {"name": "John Doe", "email": "john.doe@example.com"}
    
    # 插入数据，并获取插入的 ID
    result = users.insert_one(user_data)
    
    # 返回插入的对象 ID
    return f"User added with ID: {result.inserted_id}"

# 查询用户
@app.route('/get_user')
def get_user():
    users = mongo.db.users
    user = users.find_one({"name": "John Doe"})
    if user:
        return str(user)
    return "User not found!"

# 查询所有用户
@app.route('/get_all_users')
def get_all_users():
    users = mongo.db.users
    all_users = users.find()
    return str([user for user in all_users])

# 更新用户的电子邮件地址
@app.route('/update_user')
def update_user():
    users = mongo.db.users
    # 更新某个用户的邮箱
    result = users.update_one(
        {"name": "John Doe"},  # 查找条件
        {"$set": {"email": "john.new@example.com"}}  # 更新字段
    )
    if result.matched_count > 0:
        return "User updated!"
    return "User not found!"

# 删除某个用户
@app.route('/delete_user')
def delete_user():
    users = mongo.db.users
    result = users.delete_one({"name": "John Doe"})
    if result.deleted_count > 0:
        return "User deleted!"
    return "User not found!"

if __name__ == "__main__":
    app.run(debug=True)


# mongodb://admin:admin@localhost:27017/