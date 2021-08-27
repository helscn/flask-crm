#### TMS 贸易管理系统

- 后端框架：
  - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
  - [Flask-Restful](https://github.com/flask-restful/flask-restful)
  - [Flask-SqlAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
  - [Flask-APScheduler](https://github.com/viniciuschiele/flask-apscheduler)
  - [Gunicorn](https://gunicorn.org/)
- 前端框架
  - [Vue](https://cn.vuejs.org/)
  - [Quasar](https://quasar.dev/)
  - [bookjs-eazy](https://github.com/wuxue107/bookjs-eazy)

#### 项目结构说明

- backend：后端 python 程序，程序运行入口为 start.py，直接运行时使用 Flask 开发模式运行，默认监听 8000 端口。
- frontend：前端 vue 程序，使用 quasar dev 启用开发服务器，开发模式 API 调用本地 8000 端口，编译打包后 API 直接调用当前服务器地址。

#### 项目部署

项目程序使用 [Docker](https://www.docker.com/) 进行部署，使用以下命令进行镜像打包：

```
docker build 镜像名称:标签 .
```

镜像打包时会自动将前端项目编译为单页项目文件，并根据 backend/requirements.txt 中的依赖安装运行所需要的 Python 包。

打包后作为容器运行时，后端服务器会切换为 [Gunicorn](https://gunicorn.org/) ，并默认监听容器的 8080 端口。运行过程中支持容器 Healthcheck 健康度检查，部署时需要设置以下卷路径映射：

- /app/settings.py ：后端服务器的配置文件，数据库地址及程序运行参数均在此文件中进行设置，示例参见项目内 /backend/settings.py 文件
- /app/uploads ：客户端上传的文件保存路径
- /app/schedulers/jobs ：后端服务器需要自动运行的脚本路径

注意：如果使用 Flask-APScheduler 自动运行计划任务，gunicorn 需要使用单进程模式运行，相关容器运行的环境变量如下：

- APP_WORKERS ：Gunicorn 运行的进程数
- APP_THREADS ：Gunicorn 运行的线程数
- APP_PORT ：Gunicorn 运行时监听的端口
