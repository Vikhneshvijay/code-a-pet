# Code-a-Pet: Graphic Asset Design Guide

This document provides detailed visual descriptions, color palettes, and design guidelines for every graphic asset in the project. Use this as your reference sheet while drawing in Scratch, Figma, Inkscape, or any SVG editor.

---

## General Design Rules

| Property | Guideline |
| :--- | :--- |
| **Format** | SVG (Vector) preferred. PNG at 2x resolution (960×720) if raster. |
| **Sprite Canvas** | 200×200 px for characters and props. Center the art at (100, 100). |
| **Backdrop Canvas** | 480×360 px (matches Scratch stage exactly). |
| **Style** | Rounded, cartoon-like shapes. Thick outlines (2–4 px). Flat colors with minimal gradients. |
| **Consistency** | All frames of the same pet must share the same body proportions, outline thickness, and base colors. Only the expression/pose should change between frames. |

---

## 1. Pet Costumes

Each pet has **5 states × 2 frames = 10 costumes**. The two frames alternate to create a simple flipbook animation.

---

### 🛸 Bloop — The Alien

**Color Palette:**
| Swatch | Hex | Use |
| :--- | :--- | :--- |
| 🟢 Lime Green | `#7ED957` | Body fill |
| 🟩 Dark Green | `#4A9E2F` | Outline, shadows |
| 🟡 Yellow | `#FFD93D` | Eyes, antennae tips |
| ⚫ Black | `#2D2D2D` | Pupils, mouth |
| 🔵 Light Blue | `#6EC6FF` | Teardrop, ghost glow |

**Body Shape:** Rounded blob body (like a gumdrop or jellybean). Two short legs at the bottom. Two springy antennae on top with glowing yellow bulbs. Large oval eyes taking up ~40% of the face.

| Costume | Frame 1 | Frame 2 |
| :--- | :--- | :--- |
| **Normal** | Eyes wide open, big smile, antennae straight up, arms relaxed at sides. | Eyes closed (two curved lines), antennae slightly tilted, body 5% smaller (breathing in). |
| **Sad** | Mouth curved downward into a frown, antennae drooping at 45°, one small blue teardrop near left eye. | Body slightly shrunk inward (hunched), teardrop has fallen lower, antennae drooping further. |
| **Eating** | Mouth wide open (big "O" shape), a small piece of space fruit visible near the mouth, eyes looking down at food. | Mouth closed with puffed cheeks, eyes squeezed shut with satisfaction curves (`^^`), fruit gone. |
| **Sleeping** | Eyes are two horizontal curved lines (closed), body slightly slouched, arms limp. | Same closed eyes, but chest/body expanded ~5% outward (breathing out), head tilted slightly. |
| **Ghost** | Translucent green ghost shape (wavy bottom edge instead of legs), "X" marks for eyes, floating slightly above ground line. | Ghost bobbed upward ~10px, a tiny yellow halo appears above the head, slight transparency increase. |

---

### 🐶 Waffles — The Puppy

**Color Palette:**
| Swatch | Hex | Use |
| :--- | :--- | :--- |
| 🟤 Golden Brown | `#D4A574` | Body fill |
| 🟫 Dark Brown | `#8B5E3C` | Ears, spots, outline |
| ⬜ Cream | `#FFF5E1` | Belly, muzzle, paws |
| ⚫ Black | `#2D2D2D` | Nose, pupils |
| 🩷 Pink | `#FF9EAA` | Tongue, inner ears |

**Body Shape:** Classic cartoon puppy. Round head, floppy ears hanging down past the jawline. Small oval body with stubby legs and a curved tail. Big round eyes with shiny highlights. Pink tongue often visible.

