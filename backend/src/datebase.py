from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash

from src.settings import get_config

from .flaskextens import db
from .utlis import serialize_datetime

config = get_config()


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    registered_at: Mapped[datetime] = mapped_column(DateTime)
    token_validity_period: Mapped[int] = mapped_column(Integer, default=604800)

    @classmethod
    def create(cls, username: str, password: str) -> "User":
        user = User(
            username=username,
            password_hash=generate_password_hash(password),
            registered_at=datetime.now(),
        )  # type: ignore
        db.session.add(user)
        db.session.commit()
        return User.query.get(user.id)  # type: ignore

    def validate_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def extend_validity_period(self) -> None:
        self.token_validity_period += config.VALIDITY_INCREMENT
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            registeredAt=serialize_datetime(
                self.registered_at.astimezone(timezone.utc)
            ),
            tokenValidityPeriod=self.token_validity_period,
        )


class Visits(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    count: Mapped[int] = mapped_column(Integer, default=0)

    @classmethod
    def create(cls):
        db.session.add(Visits())
        db.session.commit()

    def increase(self) -> None:
        self.count += 1
        db.session.add(self)
        db.session.commit()
