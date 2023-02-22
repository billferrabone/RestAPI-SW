"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, Species, Vehicles, Starships, Films, People, Characters
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_users():
    users=User.query.all()

    response_body = list(map(lambda u: u.serialize(), users))

    return jsonify(response_body), 200


@app.route('/planet')
def get_planets():
    planets=Planet.query.all()

    response_body = list(map(lambda p: p.serialize(), planets))

    return jsonify(response_body), 200

@app.route('/planet/<planet_id>')
def get_single_planet(planet_id):
    planet=Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"msg": "No encontrado"}), 404
    return jsonify(planet.serialize()), 200


@app.route('/planet', methods=['POST'])
def create_planets():
    name=request.json.get("name")
    gravity=request.json.get("gravity")
    diameter=request.json.get("diameter")
    films=request.json.get("films")
    orbital_period=request.json.get("orbital_period")
    population=request.json.get("population")
    residents=request.json.get("residents")
    rotation_period=request.json.get("rotation_period")
    surface_water=request.json.get("surface_water")
    terrain=request.json.get("terrain")
    created_by=request.json.get("created_by")
    new_planet=Planet(name=name, gravity=gravity, created_by_id=1, diameter=diameter, films=films, orbital_period=orbital_period, population=population, residents=residents, rotation_period=rotation_period, surface_water=surface_water, terrain=terrain)
    db.session.add(new_planet)
    db.session.commit()
    return "ok", 201

@app.route("/planet/<planet_id>", methods=["PATCH"])
def update_planet(planet_id):
    planet=Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"msg": "No encontrado"}), 404
    if request.json.get("name") is not None:
        planet.name=request.json.get("name")
    if request.json.get("gravity") is not None:
        planet.gravity=request.json.get("gravity")
    if request.json.get("diameter") is not None:
        planet.diameter=request.json.get("diameter")
    if request.json.get("films") is not None:
        planet.films=request.json.get("films")
    if request.json.get("orbital_period") is not None:
        planet.orbital_period=request.json.get("orbital_period")
    if request.json.get("population") is not None:
        planet.population=request.json.get("population")
    if request.json.get("residents") is not None:
        planet.residents=request.json.get("residents")
    if request.json.get("rotation_period") is not None:
        planet.rotation_period=request.json.get("rotation_period")
    if request.json.get("surface_water") is not None:
        planet.surface_water=request.json.get("surface_water")
    if request.json.get("terrain") is not None:
        planet.terrain=request.json.get("terrain")
    if request.json.get("created_by") is not None:
        planet.created_by_id=request.json.get("created_by")
    
    db.session.add(planet)
    db.session.commit()
        
    return jsonify(planet.serialize()),200

@app.route('/planet/<planet_id>', methods={"DELETE"})
def delete_planet(planet_id):
    planet=Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"msg": "No encontrado"}), 404
    db.session.delete(planet)
    db.session.commit()
    
    return jsonify({"msg": "Planeta eliminado"}), 200


@app.route('/species')
def get_species():
    species=Species.query.all()

    response_body = list(map(lambda s: s.serialize(), species))

    return jsonify(response_body), 200

@app.route('/species/<species_id>')
def get_single_species(species_id):
    species=Species.query.get(species_id)
    if species is None:
        return jsonify({"msg": "No encontrado"}), 404
    return jsonify(species.serialize()), 200


@app.route('/species', methods=['POST'])
def create_speciess():
    name=request.json.get("name")
    average_lifespan=request.json.get("average_lifespan")
    classification=request.json.get("classification")
    designation=request.json.get("designation")
    eye_colors=request.json.get("eye_colors")
    hair_colors=request.json.get("hair_colors")
    skin_colors=request.json.get("skin_colors")
    homeworld=request.json.get("homeworld")
    language=request.json.get("language")
    created_by=request.json.get("created_by")
    people=request.json.get("people")
    films=request.json.get("films")
    new_species=Species(id=id, name=name, average_lifespan=average_lifespan, classification=classification, created=created, designation=designation, eye_colors=eye_colors, hair_colors=hair_colors,  homeworld=homeworld, language=language, people=people, films=films, skin_colors=skin_colors, created_by_id=created_by)
    db.session.add(new_species)
    db.session.commit()
    return "ok", 201


