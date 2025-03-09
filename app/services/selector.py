from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Theater, Application, Attendee
from app.enums.ticket import StatusEnum, TicketTypeEnum, SpecialEventEnum
import random

def calculate_priority(app: Application, theater: Theater, db: Session):
    priority = 0

    if theater.show_name.lower() in (app.attendee.address or "").lower():
        priority += 3

    num_losses = db.query(Application).filter(
        Application.user_id == app.user_id,
        Application.status == StatusEnum.lose
    ).count()
    priority += num_losses

    theater_apps_count = db.query(Application).filter(
        Application.theater_id == theater.id
    ).count()
    priority += max(0, 5 - theater_apps_count)

    theater_member_names = [member.name for member in theater.members]
    if app.attendee.favorite_member in theater_member_names:
        priority += 5

    return priority

def select_ofc_attendees(db: Session, theater_id: int, max_attendees: int):
    theater = db.query(Theater).filter(Theater.id == theater_id).first()
    if not theater:
        raise HTTPException(status_code=404, detail="Theater not found")

    eligible_apps = db.query(Application).filter(
        Application.theater_id == theater_id,
        Application.status == StatusEnum.lose,
        Application.ticket_type == TicketTypeEnum.OFC
    ).all()

    if not eligible_apps:
        raise HTTPException(status_code=404, detail="No eligible OFC attendees")

    attendees_pool = []
    for app in eligible_apps:
        num_losses = db.query(Application).filter(
            Application.user_id == app.user_id,
            Application.show_type == app.show_type,
            Application.status == StatusEnum.lose
        ).count()

        if num_losses >= 10 and random.randint(1, 100) <= random.randint(80, 90):
            attendees_pool.append(app.attendee)
            continue

        special_members = [assoc.member_id for assoc in theater.members_assoc if assoc.special_event != SpecialEventEnum.NONE]
        is_special_event = any(
            member.id in special_members and member.name == app.attendee.favorite_member
            for member in theater.members
        )

        if is_special_event and random.randint(1, 100) <= random.randint(65, 75):
            attendees_pool.append(app.attendee)
            continue

        weight = calculate_priority(app, theater, db)
        attendees_pool.extend([app.attendee] * weight)

    selected_attendees = random.sample(
        list(set(attendees_pool)),
        min(max_attendees, len(set(attendees_pool)))
    )

    return [{"uid": attendee.uid, "name": attendee.name, "favorite_member": attendee.favorite_member, "address": attendee.address}
            for attendee in selected_attendees]

def select_general_attendees(db: Session, theater_id: int, max_attendees: int):
    theater = db.query(Theater).filter(Theater.id == theater_id).first()
    if not theater:
        raise HTTPException(status_code=404, detail="Theater not found")

    eligible_general_apps = db.query(Application).filter(
        Application.theater_id == theater_id,
        Application.status == StatusEnum.lose,
        Application.ticket_type == TicketTypeEnum.GENERAL
    ).all()

    if not eligible_general_apps:
        raise HTTPException(status_code=404, detail="No eligible general attendees")

    ofc_applied_attendees = []
    pure_general_attendees = []

    for app in eligible_general_apps:
        ofc_applied_before = db.query(Application).filter(
            Application.user_id == app.user_id,
            Application.ticket_type == TicketTypeEnum.OFC
        ).count() > 0

        if ofc_applied_before:
            ofc_applied_attendees.append(app)
        else:
            pure_general_attendees.append(app)

    percentage_ofc = random.randint(30, 50)
    ofc_quota = int((percentage_ofc / 100) * max_attendees)
    general_quota = max_attendees - ofc_quota

    weighted_ofc_attendees = []
    for app in ofc_applied_attendees:
        weight = calculate_priority(app, theater, db)
        weighted_ofc_attendees.extend([app.attendee] * weight)

    weighted_pure_general_attendees = []
    for app in pure_general_attendees:
        weight = calculate_priority(app, theater, db)
        weighted_pure_general_attendees.extend([app.attendee] * weight)

    selected_ofc_attendees = random.sample(
        list(set(weighted_ofc_attendees)),
        min(ofc_quota, len(set(weighted_ofc_attendees)))
    )

    selected_pure_general_attendees = random.sample(
        list(set(weighted_pure_general_attendees)),
        min(general_quota, len(set(weighted_pure_general_attendees)))
    )

    selected_attendees = selected_ofc_attendees + selected_pure_general_attendees
    random.shuffle(selected_attendees)

    return [{"uid": attendee.uid, "name": attendee.name, "favorite_member": attendee.favorite_member, "address": attendee.address}
            for attendee in selected_attendees]
