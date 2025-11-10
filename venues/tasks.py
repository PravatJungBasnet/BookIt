from bookit.celery import app
from .models import SlotConfigurationn, TimeSlot, TimeSlotStatus
from datetime import datetime, timedelta


@app.task
def generate_slots():
    today = datetime.now().date()
    target = today + timedelta(days=30)
    for config in SlotConfigurationn.objects.all():
        start_time = config.start_time
        end_time = config.end_time
        duration = config.duration
        latest_slot = (
            TimeSlot.objects.filter(slot_condiguartion=config).order_by("-date").first()
        )
        start_date = (
            latest_slot.date + timedelta(days=1)
            if latest_slot
            else today + timedelta(days=1)
        )
        while start_date <= target:
            start_dt = datetime.combine(start_date, start_time)
            end_dt = datetime.combine(start_date, end_time)
            is_weekend = start_dt.weekday() == 5
            if is_weekend and config.weekend_price_hour:
                price = config.weekend_price_hour
            else:
                price = config.base_price_hour

            while start_dt + duration <= end_dt:
                TimeSlot.objects.create(
                    venue=config.venue,
                    slot_condiguartion=config,
                    date=start_date,
                    start_time=start_dt.time(),  # slot start time
                    end_time=(start_dt + duration).time(),  # slot end time
                    price=price,
                    status=TimeSlotStatus.AVAILABLE,
                )
                start_dt += duration
        start_date += timedelta(days=1)
