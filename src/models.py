from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(120), default="123")
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    __tablename__ = "planet"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120))
    gravity=db.Column(db.Float)
    created=db.Column(db.DateTime)
    diameter=db.Column(db.Integer)
    edited=db.Column(db.DateTime)
    films=db.Column(db.String(800))
    orbital_period=db.Column(db.Integer)
    population=db.Column(db.Integer)
    residents=db.Column(db.String(500))
    rotation_period=db.Column(db.Integer)
    surface_water=db.Column(db.Integer)
    terrain=db.Column(db.String(500))
    url=db.Column(db.String(900))
    created_by_id=db.Column(db.Integer, db.ForeignKey("user.id"))
    created_by=db.relationship(User)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "gravity": self.gravity,
            "created": self.created,
            "diameter": self.diameter,
            "edited": self.edited,
            "films": self.films,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "residents": self.residents,
            "rotation_period": self.rotation_period,
            "surface_water": self.surface_water,
            "terrain": self.terrain,
            "url": self.url
        }
        
        # def serialize_user(self):
        #     return{
        #      "id": self.id,
        #      "name": self.name,
        #      "gravity": self.gravity,
        #      "created_by": self.created_by.serialize(),
        #       "created_by_id": self.created_by_id.serialize()
        #
        
class Species(db.Model):
    __tablename__ = "species"
    id=db.Column(db.Integer, primary_key=True)
    average_lifespan=db.Column(db.Integer, nullable=False)
    classification=db.Column(db.String(120), nullable=False)
    created=db.Column(db.DateTime, nullable=False)
    designation=db.Column(db.String(120), nullable=False)
    edited=db.Column(db.DateTime, nullable=False)
    eye_colors=db.Column(db.String(120), nullable=False)
    hair_colors=db.Column(db.String(120), nullable=False)
    homeworld=db.Column(db.String(120), nullable=False)
    language=db.Column(db.String(120), nullable=False)
    name=db.Column(db.String(120), nullable=False)
    people=db.Column(db.String(900), nullable=False)
    films=db.Column(db.String(900), nullable=False)
    skin_colors=db.Column(db.String(150), nullable=False)
    url=db.Column(db.String(200), nullable=False)
    created_by_id=db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_by=db.relationship(User)


def __repr__(self):
    return '<Species %r>' % self.name


def serialize(self):
    return{
        "id": self.id,
        "average_lifespan": self.average_lifespan,
        "classification": self.classification,
        "created": self.created,
        "designation": self.designation,
        "edited": self.edited,
        "eye_colors": self.eye_colors,
        "hair_colors": self.hair_colors,
        "homeworld": self.homeworld,
        "language": self.language,
        "name": self.name,
        "people": self.people,
        "films": self.films,
        "skin_colors": self.skin_colors,
        "url": self.url
    }


class Vehicles(db.Model):
    __tablename__ = "vehicles"
    id=db.Column(db.Integer, primary_key=True)
    cargo_capacity=db.Column(db.Integer, nullable=False)
    consumables=db.Column(db.String(150), nullable=False)
    cost_in_credits=db.Column(db.Integer, nullable=False)
    created=db.Column(db.DateTime, nullable=False)
    crew=db.Column(db.Integer, nullable=False)
    edited=db.Column(db.DateTime, nullable=False)
    length=db.Column(db.Float, nullable=False)
    manufacturer=db.Column(db.String(150), nullable=False)
    max_atmosphering_speed=db.Column(db.String(150), nullable=False)
    model=db.Column(db.String(150), nullable=False)
    name=db.Column(db.String(150), nullable=False)
    passengers=db.Column(db.Integer, nullable=False)
    pilots=db.Column(db.String(500), nullable=False)
    films=db.Column(db.String(500), nullable=False)
    url=db.Column(db.String(500), nullable=False)
    vehicle_class=db.Column(db.String(150), nullable=False)
    created_by_id=db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_by=db.relationship(User)

    def __repr__(self):
        return '<Vehicles %r>' % self.name
    
    def serialize(self):
        return{
            "id": self.id,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "cost_in_credits": self.cost_in_credits,
            "created": self.created,
            "crew": self.crew,
            "edited": self.edited,
            "length": self.length,
            "manufacturer": self.manufacturer,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "model": self.model,
            "name": self.name,
            "passengers": self.passengers,
            "pilots": self.pilots,
            "films": self.films,
            "url": self.url,
            "vehicle_class": self.vehicle_class
            }


class Starships(db.Model):
    __tablename__ = "starships"
    id=db.Column(db.Integer, primary_key=True)
    MGLT=db.Column(db.String(150), nullable=False)
    cargo_capacity=db.Column(db.Integer, nullable=False)
    consumables=db.Column(db.String(150), nullable=False)
    cost_in_credits=db.Column(db.Integer, nullable=False)
    created=db.Column(db.Integer, nullable=False)
    crew=db.Column(db.Integer, nullable=False)
    edited=db.Column(db.Integer, nullable=False)
    hyperdrive_rating=db.Column(db.Float)
    length=db.Column(db.Integer, nullable=False)
    manufacturer=db.Column(db.String(150), nullable=False)
    max_atmosphering_speed=db.Column(db.String(150), nullable=False)
    model=db.Column(db.String(150), nullable=False)
    name=db.Column(db.String(150), nullable=False)
    passengers=db.Column(db.Integer, nullable=False)
    films=db.Column(db.String(900), nullable=False)
    pilots=db.Column(db.String(150), nullable=False)
    starship_class=db.Column(db.String(150), nullable=False)
    url=db.Column(db.String(500), nullable=False)


    def __repr__(self):
        return '<Starships %r>' % self.name

    def serialize(self):
        return{
            "id": self.id,
            "MGLT": self.MGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "cost_in_credits": self.cost_in_credits,
            "created": self.created,
            "crew": self.crew,
            "edited": self.edited,
            "hyperdrive_rating": self.hyperdrive_rating,
            "length": self.length,
            "manufacturer": self.manufacturer,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "model": self.model,
            "name": self.name,
            "passengers": self.passengers,
            "films": self.films,
            "pilots": self.pilots,
            "starship_class": self.starship_class,
            "url": self.url
            }


