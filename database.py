import os
import sys
import django

RUTA_DJANGO = r'C:\Users\Samue\Desktop\JuegaGratis'

sys.path.insert(0, RUTA_DJANGO)
sys.path.insert(0, os.path.join(RUTA_DJANGO, 'main'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'

django.setup()

print("¡CONEXIÓN ESTABLECIDA! Django está encendido y listo.")

from catalogo.models import Game, Company, Language, AgeGroup, Genre, Tag

def save_game(game_obj):
    try:
        if Game.objects.filter(external_id=game_obj._external_id).exists():
            print("juego existe")
            return None
        print("juego NO existe")

        publisher, _ = Company.objects.get_or_create(name=game_obj._published_by)

        new_game = Game.objects.create(
            external_id=game_obj._external_id,
            title=game_obj._title,
            published_by=publisher,
            android=game_obj._android,
            ios=game_obj._ios,
            description=game_obj._description,
            instruction=game_obj._instruction,
            )

        for lang in game_obj._languages:
            lang_db, _ = Language.objects.get_or_create(name=lang)
            new_game.languages.add(lang_db)

        for age in game_obj._age_groups:
            age_db, _ = AgeGroup.objects.get_or_create(name=age)
            new_game.age_groups.add(age_db)

        for gen in game_obj._genres:
            gen_db, _ = Genre.objects.get_or_create(name=gen)
            new_game.genres.add(gen_db)
        
        for tag in game_obj._tags:
            tag_db, _ = Tag.objects.get_or_create(name=tag)
            new_game.tags.add(tag_db)
            
        print("Juego guardado con exito!")
        return
    except Exception as e:
        print(f"error: {e}")
        return