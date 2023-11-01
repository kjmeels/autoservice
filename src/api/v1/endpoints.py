from typing import List

from fastapi import HTTPException
from sqlalchemy import select
from starlette import status

from .router import router
# from ...models import Car, Detail, Feedback, Person, Promotion, Service
from ...models.cars import Car
from ...models.details import Detail
from ...models.feedbacks import Feedback
from ...models.personal import Person
from ...models.promotions import Promotion
from ...models.services import Service
# from ...schemas import (
#     CarSchema,
#     InfoSchema,
#     PersonalListSchema,
#     DetailSchema,
#     PromotionSchema,
#     FeedbackSchema,
#     ServiceSchema
# )
from ...schemas.cars import CarSchema
from ...schemas.details import DetailSchema
from ...schemas.feedbacks import FeedbackSchema
from ...schemas.main_info import InfoSchema
from ...schemas.personal import PersonalListSchema
from ...schemas.promotions import PromotionSchema
from ...schemas.services import ServiceSchema

info_json = {
    "name": "Autoservice Name",
    "address": "Mayakovskogo 28a",
    "phone_number": "+375445214785",
    "email": "Autoservice@mail.ru"
}


@router.get("/info", response_model=InfoSchema, tags=["Info"], name="info_list")
async def service_info():
    return InfoSchema(**info_json)


@router.get("/personal", response_model=List[PersonalListSchema], tags=["Personal"], name="personal_list")
async def personal_list():
    async with Person.async_session() as session:
        personal = await session.scalars(select(Person).order_by(Person.id.asc()))
        return [PersonalListSchema(
            id=person.id,
            name=person.name,
            surname=person.surname,
            email=person.email,
        ) for person in personal.all()]


@router.post("/add_person", response_model=PersonalListSchema, tags=["Personal"], name="add_person")
async def add_person(person: PersonalListSchema):
    person = Person(**PersonalListSchema(**person.dict()).dict())
    async with Person.async_session() as session:
        session.add(person)
        try:
            await session.commit()
        except InterruptedError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="person hasn't added")
        else:
            await session.refresh(person)
            return PersonalListSchema(
                id=person.id,
                name=person.name,
                surname=person.surname,
                email=person.email,
            )


@router.get("/cars", response_model=List[CarSchema], tags=["Cars"], name="cars_list")
async def cars_list():
    async with Car.async_session() as session:
        cars = await session.scalars(select(Car).order_by(Car.id.asc()))
        return [CarSchema(
            id=car.id,
            car_brand=car.car_brand,
            car_model=car.car_model,
            car_engine_type=car.car_engine_type,
            car_drive_type=car.car_drive_type,
            car_year_of_production=car.car_year_of_production,
            car_vin=car.car_vin,
        ) for car in cars.all()]


@router.post("/add_car", response_model=CarSchema, tags=["Cars"], name="add_car")
async def add_car(car: CarSchema):
    car = Car(**CarSchema(**car.dict()).dict())
    async with Car.async_session() as session:
        session.add(car)
        try:
            await session.commit()
        except InterruptedError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="car hasn't added")
        else:
            await session.refresh(car)
            return CarSchema(
                id=car.id,
                car_brand=car.brand,
                car_model=car.model,
                car_engine_type=car.engine_type,
                car_drive_type=car.drive_type,
                car_year_of_production=car.year_of_production,
                car_vin=car.vin,
            )


@router.get("/details", response_model=List[DetailSchema], tags=["Details"], name="details_list")
async def details_list():
    async with Detail.async_session() as session:
        details = await session.scalars(select(Detail).order_by(Detail.id.asc()))
        return [DetailSchema(
            id=detail.id,
            category=detail.category,
            model=detail.model,
            price=detail.price,
            is_available=detail.is_available,
        ) for detail in details.all()]


@router.post("/add_detail", response_model=DetailSchema, tags=["Details"], name="add_detail")
async def add_detail(detail: DetailSchema):
    detail = Detail(**DetailSchema(**detail.dict()).dict())
    async with Detail.async_session() as session:
        session.add(detail)
        try:
            await session.commit()
        except InterruptedError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="detail hasn't added")
        else:
            await session.refresh(detail)
            return DetailSchema(
                id=detail.id,
                category=detail.category,
                model=detail.model,
                price=detail.price,
                is_available=detail.is_available,
            )


@router.get("/promotions", response_model=List[PromotionSchema], tags=["Promotions"], name="promotions_list")
async def promotions_list():
    async with Promotion.async_session() as session:
        promotions = await session.scalars(select(Promotion).order_by(Promotion.id.asc()))
        return [PromotionSchema(
            id_promotion=promotion.id_promotion,
            type_of_promotion=promotion.type_of_promotion,
            discount_percentage=promotion.discount_percentage,
            end_date=promotion.end_date,
        ) for promotion in promotions.all()]


@router.post("/add_promotion", response_model=PromotionSchema, tags=["Promotions"], name="add_promotion")
async def add_promotion(promotion: PromotionSchema):
    promotion = Promotion(**PromotionSchema(**promotion.dict()).dict())
    async with Promotion.async_session() as session:
        session.add(promotion)
        try:
            await session.commit()
        except InterruptedError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="promotion hasn't added")
        else:
            await session.refresh(promotion)
            return PromotionSchema(
                id_promotion=promotion.id,
                type_of_promotion=promotion.type,
                discount_percentage=promotion.discount_percentage,
                end_date=promotion.end_date,
            )


@router.get("/feedbacks", response_model=List[FeedbackSchema], tags=["Feedbacks"], name="feedbacks_list")
async def feedbacks_list():
    async with Feedback.async_session() as session:
        feedbacks = await session.scalars(select(Feedback).order_by(Feedback.id.asc()))
        return [FeedbackSchema(
            id=feedback.id,
            user_name=feedback.user_name,
            feedback_text=feedback.feedback_text,
            feedback_date=feedback.feedback_date,
        ) for feedback in feedbacks.all()]


@router.post("/add_feedback", response_model=FeedbackSchema, tags=["Feedbacks"], name="add_feedback")
async def add_feedback(feedback: FeedbackSchema):
    feedback = Feedback(**FeedbackSchema(**feedback.dict()).dict())
    async with Feedback.async_session() as session:
        session.add(feedback)
        try:
            await session.commit()
        except InterruptedError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="feedback hasn't added")
        else:
            await session.refresh(feedback)
            return FeedbackSchema(
                id=feedback.id,
                user_name=feedback.user_name,
                feedback_text=feedback.text,
                feedback_date=feedback.date,
            )


@router.get("/services", response_model=List[ServiceSchema], tags=["Services"], name="services_list")
async def services_list():
    async with Service.async_session() as session:
        services = await session.scalars(select(Service).order_by(Service.id.asc()))
        return [ServiceSchema(
            service_id=service.service_id,
            service_name=service.service_name,
            service_price=service.service_price,
        ) for service in services.all()]


@router.post("/add_service", response_model=ServiceSchema, tags=["Services"], name="add_service")
async def add_service(service: ServiceSchema):
    service = Service(**ServiceSchema(**service.dict()).dict())
    async with Service.async_session() as session:
        session.add(service)
        try:
            await session.commit()
        except InterruptedError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="service hasn't added")
        else:
            await session.refresh(service)
            return ServiceSchema(
                service_id=service.id,
                service_name=service.name,
                service_price=service.price,
            )
