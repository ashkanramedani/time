from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table, BigInteger, MetaData, Float, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression, func

# expier_date, delete_date, can_deleted, deleted, update_date, can_update, visible, create_date, priority
#    DateTime,    DateTime,        True,   False,    DateTime,       True,    True,    DateTime,      Int

metadata_obj = MetaData()

from .database import Base

class BaseTable:
    priority = Column(Integer, default=5, nullable=True)
    visible = Column(Boolean, server_default=expression.true(), nullable=False)
    expier_date = Column(DateTime(timezone=True), default=None)
    create_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    can_update = Column(Boolean, server_default=expression.true(), nullable=False)
    update_date = Column(DateTime(timezone=True), default=None, onupdate=func.now())
    deleted = Column(Boolean, server_default=expression.false(), nullable=False)
    can_deleted = Column(Boolean, server_default=expression.true(), nullable=False)
    delete_date = Column(DateTime(timezone=True), default=None)

class Day(Base, BaseTable):
    __tablename__ = "tbl_days"

    day_pk_id = Column(GUID, nullable=False, unique=True, primary_key=True, index=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)

    shamsi_year = Column(Integer, nullable=False)
    shamsi_year_is_leap = Column(Boolean, nullable=False)
    shamsi_month = Column(Integer, nullable=False)
    shamsi_month_name = Column(String(100), nullable=False)
    shamsi_day = Column(Integer, nullable=False)
    shamsi_day_of_week_name = Column(String(100), nullable=False)    
    shamsi_day_of_week = Column(Integer, nullable=False)
    shamsi_is_holiday = Column(Boolean, nullable=False)
    shamsi_events = Column(JSONB, nullable=False)

    miladi_year = Column(Integer, nullable=False)
    miladi_year_is_leap = Column(Boolean, nullable=False)
    miladi_month = Column(Integer, nullable=False)
    miladi_month_name = Column(String(100), nullable=False)
    miladi_day = Column(Integer, nullable=False)
    miladi_day_of_week_name = Column(String(100), nullable=False)    
    miladi_day_of_week = Column(Integer, nullable=False)
    miladi_is_holiday = Column(Boolean, nullable=False)
    miladi_events = Column(JSONB, nullable=False)

    ghamari_year = Column(Integer, nullable=False)
    ghamari_year_is_leap = Column(Boolean, nullable=False)
    ghamari_month = Column(Integer, nullable=False)
    ghamari_month_name = Column(String(100), nullable=False)
    ghamari_day = Column(Integer, nullable=False)
    ghamari_day_of_week_name = Column(String(100), nullable=False)    
    ghamari_day_of_week = Column(Integer, nullable=False)
    ghamari_is_holiday = Column(Boolean, nullable=False)
    ghamari_events = Column(JSONB, nullable=False)

    def __repr__(self):
        return f'<Day "{self.day_pk_id}">'

