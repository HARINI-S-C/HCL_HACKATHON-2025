# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
# from sqlalchemy import String, Integer, DateTime, ForeignKey
# from datetime import datetime

# class Base(DeclarativeBase):
#     pass

# class User(Base):
#     __tablename__ = "users"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     full_name: Mapped[str] = mapped_column(String, nullable=False)
#     email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
#     hashed_password: Mapped[str] = mapped_column(String, nullable=False)
#     role: Mapped[str] = mapped_column(String, default="customer")
#     kyc_status: Mapped[str] = mapped_column(String, default="pending")

#     kyc: Mapped["KYC"] = relationship("KYC", back_populates="user", uselist=False)
#     account: Mapped["Account"] = relationship("Account", back_populates="user", uselist=False)

# class KYC(Base):
#     __tablename__ = "kyc"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     document_type: Mapped[str] = mapped_column(String)
#     document_url: Mapped[str] = mapped_column(String)
#     status: Mapped[str] = mapped_column(String, default="under_review")
#     verified_by: Mapped[str] = mapped_column(String, nullable=True)

#     user: Mapped["User"] = relationship("User", back_populates="kyc")

# class Account(Base):
#     __tablename__ = "accounts"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     account_number: Mapped[str] = mapped_column(String, unique=True)
#     account_type: Mapped[str] = mapped_column(String)
#     balance: Mapped[int] = mapped_column(Integer, default=0)
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

#     user: Mapped["User"] = relationship("User", back_populates="account")





from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    kyc_status = Column(String, default="pending")

    accounts = relationship("Account", back_populates="user")

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    account_number = Column(String, unique=True, index=True)
    account_type = Column(String)

    user = relationship("User", back_populates="accounts")

class KYC(Base):
    __tablename__ = "kyc"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    document_path = Column(String)
    status = Column(String, default="pending")  # pending, approved, rejected

    user = relationship("User", back_populates="kyc_documents")


