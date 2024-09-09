import pygame

# Impostazioni generali
WIDTH, HEIGHT = 800, 600
GRAVITY = 0.5  # Accelerazione gravitazionale

# Colori
BIANCO = (255, 255, 255)
NERO = (0, 0, 0)

# Inizializzazione di Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class CorpoRigido:
    def __init__(self, massa, x, y, vx, vy, va, angolo, altezza, larghezza):
        self.massa = massa
        self.posizione = pygame.Vector2(x, y)
        self.velocità = pygame.Vector2(vx, vy)
        self.angolo = angolo
        self.velocità_angolare = va
        self.altezza = altezza
        self.larghezza = larghezza

    def resetta(self, x, y, vx, vy):
        self.posizione = pygame.Vector2(x, y)
        self.velocità = pygame.Vector2(vx, vy)

    def update(self):
        # Aggiorna la posizione
        self.posizione.x += self.velocità.x
        self.posizione.y += self.velocità.y
        self.angolo += self.velocità_angolare
        self.velocità.y += GRAVITY  # Applica la gravità

        # Collisione con il terreno
        if self.posizione.y + self.altezza > HEIGHT:
            self.posizione.y = HEIGHT - self.altezza
            self.velocità.y = -self.velocità.y * 0.8  # Smorzamento

        # Collisione con il soffitto
        if self.posizione.y < 0:
            self.posizione.y = 0
            self.velocità.y = -self.velocità.y * 0.8  # Smorzamento

        # Collisione con i bordi laterali (sinistra e destra)
        if self.posizione.x + self.larghezza > WIDTH:
            self.posizione.x = WIDTH - self.larghezza
            self.velocità.x = -self.velocità.x * 0.8  # Smorzamento

        if self.posizione.x < 0:
            self.posizione.x = 0
            self.velocità.x = -self.velocità.x * 0.8  # Smorzamento

    def disegna(self, superficie):
        # Disegna il rettangolo rappresentante il corpo rigido
        rect = pygame.Rect(self.posizione.x, self.posizione.y, self.larghezza, self.altezza)
        pygame.draw.rect(superficie, BIANCO, rect)


# Funzione principale
def main():
    # Crea una lista di oggetti CorpoRigido
    corpi = [
        CorpoRigido(massa=1, x=100, y=100, vx=2, vy=0, va=0.05, angolo=0, altezza=50, larghezza=50),
        CorpoRigido(massa=1.5, x=300, y=200, vx=-3, vy=-1, va=0.03, angolo=0, altezza=60, larghezza=60),
        CorpoRigido(massa=2, x=500, y=50, vx=1, vy=1, va=0.07, angolo=50, altezza=40, larghezza=40),
    ]
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Aggiorna lo stato di ogni corpo rigido
        for corpo in corpi:
            corpo.update()

        # Riempie lo schermo con colore nero
        screen.fill(NERO)

        # Disegna ogni corpo rigido
        for corpo in corpi:
            corpo.disegna(screen)

        # Aggiorna il display
        pygame.display.flip()

        # Limita i fotogrammi al secondo
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.