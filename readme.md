# Django File store

## 此项目的功能

Django 文件的上传、删除、下载，以及文件列表的查询功能


## 环境依赖

- Linux 
- Python 3
- nginx （部署用，也可直接采用 runserver 运行服务）
- python 包: requirement.txt 文件 (安装: `pip install -r requirement.txt`)

## 默认的管理员用户

- root
- @hjx1234567*
 
## 部署

### 安装 Docker （以 CentOS 下为例）

1. 安装 Docker 及 Docker-compose: `sudo yum -y install docker docker-compose`
2. 设置开机自启动: `sudo systemctl enable docker`
2. 启动 Docker: `sudo systemctl start docker`

### Docker 部署

1. 构建并启动 Docker （当前目录下）: `docker-compose up -d`
2. 创建后台管理员账号（可选，可不执行此步骤）： `docker exec -it filestore_app_1 bash create_super_user.sh`
3. 默认的服务端口为 9089，请确保防火墙开放 9089 端口
4 文件上传: 
    - URL: `http://服务器地址:9089/upload/`
    - method: `POST`
    - 表单: `uploaded_file` 字段: 文件
    - 响应 (JSON 格式):
        - 成功: `{"code": "200", "msg": "OK"}`
        - 表单错误: `{"code": "400", "msg": "Invalid data"}`
5. 获取已上传的文件列表:
    - URL: `http://服务器地址:9089/file-list/`
    - method: `GET`
    - 响应 (JSON 格式):
        - 成功: `{"code": "200", "results": [文件名列表]}` （文件列表可能为空）
6. 下载文件:
    - URL: `http://服务器地址:9089/download/文件名`
    - method: `GET`
    - 响应: 文件数据流
        - 失败: `{"code": "401", "msg": "file doesn't exist"}` 
        - 成功: 文件数据流
7. 删除文件:
    - URL: `http://服务器地址:9089/delete/文件名`
    - method: `GET`
    - 响应: 文件数据流
        - 失败: `{"code": "401", "msg": "file doesn't exist"}` 
        - 成功: `{"code": "200", "msg": "OK"}`

