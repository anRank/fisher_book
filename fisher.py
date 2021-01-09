from app import create_app

# 调用create_app()函数创建app实例
app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=81, threaded=True)
    # 单进程、单线程
    # processes = 1
    # 10 个请求
    # port 指定端口号
    # threaded=True 设置为多线程