| Costume | Frame 1 | Frame 2 |
| :--- | :--- | :--- |
| **Normal** | Sitting upright, tongue out to the right, tail curved up on the left side, ears relaxed, big sparkly eyes. | Tongue retracted (mouth closed, small smile), tail mirrored to the right side (wag), one ear slightly perked. |
| **Sad** | Ears fully drooped flat against head, eyebrows tilted inward (worried), tail curled under body, mouth closed in a frown. | Body hunched lower, head tilted down ~10°, one small teardrop near eye, ears unchanged. |
| **Eating** | Head angled downward 30°, snout buried in a food bowl shape, tail wagging up. | Head raised back up, tongue out licking the nose/muzzle area, eyes half-closed with satisfaction, bowl gone. |
| **Sleeping** | Curled into a ball (circular body shape), eyes closed (curved lines), nose resting on front paws, tail wrapped around body. | Same curled pose, but body expanded ~5% (breathing), tail tip slightly shifted. |
| **Ghost** | Floating translucent puppy shape (wavy ghost bottom), eyes are peaceful closed curves, tiny angel wings on back. | Bobbed upward ~10px, angel wings slightly larger/more visible, increased transparency. |

---

### 🤖 Gizmo — The Robo-Kitten

**Color Palette:**
| Swatch | Hex | Use |
| :--- | :--- | :--- |
| ⬜ Silver/Light Gray | `#C0C0C0` | Body panels |
| 🔵 Electric Blue | `#00B4D8` | Screen eyes, accent lights, joints |
| 🟦 Dark Navy | `#1B2838` | Outline, panel seams |
| 🟡 Amber/Yellow | `#FFB800` | Warning indicators, antenna light |
| 🔴 Red | `#FF4444` | Low battery / alert indicators |

**Body Shape:** Boxy but cute robotic cat. Rounded rectangular head with a screen/visor for the face area where digital eyes are displayed. Triangular pointed ears with small LED dots at the tips. Compact rectangular body with visible panel seams/rivets. A segmented mechanical tail. Small circular joints at shoulders and hips.

| Costume | Frame 1 | Frame 2 |
| :--- | :--- | :--- |
| **Normal** | Screen eyes showing happy arches (`^^`), ear LEDs glowing blue, tail curved upward, whisker antennae extended. | Screen eyes switch to round circle eyes (`OO`), one whisker antenna blinks/pulses (slightly thicker line), tail unchanged. |
| **Sad** | Screen eyes showing flat dashes (`--`), ear LEDs dimmed (gray instead of blue), tail drooping down, a small red triangle warning icon on the chest panel. | Screen eyes flash a battery-low icon (rectangle with one bar), ears physically angled downward ~15°, chest warning icon blinks (slightly larger). |
| **Eating** | Mouth panel open revealing small mechanical teeth, spark effects (2–3 yellow star shapes) near mouth, an oil drop or battery visible entering mouth. | Mouth closed, screen eyes showing happy arches (`^^`), two small oil drops falling from chin area, spark effects gone. |
| **Sleeping** | Screen eyes showing two dots (`..`), entire screen dimmed (darker tint overlay), ear LEDs off (gray), body slightly reclined. | Screen displays a small scrolling battery charge bar (green rectangle growing), body unchanged, a faint blue glow around the charging port on the back. |
| **Ghost** | Screen showing `X_X`, horizontal glitch lines across the screen (3 thin lines), body panels slightly ajar/offset, screws visible floating away. | More screws/gears floating upward, a faint transparent robot-shaped spirit outline rising above the body, glitch lines shifted position. |

---

## 2. Selection Buttons (Start Screen)

**Canvas:** 120×140 px each.  
**Layout:** Rounded rectangle button base with a portrait of the pet's head above the name label.

| Button | Visual Description |
| :--- | :--- |
| **`button_select_alien.svg`** | Rounded green button. Bloop's head (just the face, antennae, and eyes) centered in the top 2/3. Text label **"Bloop"** below in white bold font. |
| **`button_select_puppy.svg`** | Rounded brown/tan button. Waffles' head (face, floppy ears, tongue) centered. Text label **"Waffles"** below in white bold font. |
| **`button_select_kitten.svg`** | Rounded silver/blue button. Gizmo's head (visor face, pointed ears with LEDs) centered. Text label **"Gizmo"** below in white bold font. |

---

## 3. Action Buttons (Game Screen)

**Canvas:** 80×80 px each.  
**Style:** Circular button with a thick colored border (4px), white or light fill, and a centered icon. Should have a subtle drop shadow or darker bottom edge to look "pressable."

