from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'announcments.db')}"
db = SQLAlchemy()
db.init_app(app)
ma = Marshmallow(app)

@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('database created!')

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('database dropped!')


@app.route('/add_announcement', methods=['POST'])
def add_announcement():
    announcement_text = request.form['announcement_text']
    exists = Announcement.query.filter_by(announcement_text=announcement_text).first()
    if exists:
        return jsonify(message='There is already announcement with that text'), 409
    else:
        new_announcement = Announcement(announcement_text=announcement_text)
        db.session.add(new_announcement)
        db.session.commit()
        return jsonify(message='announcement is added'), 201


@app.route('/announcements', methods=['GET'])
def announcements():
    announcements_list = Announcement.query.all()
    result = announcements_schema.dump(announcements_list)
    return jsonify(data=result)


@app.route('/announcement_details/<int:announcement_id>', methods=['GET'])
def announcements_details(announcement_id):
    announcement = Announcement.query.filter_by(announcement_id=announcement_id).first()
    if announcement:
        result = announcement_schema.dump(announcement)
        return jsonify(result)
    else:
        return jsonify(message='announcement with that id doesnt exist'), 404


#database model
class Announcement(db.Model):
    announcement_id = Column(Integer, primary_key=True)
    announcement_text = Column(String)

class AnnouncementSchema(ma.Schema):
    class Meta:
        fields = ('announcement_id', 'announcement_text')

announcement_schema = AnnouncementSchema()
announcements_schema = AnnouncementSchema(many=True)

if __name__ == '__main__':
    app.run()