@app.route("/species/<species_id>", methods=["PATCH"])
def update_species(species_id):
    species=Species.query.get(species_id)
    if species is None:
        return jsonify({"msg": "No encontrado"}), 404
    if request.json.get("name") is not None:
        species.name=request.json.get("name")
    if request.json.get("average_lifespan") is not None:
        species.average_lifespan=request.json.get("average_lifespan")
    if request.json.get("created_by") is not None:
        species.created_by_id=request.json.get("created_by")
    if request.json.get("classification") is not None:
        species.classification=request.json.get("classification")
    if request.json.get("designation") is not None:
        species.designation=request.json.get("designation")
    if request.json.get("eye_colors") is not None:
        species.eye_colors=request.json.get("eye_colors")
    if request.json.get("hair_colors") is not None:
        species.hair_colors=request.json.get("hair_colors")
    if request.json.get("homeworld") is not None:
        species.homeworld=request.json.get("homeworld")
    if request.json.get("language") is not None:
        species.language=request.json.get("language")
    if request.json.get("people") is not None:
        species.people=request.json.get("people")
    if request.json.get("films") is not None:
        species.films=request.json.get("films")
    if request.json.get("skin_colors") is not None:
        species.skin_colors=request.json.get("skin_colors")

    db.session.add(species)
    db.session.commit()
        
    return jsonify(species.serialize()),200


@app.route('/species/<species_id>', methods={"DELETE"})
def delete_species(species_id):
    species=Species.query.get(species_id)
    if species is None:
        return jsonify({"msg": "No encontrado"}), 404
    db.session.delete(species)
    db.session.commit()
    
    return jsonify({"msg": "Especie eliminada"}), 200


@app.route('/vehicles')
def get_vehicles():
    vehicles=Vehicles.query.all()

    response_body = list(map(lambda v: v.serialize(), vehicles))

    return jsonify(response_body), 200

@app.route('/vehicles/<vehicles_id>')
def get_single_vehicles(vehicles_id):
    vehicles=Vehicles.query.get(vehicles_id)
    if vehicles is None:
        return jsonify({"msg": "No encontrado"}), 404
    return jsonify(vehicles.serialize()), 200

@app.route('/vehicles', methods=['POST'])
def create_vehicles():
    name=request.json.get("name")
    cargo_capacity=request.json.get("cargo_capacity")
    consumables=request.json.get("consumables")
    cost_in_credits=request.json.get("cost_in_credits")
    crew=request.json.get("crew")
    length=request.json.get("length")
    manufacturer=request.json.get("manufacturer")
    max_atmosphering_speed=request.json.get("max_atmosphering_speed")
    model=request.json.get("model")
    passengers=request.json.get("passengers")
    films=request.json.get("films")
    pilots=request.json.get("pilots")
    vehicle_class=request.json.get("vehicle_class")
    created_by=request.json.get("created_by")
    new_vehicles=Vehicles(id=id, name=name, cargo_capacity=cargo_capacity, consumables=consumables, cost_in_credits=cost_in_credits, crew=crew, length=length,  manufacturer= manufacturer, max_atmosphering_speed=max_atmosphering_speed, model=model, films=films, passengers=passengers, pilots=pilots, vehicle_class=vehicle_class, created_by_id=created_by)
    db.session.add(new_vehicles)
    db.session.commit()
    return "ok", 201



@app.route("/vehicles/<vehicles_id>", methods=["PATCH"])
def update_vehicles(vehicles_id):
    vehicles=Vehicles.query.get(vehicles_id)
    if vehicles is None:
        return jsonify({"msg": "No encontrado"}), 404
    if request.json.get("name") is not None:
        vehicles.name=request.json.get("name")
    if request.json.get("cargo_capacity") is not None:
        vehicles.cargo_capacity=request.json.get("cargo_capacity")
    if request.json.get("consumables") is not None:
        vehicles.consumables=request.json.get("consumables")
    if request.json.get("cost_in_credits") is not None:
        vehicles.cost_in_credits=request.json.get("cost_in_credits")
    if request.json.get("crew") is not None:
        vehicles.crew=request.json.get("crew")
    if request.json.get("length") is not None:
        vehicles.length=request.json.get("length")
    if request.json.get("manufacturer") is not None:
        vehicles.manufacturer=request.json.get("manufacturer")
    if request.json.get("max_atmosphering_speed") is not None:
        vehicles.max_atmosphering_speed=request.json.get("max_atmosphering_speed")
    if request.json.get("model") is not None:
        vehicles.model=request.json.get("model")
    if request.json.get("films") is not None:
        vehicles.films=request.json.get("films")
    if request.json.get("passengers") is not None:
        vehicles.passengers=request.json.get("passengers")
    if request.json.get("pilots") is not None:
        vehiles.pilots=request.json.get("pilots")
    if request.json.get("vehicle_class") is not None:
        vehicles.vehicle_class=request.json.get("vehicle_class")

    db.session.add(vehicles)
    db.session.commit()
        
    return jsonify(vehicles.serialize()),200