| Button | Icon Description | Border Color |
| :--- | :--- | :--- |
| **`button_feed.svg`** | A cute pet food bowl seen from a ¾ angle, filled with colorful kibble pieces. Small steam/aroma lines above. | `#FF6B6B` (Warm Red) |
| **`button_play.svg`** | A colorful striped bouncing ball with a small motion arc (two curved lines) indicating bounce. | `#4ECDC4` (Teal) |
| **`button_sleep.svg`** | A yellow crescent moon with one small star beside it, or a fluffy white pillow with a tiny "Z" above. | `#9B59B6` (Purple) |

---

## 4. HUD & UI Assets

### Stat Icons
**Canvas:** 32×32 px each. Simple, bold, instantly recognizable at small sizes.

| Icon | Visual Description |
| :--- | :--- |
| **`icon_hunger.svg`** | A cartoon meat drumstick — brown stick, rounded golden-brown meat portion. |
| **`icon_happiness.svg`** | A classic red heart shape with a small white shine/highlight in the upper left. |
| **`icon_energy.svg`** | A yellow lightning bolt with a thin dark outline. Pointed, angular, energetic shape. |

### Stat Bars
**Canvas:** 120×20 px. Each stat bar is a single sprite with **4 costumes** representing distinct fill states. The code switches costumes based on the variable value using simple conditionals.

| Costume | State | Fill Width | Fill Color | Visual Description |
| :--- | :--- | :--- | :--- | :--- |
| **`bar_full`** | 75–100% | 100% of bar | Green `#4CAF50` | Full bright green fill inside the rounded rectangle. The pet is healthy. |
| **`bar_medium`** | 40–74% | ~60% of bar | Yellow `#FFD700` | Yellow fill covering roughly the left 60%. A visual nudge that care is needed soon. |
| **`bar_low`** | 15–39% | ~30% of bar | Orange `#FF9800` | Orange fill covering the left 30%. Things are getting urgent. |
| **`bar_critical`** | 0–14% | ~10% of bar | Red `#FF4444` | Tiny red sliver on the far left. The stat is dangerously low. Bar may pulse/flash in code. |

**Shared Outer Frame:** All 4 costumes share the same rounded rectangle outline (dark gray `#555` border, 2px thick, light gray `#EEE` empty portion). Only the colored fill width and color change between costumes.

**Code Logic (per stat bar sprite):**
```
If (Hunger > 74) then switch costume to [bar_full]
Else if (Hunger > 39) then switch costume to [bar_medium]
Else if (Hunger > 14) then switch costume to [bar_low]
Else switch costume to [bar_critical]
```

---

## 5. Interactive Props

**Canvas:** 60×60 px each. These sprites glide from the button to the pet, so keep them small and visually distinct.

| Prop | Visual Description |
| :--- | :--- |
| **`prop_space_food.svg`** | A weird alien fruit: round purple body with glowing green craters/spots on the surface, a small leaf or ring floating above it. Slightly translucent glow effect. |
| **`prop_bone.svg`** | A classic cartoon dog bone: white/cream colored, two rounded knobs on each end, a slight shadow underneath. Clean and simple. |
| **`prop_oil_can.svg`** | A small metallic blue oil can with a long spout. A single amber oil drop hanging from the tip of the spout. Visible rivet details on the body. |
| **`prop_ball.svg`** | A round bouncing ball with alternating colored stripes (red/white or blue/yellow). A small white shine highlight in the upper-left quadrant. |

---

## 6. Visual Effects (VFX)

**Canvas:** 40×40 px each. These are cloned and animated at runtime, so they must be small, simple, and look good when semi-transparent.

| VFX | Visual Description |
| :--- | :--- |
| **`vfx_hearts.svg`** | A single small pink/red heart (same style as `icon_happiness` but smaller, ~20×20 px centered in the canvas). No outline — just a solid filled heart. Multiple clones will be spawned and drifted upward with ghost effect. |
| **`vfx_zzz.svg`** | The letter **"Z"** in a bold, rounded, cartoon font. Dark blue or purple fill (`#4A4E8C`). Slightly tilted at ~15°. Clones will be spawned at increasing sizes as they float up. |
| **`vfx_alert.svg`** | A red exclamation mark **"!"** inside a yellow/orange warning triangle. Bold, thick strokes. Should be immediately alarming and visible even at small sizes. |

---

## 7. Stage Backdrops & Screens

