import StartMenuState
import PlayingState
import PauseState
import GameoverState
import LevelSelectState
import Level
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 720
        self.screen_height = 405
        self.display_info = pygame.display.Info()
        self.screen = pygame.Surface((self.screen_width, self.screen_height))
        self.draw_screen = pygame.display.set_mode((self.display_info.current_w, self.display_info.current_h), pygame.FULLSCREEN)
        self.states = []
        self.current_state = None
        self.running = True
        level_1 = Level.Level("Resources\TMX\Level1.tmx")
        level_2 = Level.Level("Resources\TMX\Level2.tmx")
        level_3 = Level.Level("Resources\TMX\Level3.tmx")
        level_4 = Level.Level("Resources\TMX\Level4.tmx")
        level_s = Level.Level("Resources\TMX\Level4.tmx")
        self.levels = [level_1, level_2, level_3, level_4, level_s]
        self.clock = pygame.time.Clock()

    def Start(self):  # Set starting menu and stuff
        self.ClearStates()
        start_menu_state = StartMenuState.StartMenuState(self)
        self.NewState(start_menu_state)
        self.GameLoop()

    def GoToLevelSelect(self):
        level_select_state = LevelSelectState.LevelSelectState(self)
        self.NewState(level_select_state)

    def ChooseLevel(self, level):
        playing_state = PlayingState.PlayingState(self, level)
        self.NewState(playing_state)

    def Pause(self):
        pause_state = PauseState.PauseState(self)
        self.NewState(pause_state)

    def ContinuePlaying(self):
        self.ChangeState(self.FindState("playing"))
        self.RemoveState(self.FindState("paused"))

    def GameOver(self):
        gameover_state = GameoverState.GameoverState(self)
        self.NewState(gameover_state)

    def ChangeState(self, state):  # See if state exists in states and act accordingly
        self.current_state = state

    def RemoveState(self, state):  # Remove state from states
        self.states.remove(state)

    def NewState(self, state):  # Add state to states and set to current
        self.states.append(state)
        self.current_state = state

    def FindState(self, name):
        for state in self.states:
            if state.name == name:
                return state

    def ClearStates(self):
        for state in self.states:
            self.states.remove(state)

    def GameLoop(self):
        while self.running:
            self.current_state.HandleEvents()
            self.current_state.Update()
            self.current_state.ClearScreen()
            self.current_state.DrawScreen()
            self.current_state.UpdateDisplay()
            self.clock.tick(60)
