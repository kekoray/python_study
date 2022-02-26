""" 
curl的方式请求URL接口,并返回数据;
应用场景为: 获取汇率数据

"""
import json
from operator import truediv
from flask import Flask, request, jsonify


# 把当前这个python文件，当做一个服务
server = Flask(__name__)


@server.route('/testGet', methods=['get'])
def testGet():
    print(request)
    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    c = int(a) + int(b)
    res = {'msg': '接口-1', "result": c}
    # 设置ensure_ascii=False,显示中文
    return json.dumps(res, ensure_ascii=False)


@server.route('/testPost', methods=['post'])
def testPost():
    params = request.form if request.form else request.json
    print(params)
    a = params.get("a", 0)
    b = params.get("b", 0)
    c = a + b
    res = {'msg': '接口-1', "result": c}
    return jsonify(content_type='application/json;charset=utf-8',
                   reason='success',
                   charset='utf-8',
                   status='200',
                   content=res)


if __name__ == '__main__':
    # host='0.0.0.0'表示本机IP访问即可;
    # debug=True表示改完代码会自动重启服务,设置Fales才可以本地测试;
    server.run(host='0.0.0.0', threaded=True, port=9999, debug=False)

