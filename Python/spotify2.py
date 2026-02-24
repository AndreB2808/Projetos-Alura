class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')


houston = Musica("Houston","Big Giant Circles", "5:23")
UfME = Musica("Unknown from M.E. ver.1",'SEGA · Kenichi Tokoi · Kenichi Tokoi · Atsushi "Sushi" Kosugi', "4:31")
messageFTSsu = Musica("Messages from the Stars (Sped Up)","The Rah Band · Richard Hewson","5:27")

Musica.listar_musicas()