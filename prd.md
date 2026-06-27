# Product Requirements Document (PRD): "Code-a-Pet" Virtual Pet Simulator

## 1. Executive Summary & Vision
**"Code-a-Pet"** is an educational Scratch 3.0 project designed to teach students foundational computational thinking concepts: **variables**, **loops (iteration)**, and **conditionals (if/then logic)**. 

Students will design and customize their own digital creature (such as Bloop the Alien, Waffles the Puppy, or Gizmo the Robo-Kitten) and program it to have needs that decay over time. To keep the pet alive and happy, players must interact with it by clicking interactive buttons (Food, Play, Sleep) which replenish the pet's stats. This project feels like a real mobile game, offering high engagement through personalization and immediate interactive feedback.

---

## 2. Educational Objectives & Curriculum Mapping
This project serves as a practical application of core Computer Science concepts:

*   **Variables (State Management):**
    *   Creating, naming, and initializing variables (`Hunger`, `Happiness`, `Energy`).
    *   Incrementing (replenishing needs) and decrementing (decaying needs over time).
*   **Loops (Control Flow):**
    *   Using `forever` loops to run the background needs-decay logic continuously.
*   **Conditionals (Decision Making):**
    *   Using `if/then` and `if/then/else` blocks to monitor the pet's status.
    *   Evaluating boolean conditions (e.g., `Hunger < 20`, `Energy < 10`) to trigger costume changes or warning states.
*   **Event-Driven Programming:**
    *   Responding to user input via sprite clicks (`when this sprite clicked`).
    *   Communicating between sprites using broadcasts (e.g., clicking a "Feed" button broadcasts `"feed"`, prompting the pet to eat and play a sound).
*   **Creative Design (Aesthetics & Customization):**
    *   Creating vector/bitmap costumes for different pet states (Normal, Sad, Sleeping, Eating, Game Over).

---

## 3. Product Features & Mechanics

### 3.1 The Virtual Pet Stats (Variables)
The pet is defined by three primary variables (global variables attached to the Stage or Sprite):
1.  **`Hunger`:** Starts at `100`. Decreases slowly over time. If it reaches `0`, the pet becomes sad or starves.
2.  **`Happiness`:** Starts at `100`. Decreases slowly over time. If it reaches `0`, the pet gets lonely.
3.  **`Energy`:** Starts at `100`. Decreases slowly over time. Replenished by sleeping.

### 3.2 Background Decay Loop (The "Tick" System)
A central loop runs in the background of the Pet sprite (or Stage) that reduces the stats at regular intervals.
*   **Logic Flow:**
    *   On green flag clicked, set `Hunger`, `Happiness`, and `Energy` to `100`.
    *   Enter a `forever` loop:
        *   Wait `1.5` seconds.
        *   Decrease `Hunger` by `-2` (or `-3`).
        *   Decrease `Happiness` by `-1` (or `-2`).
        *   Decrease `Energy` by `-1.5` (or `-2`).

### 3.3 Interactive Action Buttons (Player Input)
The player interacts with the pet through three main buttons:
*   **Food Bowl Button:** 
    *   Clicking this increases `Hunger` by `15` (up to a max of `100`).
    *   Plays a munching sound effect (`munch.mp3`).
    *   Broadcasts `"feed_pet"` to trigger a temporary "eating" costume on the pet.
*   **Toy Button:** 
    *   Clicking this increases `Happiness` by `20` (up to a max of `100`).
    *   Plays a squeaking sound effect.
    *   Broadcasts `"play_with_pet"` to trigger a temporary "happy bounce" animation on the pet.
*   **Bed / Sleep Button:** 
    *   Clicking this increases `Energy` by `30` (up to a max of `100`).
    *   Plays a snoring sound effect.
    *   Broadcasts `"sleep_pet"`, which dims the background or switches the pet to a "sleeping" costume.