**Canvas:** 480×360 px (exact Scratch stage size). All backdrops should leave the **bottom 60px** relatively uncluttered for the action buttons overlay, and the **top 30px** relatively clear for the HUD stat bars.

### Title & Game Over Screens

| Backdrop | Visual Description |
| :--- | :--- |
| **`screen_title.svg`** | A vibrant, colorful background (gradient from deep purple at top to warm orange at bottom). Large, playful title text **"Code-a-Pet!"** in white with a colored outline/shadow, centered in the upper third. Silhouettes or small illustrations of all three pets (Bloop, Waffles, Gizmo) peeking from the bottom. A rounded **"START"** button graphic centered below the title. |
| **`screen_gameover.svg`** | A dark, somber background (deep navy gradient to dark gray). Large text **"GAME OVER"** in red with a slight glow/dropshadow, centered. A faded ghost silhouette in the background. A rounded **"TRY AGAIN"** button graphic centered below the text. |

### Bloop's World (Alien Planet)

| Backdrop | Visual Description |
| :--- | :--- |
| **`bg_alien_day.svg`** | **Sky:** Deep purple-to-magenta gradient. A large bright white-yellow sun in the upper right with radiating glow lines. **Landscape:** Rocky alien terrain in shades of purple and mauve. Odd mushroom/crystal formations growing from the ground. **Ground:** A flat lighter-purple ground plane in the lower third. |
| **`bg_alien_night.svg`** | **Sky:** Very dark indigo-to-black gradient. Scattered colorful stars (white, blue, yellow dots). A distant spiral galaxy smudge in the upper left. A small ringed planet visible on the horizon. **Landscape:** Same rocky terrain but darker/silhouetted. Glowing bioluminescent spots on the mushroom formations (cyan/green dots). **Ground:** Dark purple ground plane. |

### Waffles' World (Backyard)

| Backdrop | Visual Description |
| :--- | :--- |
| **`bg_puppy_day.svg`** | **Sky:** Bright blue gradient with two fluffy white clouds. A cheerful yellow sun in the upper left. **Landscape:** A green grassy lawn with a white picket fence along the back. A small brown wooden doghouse on the right side with **"WAFFLES"** written above the door. A single tree on the left. **Ground:** Bright green grass plane. |
| **`bg_puppy_night.svg`** | **Sky:** Dark navy gradient with a large glowing yellow crescent moon upper right. Scattered white star dots. **Landscape:** Same scene but in darker tones (dark green grass, dark brown fence). 3–5 small yellow-green firefly dots scattered in the air (with a faint glow around each). The doghouse has a small warm-yellow light glowing from inside. **Ground:** Dark green grass plane. |

### Gizmo's World (Robo Laboratory)

| Backdrop | Visual Description |
| :--- | :--- |
| **`bg_robo_day.svg`** | **Setting:** Interior of a futuristic laboratory/spaceship bridge. **Walls:** Smooth light gray metallic panels with visible seam lines and small rivets. **Screens:** 2–3 monitor screens on the back wall showing colorful data readouts (green bar charts, blue waveforms). Bright white overhead lighting (a glowing strip across the top). **Floor:** Dark gray tiled/grid floor. A few blinking LED indicator lights (green/amber dots) on the walls. |
| **`bg_robo_night.svg`** | **Setting:** Same laboratory interior. **Lighting:** Main overhead lights are OFF (no white strip). The room is dark navy/charcoal. **Screens:** Monitor screens are now in "standby" mode showing dim blue screensavers or a single blinking cursor. The screens cast a faint blue glow onto the surrounding walls. **Floor:** Barely visible dark grid floor. Small red "standby" LED dots replace the green ones. A cool blue ambient glow fills the lower portion of the room. |

---

## Quick Reference: Full Asset Count

| Category | Count |
| :--- | :--- |
| Pet Costumes (3 pets × 5 states × 2 frames) | **30** |
| Selection Buttons | **3** |
| Action Buttons | **3** |
| HUD Icons | **3** |
| Stat Bars (empty + fill set) | **2** |
| Interactive Props | **4** |
| VFX Particles | **3** |
| Stage Backdrops & Screens | **8** |
| **Total Graphic Assets** | **56** |
