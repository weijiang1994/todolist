from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
CORS(app=app)
db = SQLAlchemy(app)


class TodoList(db.Model):
    __tablename__ = 'todolist'

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    content = db.Column(db.TEXT, nullable=False, default='')
    c_time = db.Column(db.DATETIME, default=datetime.datetime.now)


db.create_all()

todos = ['买一张彩票，中了500W！', '买两张彩票，中了1500W！！', '买三张彩票，中了1E5000W！！！']
for td in todos:
    db.session.add(TodoList(content=td))
    db.session.commit()


@app.route('/add-todolist', methods=['POST'])
def add_todolist():
    content = request.json.get('text')
    tl = TodoList(content=content)
    db.session.add(tl)
    db.session.commit()
    return jsonify({'code': 200, 'msg': '添加成功!', 'id': tl.id})


@app.route('/remove-todolist', methods=['POST'])
def remove_todolist():
    tl_id = request.json.get('id')
    tl = TodoList.query.filter_by(id=tl_id).first()
    if tl:
        db.session.delete(tl)
        db.session.commit()
        return jsonify({'code': 200, 'msg': '删除成功！'})
    else:
        return jsonify({'code': 404, 'msg': '未找到todolist!'})


@app.route('/get-todolist')
def get_todolist():
    result = []
    todolists = TodoList.query.all()
    for todolist in todolists:
        dic = {
            'id': todolist.id,
            'text': todolist.content
        }
        result.append(dic)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
