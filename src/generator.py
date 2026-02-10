import random
import re
from faker import Faker
from .models import IdentityModel
from .providers.osm_client import OSMClient


class IdentityGenerator:
    def __init__(self, locale: str = 'it_IT'):
        self.fake = Faker(locale)
        self.osm = OSMClient()
        # Dizionario per tradurre e arricchire i job (Semantic Bio)
        self.job_mapping = {
            "Surveyor": {"ita": "Geometra", "skills": ["Rilievi topografici", "CAD", "GPS", "Normativa edilizia"]},
            "Engineer": {"ita": "Ingegnere", "skills": ["Problem solving", "Project Management", "Analisi tecnica"]},
            "Doctor": {"ita": "Medico", "skills": ["Diagnostica", "Assistenza paziente", "Ricerca clinica"]},
            "Teacher": {"ita": "Insegnante", "skills": ["Didattica", "Comunicazione", "Pianificazione"]},
            # Se il job non è qui, useremo valori generici
        }

    def _generate_cf(self, name, surname, birth_date, gender):
        """Genera un Codice Fiscale con logica reale per nomi e cognomi."""

        def get_vowels(s):
            return "".join(re.findall(r'[aeiouAEIOU]', s)).upper()

        def get_cons(s):
            return "".join(re.findall(r'[^aeiouAEIOU]', s)).upper()

        # Logica Cognome: prime 3 consonanti (o vocali se mancano)
        c_cons = (get_cons(surname) + get_vowels(surname) + "XXX")[:3]

        # Logica Nome: consonanti 1, 3, 4 (se sono almeno 4), altrimenti le prime 3
        n_cons_all = get_cons(name)
        if len(n_cons_all) >= 4:
            n_cons = n_cons_all[0] + n_cons_all[2] + n_cons_all[3]
        else:
            n_cons = (n_cons_all + get_vowels(name) + "XXX")[:3]

        year = birth_date[2:4]
        # Mappa mesi reale
        months = ["A", "B", "C", "D", "E", "H", "L", "M", "P", "R", "S", "T"]
        month_letter = months[int(birth_date[5:7]) - 1]

        day = int(birth_date[8:10]) + (40 if gender == 'F' else 0)
        day_str = str(day).zfill(2)

        return f"{c_cons}{n_cons}{year}{month_letter}{day_str}H501Z"

    def _generate_coherent_password(self, name, birth_date):
        """Crea una password che un umano sceglierebbe davvero."""
        year = birth_date[:4]
        clean_name = name.split()[0].title()
        special = random.choice(["!", "?", "*", "$"])
        return f"{clean_name}{year}{special}"

    def _generate_education(self, birth_date):
        """Genera un percorso accademico in una città universitaria reale."""
        universita_top = ["Roma", "Milano", "Bologna", "Padova", "Napoli", "Torino", "Pisa", "Firenze"]
        citta_uni = random.choice(universita_top)
        anno_laurea = int(birth_date[:4]) + 24
        return f"Laurea conseguita nel {anno_laurea} presso l'Università degli Studi di {citta_uni}"

    def _generate_documents(self):
        """Genera numeri di documenti con formati reali italiani."""
        # CIE: 2 lettere, 5 numeri, 2 lettere (es. CA12345BB)
        cie = f"{self.fake.bothify(text='??#####??').upper()}"
        # Patente: U1 seguito da 7 numeri e 1 lettera
        patente = f"U1{self.fake.bothify(text='#######?').upper()}"
        return cie, patente

    def _get_credit_card(self):
        """Genera una carta coerente (non scaduta)."""
        brand = random.choice(["Visa", "Mastercard"])
        return {
            "tipo": brand,
            "numero": self.fake.credit_card_number(card_type=brand.lower()),
            "scadenza": self.fake.credit_card_expire(),
            "cvv": self.fake.credit_card_security_code()
        }

    def _generate_social_presence(self, first_name, last_name):
        """Genera un ecosistema di profili social coerenti."""
        base_handle = f"{first_name.lower()}_{last_name.lower()}"
        year_short = self.fake.date_of_birth(minimum_age=25, maximum_age=65).strftime("%y")

        profiles = [
            {
                "platform": "LinkedIn",
                "handle": f"in/{base_handle}",
                "url": f"https://www.linkedin.com/in/{base_handle}",
                "focus": "Professionale"
            },
            {
                "platform": "Instagram",
                "handle": f"@{base_handle}_{year_short}",
                "url": f"https://www.instagram.com/{base_handle}_{year_short}",
                "focus": "Personale/Lifestyle"
            },
            {
                "platform": "Facebook",
                "handle": f"{first_name}.{last_name}.ufficiale",
                "url": f"https://www.facebook.com/{first_name}.{last_name}",
                "focus": "Privato"
            },
            {
                "platform": "X (Twitter)",
                "handle": f"@{last_name}{first_name[0]}{random.randint(10, 99)}",
                "url": f"https://x.com/{last_name}{first_name[0]}{random.randint(10, 99)}",
                "focus": "News/Opinioni"
            }
        ]
        return profiles

    def _generate_digital_fingerprint(self):
        """Genera l'impronta tecnica del dispositivo dell'utente."""
        # User Agents realistici (Browser e OS)
        user_agents = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        ]

        return {
            "user_agent": random.choice(user_agents),
            "local_ip": f"192.168.1.{random.randint(2, 254)}",
            "ssh_key": f"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC{self.fake.password(length=40)}... ghostid@access",
            "browser_lang": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7"
        }

    def generate_full_profile(self) -> IdentityModel:
        gender = random.choice(['M', 'F'])
        first_name = self.fake.first_name_male() if gender == 'M' else self.fake.first_name_female()
        last_name = self.fake.last_name()
        birth_date = str(self.fake.date_of_birth(minimum_age=25, maximum_age=65))

        # --- 1. Logica Job e Bio ---
        raw_job = self.fake.job()
        job_info = self.job_mapping.get(raw_job, {"ita": raw_job, "skills": ["Analisi", "Problem Solving"]})

        # Pulizia e traduzione
        job_name = job_info['ita'].lower().replace(",", " e")
        if "engineer" in job_name:
            job_ita = job_name.replace("engineer", "ingegnere")
        elif "drilling" in job_name:
            job_ita = "ingegnere di perforazione"
        else:
            job_ita = job_name.replace("manager", "responsabile")

        suffix = "a" if gender == "F" else "o"
        education = self._generate_education(birth_date)
        bio = f"Sono {first_name}, espert{suffix} in {job_ita}. {education}. Competenze chiave: {', '.join(job_info['skills'])}."

        # --- 2. Social Presence (Multi-Profilo) ---
        # Richiamiamo il metodo che crea la lista di dizionari per FB, IG, LinkedIn e X
        social_ecosystem = self._generate_social_presence(first_name, last_name)

        # --- 3. GPS e Indirizzo ---
        city = self.fake.city()
        osm_data = self.osm.fetch_real_address(city=city)

        if osm_data and osm_data.get("lat"):
            address = osm_data["display_name"]
            lat_lon = (float(osm_data["lat"]), float(osm_data["lon"]))
        else:
            address = f"Piazza Centrale 1, {city}, Italia"
            lat_lon = (41.8902, 12.4922)

        # --- 4. Finanza ---
        eta = 2026 - int(birth_date[:4])
        ral_base = 30000 + (eta * 500) + random.randint(-5000, 10000)

        # --- 5. Digital Fingerprint ---
        fingerprint = self._generate_digital_fingerprint()

        # --- 6. Return finale con i nuovi campi ---
        return IdentityModel(
            full_name=f"{first_name} {last_name}",
            gender=gender,
            birth_date=birth_date,
            birth_place=self.fake.city(),
            codice_fiscale=self._generate_cf(first_name, last_name, birth_date, gender),
            documento_id=f"{self.fake.bothify(text='??#####??').upper()}",
            patente=f"U1{self.fake.bothify(text='#######?').upper()}",
            email=f"{first_name.lower()}.{last_name.lower()}@{self.fake.free_email_domain()}",
            password=self._generate_coherent_password(first_name, birth_date),
            address=address,
            lat_lon=lat_lon,
            social_profiles=social_ecosystem,
            education=education,
            skills=job_info["skills"],
            digital_fingerprint=fingerprint,
            bio=bio,
            credito={**self._get_credit_card(), "stima_ral": f"€{ral_base:,}"}
        )