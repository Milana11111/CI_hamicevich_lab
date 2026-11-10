from typing import Dict, List
from app.schemas import AuditRead
from datetime import date

# Имитация базы данных
_audits: Dict[int, AuditRead] = {}
_next_id = 1

def get_all() -> List[AuditRead]:
    return list(_audits.values())

def get_by_id(audit_id: int) -> AuditRead | None:
    return _audits.get(audit_id)

def create(audit_data: dict) -> AuditRead:
    global _next_id
    new_audit = AuditRead(
        id=_next_id,
        created_at=date.today(),
        **audit_data
    )
    _audits[_next_id] = new_audit
    _next_id += 1
    return new_audit

def delete(audit_id: int) -> bool:
    if audit_id in _audits:
        del _audits[audit_id]
        return True
    return False

# Наполним тестовыми данными (для демонстрации)
create({
    "title": "Аудит процесса закупок",
    "scope": "ISO 9001, раздел 8.4",
    "auditor_name": "Петров П.П.",
    "audit_date": date(2026, 6, 15),
    "status": "planned"
})