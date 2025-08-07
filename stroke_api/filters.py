from typing import Optional
import pandas as pd
from fastapi import APIRouter
from api import router

router= APIRouter()
# Chargement des données (une fois)
df= pd.read_csv('data/df_final_test1.csv')

# Tester l'app avec :
# poetry run fastapi dev stroke_api/main.py
# http://127.0.0.1:8000/docs : utiliser la fonctionnalité Try it out pour tester les routes

# Ajout des fonctions de filtrage des données cf notebook 1
@router.get("/patients/")
def filter_patients(df: pd.DataFrame, gender: Optional[str] = None, stroke: Optional[int] = None, max_age: Optional[float] = None) -> list[dict]:

    filtered_df = df.copy()



    if gender is not None:
        filtered_df = filtered_df[filtered_df['gender'] == gender]
    
    if stroke is not None:
        filtered_df = filtered_df[filtered_df['stroke'] == stroke]

    if max_age is not None:
        filtered_df = filter_patients[filtered_df['age'] <= max_age]
    
        return filtered_df.to_dict(orient='records')

# Ensuite faire appel à ces fonctions dans le fichier api.py où sont définies les routes.

# Ajouter les fonctions de filtrage pour les autres routes.


   