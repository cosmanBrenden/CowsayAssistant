import sys
from typing import Any
# from Xlib import X, display, Xutil
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()


def draw_input_box(surface, rect, color, text, font, text_color):
    pygame.draw.rect(surface, color, rect, border_radius=5)
    txt_surface = font.render(text, True, text_color)
    surface.blit(txt_surface, (rect.x + 8, rect.y + (rect.height - txt_surface.get_height()) // 2))

def draw_text(surface, text, pos, font, color):
    text_surf = font.render(text, True, color)
    surface.blit(text_surf, pos)

def process_input(text: str) -> str:
#     print(text)
    return text

def draw_message_stack(
    surface, 
    messages, 
    pos, 
    font, 
    color, 
    max_messages=10, 
    line_spacing=5
    ) -> None:
    x, y = pos # list msg (recent** -> last)
    #messages_to_draw = messages[-max_messages:] # cutoff at max_messages
#     print("messages to draw", messages_to_draw)
    for idx, msg in enumerate[Any](messages):
        text_surf = font.render(msg, True, color)
        surface.blit(
            text_surf, 
            (x, y + idx * (text_surf.get_height() + line_spacing))
        )



pygame.display.set_caption("jarvis")
screen = pygame.display.set_mode((800, 600)) # win w, h 

# clock = pygame.time.Clock()

input_rect = pygame.Rect(50, 500, 700, 40)
input_color = (216, 216, 216)
active_color = (200, 200, 200)
text_color = (0, 0, 0)
# font = pygame.font.SysFont('Arial', 28)
screen.fill((255, 255, 255))
message_history = []
pygame.display.flip()






def update(prompt):
        input_text = ""
        input_active = False
        real_text = ""
        running = True

        while(running):
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                print("here")
                                running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                if input_rect.collidepoint(event.pos):
                                        input_active = True
                                else:
                                        input_active = False
                        elif event.type == pygame.KEYDOWN and input_active:
                                if event.key == pygame.K_BACKSPACE:
                                        input_text = input_text[:-1]
                                elif event.key == pygame.K_RETURN:
                                        # handle submission of input_text here
                                        
                                        real_text = process_input(input_text)
                                        input_text = ""
                                        running = False
                                        
                                else:
                                        input_text += event.unicode


                screen.fill((255, 255, 255))
                draw_text(
                screen,
                prompt,
                (50, 460),
                font,
                text_color
                )
        
                draw_input_box(
                screen, 
                input_rect, 
                active_color \
                        if input_active\
                        else input_color,
                input_text,
                font,
                text_color
                )

                draw_message_stack(
                screen,
                message_history,
                pos=(50, 30),    # @x50 @y30
                font=font,
                color=text_color,
                max_messages=10,
                line_spacing=0
                )
             
                pygame.display.flip()
        pygame.display.flip()
                # clock.tick(12)
        return real_text
        
def jarvis_speak(message):
        input_text = ""
        input_active = False
        
        
        screen.fill((255, 255, 255))
        draw_text(
                screen,
                "",
                (50, 460),
                font,
                text_color
                )
        
        draw_input_box(
                screen, 
                input_rect, 
                active_color \
                        if input_active\
                        else input_color,
                input_text,
                font,
                text_color
                )
        
        global message_history
        message_history.append(message)
        
        # for char in message:
        #         print(char)
        

        if(len(message_history) > 10):
               message_history = message_history[1:]
        # print(len(message_history))
        # print(message_history)
        draw_message_stack(
                screen,
                message_history,
                pos=(50, 30),    # @x50 @y30
                font=font,
                color=text_color,
                max_messages=10,
                line_spacing=0
                )
        pygame.display.flip()
        
