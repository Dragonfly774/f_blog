import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Departments(SqlAlchemyBase):
    __tablename__ = 'departments'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    members = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.name"))
    email = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.email"), unique=True)

    user = orm.relation('User')
    """Я так понимаю, что в members входят id членов, в cheef id кого главного, и email тоже кого то главного"""
