## VSC网页版docker部署



### docker容器部署

#### docker-compose.yml

```yml
version: "3"

services:
  code-server:
    container_name: code-server
    image: codercom/code-server
    ports:
      - "1024:8080"
    volumes:0
      - "/soft/code-server/.config:/home/coder/.config"  # 配置文件
      - "/soft/code-server/project:/home/coder/project"  # 项目存放
    environment:
      PASSWORD: koray2021
    restart: always
    privileged: true
    user: root
```



#### 配置文件

`/home/coder/.config/code-server/config.yaml `  

```yaml
bind-addr: 127.0.0.1:8080
auth: password
password: 171df325f5f26f610fdd5eaa
cert: false
```









