from dataclasses import dataclass


@dataclass
class CrimeCodes:
    id: int
    crime_code: int
    crime_desc: str


@dataclass
class CityCodes:
    id: int
    city_code: int
    city_name: str
    type: str


@dataclass
class Features:
    id: int
    object_id: int
    year: int
    period: int
    crime_code: str
    time_period: int
    hard_code: str
    ud: str
    organ: str
    dat_vozb: int
    dat_sover: int
    stat: str
    dat_vozb_str: str
    dat_sover_str: str
    tz1id: str
    reg_code: str
    city_code: int
    status: int
    org_code: str
    entrydate: int
    fz1r18p5: str
    fz1r18p6: str
    transgression: str
    organ_kz: str
    organ_en: str
    fe1r29p1_id: str
    fe1r32p1: str
    x_geo: float
    y_geo: float
