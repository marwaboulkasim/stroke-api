from fastapi import APIRouter
from typing import Optional
import filters

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Stroke Prediction !"}

@router.get("/patients/")
def get_patients(
    gender: Optional[str] = None,
    stroke: Optional[int] = None,
    max_age: Optional[float] = None
):
    patients = filters.filter_patients(
        gender=gender,
        stroke=stroke,
        max_age=max_age
    )
    return patients.to_dict(orient='records')




   

# TODO décommenter et compléter
#@router.get("/patients/{patient_id}")
    # Gérer le cas où l'id de patient passé en paramètre n'existe pas


# TODO Ajout de la route stats
