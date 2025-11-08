from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import click
from flask import g, current_app
from .schema import Question, Base, User


def get_db():
    if "db" not in g:
        g.engine = create_engine(current_app.config["DATABASE"])
    g.db = Session(g.engine)
    return g.db


def close_db(e=None):
    _ = g.pop("engine", None)
    session = g.pop("db", None)
    if session is not None:
        session.close()


def init_db(questions: str | None = None):
    _ = get_db()
    engine = g.engine
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    if questions is not None:
        add_multiquestion(questions)


@click.command("init-db")
@click.option("-q", "--questions", default=None)
def init_db_command(questions):
    """initializes the db"""
    init_db(questions)
    click.echo("database has been initialized")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(add_question_command)
    app.cli.add_command(multi_question_command)


def add_user(username):
    session = get_db()
    session.add(User(username=username))
    session.commit()


@click.command("add-question")
@click.argument("question")
def add_question_command(question):
    question_obj = Question(question_text=question)
    session = get_db()
    session.add(question_obj)
    session.commit()
    click.echo(f"question {question} was added")


def questions_ui() -> list[str]:
    questions = []
    while True:
        q = input(
            "please enter a new question. Type 'oops' to delete the last question added: "
        )
        if len(q) <= 0:
            break
        if q.lower().strip() == "oops":
            questions = questions[:-1]
            continue
        question = Question(question_text=q)
        questions.append(question)
    return questions


def add_multiquestion(file: str | None = None):
    if file is not None:
        with open(file) as fp:
            questions = [Question(question_text=q) for q in fp.read().split("\n")]
    else:
        questions = questions_ui()
    session = get_db()
    session.add_all(questions)
    session.commit()


@click.command("multi-question")
@click.option("-f", "--file", default=None)
def multi_question_command(file: str | None = None):
    return add_multiquestion(file)
