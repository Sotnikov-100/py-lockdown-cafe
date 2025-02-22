from datetime import date
from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    if any("vaccine" not in friend for friend in friends):
        return "All friends should be vaccinated"

    for friend in friends:
        expiration_date = friend["vaccine"]["expiration_date"]
        if expiration_date < date.today():
            return "All friends should be vaccinated"

    masks_to_buy = sum(
        1 for friend in friends if not friend.get("wearing_a_mask", False)
    )
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    try:
        for friend in friends:
            cafe.visit_cafe(friend)
        return f"Friends can go to {cafe.name}"
    except VaccineError:
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        return f"Friends should buy {masks_to_buy} masks"