### 3.4 Conditionals & Costume States
The Pet sprite must continuously evaluate its current variables to reflect its mood visually:
*   **Normal State:** `Hunger >= 20` and `Happiness >= 20` and `Energy >= 20` $\rightarrow$ Switch to `costume_happy`.
*   **Sad State:** `Hunger < 20` or `Happiness < 20` $\rightarrow$ Switch to `costume_sad` (droopy eyes, frowning, or crying animation).
*   **Exhausted State:** `Energy < 20` $\rightarrow$ Switch to `costume_tired` (droopy eyes, yawning).
*   **Game Over:** If `Hunger <= 0` or `Happiness <= 0`, switch to `costume_ghost`, trigger the Game Over backdrop, and stop all scripts.

### 3.5 Custom HUD & Stat Bars
Rather than showing default Scratch variable readouts, the project uses a custom graphic HUD:
*   **Stats Display:** Each stat (Hunger, Happiness, Energy) is represented by a small SVG icon (drumstick, heart, lightning bolt) and a corresponding visual progress bar.
*   **Stat Bar Logic:** Each stat bar is a sprite with **4 costumes** representing distinct health states: `bar_full` (green, 75–100%), `bar_medium` (yellow, 40–74%), `bar_low` (orange, 15–39%), and `bar_critical` (red, 0–14%). As a variable changes, the code uses an `if/else if` chain to switch to the correct costume (e.g., `Hunger = 75` $\rightarrow$ switch to `bar_full`).

### 3.6 Glide-to-Pet Interactive Props
Clicking action buttons triggers a dynamic physical interaction using dedicated prop sprites:
*   **Food Prop:** Clicking the "Feed" button spawns the pet-specific food prop at the button's position. The food then glides smoothly toward the Pet's mouth position, plays the `munch` sound, triggers the Pet's `eating` costume, and fades away.
    *   *Alien:* Glides `prop_space_food.svg`
    *   *Puppy:* Glides `prop_bone.svg`
    *   *Robo-Kitten:* Glides `prop_oil_can.svg`
*   **Toy Prop (`prop_ball.svg`):** Clicking the "Play" button spawns a toy ball that bounces across the screen (using basic reflection math or coordinate increments) while the pet follows it with its eyes or head, before returning to the toy box.

### 3.7 Visual Effects (VFX) "Juice"
Feedback events are accompanied by floating visual effect clones that spawn, animate, and disappear:
*   **`vfx_hearts.svg`:** Floating heart clones spawn around the pet when fed or played with, drifting upwards while shrinking/fading out.
*   **`vfx_zzz.svg`:** Snoring "Z" clones float up from the pet's head when sleeping.
*   **`vfx_alert.svg`:** A red exclamation mark (!) flashes above the pet's head in a loop when any stat drops below 20%, warning the player.

### 3.8 Complete Game Loop & Extra Screens
A full game loop is implemented using backdrop switching and starting states:
1.  **Title Screen (`screen_title`):** Welcome screen with the game name ("Code-a-Pet!"). The player clicks "Start" to enter the pet selection screen.
2.  **Selection Screen:** Player selects one of the three default pets: **Bloop (The Alien)**, **Waffles (The Puppy)**, or **Gizmo (The Robo-Kitten)**. This choice initializes the pet type and transitions the backdrop to the game stage.
3.  **Active Stage (Dynamic Backdrop):** The main play space with action buttons, stat bars, and the pet. The backdrop is selected dynamically based on the chosen pet and whether it is awake or sleeping (e.g., `bg_alien_day`, `bg_alien_night`, `bg_puppy_day`, etc.).
4.  **Game Over Screen (`screen_gameover`):** Triggers when a stat hits 0. Shows a sad summary screen and a clickable "Restart" button that resets variables and returns to the Title Screen.

---

## 4. User Interface (UI) & Layout Specification

### 4.1 Main Game Screen Layout
The Scratch stage (480x360 pixels) is arranged with the custom HUD, main pet, floating VFX, gliding props, and interactive action buttons:

