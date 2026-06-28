# Code-a-Pet Project Checklist

Use this checklist to track the creation of custom assets and the subsequent coding tasks.

## 1. Graphic Assets (PNG format used)
Save these in your project's `assets/` folder.

### Pet 1: Alien Costumes (Bloop)
- `[x]` **`bloop_normal_f1.png`** — Default state Frame 1.
- `[x]` **`bloop_normal_f2.png`** — Default state Frame 2 (blink/idle).
- `[x]` **`bloop_sad_f1.png`** — Sad state Frame 1.
- `[x]` **`bloop_sad_f2.png`** — Sad state Frame 2 (shiver/cry).
- `[x]` **`bloop_eating_f1.png`** — Eating animation Frame 1.
- `[x]` **`bloop_eating_f2.png`** — Eating animation Frame 2 (chew).
- `[x]` **`bloop_sleeping_f1.png`** — Sleeping state Frame 1.
- `[x]` **`bloop_sleeping_f2.png`** — Sleeping state Frame 2 (breathing/chest rise).
- `[x]` **`bloop_ghost_f1.png`** — Game Over state Frame 1.
- `[x]` **`bloop_ghost_f2.png`** — Game Over state Frame 2 (float/halo).

### Pet 2: Puppy Costumes (Waffles)
- `[x]` **`waffles_normal_f1.png`** — Default state Frame 1.
- `[x]` **`waffles_normal_f2.png`** — Default state Frame 2 (pant/wag).
- `[x]` **`waffles_sad_f1.png`** — Sad state Frame 1.
- `[x]` **`waffles_sad_f2.png`** — Sad state Frame 2 (shiver).
- `[x]` **`waffles_eating_f1.png`** — Eating animation Frame 1 (bowl).
- `[x]` **`waffles_eating_f2.png`** — Eating animation Frame 2 (snout raised).
- `[x]` **`waffles_sleeping_f1.png`** — Sleeping state Frame 1 (curled).
- `[x]` **`waffles_sleeping_f2.png`** — Sleeping state Frame 2 (breathing).
- `[x]` **`waffles_ghost_f1.png`** — Game Over state Frame 1.
- `[x]` **`waffles_ghost_f2.png`** — Game Over state Frame 2 (float/wings).

### Pet 3: Robo-Kitten Costumes (Gizmo)
- `[x]` **`gizmo_normal_f1.png`** — Default state Frame 1.
- `[x]` **`gizmo_normal_f2.png`** — Default state Frame 2 (eyes change).
- `[x]` **`gizmo_sad_f1.png`** — Sad state Frame 1.
- `[x]` **`gizmo_sad_f2.png`** — Sad state Frame 2 (battery alert).
- `[x]` **`gizmo_eating_f1.png`** — Eating animation Frame 1 (chewing).
- `[x]` **`gizmo_eating_f2.png`** — Eating animation Frame 2 (sparks).
- `[x]` **`gizmo_sleeping_f1.png`** — Sleeping state Frame 1 (dots).
- `[x]` **`gizmo_sleeping_f2.png`** — Sleeping state Frame 2 (charging).
- `[x]` **`gizmo_ghost_f1.png`** — Game Over state Frame 1 (error screen).
- `[x]` **`gizmo_ghost_f2.png`** — Game Over state Frame 2 (robot spirit).

### Selection Buttons (Start Screen)
- `[x]` **`button_select_alien.png`** — Clickable button to choose Bloop (Alien).
- `[x]` **`button_select_puppy.png`** — Clickable button to choose Waffles (Puppy).
- `[x]` **`button_select_kitten.png`** — Clickable button to choose Gizmo (Kitten).

### Action Buttons (Main Game Screen)
- `[x]` **`button_feed.png`** — Feed button icon.
- `[x]` **`button_play.png`** — Play button icon.
- `[x]` **`button_sleep.png`** — Sleep button icon.

### HUD & UI Assets
- `[x]` **`icon_hunger.png`** — Hunger icon (drumstick/stomach).
- `[x]` **`icon_happiness.png`** — Happiness icon (heart/smiley).
- `[x]` **`icon_energy.png`** — Energy icon (lightning bolt).
- `[x]` **`bar_full.png`** — Bar at 75–100% (green fill).
- `[x]` **`bar_medium.png`** — Bar at 40–74% (yellow fill).
- `[x]` **`bar_low.png`** — Bar at 15–39% (orange fill).
- `[x]` **`bar_critical.png`** — Bar at 0–14% (red sliver).

### Interactive Props
- `[x]` **`prop_space_food.png`** — Alien food (space fruit).
- `[x]` **`prop_bone.png`** — Puppy food (dog bone).
- `[x]` **`prop_oil_can.png`** — Kitten food (oil can).
- `[x]` **`prop_ball.png`** — Toy ball for playing.

### Visual Effects (VFX)
- `[x]` **`vfx_hearts.png`** — Floating heart particles.
- `[x]` **`vfx_zzz.png`** — Floating sleeping "Z" particles.
- `[x]` **`vfx_alert.png`** — Red warning indicator (!) icon.

### Stage Backdrops & Screens
- `[x]` **`screen_title.png`** — Title splash screen.
- `[x]` **`screen_gameover.png`** — Game Over screen.
- `[x]` **`bg_alien_day.png`** — Alien's planet (Day).
- `[x]` **`bg_alien_night.png`** — Alien's planet (Night).
- `[x]` **`bg_puppy_day.png`** — Puppy's backyard (Day).
- `[x]` **`bg_puppy_night.png`** — Puppy's backyard (Night).
- `[x]` **`bg_robo_day.png`** — Robo-Kitten's laboratory (Day).
- `[x]` **`bg_robo_night.png`** — Robo-Kitten's laboratory (Night).

## 2. Audio Assets (WAV or MP3 format)
Sound effects for interactions and state changes.

### Alien Sounds
- `[x]` **`sound_alien_munch.wav`** — Sci-fi chew sound.
- `[x]` **`sound_alien_boing.wav`** — Space spring bounce sound.
- `[x]` **`sound_alien_snore.wav`** — Bubbly space snore.
- `[x]` **`sound_alien_hello.wav`** — Sci-fi greeting sound when chosen.

### Puppy Sounds
- `[x]` **`sound_puppy_munch.wav`** — Crunching/chewing sound.
- `[x]` **`sound_puppy_boing.wav`** — Squeaky toy sound.
- `[x]` **`sound_puppy_snore.wav`** — Gentle puppy breathing.
- `[x]` **`sound_puppy_hello.wav`** — Happy greeting bark when chosen.

### Robo-Kitten Sounds
- `[x]` **`sound_kitten_munch.wav`** — Electric/oil slurping sound.
- `[x]` **`sound_kitten_boing.wav`** — Synth bounce/beep-boop sound.
- `[x]` **`sound_kitten_snore.wav`** — Standby hum/fan whirring.
- `[x]` **`sound_kitten_hello.wav`** — Power boot-up/meow sound when chosen.

### Shared Sounds
- `[x]` **`sound_warning.wav`** — Low stat alert sound.
- `[x]` **`sound_gameover.wav`** — Sad retro game-over melody.

## 3. Project Configuration & Code Tasks
These have been successfully executed and verified.

- `[x]` Create `project.json` incorporating the custom assets.
- `[x]` Implement background decay loops for stats (`Hunger`, `Happiness`, `Energy`).
- `[x]` Implement button click event handlers & broadcast logic.
- `[x]` Implement pet costume switching logic based on variables.
- `[x]` Set up build (`build.py`) and validation (`validate.py`) scripts.
- `[x]` Package project into `output.sb3` and verify correctness.
