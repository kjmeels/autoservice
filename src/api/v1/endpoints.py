from typing import List

from fastapi import HTTPException
from sqlalchemy import select, delete
from starlette import status

from .router import router
from ...models import Car, Detail, Feedback, Person, Promotion, Service
from ...schemas import (
    CarSchema,
    PersonalListSchema,
    DetailSchema,
    PromotionSchema,
    FeedbackSchema,
    ServiceSchema
)


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


@router.delete("/delete_person/{person_id}", tags=["Personal"], name="delete person")
async def delete_person(person_id: int):
    async with Person.async_session() as session:
        person = await session.execute(delete(Person).where(Person.id == person_id))
        try:
            await session.commit()
        except InterruptedError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="person doesn't deleted")
        return {"status": "OK"}


@router.get("/cars", response_model=List[CarSchema], tags=["Cars"], name="cars_list")
async def cars_list():
    async with Car.async_session() as session:
        cars = await session.scalars(select(Car).order_by(Car.id.asc()))
        return [CarSchema(
            id=car.id,
            brand=car.brand,
            model=car.model,
            engine_type=car.engine_type,
            drive_type=car.drive_type,
            year_of_production=car.year_of_production,
            vin=car.vin,
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
                brand=car.brand,
                model=car.model,
                engine_type=car.engine_type,
                drive_type=car.drive_type,
                year_of_production=car.year_of_production,
                vin=car.vin,
            )


@router.delete("/delete_car/{car_id}", tags=["Cars"], name="delete car")
async def delete_car(car_id: int):
    async with Car.async_session() as session:
        car = await session.execute(delete(Car).where(Car.id == car_id))
        try:
            await session.commit()
        except InterruptedError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="car doesn't deleted")
        return {"status": "OK"}


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
            car_id=detail.car_id,
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
                car_id=detail.car_id,
            )


@router.delete("/delete_detail/{detail_id}", tags=["Details"], name="delete detail")
async def delete_detail(detail_id: int):
    async with Car.async_session() as session:
        detail = await session.execute(delete(Detail).where(Detail.id == detail_id))
        try:
            await session.commit()
        except InterruptedError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="detail doesn't deleted")
        return {"status": "OK"}


@router.get("/promotions", response_model=List[PromotionSchema], tags=["Promotions"], name="promotions_list")
async def promotions_list():
    async with Promotion.async_session() as session:
        promotions = await session.scalars(select(Promotion).order_by(Promotion.id.asc()))
        return [PromotionSchema(
            id=promotion.id,
            type=promotion.type,
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
                id=promotion.id,
                type=promotion.type,
                discount_percentage=promotion.discount_percentage,
                end_date=promotion.end_date,
            )


@router.delete("/delete_promotion/{promotion_id}", tags=["Promotions"], name="delete promotion")
async def delete_promotion(promotion_id: int):
    async with Promotion.async_session() as session:
        promotion = await session.execute(delete(Promotion).where(Promotion.id == promotion_id))
        try:
            await session.commit()
        except InterruptedError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="promotion doesn't deleted")
        return {"status": "OK"}


@router.get("/feedbacks", response_model=List[FeedbackSchema], tags=["Feedbacks"], name="feedbacks_list")
async def feedbacks_list():
    async with Feedback.async_session() as session:
        feedbacks = await session.scalars(select(Feedback).order_by(Feedback.id.asc()))
        return [FeedbackSchema(
            id=feedback.id,
            user_name=feedback.user_name,
            text=feedback.text,
            date=feedback.date,
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
                text=feedback.text,
                date=feedback.date,
            )


@router.delete("/delete_feedback/{feedback_id}", tags=["Feedbacks"], name="delete feedback")
async def delete_feedback(feedback_id: int):
    async with Feedback.async_session() as session:
        feedback = await session.execute(delete(Feedback).where(Feedback.id == feedback_id))
        try:
            await session.commit()
        except InterruptedError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="feedback doesn't deleted")
        return {"status": "OK"}


@router.get("/services", response_model=List[ServiceSchema], tags=["Services"], name="services_list")
async def services_list():
    async with Service.async_session() as session:
        services = await session.scalars(select(Service).order_by(Service.id.asc()))
        return [ServiceSchema(
            id=service.id,
            name=service.name,
            price=service.price,
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
                id=service.id,
                name=service.name,
                price=service.price,
            )


@router.delete("/delete_service/{service_id}", tags=["Services"], name="delete service")
async def delete_service(service_id: int):
    async with Service.async_session() as session:
        service = await session.execute(delete(Service).where(Service.id == service_id))
        try:
            await session.commit()
        except InterruptedError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="service doesn't deleted")
        return {"status": "OK"}