class Films(db.Model):
    __tablename__ = "films"
    id=db.Column(db.Integer, primary_key=True)
    characters=db.Column(db.String(500), nullable=False)
    created=db.Column(db.DateTime, nullable=False)
    director=db.Column(db.String(150), nullable=False)
    edited=db.Column(db.DateTime, nullable=False)
    episode_id=db.Column(db.Integer, nullable=False)
    opening_crawl=db.Column(db.String(500), nullable=False)
    planets=db.Column(db.String(550), nullable=False)
    producer=db.Column(db.String(150), nullable=False)
    release_date=db.Column(db.Date, nullable=False)
    species=db.Column(db.String(500), nullable=False)
    starships=db.Column(db.String(550), nullable=False)
    title=db.Column(db.String(150), nullable=False)
    url=db.Column(db.String(500), nullable=False)
    vehicles=db.Column(db.String(500), nullable=False)


    def __repr__(self):
        return '<Films %r>' % self.name


    def serialize(self):
        return{
            "id": self.id,
            "characters": self.characters,
            "created": self.created,
            "director": self.director,
            "edited": self.edited,
            "episode_id": self.episode_id,
            "opening_crawl": self.opening_crawl,
            "planets": self.planets,
            "producer": self.producer,
            "release_date": self.release_date,
            "species": self.species,
            "starships": self.starships,
            "title": self.title,
            "url": self.url,
            "vehicles": self.vehicles
            }



class People(db.Model):
    __tablename__ = "people"
    id=db.Column(db.Integer, primary_key=True)
    eye_colors=db.Column(db.String(120), nullable=False)
    films=db.Column(db.String(900), nullable=False)
    gender=db.Column(db.String(120), nullable=False)
    hair_colors=db.Column(db.String(120), nullable=False)
    height=db.Column(db.Float, nullable=False)
    homeworld=db.Column(db.String(120), nullable=False)
    mass=db.Column(db.Integer, nullable=False)
    name=db.Column(db.String(120), nullable=False)
    skin_color=db.Column(db.String(150), nullable=False)
    created=db.Column(db.DateTime, nullable=False)
    edited=db.Column(db.DateTime, nullable=False)
    species=db.Column(db.String(500), nullable=False)
    starships=db.Column(db.String(900), nullable=False)
    url=db.Column(db.String(200), nullable=False)
    vehicles=db.Column(db.String(200), nullable=False)
    created_by_id=db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_by=db.relationship(User)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
            return{
                "id": self.id,
                "eye_colors": self.eye_colors,
                "films": self.films,
                "gender": self.gender,
                "hair_colors": self.hair_colors,
                "height": self.height,
                "homeworld": self.homeworld,
                "mass": self.mass,
                "name": self.name,
                "skin_color": self.skin_color,
                "created": self.created,
                "edited": self.edited,
                "species": self.species,
                "starships": self.starships,
                "url": self.url,
                "vehicles": self.vehicles
                }


class Characters(db.Model):
    __tablename__ = "characters"
    id=db.Column(db.Integer, primary_key=True)
    people_id=db.Column(db.Integer, db.ForeignKey("people.id"))
    people=db.relationship(People)
    film_id=db.Column(db.Integer, db.ForeignKey("films.id"))
    film=db.relationship(Films)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return{
            "id": self.id,
            "people_id": self.people_id,
            "people": self.people,
            "film_id": self.film_id,
            "film": self.film
            }

class UserFavorite(db.Model):
    __tablename__ = "user_favorite"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey("user.id"))
    user=db.relationship(User)
    film_id=db.Column(db.Integer, db.ForeignKey("films.id"))
    film=db.relationship(Films)
    starships_id=db.Column(db.Integer, db.ForeignKey("starships.id"))
    starships=db.relationship(Starships)
    people_id=db.Column(db.Integer, db.ForeignKey("people.id"))
    people=db.relationship(People)
    vehicles_id=db.Column(db.Integer, db.ForeignKey("vehicles.id"))
    vehicles=db.relationship(Vehicles)
    characters_id=db.Column(db.Integer, db.ForeignKey("characters.id"))
    characters=db.relationship(Characters)
    species_id=db.Column(db.Integer, db.ForeignKey("species.id"))
    species=db.relationship(Species)
    planet_id=db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet=db.relationship(Planet)

    def __repr__(self):
        return '<UserFavorite %r>' % self.name

    def serialize(self):
        return{
            "id": self.id,
            "user_id": self.user_id,
            "user": self.user,
            "film_id": self.film_id,
            "film": self.film,
            "starships_id": self.starships_id,
            "starships": self.starships,
            "people_id": self.people_id,
            "people": self.people,
            "vehicles_id": self.vehicles_id,
            "vehicles": self.vehicles,
            "characters_id": self.characters_id,
            "characters": self.characters,
            "species_id": self.species_id,
            "species": self.species,
            "planet_id": self.planet_id,
            "planet": self.planet
            }