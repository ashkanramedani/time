
from datetime import datetime, date
from enum import Enum
from typing import Optional, List, Any
from uuid import UUID

from fastapi import File, UploadFile
from pydantic import BaseModel, PositiveInt


# expier_date, delete_date, can_deleted, deleted, update_date, can_update, visible, create_date, priority
#    DateTime,    DateTime,        True,   False,    DateTime,       True,    True,    DateTime,      Int


# -------------------------------   Users   -------------------------------
# -------------------------------   Groups   -------------------------------

# -------------------------------   Alert   -------------------------------

# class AlertBase(BaseModel): 
#     pass
# class AlertCreate(alertBase):
#     pass
# class Alert(alertBase):
#     alert_pk_id: UUID
#     class Config:
#         orm_mode = True

# -------------------------------   Users   -------------------------------
# -------------------------------   Users   -------------------------------

