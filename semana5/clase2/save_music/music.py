import os #Libreria que nos ayuda a crear archivos y carpetas

class Music:
    def __init__(self, title, lyrics):
        self.title = title # Establece el titulo de la musica
        self.lyrics = lyrics # Establece la letra de la musica
        
    def save(self, folder=""):
        # Establece la carpeta de destino donde se guardara el archivo
        self.folder = folder 
        
        # Crea la ruta completa del archivo de texto a guardar
        file_path = os.path.join(f"semana5/clase2/save_music/{self.folder}", f"{self.title}.txt")
        
        # Crea el archivo y guarda la letra
        with open(file_path, 'w') as file_music:
            file_music.write(self.lyrics)
            
        # Confirmar que los archivos fueron guardados
        print(f"\n💾 {self.title} was saved in the rute: {file_path}")


class Hymn(Music):
    def save(self, folder="hymns"):
        super().save(folder)

    
class Song(Music):
    def save(self, folder="songs"):
        super().save(folder)
        
        

colombia_hymn = """
CORO 

Oh gloria inmarcesible 
Oh júbilo inmortal 
En surcos de dolores 
El bien germina ya. 

Primera estrofa. 

Cesó la horrible noche 
La libertad sublime 
Derrama las auroras 
De su invencible luz. 
La humanidad entera, 
Que entre cadenas gime, 
Comprende las palabras 
Del que murió en la cruz
""".strip()        
        
hymn1 = Hymn("Himno Colombia", colombia_hymn)
hymn1.save()


''''''


simple_futbol_song = """
Hace tamtos domingos que te espero
Hace tantos domingos que no estas
Simplemente futbol es lo que quiero
Simplemente alegria popular

Un domingo sin poder ir a la cancha
Donde estaba sin poder gritar un gol
Ya la noche de cafe no tenemos de que hablar
Solo vamos a la cancha a disfrutar

Si el mundo tiene forma de pelota
Al arco iris le puedo hacer un gol
Vamos vamos a ganar
Hay que saber diferenciar entre los que juegan bien
O juegan malll

Si no fuera por esfuerzo su talento y su pasion
Solo podria alegrar mi corazon
"""

song1 = Song("Simplemente Futbol", simple_futbol_song)
song1.save()