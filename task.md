# Code-a-Pet Project Checklist

Use this checklist to track the creation of custom assets and the subsequent coding tasks.

## 1. Graphic Assets (SVG format recommended)
Save these in your project's `assets/` folder.

### Pet 1: Alien Costumes (Bloop)
- `[ ]` **`alien_normal_1.svg`** — Default state Frame 1.
- `[ ]` **`alien_normal_2.svg`** — Default state Frame 2 (blink/idle).
- `[ ]` **`alien_sad_1.svg`** — Sad state Frame 1.
- `[ ]` **`alien_sad_2.svg`** — Sad state Frame 2 (shiver/cry).
- `[ ]` **`alien_eating_1.svg`** — Eating animation Frame 1.
- `[ ]` **`alien_eating_2.svg`** — Eating animation Frame 2 (chew).
- `[ ]` **`alien_sleeping_1.svg`** — Sleeping state Frame 1.
- `[ ]` **`alien_sleeping_2.svg`** — Sleeping state Frame 2 (breathing/chest rise).
- `[ ]` **`alien_ghost_1.svg`** — Game Over state Frame 1.
- `[ ]` **`alien_ghost_2.svg`** — Game Over state Frame 2 (float/halo).

### Pet 2: Puppy Costumes (Waffles)
- `[ ]` **`puppy_normal_1.svg`** — Default state Frame 1.
- `[ ]` **`puppy_normal_2.svg`** — Default state Frame 2 (pant/wag).
- `[ ]` **`puppy_sad_1.svg`** — Sad state Frame 1.
- `[ ]` **`puppy_sad_2.svg`** — Sad state Frame 2 (shiver).
- `[ ]` **`puppy_eating_1.svg`** — Eating animation Frame 1 (bowl).
- `[ ]` **`puppy_eating_2.svg`** — Eating animation Frame 2 (snout raised).
- `[ ]` **`puppy_sleeping_1.svg`** — Sleeping state Frame 1 (curled).
- `[ ]` **`puppy_sleeping_2.svg`** — Sleeping state Frame 2 (breathing).
- `[ ]` **`puppy_ghost_1.svg`** — Game Over state Frame 1.
- `[ ]` **`puppy_ghost_2.svg`** — Game Over state Frame 2 (float/wings).

### Pet 3: Robo-Kitten Costumes (Gizmo)
- `[ ]` **`kitten_normal_1.svg`** — Default state Frame 1.
- `[ ]` **`kitten_normal_2.svg`** — Default state Frame 2 (eyes change).
- `[ ]` **`kitten_sad_1.svg`** — Sad state Frame 1.
- `[ ]` **`kitten_sad_2.svg`** — Sad state Frame 2 (battery alert).
- `[ ]` **`kitten_eating_1.svg`** — Eating animation Frame 1 (chewing).
- `[ ]` **`kitten_eating_2.svg`** — Eating animation Frame 2 (sparks).
- `[ ]` **`kitten_sleeping_1.svg`** — Sleeping state Frame 1 (dots).
- `[ ]` **`kitten_sleeping_2.svg`** — Sleeping state Frame 2 (charging).
- `[ ]` **`kitten_ghost_1.svg`** — Game Over state Frame 1 (error screen).
- `[ ]` **`kitten_ghost_2.svg`** — Game Over state Frame 2 (robot spirit).

### Selection Buttons (Start Screen)
- `[ ]` **`button_select_alien.svg`** — Clickable button to choose Bloop (Alien).
- `[ ]` **`button_select_puppy.svg`** — Clickable button to choose Waffles (Puppy).
- `[ ]` **`button_select_kitten.svg`** — Clickable button to choose Gizmo (Kitten).

### Action Buttons (Main Game Screen)
- `[ ]` **`button_feed.svg`** — Feed button icon.
- `[ ]` **`button_play.svg`** — Play button icon.
- `[ ]` **`button_sleep.svg`** — Sleep button icon.

