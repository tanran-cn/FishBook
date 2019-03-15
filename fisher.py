# _*_ coding: utf-8 _*_
from app import create_app

__auther__ = "tanran"
__date__ = "2019/1/24 22:00"

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])

