# -*- coding: utf-8 -*-
from flask import url_for, jsonify, request

from app import app, db
from app.models import User, Product, Factory
from app.util import try_commit


# -- 主页 --
@app.route('/')
@app.route('/index')
def index():
    host = 'http://{HOST}:{PORT}'.format(HOST=app.config['HOST'], PORT=app.config['PORT'])
    return "用户商品管理系统:</br>" \
            + "<a href='{0}/user'>{0}/user</a></br>".format(host) \
            + "<a href='{0}/product'>{0}/product</a></br>".format(host) \
            + "<a href='{0}/factory'>{0}/factory</a></br>".format(host)


# -- 用户 --
@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        payload = request.get_json()
        app.logger.debug('request payload: %s', payload)

        username = payload['username'] # 用户名
        password = payload['password'] # 密码
        name = payload['name'] # 姓名
        id_card_num = payload['id-card-num'] # 身份证

        user = User(
            username=username,
            password=password,
            name=name,
            id_card_num=id_card_num
        )
        db.session.add(user)
        try_commit(db.session)

        response = {
            'status': '%s created successfully!' % user,
            'username': username,
            'password': password,
            'name': name,
            'id-card-num': id_card_num,
        }
        return jsonify(response)
    elif request.method == 'GET':
        users = User.query.all()
        response = {
            'users': [user.to_dict() for user in users],
            'total': len(users)
        }
        return jsonify(response)


@app.route('/user/<user_id>', methods=['GET'])
def user_info(user_id):
    user = User.query.filter_by(id=user_id).first()
    response = user.to_dict()
    return jsonify(response)


# -- 商品 --
@app.route('/product', methods=['GET', 'POST'])
def product():
    if request.method == 'POST':
        payload = request.get_json()
        app.logger.debug('request payload: %s', payload)

        name = payload['name'] # 名称
        tag = payload['tag'] # 标签
        code = payload['code']  # 商品码
        batch = payload['batch'] # 批次
        spec = payload['spec'] # 规格

        product = Product(
            name=name,
            tag=tag,
            code=code,
            batch=batch,
            spec=spec
        )
        db.session.add(product)
        try_commit(db.session)

        response = {
            'status': '%s created successfully!' % product,
            'name': name,
            'code': code,
            'batch': batch,
            'spec': spec,
        }
        return jsonify(response)
    elif request.method == 'GET':
        products = Product.query.all()
        response = {
            'products': [product.to_dict() for product in products],
            'total': len(products)
        }
        return jsonify(response)


@app.route('/product/<product_id>', methods=['GET'])
def product_info(product_id):
    product = Product.query.filter_by(id=product_id).first()
    response = product.to_dict()
    return jsonify(response)


# -- 工厂 --
@app.route('/factory', methods=['GET', 'POST'])
def factory():
    if request.method == 'POST':
        payload = request.get_json()
        app.logger.debug('request payload: %s', payload)

        name = payload['name'] # 名称
        code = payload['code'] # 代码
        address = payload['address'] # 地址

        factory = Factory(
            name=name,
            code=code,
            address=address
        )
        db.session.add(factory)
        try_commit(db.session)

        response = {
            'status': '%s created successfully!' % factory,
            'name': name,
            'code': code,
            'address': address
        }
        return jsonify(response)
    elif request.method == 'GET':
        factorys = Factory.query.all()
        response = {
            'factorys': [factory.to_dict() for factory in factorys],
            'total': len(factorys)
        }
        return jsonify(response)


@app.route('/factory/<factory_id>', methods=['GET'])
def factory_info(factory_id):
    factory = factory.query.filter_by(id=factory_id).first()
    response = factory.to_dict()
    return jsonify(response)
