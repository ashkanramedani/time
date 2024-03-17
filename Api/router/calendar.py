from lib import logger
import schemas as sch
import db.models as dbm
import sqlalchemy.sql.expression as sse
from datetime import datetime, timedelta
from uuid import UUID
from typing import Optional, List, Dict, Any, Union, Annotated
from fastapi import APIRouter, Query, Body, Path, Depends, Response, HTTPException, status, UploadFile, File
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from db.database import get_db
from fastapi_limiter.depends import RateLimiter
from lib.hash import Hash
from lib.functions import Massenger, Tools

# expier_date, delete_date, can_deleted, deleted, update_date, can_update, visible, create_date, priority
#    DateTime,    DateTime,        True,   False,    DateTime,       True,    True,    DateTime,      Int

from db import db_calendar

router = APIRouter(prefix='/api/v1/calendar', tags=['Calendar'])

@router.get("/generat/from/{from_year}/{from_month}/{from_day}/to/{to_year}/{to_month}/{to_day}", dependencies=[Depends(RateLimiter(times=10, seconds=5))])
def generat_calender(
    from_year: Annotated[int, Path(title="from Year", gt=0, le=2000)] ,
    from_month: Annotated[int, Path(title="from Month", gt=0, le=12)] ,
    from_day: Annotated[int, Path(title="from Day", gt=0, le=31)] ,
    to_year: Annotated[int, Path(title="to Year", gt=0, le=2000)] ,
    to_month: Annotated[int, Path(title="to Month", gt=0, le=12)] ,
    to_day: Annotated[int, Path(title="to Day", gt=0, le=31)] ,
    db=Depends(get_db)):
    exam_schedule = []

    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() in selected_days:
            current_time = JalaliDatetime.combine(current_date, start_time)
            end_of_day = JalaliDatetime.combine(current_date, end_time)
            while current_time < end_of_day:
                if str(current_time)[:10] not in schedule_exceptions:
                    x = {
                        "day_of_week": current_date.weekday(),
                        "start_date": str(current_time)[:10],
                        "end_date": str(current_time)[:10],
                        "start_time": (current_time)._time,
                        "end_time": (current_time + timedelta(minutes=time_slot_minutes))._time,
                    }
                    exam_schedule.append(x)
                current_time += timedelta(minutes=time_slot_minutes)

        current_date += timedelta(days=1)

    return exam_schedule

@router.get("/today", dependencies=[Depends(RateLimiter(times=10, seconds=5))])
def get_today(db=Depends(get_db)):

    pass
    
@router.get("/{year}/{month}/{day}", dependencies=[Depends(RateLimiter(times=10, seconds=5))])
def get_day(
    year: Annotated[int, Path(title="Year", gt=0, le=2000)] ,
    month: Annotated[int, Path(title="Month", gt=0, le=12)] ,
    day: Annotated[int, Path(title="Day", gt=0, le=31)] ,
    db=Depends(get_db)):

    pass
    
@router.get("/from/{from_year}/{from_month}/{from_day}/to/{to_year}/{to_month}/{to_day}", dependencies=[Depends(RateLimiter(times=10, seconds=5))])
def get_calendar(
    from_year: Annotated[int, Path(title="from Year", gt=0, le=2000)] ,
    from_month: Annotated[int, Path(title="from Month", gt=0, le=12)] ,
    from_day: Annotated[int, Path(title="from Day", gt=0, le=31)] ,
    to_year: Annotated[int, Path(title="to Year", gt=0, le=2000)] ,
    to_month: Annotated[int, Path(title="to Month", gt=0, le=12)] ,
    to_day: Annotated[int, Path(title="to Day", gt=0, le=31)] ,
    db=Depends(get_db)):

    pass
    
@router.get("/holiday/from/{from_year}/{from_month}/{from_day}/to/{to_year}/{to_month}/{to_day}", dependencies=[Depends(RateLimiter(times=10, seconds=5))])
def get_holiday(
    from_year: Annotated[int, Path(title="from Year", gt=0, le=2000)] ,
    from_month: Annotated[int, Path(title="from Month", gt=0, le=12)] ,
    from_day: Annotated[int, Path(title="from Day", gt=0, le=31)] ,
    to_year: Annotated[int, Path(title="to Year", gt=0, le=2000)] ,
    to_month: Annotated[int, Path(title="to Month", gt=0, le=12)] ,
    to_day: Annotated[int, Path(title="to Day", gt=0, le=31)] ,
    db=Depends(get_db)):

    pass
    # raise HTTPException(status_code=500, detail="خطا در فرمت اطلاعات")          
    # return {"details": "اخطار با موفقیت ارسال شد"}