```
+-------------------------------------------------------+
| (H) [======  ]     (P) [====    ]     (E) [========]  |  <- Custom HUD (Icons + Bars)
|                                                       |
|              (VFX: Hearts/Zzz/Alert)                  |
|                      \   /                            |
|                     ,\___/\   <-- (Prop Gliding)      |
|                    ( o   o )      [Space Fruit/Bone]  |
|                     )  =  (                           |
|                    (_______)  <- Main Pet Sprite      |
|                                                       |
|                                                       |
|    +---------+       +---------+       +---------+    |
|    |  FEED   |       |  PLAY   |       |  SLEEP  |    |  <- Action Buttons
|    +---------+       +---------+       +---------+    |
+-------------------------------------------------------+
```

### 4.2 Start / Title Screen Layout
*   Centered title graphic ("Code-a-Pet!").
*   "START" button in the center-bottom.
*   Clicking transitions to the Pet Selection Screen.

### 4.3 Pet Selection Screen Layout
*   Instructions: "Choose Your Virtual Pet!"
*   Three large select buttons lined up horizontally: [ Bloop (Alien) ]  [ Waffles (Puppy) ]  [ Gizmo (Kitten) ].
*   Clicking a selection sets a global variable `PetType` (e.g., "Bloop", "Waffles", "Gizmo") and broadcasts the game start.

### UI Guidelines:
*   **Custom HUD:** Variables are kept hidden from default view. Instead, the stat bar sprites are positioned at the top left, top center, and top right. Icons are placed immediately to the left of each stat bar.
*   **Action Buttons:** Placed at the bottom of the screen. They should have clear icons/words and a subtle hover effect (e.g., enlarging slightly when touched) or click effect (briefly shrinking).
*   **Background / Backdrop:** A cozy living room, a space station, or a pet cage/habitat, changing to Night (dark blue overlay or night graphic) when the sleeping state is activated.

---

## 5. Technical Implementation Details (Scratch JSON Structure)

If compiling or generating this project programmatically, the Scratch `project.json` targets will consist of:

### 5.1 Targets
1.  **Stage (Index 0):**
    *   Holds the backdrop costumes.
    *   Owns the global variables (`Hunger`, `Happiness`, `Energy`).
2.  **Pet Sprite:**
    *   Contains the core logic and mood-evaluation script.
    *   Costumes: `normal`, `sad`, `sleeping`, `eating`, `ghost`.
3.  **Feed Button Sprite:**
    *   Listens for click events.
    *   Increases `Hunger` and broadcasts `"feed"`.
4.  **Play Button Sprite:**
    *   Listens for click events.
    *   Increases `Happiness` and broadcasts `"play"`.
5.  **Sleep Button Sprite:**
    *   Listens for click events.
    *   Increases `Energy` and broadcasts `"sleep"`.

### 5.2 Key Code Blocks & Opcodes

#### Needs-Decay Loop (Pet Sprite or Stage)
Runs forever, decrementing stats:
```jsonc
// When green flag clicked, set variables and start decay loop
{
  "opcode": "event_whenflagclicked",
  "next": "set_hunger_1",
  "parent": null,
  "topLevel": true,
  "x": 100,
  "y": 100
},
{
  "opcode": "data_setvariableto",
  "id": "set_hunger_1",
  "next": "set_happiness_1",
  "parent": "event_whenflagclicked",
  "fields": { "VARIABLE": ["Hunger", "var_hunger_id"] },
  "inputs": { "VALUE": [1, [4, "100"]] }
},
// ... Similar for Happiness and Energy ...
{
  "opcode": "control_forever",
  "id": "decay_loop",
  "next": null,
  "parent": "set_energy_1",
  "inputs": {
    "SUBSTACK": [2, "wait_decay_1"]
  }
},
{
  "opcode": "control_wait",
  "id": "wait_decay_1",
  "next": "change_hunger_decay",
  "parent": "decay_loop",
  "inputs": { "DURATION": [1, [5, "1.5"]] }
},
{
  "opcode": "data_changevariableby",
  "id": "change_hunger_decay",
  "next": "change_happiness_decay",
  "parent": "wait_decay_1",
  "fields": { "VARIABLE": ["Hunger", "var_hunger_id"] },
  "inputs": { "VALUE": [1, [4, "-2"]] }
}
// ... and so on ...
```