### HUD & UI Assets
- `[ ]` **`icon_hunger.svg`** — Hunger icon (drumstick/stomach).
- `[ ]` **`icon_happiness.svg`** — Happiness icon (heart/smiley).
- `[ ]` **`icon_energy.svg`** — Energy icon (lightning bolt).
- `[ ]` **`ui_stat_bar_full.svg`** — Bar at 75–100% (green fill).
- `[ ]` **`ui_stat_bar_medium.svg`** — Bar at 40–74% (yellow fill).
- `[ ]` **`ui_stat_bar_low.svg`** — Bar at 15–39% (orange fill).
- `[ ]` **`ui_stat_bar_critical.svg`** — Bar at 0–14% (red sliver).

### Interactive Props
- `[ ]` **`prop_space_food.svg`** — Alien food (space fruit).
- `[ ]` **`prop_bone.svg`** — Puppy food (dog bone).
- `[ ]` **`prop_oil_can.svg`** — Kitten food (oil can).
- `[ ]` **`prop_ball.svg`** — Toy ball for playing.

### Visual Effects (VFX)
- `[ ]` **`vfx_hearts.svg`** — Floating heart particles.
- `[ ]` **`vfx_zzz.svg`** — Floating sleeping "Z" particles.
- `[ ]` **`vfx_alert.svg`** — Red warning indicator (!) icon.

### Stage Backdrops & Screens
- `[ ]` **`screen_title.svg`** — Title splash screen.
- `[ ]` **`screen_gameover.svg`** — Game Over screen.
- `[ ]` **`bg_alien_day.svg`** — Alien's planet (Day).
- `[ ]` **`bg_alien_night.svg`** — Alien's planet (Night).
- `[ ]` **`bg_puppy_day.svg`** — Puppy's backyard (Day).
- `[ ]` **`bg_puppy_night.svg`** — Puppy's backyard (Night).
- `[ ]` **`bg_robo_day.svg`** — Robo-Kitten's laboratory (Day).
- `[ ]` **`bg_robo_night.svg`** — Robo-Kitten's laboratory (Night).

## 2. Audio Assets (WAV or MP3 format)
Sound effects for interactions and state changes.

### Alien Sounds
- `[x]` **`sound_alien_munch.wav`** (or `.mp3`) — Sci-fi chew sound.
- `[x]` **`sound_alien_boing.wav`** (or `.mp3`) — Space spring bounce sound.
- `[x]` **`sound_alien_snore.wav`** (or `.mp3`) — Bubbly space snore.
- `[x]` **`sound_alien_hello.wav`** (or `.mp3`) — Sci-fi greeting sound when chosen.

### Puppy Sounds
- `[x]` **`sound_puppy_munch.wav`** (or `.mp3`) — Crunching/chewing sound.
- `[x]` **`sound_puppy_boing.wav`** (or `.mp3`) — Squeaky toy sound.
- `[x]` **`sound_puppy_snore.wav`** (or `.mp3`) — Gentle puppy breathing.
- `[x]` **`sound_puppy_hello.wav`** (or `.mp3`) — Happy greeting bark when chosen.

### Robo-Kitten Sounds
- `[x]` **`sound_kitten_munch.wav`** (or `.mp3`) — Electric/oil slurping sound.
- `[x]` **`sound_kitten_boing.wav`** (or `.mp3`) — Synth bounce/beep-boop sound.
- `[x]` **`sound_kitten_snore.wav`** (or `.mp3`) — Standby hum/fan whirring.
- `[x]` **`sound_kitten_hello.wav`** (or `.mp3`) — Power boot-up/meow sound when chosen.

### Shared Sounds
- `[x]` **`sound_warning.wav`** (or `.mp3`) — Low stat alert sound.
- `[x]` **`sound_gameover.wav`** (or `.mp3`) — Sad retro game-over melody.

## 3. Project Configuration & Code Tasks
These will be executed once the assets are in place.

- `[ ]` Create `project.json` incorporating the custom assets.
- `[ ]` Implement background decay loops for stats (`Hunger`, `Happiness`, `Energy`).
- `[ ]` Implement button click event handlers & broadcast logic.
- `[ ]` Implement pet costume switching logic based on variables.
- `[ ]` Set up build (`build.py`) and validation (`validate.py`) scripts.
- `[ ]` Package project into `output.sb3` and verify correctness.
