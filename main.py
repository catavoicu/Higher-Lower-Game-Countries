import pygame
import random
import pandas as pd
import os

pygame.init()

WIDTH = 1200
HEIGHT = 586
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Higher Lower Game")
HL = pygame.transform.scale(pygame.image.load("lower_higher.png"), (WIDTH, HEIGHT))
BL = pygame.transform.scale(pygame.image.load("poza_fundal.png"), (WIDTH, HEIGHT))
GO = pygame.transform.scale(pygame.image.load("gameover.png"), (WIDTH, HEIGHT))

SCORE_FONT = pygame.font.SysFont(None, 50)
score = 0
high_score = 0
score_text = SCORE_FONT.render(f"Score: {score}", True, (255, 255, 255))
high_score_text = SCORE_FONT.render(f"High Score: {high_score}", True, (255, 255, 255))

BUTTON_WIDTH, BUTTON_HEIGHT = 140, 60
BUTTON_PLAY_POS = (WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT - 100)
BUTTON_HIGH_POS = (WIDTH - 340, HEIGHT - 240)
BUTTON_LOWER_POS = (WIDTH - 340, HEIGHT - 160)

BUTTON_COLOR_ACTIVE = (0, 255, 0)
font = pygame.font.SysFont(None, 30)
text_play = font.render("PLAY", True, (255, 255, 255))
text_higher = font.render("HIGHER", True, (255, 255, 255))
text_lower = font.render("LOWER", True, (255, 255, 255))

data = pd.read_excel("lista_tarilor.xlsx")


