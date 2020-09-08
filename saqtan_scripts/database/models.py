from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .db import base


class CrimeCodes(base):
    __tablename__ = "crime_codes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    crime_code = Column(Integer)
    crime_desc = Column(String(length=500), default="No desc")

    # relationships
    crime_counts = relationship("CrimeCountsByTypes", back_populates="crime_info")

    def __repr__(self):
        return f"<{self.__tablename__}(crime_code={self.crime_code}, crime_desc={self.crime_desc})>"


class CityCodes(base):
    __tablename__ = "city_codes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    city_code = Column(Integer)
    city_name = Column(String(length=100))
    type = Column(String(length=20))

    # relationships
    count_crimes = relationship("CountCrimesByCities", back_populates="city_info")
    features = relationship("Features", back_populates="city_info")

    def __repr__(self):
        return f"<{self.__tablename__}(city_code={self.city_code}, city_name={self.city_name}, type={self.type})>"


class CountCrimesByCities(base):
    __tablename__ = "count_crimes_by_cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    city_code = Column(Integer, ForeignKey("city_codes.city_code"), unique=True)
    json_data = Column(Text)

    # relationships
    city_info = relationship("CityCodes", back_populates="count_crimes")

    def __repr__(self):
        return f"<{self.__tablename__}(city_code={self.city_code}, json_data={self.json_data})>"


class Features(base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    object_id = Column(Integer, index=True, unique=True)
    year = Column(Integer, index=True)
    period = Column(Integer, index=True)
    crime_code = Column(String(length=10), index=True)
    time_period = Column(Integer, index=True)
    hard_code = Column(String(length=4), index=True)
    ud = Column(String(length=100), index=True)
    organ = Column(String(length=255), index=True)
    dat_vozb = Column(Integer, index=True)
    dat_sover = Column(String(length=4), index=True)
    stat = Column(String(length=255), index=True)
    dat_vozb_str = Column(String(length=255), index=True)
    dat_sover_str = Column(String(length=255), index=True)
    tz1id = Column(String(length=255), index=True)
    reg_code = Column(String(length=100), index=True)
    city_code = Column(Integer, ForeignKey("city_codes.city_code"), index=True)
    status = Column(Integer, index=True)
    org_code = Column(String(length=100), index=True)
    entrydate = Column(Integer, index=True)
    fz1r18p5 = Column(String(length=255), index=True)
    fz1r18p6 = Column(String(length=255), index=True)
    transgression = Column(String(length=255), index=True)
    organ_kz = Column(String(length=255), index=True)
    organ_en = Column(String(length=255), index=True)
    fe1r29p1_id = Column(String(length=100), index=True)
    fe1r32p1 = Column(String(length=255), nullable=True, index=True)
    x_geo = Column(String(length=255), index=True)
    y_geo = Column(String(length=255), index=True)

    # relationships
    city_info = relationship("CityCodes", back_populates="features")

    def __repr__(self):
        return (
            f"<{self.__tablename__}(object_id={self.object_id}, year={self.year}, period={self.period}, "
            f"crime_code={self.crime_code}, time_period={self.time_period}, hard_code={self.hard_code}, "
            f"ud={self.ud}, organ={self.organ}, dat_vozb={self.dat_vozb}, dat_sover={self.dat_sover}, "
            f"stat={self.stat}, dat_vozb_str={self.dat_vozb_str}, dat_sover_str={self.dat_sover_str}, "
            f"tz1id={self.tz1id}, reg_code={self.reg_code}, city_code={self.city_code}, status={self.status}, "
            f"org_code={self.org_code}, entrydate={self.entrydate}, fz1r18p5={self.fz1r18p5}, "
            f"fz1r18p6={self.fz1r18p6}, transgression={self.transgression}, organ_kz={self.organ_kz}, "
            f"organ_en={self.organ_en}, fe1r29p1_id={self.fe1r29p1_id}, fe1r32p1={self.fe1r32p1}, "
            f"x_geo={self.x_geo}, y_geo={self.y_geo})>"
        )


class CrimeCountsByTypes(base):
    __tablename__ = "crime_counts_by_types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer)
    crime_code = Column(Integer, ForeignKey("crime_codes.crime_code"))
    crime_type = Column(String(length=255))
    crime_count = Column(Integer)

    # relationships
    crime_info = relationship("CrimeCodes", back_populates="crime_counts")

    def __repr__(self):
        return (
            f"<{self.__tablename__}(crime_code={self.crime_code}, crime_type={self.crime_type}, "
            f"crime_count={self.crime_count})>"
        )


class CrimesCountPeriods(base):
    __tablename__ = "crimes_count_periods"

    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer)
    json_data = Column(Text)

    def __repr__(self):
        return f"<{self.__tablename__}(year={self.year}, json_data={self.json_data})>"


class CrimesCount(base):
    __tablename__ = "crimes_count"

    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer)
    crimes_count = Column(Integer)
    before_perc = Column(Float)

    def __repr__(self):
        return (
            f"<{self.__tablename__}(year={self.year}, crimes_count={self.crimes_count}, "
            f"before_perc={self.before_perc})>"
        )
