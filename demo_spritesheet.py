import pygame
import json
import os

# ==========================================
# 1. LOAD METADATA AUTOMATICALLY
# ==========================================
METADATA_PATH = "animation.json"

if not os.path.exists(METADATA_PATH):
    print(f"Error: Could not find '{METADATA_PATH}'. Did you export from the Animator?")
    exit()

with open(METADATA_PATH, 'r') as f:
    data = json.load(f)

SPRITESHEET_PATH = data["image"]
FRAME_WIDTH = data["frame_width"]
FRAME_HEIGHT = data["frame_height"]
COLS = data["columns"]
TOTAL_FRAMES = data["total_frames"]
FPS = data.get("fps", 12)

print(f"Loaded Metadata: {TOTAL_FRAMES} frames, {FRAME_WIDTH}x{FRAME_HEIGHT} pixels.")

# ==========================================
# 2. INITIALIZATION
# ==========================================
pygame.init()
# Make the window exactly the right size for the animation + a 40px border for HUD
WIN_WIDTH = FRAME_WIDTH + 40
WIN_HEIGHT = FRAME_HEIGHT + 80
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Skeletal Animator - Auto Demo")
clock = pygame.time.Clock()

# ==========================================
# 3. LOAD AND SLICE THE SPRITESHEET
# ==========================================
def load_spritesheet(filepath, frame_w, frame_h, cols, total_frames):
    if not os.path.exists(filepath):
        print(f"Error: Could not find '{filepath}'!")
        pygame.quit()
        exit()

    sheet = pygame.image.load(filepath).convert_alpha()
    frames = []
    for i in range(total_frames):
        row = i // cols
        col = i % cols
        rect = pygame.Rect(col * frame_w, row * frame_h, frame_w, frame_h)
        frame_surface = pygame.Surface((frame_w, frame_h), pygame.SRCALPHA)
        frame_surface.blit(sheet, (0, 0), rect)
        frames.append(frame_surface)
    return frames

animation_frames = load_spritesheet(SPRITESHEET_PATH, FRAME_WIDTH, FRAME_HEIGHT, COLS, TOTAL_FRAMES)

# ==========================================
# 4. MAIN GAME LOOP
# ==========================================
running = True
current_frame_index = 0
frame_timer = 0.0

while running:
    dt = clock.tick(60) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    # Animation Logic
    frame_timer += dt
    if frame_timer >= 1.0 / FPS:
        frame_timer = 0.0
        current_frame_index += 1
        if current_frame_index >= len(animation_frames):
            current_frame_index = 0

    # Drawing
    screen.fill((50, 50, 50))  # Dark gray background
    
    # Center the sprite perfectly in the window
    blit_x = (WIN_WIDTH - FRAME_WIDTH) // 2
    blit_y = (WIN_HEIGHT - FRAME_HEIGHT) // 2
    
    current_image = animation_frames[current_frame_index]
    screen.blit(current_image, (blit_x, blit_y))
    
    # HUD
    font = pygame.font.SysFont("Arial", 18)
    hud_text = f"Frame: {current_frame_index + 1}/{TOTAL_FRAMES} | Size: {FRAME_WIDTH}x{FRAME_HEIGHT} | ESC: Exit"
    text_surface = font.render(hud_text, True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    pygame.display.flip()

pygame.quit()