#### Mood & Costume Check (Pet Sprite)
Evaluates status to update appearance:
```jsonc
// Checks if hunger or happiness is low
{
  "opcode": "control_forever",
  "id": "mood_check_loop",
  "next": null,
  "parent": "when_flag_for_mood",
  "inputs": { "SUBSTACK": [2, "if_sad_or_happy"] }
},
{
  "opcode": "control_if_else",
  "id": "if_sad_or_happy",
  "next": null,
  "parent": "mood_check_loop",
  "inputs": {
    "CONDITION": [2, "or_low_stats"],
    "SUBSTACK": [2, "switch_sad_costume"],      // If condition is true (sad)
    "SUBSTACK2": [2, "switch_happy_costume"]     // If condition is false (happy)
  }
}
```

---

## 6. Project Extensions & Customization (For Advanced Students)

Once the core virtual pet mechanics are complete, students can customize and expand their project with these features:

1.  **Evolution Cycles:**
    *   Track the pet's age with a `Days` variable. 
    *   Change the pet's size or switch to a "Teen" or "Adult" costume set after a certain time.
2.  **Store & Currency System:**
    *   Introduce a `Coins` variable earned by keeping the pet happy.
    *   Use coins to purchase special food items, premium toys, or background decorations.
3.  **Dynamic Expression Overrides:**
    *   When the Feed button is clicked, trigger a broadcast that switches the pet's costume to `eating` for 1 second, then reverts to the standard check loop.
4.  **Weather / Environment Changes:**
    *   Add a light switch that changes the room backdrop from Day to Night (which accelerates Energy replenishment but decreases Happiness).
5.  **Multi-Pet Selection:**
    *   Allow the player to choose between a set of different pets (e.g., Alien, Puppy, Robo-kitten) at the start of the game, changing the starting costumes accordingly.

---

## 7. Asset Specification & Manifest
Below is the complete list of graphical and audio assets required to implement the Tamagotchi Virtual Pet. To make customizing easy for students, all graphics are recommended to be in **SVG (Scalable Vector Graphics)** format, which allows crisp rendering at any size on the Scratch Stage.

### 7.1 Pet Sprite Costumes (Multi-Pet Support & 2-Frame Costume Flip)
The project supports selecting one of three pets at the start. The main pet sprite contains all costumes for the three pets, and uses a **2-frame costume flip** for idle, sad, eating, sleeping, and game-over animation loops:

#### Pet 1: Alien
| Costume Name | Filename Reference | Visual Description / Design Guidelines |
| :--- | :--- | :--- |
| **`alien_normal_1`** | `alien_normal_1.svg` | Frame 1: Default state. Bright open eyes, happy smile, antennae up. |
| **`alien_normal_2`** | `alien_normal_2.svg` | Frame 2: Idle blink. Same posture but with eyes closed or body slightly breathing. |
| **`alien_sad_1`** | `alien_sad_1.svg` | Frame 1: Low Hunger/Happiness. Frowning mouth, droopy antennae, small teardrop. |
| **`alien_sad_2`** | `alien_sad_2.svg` | Frame 2: Shivering. Body slightly shrunk, teardrop falling. |
| **`alien_eating_1`** | `alien_eating_1.svg` | Frame 1: Eating. Mouth wide open about to chew space fruit. |
| **`alien_eating_2`** | `alien_eating_2.svg` | Frame 2: Eating. Closed mouth chewing, fruit partially consumed. |
| **`alien_sleeping_1`**| `alien_sleeping_1.svg`| Frame 1: Sleeping. Closed eyes, flat chest, head rested. |
| **`alien_sleeping_2`**| `alien_sleeping_2.svg`| Frame 2: Sleeping. Closed eyes, chest expanded, head slightly raised. |
| **`alien_ghost_1`** | `alien_ghost_1.svg` | Frame 1: Game Over. Green ghost shape floating, closed "X" eyes. |
| **`alien_ghost_2`** | `alien_ghost_2.svg` | Frame 2: Game Over. Bobbing green ghost, tiny halo appearing above. |

