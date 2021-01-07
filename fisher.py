from app import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=81, threaded=True)
    #单进程、单线程
    # processes = 1
    # 10 个请求
