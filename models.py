class Games:
    def __init__(self, external_id, title, published_by, languages, android, ios, description, age_groups, genres, tags, instruction):
        self._external_id = external_id
        self._title = title
        self._published_by = published_by
        self._languages = languages
        self._android = android
        self._ios = ios
        self._description = description
        self._age_groups = age_groups
        self._genres = genres
        self._tags = tags
        self._instruction = instruction

    def __str__(self):
        return (
            f"\n=== DATOS DEL JUEGO ===\n"
            f"{'ID Externo':<15}: {self._external_id}\n"
            f"{'Título':<15}: {self._title}\n"
            f"{'Publicado por':<15}: {self._published_by}\n"
            f"{'Idiomas':<15}: {', '.join(self._languages) if self._languages else 'Ninguno'}\n"
            f"{'Android':<15}: {self._android}\n"
            f"{'iOS':<15}: {self._ios}\n"
            f"{'Grupos de Edad':<15}: {', '.join(self._age_groups) if self._age_groups else 'Ninguno'}\n"
            f"{'Géneros':<15}: {', '.join(self._genres) if self._genres else 'Ninguno'}\n"
            f"{'Etiquetas (Tags)':<15}: {', '.join(self._tags) if self._tags else 'Ninguno'}\n"
            f"{'Descripción':<15}: {self._description[:60]}...\n"
            f"{'Instrucciones':<15}: {self._instruction[:60]}...\n"
            f"======================="
        )