#### Pet 2: Puppy
| Costume Name | Filename Reference | Visual Description / Design Guidelines |
| :--- | :--- | :--- |
| **`puppy_normal_1`** | `puppy_normal_1.svg` | Frame 1: Default state. Happy face, open mouth, tongue sticking out. |
| **`puppy_normal_2`** | `puppy_normal_2.svg` | Frame 2: Idle pant. Mouth slightly more closed, tail wagged to the other side. |
| **`puppy_sad_1`** | `puppy_sad_1.svg` | Frame 1: Low stats. Droopy ears, sad whimpering eyes, tail down. |
| **`puppy_sad_2`** | `puppy_sad_2.svg` | Frame 2: Whimpering. Body shivering, head slightly lowered. |
| **`puppy_eating_1`** | `puppy_eating_1.svg` | Frame 1: Eating. Snout buried in bowl with food. |
| **`puppy_eating_2`** | `puppy_eating_2.svg` | Frame 2: Eating. Head raised, licking snout with tongue. |
| **`puppy_sleeping_1`**| `puppy_sleeping_1.svg`| Frame 1: Sleeping. Curled up dog, eyes closed. |
| **`puppy_sleeping_2`**| `puppy_sleeping_2.svg`| Frame 2: Sleeping. Chest expanded slightly breathing, sleeping tail relaxed. |
| **`puppy_ghost_1`** | `puppy_ghost_1.svg` | Frame 1: Game Over. Floating puppy ghost shape with closed eyes. |
| **`puppy_ghost_2`** | `puppy_ghost_2.svg` | Frame 2: Game Over. Bobbed puppy ghost, floating angel wings visible. |

#### Pet 3: Robo-Kitten
| Costume Name | Filename Reference | Visual Description / Design Guidelines |
| :--- | :--- | :--- |
| **`kitten_normal_1`**| `kitten_normal_1.svg`| Frame 1: Default state. Robot cat face, screen eyes showing happy arches (`^^`). |
| **`kitten_normal_2`**| `kitten_normal_2.svg`| Frame 2: Idle scan. Whiskers blinking light, screen eyes showing normal circle eyes. |
| **`kitten_sad_1`** | `kitten_sad_1.svg` | Frame 1: Low stats. Screen eyes showing flat lines (`--`), droopy tail. |
| **`kitten_sad_2`** | `kitten_sad_2.svg` | Frame 2: Low battery warning. Screen eyes flashing warning triangle, ears down. |
| **`kitten_eating_1`**| `kitten_eating_1.svg`| Frame 1: Eating. Chewing action with oil/battery, pixels sparking. |
| **`kitten_eating_2`**| `kitten_eating_2.svg`| Frame 2: Eating. Screen eyes showing happy arcs, oil drops falling. |
| **`kitten_sleeping_1`**| `kitten_sleeping_1.svg`| Frame 1: Sleeping. Screen eyes showing sleeping dots (`..`), face screen dimmed. |
| **`kitten_sleeping_2`**| `kitten_sleeping_2.svg`| Frame 2: Charging. Screen showing small scrolling battery indicator bar. |
| **`kitten_ghost_1`** | `kitten_ghost_1.svg` | Frame 1: Game Over. Offline screen sign (`X_X`), screen glitch lines. |
| **`kitten_ghost_2`** | `kitten_ghost_2.svg` | Frame 2: Game Over. Screws/gears floating up, robot spirit outline. |

