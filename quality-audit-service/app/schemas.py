from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

# Базовая модель аудита
class AuditBase(BaseModel):
    title: str = Field(..., description="Название аудита (Заявка на аудит)", example="Внутренний аудит отдела продаж")
    scope: str = Field(..., description="Область и критерии аудита", example="ISO 9001:2015, п.8.2")
    auditor_name: str = Field(..., description="ФИО аудитора", example="Иванов И.И.")
    audit_date: date = Field(..., description="Дата проведения аудита", example="2026-05-20")
    status: str = Field(default="planned", description="Статус аудита (planned, in_progress, completed)")

# Модель для создания (без ID)
class AuditCreate(AuditBase):
    pass

# Модель для чтения (с ID)
class AuditRead(AuditBase):
    id: int
    created_at: date

# Модель ошибки
class ErrorResponse(BaseModel):
    detail: str