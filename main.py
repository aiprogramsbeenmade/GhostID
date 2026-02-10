from src.generator import IdentityGenerator
import os
from datetime import datetime


def crea_testo_dossier(p):
    """Genera la stringa del dossier stile agenzia."""
    testo = []
    testo.append(f"{'#' * 60}")
    testo.append(f"{'GHOSTID - DOSSIER RISERVATO':^60}")
    testo.append(f"{'#' * 60}")
    testo.append(f"\n[ANAGRAFICA]")
    testo.append(f"Nome: {p.full_name:<25} Genere: {p.gender}")
    testo.append(f"Data di Nascita: {p.birth_date:<18} Luogo: {p.birth_place}")
    testo.append(f"Codice Fiscale: {p.codice_fiscale:<19} Documento: {p.documento_id}")

    testo.append(f"\n[DOMICILIO E GPS]")
    testo.append(f"Indirizzo: {p.address}")
    testo.append(f"Coordinate: LAT {p.lat_lon[0]}, LON {p.lat_lon[1]}")

    testo.append(f"\n[PRESENZA DIGITALE]")
    testo.append(f"Email: {p.email:<25} Password: {p.password}")
    for soc in p.social_profiles:
        testo.append(f"- {soc['platform']}: {soc['handle']} ({soc['focus']})")

    testo.append(f"\n[PROFILO PROFESSIONALE]")
    testo.append(f"Istruzione: {p.education}")
    testo.append(f"RAL Stimata: {p.credito['stima_ral']}")
    testo.append(f"Bio: {p.bio}")
    testo.append(f"\n[DIGITAL FINGERPRINT & SECURITY]")
    testo.append(f"Local IP: {p.digital_fingerprint['local_ip']:<20} Lang: {p.digital_fingerprint['browser_lang']}")
    testo.append(f"User-Agent: {p.digital_fingerprint['user_agent']}")
    testo.append(f"SSH Key: {p.digital_fingerprint['ssh_key'][:50]}...")

    testo.append(f"\n{'#' * 60}\n")

    return "\n".join(testo)


def salva_dossier_su_file(dossier_testo, nome_soggetto):
    """Salva il dossier testuale in una cartella dedicata."""
    folder = "data/dossiers"
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/Dossier_{nome_soggetto.replace(' ', '_')}_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(dossier_testo)

    print(f"📁 Dossier archiviato con successo: {filename}")


def main():
    print("--- GhostID: Professional Identity Framework ---")
    generator = IdentityGenerator(locale='it_IT')

    # 1. Generazione
    new_identity = generator.generate_full_profile()

    # 2. Creazione testo
    dossier_txt = crea_testo_dossier(new_identity)

    # 3. Output a video
    print(dossier_txt)

    # 4. Archiviazione
    salva_dossier_su_file(dossier_txt, new_identity.full_name)


if __name__ == "__main__":
    main()