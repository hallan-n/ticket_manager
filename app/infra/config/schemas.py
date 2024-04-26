from datetime import datetime

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer,
                        MetaData, String, Table, Text)

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("login", String(255), nullable=False),
    Column("password", String(255), nullable=False),
    Column("create_at", DateTime, default=datetime.now),
    Column("update_at", DateTime, default=datetime.now, onupdate=datetime.now),
    extend_existing=True,
)
ticket = Table(
    "ticket",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(255), nullable=False),
    Column("open_date", DateTime, nullable=False),
    Column("resolution_date", DateTime, nullable=False),
    Column("status", String(255)),
    Column("sla", Boolean, default=False),
    extend_existing=True,
)

chat = Table(
    "chat",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("update_at", DateTime, default=datetime.now, onupdate=datetime.now),
    extend_existing=True,
)
message = Table(
    "message",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("msg", Text, nullable=False),
    Column("sent_at", DateTime, default=datetime.now),
    Column("chat_id", Integer, ForeignKey("chat.id"), nullable=False),
    Column("sender_id", Integer, ForeignKey("user.id"), nullable=False),
    Column("recipient_id", Integer, ForeignKey("user.id"), nullable=False),
    extend_existing=True,
)