def draw(country1, population1, country2, population2, show_play_button=True, game_over=False):
    WIN.blit(HL, (0, 0))

    if country1 and country2:
        steag_tara1 = pygame.transform.scale(
            pygame.image.load(os.path.join("tari", f"{country1}.png")), (350, 200))
        steag_tara2 = pygame.transform.scale(
            pygame.image.load(os.path.join("tari", f"{country2}.png")), (350, 200))
        WIN.blit(BL, (0, 0))
        WIN.blit(steag_tara1,
                 (WIDTH - 950 - steag_tara1.get_width() // 2, HEIGHT - 400 - steag_tara1.get_height() // 2))
        WIN.blit(steag_tara2,
                 (WIDTH - 270 - steag_tara2.get_width() // 2, HEIGHT - 400 - steag_tara2.get_height() // 2))

    font = pygame.font.SysFont(None, 42)
    text_country1 = font.render(f"{country1}", True, (255, 255, 255))
    text_population1 = font.render(f"Population: {population1}", True, (255, 255, 255))
    WIN.blit(text_country1, (WIDTH - 950 - text_country1.get_width() / 2, HEIGHT // 2 + 10))

    text_country2 = font.render(f"{country2}", True, (255, 255, 255))
    text_population2 = font.render(f"Population: {population2}", True, (255, 255, 255))
    WIN.blit(text_country2, (WIDTH - 270 - text_country2.get_width() // 2, HEIGHT // 2 + 10))

    if game_over:
        WIN.blit(GO, (0, 0))
    elif show_play_button:
        # Desenează butonul PLAY
        pygame.draw.rect(WIN, BUTTON_COLOR_ACTIVE,
                         (BUTTON_PLAY_POS[0], BUTTON_PLAY_POS[1], BUTTON_WIDTH, BUTTON_HEIGHT))
        WIN.blit(text_play, (BUTTON_PLAY_POS[0] + (BUTTON_WIDTH - text_play.get_width()) // 2,
                             BUTTON_PLAY_POS[1] + (BUTTON_HEIGHT - text_play.get_height()) // 2))
    else:
        # Desenează butoanele HIGHER și LOWER
        pygame.draw.rect(WIN, BUTTON_COLOR_ACTIVE,
                         (BUTTON_HIGH_POS[0], BUTTON_HIGH_POS[1], BUTTON_WIDTH, BUTTON_HEIGHT))
        WIN.blit(text_higher, (BUTTON_HIGH_POS[0] + (BUTTON_WIDTH - text_higher.get_width()) // 2,
                               BUTTON_HIGH_POS[1] + (BUTTON_HEIGHT - text_higher.get_height()) // 2))

        # Desenează butonul LOWER în roșu
        pygame.draw.rect(WIN, (255, 0, 0), (BUTTON_LOWER_POS[0], BUTTON_LOWER_POS[1], BUTTON_WIDTH, BUTTON_HEIGHT))
        WIN.blit(text_lower, (BUTTON_LOWER_POS[0] + (BUTTON_WIDTH - text_lower.get_width()) // 2,
                              BUTTON_LOWER_POS[1] + (BUTTON_HEIGHT - text_lower.get_height()) // 2))
        WIN.blit(score_text, (10, 550))
        WIN.blit(high_score_text, (950, 550))
        WIN.blit(text_population1, (WIDTH - 950 - text_population1.get_width() / 2, HEIGHT // 2 + 60))

    pygame.display.update()


def main():
    global score, high_score, score_text, high_score_text
    run = True
    play_button_clicked = False
    game_over = False
    game_over_start_time = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if not play_button_clicked and BUTTON_PLAY_POS[0] <= x <= BUTTON_PLAY_POS[0] + BUTTON_WIDTH and \
                        BUTTON_PLAY_POS[1] <= y <= BUTTON_PLAY_POS[1] + BUTTON_HEIGHT:
                    print("Button PLAY clicked!")
                    play_button_clicked = True
        if game_over:
            draw("", 0, "", 0, show_play_button=False, game_over=True)
        elif play_button_clicked:
            # Alege două țări aleatoare din datele încărcate din fișierul Excel
            countries = random.sample(list(data["country"]), 2)
            country1, country2 = countries[0], countries[1]
            population1 = int(data[data["country"] == country1]["population"].iloc[0])
            population2 = int(data[data["country"] == country2]["population"].iloc[0])
            draw(country1, population1, country2, population2, show_play_button=False, game_over=False)

            # Așteaptă ca utilizatorul să aleagă HIGHER sau LOWER
            user_choice = None
            while user_choice not in ["HIGHER", "LOWER"]:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if BUTTON_HIGH_POS[0] <= x <= BUTTON_HIGH_POS[0] + BUTTON_WIDTH and BUTTON_HIGH_POS[1] <= y <= \
                                BUTTON_HIGH_POS[1] + BUTTON_HEIGHT:
                            user_choice = "HIGHER"
                        elif BUTTON_LOWER_POS[0] <= x <= BUTTON_LOWER_POS[0] + BUTTON_WIDTH and BUTTON_LOWER_POS[
                            1] <= y <= BUTTON_LOWER_POS[1] + BUTTON_HEIGHT:
                            user_choice = "LOWER"
            # Verifică dacă răspunsul este corect și actualizează scorul
            if (user_choice == "HIGHER" and population2 > population1) or (
                    user_choice == "LOWER" and population2 < population1):
                game_over = False
                score += 1
                score_text = SCORE_FONT.render(f"Score: {score}", True, (255, 255, 255))
                print("Correct! Score:", score)
            else:
                print("You Lost! Game Over. Score:", score)
                if score > high_score:
                    high_score = score
                    high_score_text = SCORE_FONT.render(f"High Score: {high_score}", True, (255, 255, 255))
                score = 0
                score_text = SCORE_FONT.render(f"Score: {score}", True, (255, 255, 255))
                game_over = True
                game_over_start_time = pygame.time.get_ticks()

        else:
            draw("", 0, "", 0, show_play_button=True, game_over=False)

        if game_over and pygame.time.get_ticks() - game_over_start_time > 5000:
            game_over = False
            play_button_clicked = False
            score = 0
            score_text = SCORE_FONT.render(f"Score: {score}", True, (255, 255, 255))

    pygame.quit()


if __name__ == "__main__":
    main()
