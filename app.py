from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# 配置 MySQL 数据库连接信息
db_config = {
    'user': 'root',
    'password': 'x136928',
    'host': '127.0.0.1',
    'database': 'bysj',
    'raise_on_warnings': True
}

# 初始化数据库
def init_db():
    try:
        # 建立与 MySQL 数据库的连接
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # 创建 users 表，如果表不存在的话
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        '''
        cursor.execute(create_table_query)
        # 提交事务
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            # 关闭游标和数据库连接
            cursor.close()
            conn.close()

# 根路由，渲染包含 Vue 应用的 HTML 页面
@app.route('/')
def index():
    return render_template('index.html')

# 处理登录请求的路由
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    try:
        # 建立与 MySQL 数据库的连接
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # 执行 SQL 查询语句，查找匹配的用户记录
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        # 获取查询结果的第一条记录
        user = cursor.fetchone()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        response = {'message': 'Database error', 'success': False}
    finally:
        if conn.is_connected():
            # 关闭游标和数据库连接
            cursor.close()
            conn.close()

    if user:
        response = {'message': 'Login successful', 'success': True}
    else:
        response = {'message': 'Invalid username or password', 'success': False}

    return jsonify(response)

if __name__ == '__main__':
    #init_db()
    app.run(debug=True,port=8080)