@app.route('/vehicles/<vehicles_id>', methods={"DELETE"})
def delete_vehicles(vehicles_id):
    vehicles=Vehicles.query.get(vehicles_id)
    if vehicles is None:
        return jsonify({"msg": "No encontrado"}), 404
    db.session.delete(vehicles)
    db.session.commit()
    
    return jsonify({"msg": "Vehiculo eliminado"}), 200



@app.route('/starships')
def get_starships():
    starships=Starships.query.all()

    response_body = list(map(lambda z: z.serialize(), starships))

    return jsonify(response_body), 200

@app.route('/starships/<starships_id>')
def get_single_starships(starships_id):
    starships=Starships.query.get(starships_id)
    if starships is None:
        return jsonify({"msg": "No encontrado"}), 404
    return jsonify(starships.serialize()), 200

@app.route('/starships', methods=['POST'])
def create_starshipss():
    name=request.json.get("name")
    cargo_capacity=request.json.get("cargo_capacity")
    consumables=request.json.get("consumables")
    cost_in_credits=request.json.get("cost_in_credits")
    crew=request.json.get("crew")
    length=request.json.get("length")
    manufacturer=request.json.get("manufacturer")
    max_atmosphering_speed=request.json.get("max_atmosphering_speed")
    model=request.json.get("model")
    passengers=request.json.get("passengers")
    hyperdrive_rating=request.json.get("hyperdrive_rating")
    films=request.json.get("films")
    pilots=request.json.get("pilots")
    vehicle_class=request.json.get("vehicle_class")
    created_by=request.json.get("created_by")
    new_starships=Starships(id=id, MGLT=MGLT, cargo_capacity=cargo_capacity, consumables=consumables, cost_in_credits=cost_in_credits, crew=crew, length=length,  manufacturer=manufacturer, max_atmosphering_speed=max_atmosphering_speed, model=model, films=films, name=name, passengers=passengers, pilots=pilots, hyperdrive_rating=hyperdrive_rating, starship_class=starship_class, created_by_id=created_by)
    db.session.add(new_starships)
    db.session.commit()
    return "ok", 201

@app.route("/starships/<starships_id>", methods=["PATCH"])
def update_starships(starships_id):
    starships=Starships.query.get(starships_id)
    if starships is None:
        return jsonify({"msg": "No encontrado"}), 404
    if request.json.get("name") is not None:
        starships.name=request.json.get("name")
    if request.json.get("cargo_capacity") is not None:
        starships.cargo_capacity=request.json.get("cargo_capacity")
    if request.json.get("consumables") is not None:
        starships.consumables=request.json.get("consumables")
    if request.json.get("cost_in_credits") is not None:
        starships.cost_in_credits=request.json.get("cost_in_credits")
    if request.json.get("crew") is not None:
        starships.crew=request.json.get("crew")
    if request.json.get("length") is not None:
        starships.length=request.json.get("length")
    if request.json.get("manufacturer") is not None:
        starships.manufacturer=request.json.get("manufacturer")
    if request.json.get("max_atmosphering_speed") is not None:
        starships.max_atmosphering_speed=request.json.get("max_atmosphering_speed")
    if request.json.get("model") is not None:
        starships.model=request.json.get("model")
    if request.json.get("passengers") is not None:
        starships.passengers=request.json.get("passengers")
    if request.json.get("films") is not None:
        starships.films=request.json.get("films")
    if request.json.get("pilots") is not None:
        starships.pilots=request.json.get("pilots")
    if request.json.get("vehicle_class") is not None:
        starships.vehicle_class=request.json.get("vehicle_class")
    if request.json.get("hyperdrive_rating") is not None:
        starships.hyperdrive_rating=request.json.get("hyperdrive_rating")

    db.session.add(starships)
    db.session.commit()
        
    return jsonify(starships.serialize()),200