### 7.2 Action & Selection Button Sprites
Buttons are divided into start-screen Selection Buttons (to choose your pet) and game-screen Action Buttons (to interact with the pet).

#### Selection Buttons (Start Screen)
| Button Sprite | Costume Name | Filename Reference | Visual Description / Design Guidelines |
| :--- | :--- | :--- | :--- |
| **Select Alien** | `select_alien` | `button_select_alien.svg`| A button showing the head of the Alien. |
| **Select Puppy** | `select_puppy` | `button_select_puppy.svg`| A button showing the head of the Puppy. |
| **Select Kitten**| `select_kitten`| `button_select_kitten.svg`| A button showing the head of the Kitten. |

#### Action Buttons (Main Game Screen)
| Button Sprite | Costume Name | Filename Reference | Visual Description / Design Guidelines |
| :--- | :--- | :--- | :--- |
| **Feed Button** | `feed_icon` | `button_feed.svg` | A cute pet bowl filled with food or treats. |
| **Play Button** | `play_icon` | `button_play.svg` | A colorful bouncing ball or squeaky toy. |
| **Sleep Button**| `sleep_icon`| `button_sleep.svg`| A cozy pillow or crescent moon. |

### 7.3 HUD & UI Assets
These assets compose the custom visual Heads-Up Display for the stats.

| Asset Name | Costume Name / Frame | Filename Reference | Visual Description / Design Guidelines |
| :--- | :--- | :--- | :--- |
| **Hunger Icon** | `icon_hunger` | `icon_hunger.svg` | A little meat drumstick, food bowl, or stomach icon. |
| **Happiness Icon**| `icon_happiness`| `icon_happiness.svg` | A red heart or grinning emoji icon. |
| **Energy Icon** | `icon_energy` | `icon_energy.svg` | A yellow lightning bolt or battery icon. |
| **Stat Bar Full** | `bar_full` | `ui_stat_bar_full.svg` | Green `#4CAF50` fill at 100% width. Pet is healthy (75–100%). |
| **Stat Bar Medium**| `bar_medium`| `ui_stat_bar_medium.svg`| Yellow `#FFD700` fill at ~60% width. Needs attention (40–74%). |
| **Stat Bar Low** | `bar_low` | `ui_stat_bar_low.svg` | Orange `#FF9800` fill at ~30% width. Getting urgent (15–39%). |
| **Stat Bar Critical**| `bar_critical`| `ui_stat_bar_critical.svg`| Red `#FF4444` fill at ~10% width. Dangerously low (0–14%). |

### 7.4 Interactive Prop Sprites
Physical items spawned and animated on button click.

| Prop Sprite | Costume Name | Filename Reference | Visual Description / Design Guidelines |
| :--- | :--- | :--- | :--- |
| **Space Food** | `food_alien` | `prop_space_food.svg` | A weird, glowing alien fruit with craters or rings. |
| **Dog Bone** | `food_puppy` | `prop_bone.svg` | A classic white cartoon bone. |
| **Oil Can** | `food_kitten` | `prop_oil_can.svg` | A metallic blue or red oil can dripping oil. |
| **Bouncing Ball**| `ball_toy` | `prop_ball.svg` | A colorful striped ball that bounces around. |

### 7.5 Visual Effect (VFX) Sprites
Temporary feedback animations spawned at runtime.

| VFX Sprite | Costume Name | Filename Reference | Visual Description / Design Guidelines |
| :--- | :--- | :--- | :--- |
| **Floating Hearts**| `heart_particle`| `vfx_hearts.svg` | Small floating pink/red hearts that rise and shrink. |
| **Sleeping Zs** | `zzz_particle` | `vfx_zzz.svg` | Expanding, drifting cartoon "Zzz" letters. |
| **Warning Alert** | `alert_flash` | `vfx_alert.svg` | A bright red exclamation point symbol in a triangle. |

