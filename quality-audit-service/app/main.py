from fastapi import FastAPI, HTTPException, status
from app import store
from app.schemas import AuditCreate, AuditRead, ErrorResponse
from typing import List

app = FastAPI(
    title="API Внутреннего Аудита Качества",
    description="REST API для управления внутренними аудитами (на основе модели IDEF0)",
    version="1.0.0"
)

# 1. Получение списка
@app.get(
    "/api/v1/audits/",
    response_model=List[AuditRead],
    summary="Получить список всех аудитов",
    tags=["Аудиты"]
)
def get_audits():
    return store.get_all()

# 2. Получение по ID
@app.get(
    "/api/v1/audits/{audit_id}",
    response_model=AuditRead,
    responses={404: {"model": ErrorResponse, "description": "Не найдено"}},
    summary="Получить детали аудита",
    tags=["Аудиты"]
)
def get_audit(audit_id: int):
    audit = store.get_by_id(audit_id)
    if not audit:
        raise HTTPException(status_code=404, detail="Аудит не найден")
    return audit

# 3. Создание
@app.post(
    "/api/v1/audits/",
    response_model=AuditRead,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": ErrorResponse, "description": "Ошибка валидации"}},
    summary="Создать новый аудит",
    tags=["Аудиты"]
)
def create_audit(payload: AuditCreate):
    return store.create(payload.model_dump())

# 4. Удаление
@app.delete(
    "/api/v1/audits/{audit_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse, "description": "Не найдено"}},
    summary="Удалить аудит",
    tags=["Аудиты"]
)
def delete_audit(audit_id: int):
    if not store.delete(audit_id):
        raise HTTPException(status_code=404, detail="Аудит не найден")
    return None