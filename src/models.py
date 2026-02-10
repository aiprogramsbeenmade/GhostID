from pydantic import BaseModel, EmailStr
from typing import List, Optional


class IdentityModel(BaseModel):
    # Anagrafica e Physical Roots
    full_name: str
    gender: str
    birth_date: str
    birth_place: str
    codice_fiscale: str
    documento_id: str
    patente: str
    credito: dict

    # Contact & Digital
    email: EmailStr
    password: str
    address: str
    lat_lon: tuple

    # Social & Semantic Bio
    social_profiles: List[dict]
    education: str
    skills: List[str]
    bio: str

    # Digital Fingerprint
    digital_fingerprint: dict