### 7.6 Stage Backdrops & Screens
The background layout frames.

| Backdrop Name | Filename Reference | Visual Description / Design Guidelines |
| :--- | :--- | :--- |
| **`screen_title`** | `screen_title.svg` | Splash screen with large "Virtual Pet Simulator!" title and "Start" button. |
| **`screen_gameover`**| `screen_gameover.svg`| Dark, solemn screen with "GAME OVER", score summaries, and a "Restart" button. |
| **`bg_alien_day`** | `bg_alien_day.svg` | Rocky purple planet landscape under a bright space sun. |
| **`bg_alien_night`**| `bg_alien_night.svg`| The purple planet at night under glowing stars and a colorful galaxy. |
| **`bg_puppy_day`** | `bg_puppy_day.svg` | Bright, grassy backyard featuring a cute wooden doghouse. |
| **`bg_puppy_night`**| `bg_puppy_night.svg`| The grassy backyard at night with a glowing moon and yellow fireflies. |
| **`bg_robo_day`** | `bg_robo_day.svg` | Futuristic laboratory or spaceship interior with neon console lights. |
| **`bg_robo_night`**| `bg_robo_night.svg`| The lab with main lights switched off, glowing with blue standby computer monitors. |

### 7.7 Sound Effects (WAV / MP3)
Audio feedback makes the virtual pet feel interactive and premium. The project uses pet-specific sounds for main activities, prompting students to use conditional coding:

#### Alien Audio
| Sound Name | Filename Reference | Audio Characteristics / Use Case |
| :--- | :--- | :--- |
| **`alien_munch`** | `sound_alien_munch.wav` | Sci-fi gulping, laser chew, or squishy eating sound. |
| **`alien_boing`** | `sound_alien_boing.wav` | Futuristic bouncy spring or alien giggle sound. |
| **`alien_snore`** | `sound_alien_snore.wav` | Weird, bubbly alien breathing/snoring sound. |
| **`alien_hello`** | `sound_alien_hello.wav` | Sci-fi greeting chirp or cute alien noise when chosen. |

#### Puppy Audio
| Sound Name | Filename Reference | Audio Characteristics / Use Case |
| :--- | :--- | :--- |
| **`puppy_munch`** | `sound_puppy_munch.wav` | Classic crunching, chewing bone, or chewing kibble sound. |
| **`puppy_boing`** | `sound_puppy_boing.wav` | High-pitched toy squeaker or happy short bark. |
| **`puppy_snore`** | `sound_puppy_snore.wav` | Gentle dog breathing or soft snoring sound. |
| **`puppy_hello`** | `sound_puppy_hello.wav` | Excited bark or greeting yip when chosen. |

#### Robo-Kitten Audio
| Sound Name | Filename Reference | Audio Characteristics / Use Case |
| :--- | :--- | :--- |
| **`kitten_munch`** | `sound_kitten_munch.wav` | Electric crunching, metallic chew, or oil slurping sound. |
| **`kitten_boing`** | `sound_kitten_boing.wav` | Digitized video game beep-boop, synth bounce, or robotic purr. |
| **`kitten_snore`** | `sound_kitten_snore.wav` | Hum, whirring computer fan, or electronic standby buzz. |
| **`kitten_hello`** | `sound_kitten_hello.wav` | Electronic boot-up chime or digital meow when chosen. |

#### Shared System Audio
| Sound Name | Filename Reference | Audio Characteristics / Use Case |
| :--- | :--- | :--- |
| **`warning`** | `sound_warning.wav` | A repeating warning alert or beep when any stat drops below 20%. |
| **`gameover`** | `sound_gameover.wav` | A sad descending retro melody played once when the pet becomes a ghost. |
