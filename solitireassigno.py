import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 80, 120
BACKGROUND_COLOR = (34, 139, 34)  # Green table background
CARD_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Solitaire")

# Card class
class Card:
    def __init__(self, value, suit, x, y):
        self.value = value
        self.suit = suit
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        self.dragging = False

    def draw(self, screen):
        pygame.draw.rect(screen, CARD_COLOR, self.rect, border_radius=10)
        pygame.draw.rect(screen, TEXT_COLOR, self.rect, 2, border_radius=10)
        font = pygame.font.Font(None, 36)
        text = font.render(f"{self.value}{self.suit}", True, TEXT_COLOR)
        screen.blit(text, (self.rect.x + 10, self.rect.y + 10))

# Create deck
suits = ['♠', '♥', '♦', '♣']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [Card(value, suit, random.randint(100, WIDTH-100), random.randint(50, HEIGHT-150)) for suit in suits for value in values]

# Game loop
running = True
selected_card = None
while running:
    screen.fill(BACKGROUND_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for card in reversed(deck):
                if card.rect.collidepoint(event.pos):
                    selected_card = card
                    card.dragging = True
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_card:
                selected_card.dragging = False
                selected_card = None
        elif event.type == pygame.MOUSEMOTION:
            if selected_card and selected_card.dragging:
                selected_card.rect.x, selected_card.rect.y = event.pos
    
    for card in deck:
        card.draw(screen)
    
    pygame.display.flip()

pygame.quit()
