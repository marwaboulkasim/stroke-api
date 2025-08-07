from fastapi import APIRouter
from typing import Optional
import filters

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Stroke Prediction !"}

<<<<<<< HEAD
@router.get("/patients/")
def get_patients(
    gender: Optional[str] = None,
    stroke: Optional[int] = None,
    max_age: Optional[float] = None
):
    patients = filters.filter_patients(
=======
# TODO décommenter et compléter
@router.get('/patients/')
def get_patients(gender: str = None, stroke: int = None, max_age: float = None):
    filtered_df = filters.filter_patient(
        stroke_data_df=filters.df,
>>>>>>> main
        gender=gender,
        stroke=stroke,
        max_age=max_age
    )
<<<<<<< HEAD
    return patients.to_dict(orient='records')




   
=======
    return filtered_df
>>>>>>> main

# TODO décommenter et compléter
# @router.get("/patients/{patient_id}")
    # Gérer le cas où l'id de patient passé en paramètre n'existe pas


#  Ajout de la route stats 