@app.route('/starships/<starships_id>', methods={"DELETE"})
def delete_starships(starships_id):
    starships=Starships.query.get(starships_id)
    if starships is None:
        return jsonify({"msg": "No encontrado"}), 404
    db.session.delete(starships)
    db.session.commit()
    
    return jsonify({"msg": "Starship eliminado"}), 200



@app.route('/films')
def get_films():
    films=Films.query.all()

    response_body = list(map(lambda f: f.serialize(), films))

    return jsonify(response_body), 200


@app.route('/films/<films_id>')
def get_single_films(films_id):
    films=Films.query.get(films_id)
    if films is None:
        return jsonify({"msg": "No encontrado"}), 404
    return jsonify(films.serialize()), 200


@app.route('/films', methods=['POST'])
def create_filmss():
    title=request.json.get("title")
    characters=request.json.get("characters")
    director=request.json.get("director")
    episode_id=request.json.get("episode_id")
    opening_crawl=request.json.get("opening_crawl")
    planets=request.json.get("planets")
    producer=request.json.get("producer")
    release_date=request.json.get("release_date")
    species=request.json.get("species")
    starships=request.json.get("starships")
    vehicles=request.json.get("vehicles")
    created_by=request.json.get("created_by")
    new_films=Films(id=id, characters=characters, director=director, episode_id=episode_id, opening_crawl=opening_crawl, planets=planets,  producer=producer, release_date=release_date, species=species, title=title, starships=starships, vehicles=vehicles, starship_class=starship_class, created_by_id=created_by)
    db.session.add(new_films)
    db.session.commit()
    return "ok", 201


@app.route("/films/<films_id>", methods=["PATCH"])
def update_films(films_id):
    films=Films.query.get(films_id)
    if films is None:
        return jsonify({"msg": "No encontrado"}), 404
    if request.json.get("title") is not None:
        starships.title=request.json.get("title")
    if request.json.get("characters") is not None:
        films.characters=request.json.get("characters")
    if request.json.get("director") is not None:
        films.director=request.json.get("director")
    if request.json.get("episode_id") is not None:
        films.episode_id=request.json.get("episode_id")
    if request.json.get("opening_crawl") is not None:
        films.opening_crawl=request.json.get("opening_crawl")
    if request.json.get("planets") is not None:
        films.planets=request.json.get("planets")
    if request.json.get("producer") is not None:
        films.producer=request.json.get("producer")
    if request.json.get("release_date") is not None:
        films.release_date=request.json.get("release_date")
    if request.json.get("species") is not None:
        films.species=request.json.get("species")
    if request.json.get("starships") is not None:
        films.starships=request.json.get("starships")
    if request.json.get("vehicles") is not None:
        films.vehicles=request.json.get("vehicles")

    db.session.add(films)
    db.session.commit()
        
    return jsonify(films.serialize()),200



@app.route('/films/<films_id>', methods={"DELETE"})
def delete_films(films_id):
    films=Films.query.get(films_id)
    if films is None:
        return jsonify({"msg": "No encontrado"}), 404
    db.session.delete(films)
    db.session.commit()
    
    return jsonify({"msg": "Film eliminado"}), 200



@app.route('/people')
def get_people():
    people=People.query.all()

    response_body = list(map(lambda x: x.serialize(), people))

    return jsonify(response_body), 200


@app.route('/people/<people_id>')
def get_single_people(people_id):
    people=People.query.get(people_id)
    if people is None:
        return jsonify({"msg": "No encontrado"}), 404
    return jsonify(people.serialize()), 200


