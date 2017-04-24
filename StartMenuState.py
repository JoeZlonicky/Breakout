import pygame
import GameState
import Button
import Ball

class StartMenuState(GameState.GameState):
    def __init__(self, game):
        self.name = "startmenu"
        self.game = game
        start = Button.StartGameButton(self.game)
        start.SetPosition(game.screen_width / 2 - start.rect.width /2,
                          game.screen_height / 2 - start.rect.height / 2)
        self.buttons = [start]
        self.mouse_pos = None
        ball_1 = Ball.Ball(200, 300)
        ball_2 = Ball.Ball(400, 200)
        ball_2.InvertXSpeed()
        ball_3 = Ball.Ball(100, 100)
        ball_3.InvertYSpeed()
        self.balls = [ball_1, ball_2, ball_3]

    def HandleEvents(self):  # Handle events such as exiting and certain key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.hovered:
                        button.Clicked()

    def Update(self): # Update GUI
        self.mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.Update(self.mouse_pos)

        for ball in self.balls:
            ball.UpdateMovement([])
            ball.CheckForOutOfBoundry(self.game.screen_width, self.game.screen_height, False)

    def DrawScreen(self):  # Draw buttons and background
        for ball in self.balls:
            self.game.screen.blit(ball.image, ball.rect)

        for button in self.buttons:
            self.game.screen.blit(button.image, button.rect)
