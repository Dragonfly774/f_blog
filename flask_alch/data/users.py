import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    position = sqlalchemy.Column(sqlalchemy.String)
    speciality = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime)

    news = orm.relation("News", back_populates='user')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


"""
- sqlalchemy.Integer (sqlalchemy.String, sqlalchemy.DateTime и т. д.) — указания типа данных

- primary_key=True — указание на то, что столбец является первичным ключом. 
Обычно первичный ключ — некоторый числовой идентификатор, который однозначно 
идентифицирует каждую запись в таблице

- autoincrement=True — признак автоинкрементного поля. Используется для 
увеличения значения первичного ключа на единицу при вставке каждой новой записи

- nullable=True/False — может ли поле не содержать никакой информации и быть пустым

- unique=True/False — содержит ли поле только уникальные значения или они могут повторяться

- default=datetime.datetime.now — значение по умолчанию. В данном случае мы говорим,
что при вставке нового пользователя будет вставлена дата и время на момент его 
создания. Обратите внимание: мы не вызываем функцию, а передаем ее. Если бы мы 
вызвали функцию, то текущее время было бы вычислено только один раз при запуске 
сервера и было бы одинаковое для всех пользователей, которые были бы созданы после этого
 
- index=True — создать индекс по этому полю. Индекс, если говорить упрощенно, 
позволяет значительно повысить скорость поиска по одному или нескольким полям
базы данных. Цена этого — уменьшение скорости вставки данных, поэтому не стоит
делать индексы на абсолютно все поля, а только на те (и ту их комбинацию), 
по которым будет часто осуществляться поиск
"""