@app.route('/people', methods=['POST'])
def create_peoples():
    birth_year=request.json.get("birth_year")
    eye_color=request.json.get("eye_color")
    films=request.json.get("films")
    gender=request.json.get("gender")
    hair_colors=request.json.get("hair_colors")
    height=request.json.get("height")
    homeworld=request.json.get("homeworld")
    mass=request.json.get("mass")
    name=request.json.get("name")
    skin_color=request.json.get("skin_color")
    species=request.json.get("species")
    starships=request.json.get("starships")
    vehicles=request.json.get("vehicles")
    created_by=request.json.get("created_by")
    new_people=People(id=id, birth_year=birth_year, vehicles=vehicles, starships=starships, mass=mass, gender=gender, height=height, eye_color=eye_color, name=name, created=created, hair_colors=hair_colors,  homeworld=homeworld, films=films, species=species, skin_color=skin_color, created_by_id=created_by)
    db.session.add(new_people)
    db.session.commit()
    return "ok", 201



@app.route("/people/<people_id>", methods=["PATCH"])
def update_people(people_id):
    people=People.query.get(people_id)
    if people is None:
        return jsonify({"msg": "No encontrado"}), 404
    if request.json.get("birth_year") is not None:
        people.birth_year=request.json.get("birth_year")
    if request.json.get("eye_color") is not None:
        people.eye_color=request.json.get("eye_color")
    if request.json.get("films") is not None:
        people.films=request.json.get("films")
    if request.json.get("gender") is not None:
        people.gender=request.json.get("gender")
    if request.json.get("hair_colors") is not None:
        people.hair_colors=request.json.get("hair_colors")
    if request.json.get("height") is not None:
        people.height=request.json.get("height")
    if request.json.get("homeworld") is not None:
        people.homeworld=request.json.get("homeworld")
    if request.json.get("mass") is not None:
        people.mass=request.json.get("mass")
    if request.json.get("name") is not None:
        people.name=request.json.get("name")
    if request.json.get("skin_color") is not None:
        people.skin_color=request.json.get("skin_color")
    if request.json.get("species") is not None:
        people.species=request.json.get("species")
    if request.json.get("starships") is not None:
        people.starships=request.json.get("starships")
    if request.json.get("vehicles") is not None:
        people.vehicles=request.json.get("vehicles")

    db.session.add(films)
    db.session.commit()
        
    return jsonify(films.serialize()),200


@app.route('/people/<people_id>', methods={"DELETE"})
def delete_people(people_id):
    people=People.query.get(people_id)
    if people is None:
        return jsonify({"msg": "No encontrado"}), 404
    db.session.delete(people)
    db.session.commit()
    
    return jsonify({"msg": "People eliminado"}), 200


@app.route('/characters')
def get_characters():
    characters=Characters.query.all()

    response_body = list(map(lambda h: h.serialize(), characters))

    return jsonify(response_body), 200

@app.route('/characters/<characters_id>')
def get_single_characters(characters_id):
    characters=Characters.query.get(characters_id)
    if characters is None:
        return jsonify({"msg": "No encontrado"}), 404
    return jsonify(characters.serialize()), 200

@app.route('/characters', methods=['POST'])
def create_characters():
    people_id=request.json.get("people_id")
    people=request.json.get("people")
    film=request.json.get("film")
    film_id=request.json.get("film_id")
    new_character=Characters(id=id, people_id=people_id, people=people, film=film, film_id=film_id)
    db.session.add(new_character)
    db.session.commit()
    return "ok", 201

@app.route("/characters/<characters_id>", methods=["PATCH"])
def update_characters(characters_id):
    characters=Characters.query.get(characters_id)
    if characters is None:
        return jsonify({"msg": "No encontrado"}), 404
    if request.json.get("people_id") is not None:
        characters.people_id=request.json.get("people_id")
    if request.json.get("people") is not None:
        characters.people=request.json.get("people")
    if request.json.get("film") is not None:
        characters.film=request.json.get("film")
    if request.json.get("film_id") is not None:
        characters.film_id=request.json.get("film_id")

    db.session.add(films)
    db.session.commit()
        
    return jsonify(films.serialize()),200

@app.route('/characters/<characters_id>', methods={"DELETE"})
def delete_characters(characters_id):
    characters=Characters.query.get(characters_id)
    if characters is None:
        return jsonify({"msg": "No encontrado"}), 404
    db.session.delete(characters)
    db.session.commit()
    
    return jsonify({"msg": "Personaje eliminado"}), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
