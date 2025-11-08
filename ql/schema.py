from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, ForeignKey


class Base(DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = "question"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question_text: Mapped[str] = mapped_column(String(250))

    def __repr__(self) -> str:
        return f"Question(id={self.id!r}, question={self.question!r}"


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30))


class Answer(Base):
    __tablename__ = "answer"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
    answer_text: Mapped[str] = mapped_column(String(280))


class Vote(Base):
    __tablename__ = "vote"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    answer_id: Mapped[int] = mapped_column(ForeignKey("answer.id"))
