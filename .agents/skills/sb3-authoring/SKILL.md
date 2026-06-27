---
name: sb3-authoring
description: Scratch 3.0 project JSON authoring and packaging skill. Use when creating, editing, validating, or building Scratch 3.0 projects (.sb3 files) from project.json and flat assets.
---
# SKILL: SB3 (Scratch 3.0) Project Authoring as JSON

## When to use this skill
Use this skill any time the user wants to:
- Create, edit, or understand `.sb3` / `project.json` files as raw JSON code
- Author Scratch 3.0 projects programmatically in VS Code
- Package a `project.json` + assets into a valid `.sb3` ZIP archive
- Inspect, modify, or generate Scratch project structures without the Scratch editor
- Write helper/build scripts for Scratch projects

---

## STEP 0 — Read this entire skill before generating any JSON or code.

SB3 is a **ZIP archive** renamed `.sb3`. Inside it lives exactly one `project.json` (the full program state as JSON) plus flat asset files (PNG/SVG/WAV/MP3) whose filenames are their MD5 hash + extension.

---

## RULE SET

### R1 — File Layout
- An `.sb3` file **must** be a ZIP archive with NO internal directories — all files sit at the root.
- The JSON file **must** be named `project.json` (lowercase, no spaces).
- Asset filenames **must** match the `md5ext` field exactly (e.g. `cd21514d0531fdffb22204e0ec5ed84a.svg`).
- A `.sprite3` file follows the same rules but the JSON is named `sprite.json`.

### R2 — Top-Level JSON Keys
Every `project.json` **must** contain exactly these four top-level keys:

```json
{
  "targets":    [],   // required — array of stage + sprite objects
  "monitors":   [],   // required — can be empty array
  "extensions": [],   // required — can be empty array
  "meta":       {}    // required — version metadata object
}
```

Missing any of these will fail to load in Scratch.

### R3 — Targets Array Order
- `targets[0]` **must** be the Stage (`"isStage": true`).
- All subsequent entries are sprites in front-to-back layer order.
- A project must have at least one target (the Stage).

### R4 — Target Object: Shared Properties
Every target (Stage or Sprite) must have:

```jsonc
{
  "isStage":        false,            // boolean; true only for Stage
  "name":           "Sprite1",        // string; Stage must be "Stage"
  "variables":      {},               // object; see R8
  "lists":          {},               // object; see R8
  "broadcasts":     {},               // object; see R8
  "blocks":         {},               // object; see R5
  "comments":       {},               // object; see R11
  "currentCostume": 0,                // integer index into costumes array
  "costumes":       [],               // array; see R9
  "sounds":         [],               // array; see R10
  "volume":         100,              // integer 0–100
  "layerOrder":     0                 // integer; Stage = 0, sprites ≥ 1
}
```

### R4a — Stage-Only Additional Properties

```jsonc
{
  "tempo":               60,    // BPM, integer
  "videoTransparency":   50,    // 0–100; default 50
  "videoState":          "on",  // "on" | "off" | "on-flipped"
  "textToSpeechLanguage": null  // string or null
}
```

### R4b — Sprite-Only Additional Properties

```jsonc
{
  "visible":       true,          // boolean
  "x":             0,             // number; Scratch stage X (-240 to 240)
  "y":             0,             // number; Scratch stage Y (-180 to 180)
  "size":          100,           // number; percentage
  "direction":     90,            // number; degrees clockwise from up
  "draggable":     false,         // boolean
  "rotationStyle": "all around"   // "all around" | "left-right" | "don't rotate"
}
```

### R5 — Block Objects

Blocks live in `target.blocks` as a flat object keyed by **unique block IDs** (any unique string — Scratch uses UID-like strings, e.g. `"abc123DEF456"`).

#### R5a — Standard Block Structure

```jsonc
{
  "opcode":   "motion_movesteps",  // string; see R6 for opcode reference
  "next":     null,                // string ID of next block | null
  "parent":   null,                // string ID of parent block | null
  "inputs":   {},                  // object; see R5c
  "fields":   {},                  // object; see R5d
  "shadow":   false,               // boolean; true only for shadow blocks
  "topLevel": true,                // true if no parent; false otherwise
  "x":        100,                 // number; only present when topLevel === true
  "y":        100                  // number; only present when topLevel === true
}
```

Remove `x` and `y` when `topLevel` is false.

#### R5b — Primitive (Array) Blocks
Some blocks are stored as compact arrays inside `inputs`. Array format by type code:

| Code | Type            | Array Format                     |
|------|-----------------|----------------------------------|
| 4    | Number          | `[4, value]`                     |
| 5    | Positive number | `[5, value]`                     |
| 6    | Positive integer| `[6, value]`                     |
| 7    | Integer         | `[7, value]`                     |
| 8    | Angle           | `[8, value]`                     |
| 9    | Color           | `[9, "#rrggbb"]`                 |
| 10   | String          | `[10, "text"]`                   |
| 11   | Broadcast       | `[11, "name", "id"]`             |
| 12   | Variable        | `[12, "name", "id"]`             |
| 13   | List            | `[13, "name", "id"]`             |

Variables and lists that appear as top-level reporter blocks also receive `x` and `y` as 4th and 5th elements.

#### R5c — Input Encoding
Each entry in `block.inputs` is an array:

```
[shadowCode, block_or_array, optional_shadow_id_or_array]
```

- `shadowCode = 1` — input IS a shadow (the only sub-block is a shadow)
- `shadowCode = 2` — input has NO shadow (a real block fills it)
- `shadowCode = 3` — input has a shadow that is OBSCURED by a real block (both present)

The second element is either a block ID string or a primitive array (R5b). The optional third element (only when `shadowCode = 3`) is the shadow block ID or array.

**Example — `move (10) steps`:**
```json
"inputs": {
  "STEPS": [1, [4, "10"]]
}
```

**Example — `move (variable) steps`:**
```json
"inputs": {
  "STEPS": [3, "blockId_of_variable_reporter", [4, "10"]]
}
```

#### R5d — Field Encoding
Each entry in `block.fields` is an array:

```
["value"]              // most fields
["value", "id"]        // variable/list/broadcast dropdowns include the ID
```

**Example — `set x to (50)` field:**
```json
"fields": {
  "X": ["50"]
}
```

**Example — `set [myVar] to (0)` variable field:**
```json
"fields": {
  "VARIABLE": ["myVar", "uniqueVariableId"]
}
```

### R6 — Opcode Reference (complete core set)

#### Motion
```
motion_movesteps           STEPS
motion_turnright           DEGREES
motion_turnleft            DEGREES
motion_pointindirection    DIRECTION
motion_pointtowards        TOWARDS (field)
motion_gotoxy              X, Y
motion_goto                TO (field)
motion_glidesecstoxy       SECS, X, Y
motion_glideto             SECS, TO (field)
motion_changexby           DX
motion_setx                X
motion_changeyby           DY
motion_sety                Y
motion_ifonedgebounce      (no inputs/fields)
motion_setrotationstyle    STYLE (field: "all around"|"left-right"|"don't rotate")
motion_xposition           (reporter)
motion_yposition           (reporter)
motion_direction           (reporter)
```

#### Looks
```
looks_sayforsecs           MESSAGE, SECS
looks_say                  MESSAGE
looks_thinkforsecs         MESSAGE, SECS
looks_think                MESSAGE
looks_switchcostumeto      COSTUME (field)
looks_nextcostume
looks_switchbackdropto     BACKDROP (field)
looks_nextbackdrop
looks_changesizeby         CHANGE
looks_setsizeto            SIZE
looks_changeeffectby       EFFECT (field), CHANGE
looks_seteffectto          EFFECT (field), VALUE
looks_cleargraphiceffects
looks_show
looks_hide
looks_gotofrontback        FRONT_BACK (field: "front"|"back")
looks_goforwardbackwardlayers FORWARD_BACKWARD (field), NUM
looks_costumenumbername    NUMBER_NAME (field: "number"|"name")
looks_backdropnumbername   NUMBER_NAME (field)
looks_size                 (reporter)
```

#### Sound
```
sound_playuntildone        SOUND_MENU
sound_play                 SOUND_MENU
sound_stopallsounds
sound_changeeffectby       EFFECT (field), VALUE
sound_seteffectto          EFFECT (field), VALUE
sound_cleareffects
sound_changevolumeby       VOLUME
sound_setvolumeto          VOLUME
sound_volume               (reporter)
```

#### Events
```
event_whenflagclicked      (hat; no inputs)
event_whenkeypressed       KEY_OPTION (field)
event_whenthisspriteclicked
event_whenstageclicked
event_whenbackdropswitchesto BACKDROP (field)
event_whengreaterthan      WHENGREATERTHANMENU (field), VALUE
event_whenbroadcastreceived MESSAGE (field with ID)
event_broadcast            BROADCAST_INPUT
event_broadcastandwait     BROADCAST_INPUT
```

#### Control
```
control_wait               DURATION
control_repeat             TIMES, SUBSTACK
control_forever            SUBSTACK
control_if                 CONDITION, SUBSTACK
control_if_else            CONDITION, SUBSTACK, SUBSTACK2
control_wait_until         CONDITION
control_repeat_until       CONDITION, SUBSTACK
control_stop               STOP_OPTION (field: "all"|"this script"|"other scripts in sprite")
control_start_as_clone
control_create_clone_of    CLONE_OPTION
control_delete_this_clone
```

#### Sensing
```
sensing_touchingobject     TOUCHINGOBJECTMENU
sensing_touchingcolor      COLOR
sensing_coloristouchingcolor COLOR, COLOR2
sensing_distanceto         DISTANCETOMENU
sensing_askandwait         QUESTION
sensing_answer             (reporter)
sensing_keypressed         KEY_OPTION
sensing_mousedown          (reporter boolean)
sensing_mousex             (reporter)
sensing_mousey             (reporter)
sensing_setdragmode        DRAG_MODE (field)
sensing_loudness           (reporter)
sensing_loud               (reporter boolean)
sensing_timer              (reporter)
sensing_resettimer
sensing_of                 OBJECT (field), PROPERTY (field)
sensing_current            CURRENTMENU (field)
sensing_dayssince2000      (reporter)
sensing_username           (reporter)
sensing_userid             (reporter — deprecated)
```

#### Operators
```
operator_add               NUM1, NUM2
operator_subtract          NUM1, NUM2
operator_multiply          NUM1, NUM2
operator_divide            NUM1, NUM2
operator_random            FROM, TO
operator_gt                OPERAND1, OPERAND2
operator_lt                OPERAND1, OPERAND2
operator_equals            OPERAND1, OPERAND2
operator_and               OPERAND1, OPERAND2
operator_or                OPERAND1, OPERAND2
operator_not               OPERAND
operator_join              STRING1, STRING2
operator_letter_of         LETTER, STRING
operator_length            STRING
operator_contains          STRING1, STRING2
operator_mod               NUM1, NUM2
operator_round             NUM
operator_mathop            OPERATOR (field), NUM
```

#### Data (Variables / Lists)
```
data_setvariableto         VARIABLE (field with ID), VALUE
data_changevariableby      VARIABLE (field with ID), VALUE
data_showvariable          VARIABLE (field with ID)
data_hidevariable          VARIABLE (field with ID)
data_addtolist             ITEM, LIST (field with ID)
data_deleteoflist          INDEX, LIST (field with ID)
data_deletealloflist       LIST (field with ID)
data_insertatlist          ITEM, INDEX, LIST (field with ID)
data_replaceitemoflist     INDEX, ITEM, LIST (field with ID)
data_itemoflist            INDEX, LIST (field with ID)
data_itemnumoflist         ITEM, LIST (field with ID)
data_lengthoflist          LIST (field with ID)
data_listcontainsitem      LIST (field with ID), ITEM
data_showlist              LIST (field with ID)
data_hidelist              LIST (field with ID)
```

#### Custom Blocks (My Blocks)
```
procedures_definition      custom_block (input referencing prototype)
procedures_prototype       (special — see R12 on mutations)
procedures_call            (special — see R12 on mutations)
argument_reporter_string_number  VALUE (field)
argument_reporter_boolean        VALUE (field)
```

#### Extension opcodes follow the pattern `extensionId_blockname`
e.g. `pen_clear`, `music_playDrumForBeats`, `text2speech_speakAndWait`

### R7 — Block Chaining Rules
- Blocks in a script stack are linked via `next` / `parent`.
- The **first** block of a stack (hat or orphan) has `topLevel: true`, `parent: null`, and carries `x`/`y` coordinates.
- Every subsequent block has `topLevel: false`, `parent` = the preceding block's ID, and no `x`/`y`.
- The last block in a stack has `next: null`.
- C-blocks (control_if, control_repeat, etc.) reference their body via the `SUBSTACK` input, which has `shadowCode = 2`.
- The first block inside a C mouth has `parent` = the C-block's ID.

### R8 — Variables, Lists, Broadcasts

#### Variables
Stored on the target that owns them (`target.variables`):
```json
"variables": {
  "uniqueId": ["variableName", 0],
  "cloudVarId": ["⛅ cloudVar", 0, true]
}
```
- Array: `[name, initialValue]` or `[name, initialValue, true]` for cloud variables.
- Global variables belong to the Stage.
- Sprite-local variables belong to the sprite.

#### Lists
```json
"lists": {
  "uniqueListId": ["listName", []]
}
```
- Array: `[name, arrayOfItems]`.

#### Broadcasts
```json
"broadcasts": {
  "uniqueBroadcastId": "broadcastName"
}
```
- Normally only present in Stage, but can appear on any target.

### R9 — Costumes

```jsonc
{
  "assetId":         "cd21514d0531fdffb22204e0ec5ed84a",  // MD5 hash of file content
  "name":            "backdrop1",                          // display name
  "md5ext":          "cd21514d0531fdffb22204e0ec5ed84a.svg", // assetId + extension
  "dataFormat":      "svg",                                // "svg" | "png" | "jpg" | "bmp"
  "rotationCenterX": 240,                                  // pixels from left
  "rotationCenterY": 180,                                  // pixels from top
  "bitmapResolution": 1                                    // only for bitmap; omit for SVG
}
```

**Rules:**
- SVG costumes omit `bitmapResolution`.
- Bitmap costumes in Scratch 3 are double-resolution; `bitmapResolution: 2` is typical.
- `rotationCenterX`/`Y` default to the image center if not provided.
- The asset file named `{md5ext}` **must exist** in the ZIP archive (or on Scratch servers for cloud-loaded projects).

### R10 — Sounds

```jsonc
{
  "assetId":    "83a9787d4cb6f3b7632b4ddfebf74367",
  "name":       "pop",
  "dataFormat": "wav",                                    // "wav" | "mp3"
  "format":     "",                                       // can be empty string
  "rate":       44100,                                    // sampling rate (Hz)
  "sampleCount": 1032,                                    // number of samples
  "md5ext":     "83a9787d4cb6f3b7632b4ddfebf74367.wav"
}
```

**Note:** `rate` and `sampleCount` are ignored and overwritten on load; they may be omitted in practice but are commonly included.

### R11 — Comments

```jsonc
{
  "commentId": {
    "blockId":    "attachedBlockId",  // null if floating comment
    "x":          100,
    "y":          200,
    "width":      200,
    "height":     200,
    "minimized":  false,
    "text":       "My comment text"
  }
}
```

### R12 — Mutations (Custom Blocks)

Only `procedures_prototype`, `procedures_call`, and `control_stop` have a `mutation` property.

#### `procedures_prototype` mutation:
```json
"mutation": {
  "tagName":         "mutation",
  "children":        [],
  "proccode":        "myBlock %s and %b",
  "argumentids":     "[\"argId1\",\"argId2\"]",
  "argumentnames":   "[\"label1\",\"label2\"]",
  "argumentdefaults": "[\"\",\"false\"]",
  "warp":            false
}
```

#### `procedures_call` mutation:
```json
"mutation": {
  "tagName":     "mutation",
  "children":    [],
  "proccode":    "myBlock %s and %b",
  "argumentids": "[\"argId1\",\"argId2\"]",
  "warp":        false
}
```

#### `control_stop` mutation:
```json
"mutation": {
  "tagName":  "mutation",
  "children": [],
  "hasnext":  false
}
```
- `hasnext: false` for "stop all" / "stop this script"
- `hasnext: true` for "stop other scripts in sprite"

**IMPORTANT:** `argumentids`, `argumentnames`, `argumentdefaults` in mutations are **JSON-encoded strings** (strings containing JSON arrays), NOT actual arrays.

### R13 — Monitors

```jsonc
{
  "id":         "uniqueMonitorId",
  "mode":       "default",        // "default" | "large" | "slider" | "list"
  "opcode":     "data_variable",  // block opcode this monitor shows
  "params":     { "VARIABLE": "myVar" },
  "spriteName": null,             // sprite name or null for global
  "value":      0,                // current displayed value
  "width":      0,                // display width
  "height":     0,                // display height
  "x":          5,                // position on stage
  "y":          5,
  "visible":    true,
  "sliderMin":  0,                // only for non-list monitors
  "sliderMax":  100,
  "isDiscrete": true              // true = integer-only slider
}
```

List monitors additionally have `"mode": "list"` and a larger default height.

### R14 — Extensions Array

Known extension identifiers:

```json
["pen", "wedo2", "music", "microbit", "text2speech", "translate", "videoSensing", "ev3", "makeymakey", "boost", "gdxfor"]
```

Only include extensions actually used in the project. If no extensions are used, use `[]`.

### R15 — Meta Object

```json
"meta": {
  "semver": "3.0.0",
  "vm":     "0.2.0",
  "agent":  "Mozilla/5.0 ..."
}
```

- `semver` must always be `"3.0.0"`.
- `vm` is the Scratch VM version string. Use `"0.2.0"` as a safe default.
- `agent` is the user-agent string. Can be any string or empty.

### R16 — ID Generation Rules
- Block IDs, variable IDs, list IDs, broadcast IDs, and comment IDs must be **unique within the project**.
- Scratch uses strings resembling `"abc123XYZ!@#"` (random printable ASCII).
- For authored JSON, use short descriptive IDs or UUIDs for readability, e.g., `"hat_flag_1"`, `"move_block_1"`.
- IDs are **case-sensitive** strings.

---

## VS CODE WORKSPACE SETUP

### Directory structure for a project:

```
my-scratch-project/
├── project.json          ← main JSON (edit this)
├── assets/               ← raw asset files
│   ├── backdrop.svg
│   └── sprite.svg
├── build.js              ← packaging script (Node.js)
├── package.json
└── .vscode/
    ├── settings.json
    └── extensions.json
```

### `.vscode/extensions.json` — recommended extensions:

```json
{
  "recommendations": [
    "esbenp.prettier-vscode",
    "ZainChen.json",
    "nickdemayo.vscode-json-editor",
    "streetsidesoftware.code-spell-checker"
  ]
}
```

### `.vscode/settings.json` — JSON formatting:

```json
{
  "editor.formatOnSave": true,
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.tabSize": 2
  },
  "json.schemas": [
    {
      "fileMatch": ["project.json", "sprite.json"],
      "url": "./sb3-schema.json"
    }
  ],
  "files.associations": {
    "*.sb3": "zip"
  }
}
```

### `package.json` — build scripts:

```json
{
  "name": "my-scratch-project",
  "version": "1.0.0",
  "scripts": {
    "build":   "node build.js",
    "watch":   "node build.js --watch",
    "validate": "node validate.js"
  },
  "devDependencies": {
    "archiver": "^6.0.0",
    "chokidar": "^3.5.3",
    "ajv":      "^8.12.0"
  }
}
```

---

## PACKAGING SCRIPT (Node.js)

### `build.js` — creates the `.sb3` file from `project.json` + assets:

```javascript
const fs       = require('fs');
const path     = require('path');
const archiver = require('archiver');

const PROJECT_JSON = path.resolve(__dirname, 'project.json');
const ASSETS_DIR   = path.resolve(__dirname, 'assets');
const OUTPUT_SB3   = path.resolve(__dirname, 'output.sb3');

async function build() {
  // 1. Read and validate project.json
  const raw     = fs.readFileSync(PROJECT_JSON, 'utf8');
  const project = JSON.parse(raw);

  validateTopLevel(project);

  // 2. Collect all md5ext asset filenames referenced by the project
  const requiredAssets = collectAssets(project);

  // 3. Create the ZIP / .sb3 archive
  const output  = fs.createWriteStream(OUTPUT_SB3);
  const archive = archiver('zip', { zlib: { level: 9 } });

  archive.pipe(output);

  // 4. Add project.json (minified for smaller file size)
  archive.append(JSON.stringify(project), { name: 'project.json' });

  // 5. Add each referenced asset from the assets/ directory
  for (const filename of requiredAssets) {
    const assetPath = path.join(ASSETS_DIR, filename);
    if (!fs.existsSync(assetPath)) {
      console.warn(`[WARN] Asset not found: ${filename} — creating placeholder`);
      archive.append('', { name: filename });   // empty placeholder
    } else {
      archive.file(assetPath, { name: filename }); // flat root, no subdirs
    }
  }

  await new Promise((resolve, reject) => {
    output.on('close', resolve);
    archive.on('error', reject);
    archive.finalize();
  });

  console.log(`[OK] ${OUTPUT_SB3} (${archive.pointer()} bytes)`);
}

// ── Helpers ────────────────────────────────────────────────────────────────

function validateTopLevel(project) {
  const required = ['targets', 'monitors', 'extensions', 'meta'];
  for (const key of required) {
    if (!(key in project)) throw new Error(`Missing top-level key: "${key}"`);
  }
  if (!Array.isArray(project.targets) || project.targets.length === 0) {
    throw new Error('"targets" must be a non-empty array');
  }
  if (!project.targets[0].isStage) {
    throw new Error('targets[0] must have isStage: true (the Stage)');
  }
  if (project.meta.semver !== '3.0.0') {
    throw new Error('meta.semver must be "3.0.0"');
  }
}

function collectAssets(project) {
  const assets = new Set();
  for (const target of project.targets) {
    for (const costume of target.costumes || []) {
      if (costume.md5ext) assets.add(costume.md5ext);
    }
    for (const sound of target.sounds || []) {
      if (sound.md5ext) assets.add(sound.md5ext);
    }
  }
  return assets;
}

build().catch(err => { console.error('[ERROR]', err.message); process.exit(1); });
```

### Python alternative (`build.py`):

```python
import json, zipfile, os, sys, hashlib

PROJECT_JSON = "project.json"
ASSETS_DIR   = "assets"
OUTPUT_SB3   = "output.sb3"

def collect_assets(project):
    assets = set()
    for target in project.get("targets", []):
        for c in target.get("costumes", []):
            if "md5ext" in c: assets.add(c["md5ext"])
        for s in target.get("sounds", []):
            if "md5ext" in s: assets.add(s["md5ext"])
    return assets

def validate(project):
    for key in ("targets","monitors","extensions","meta"):
        if key not in project:
            sys.exit(f"Missing top-level key: {key!r}")
    if not project["targets"] or not project["targets"][0].get("isStage"):
        sys.exit("targets[0] must have isStage: true")
    if project["meta"].get("semver") != "3.0.0":
        sys.exit('meta.semver must be "3.0.0"')

with open(PROJECT_JSON, encoding="utf-8") as f:
    project = json.load(f)

validate(project)
required = collect_assets(project)

with zipfile.ZipFile(OUTPUT_SB3, "w", zipfile.ZIP_DEFLATED) as zf:
    zf.writestr("project.json", json.dumps(project, separators=(",", ":")))
    for filename in required:
        fp = os.path.join(ASSETS_DIR, filename)
        if os.path.isfile(fp):
            zf.write(fp, filename)   # flat root — no subdirectory path
        else:
            print(f"[WARN] Asset not found: {filename}")
            zf.writestr(filename, b"")

print(f"[OK] {OUTPUT_SB3}")
```

---

## UNPACKING SCRIPT (to edit an existing .sb3)

### `unpack.js`:

```javascript
const fs     = require('fs');
const path   = require('path');
const AdmZip = require('adm-zip');   // npm install adm-zip

const SB3_FILE  = process.argv[2];
const OUT_DIR   = process.argv[3] || 'unpacked';

if (!SB3_FILE) { console.error('Usage: node unpack.js <file.sb3> [outDir]'); process.exit(1); }

const zip = new AdmZip(SB3_FILE);
zip.extractAllTo(OUT_DIR, true);

// Pretty-print project.json for easy editing
const jsonPath = path.join(OUT_DIR, 'project.json');
const project  = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
fs.writeFileSync(jsonPath, JSON.stringify(project, null, 2), 'utf8');

console.log(`[OK] Unpacked to ${OUT_DIR}/`);
console.log(`[OK] project.json formatted for editing`);
```

---

## MINIMAL VALID `project.json` TEMPLATE

The smallest valid project (Stage only, blank backdrop, no sprites, no scripts):

```json
{
  "targets": [
    {
      "isStage": true,
      "name": "Stage",
      "variables": {},
      "lists": {},
      "broadcasts": {},
      "blocks": {},
      "comments": {},
      "currentCostume": 0,
      "costumes": [
        {
          "assetId": "cd21514d0531fdffb22204e0ec5ed84a",
          "name": "backdrop1",
          "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
          "dataFormat": "svg",
          "rotationCenterX": 240,
          "rotationCenterY": 180
        }
      ],
      "sounds": [
        {
          "assetId": "83a9787d4cb6f3b7632b4ddfebf74367",
          "name": "pop",
          "dataFormat": "wav",
          "format": "",
          "rate": 44100,
          "sampleCount": 1032,
          "md5ext": "83a9787d4cb6f3b7632b4ddfebf74367.wav"
        }
      ],
      "volume": 100,
      "layerOrder": 0,
      "tempo": 60,
      "videoTransparency": 50,
      "videoState": "on",
      "textToSpeechLanguage": null
    }
  ],
  "monitors": [],
  "extensions": [],
  "meta": {
    "semver": "3.0.0",
    "vm": "0.2.0",
    "agent": "vs-code-sb3-author"
  }
}
```

---

## WORKED EXAMPLE — "When 🏴 clicked, move 10 steps" on a Sprite

```json
{
  "targets": [
    {
      "isStage": true, "name": "Stage",
      "variables": {}, "lists": {}, "broadcasts": {},
      "blocks": {}, "comments": {},
      "currentCostume": 0,
      "costumes": [{
        "assetId": "cd21514d0531fdffb22204e0ec5ed84a",
        "name": "backdrop1",
        "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
        "dataFormat": "svg",
        "rotationCenterX": 240, "rotationCenterY": 180
      }],
      "sounds": [],
      "volume": 100, "layerOrder": 0,
      "tempo": 60, "videoTransparency": 50,
      "videoState": "on", "textToSpeechLanguage": null
    },
    {
      "isStage": false, "name": "Sprite1",
      "variables": {}, "lists": {}, "broadcasts": {},
      "blocks": {
        "hat1": {
          "opcode": "event_whenflagclicked",
          "next": "move1",
          "parent": null,
          "inputs": {},
          "fields": {},
          "shadow": false,
          "topLevel": true,
          "x": 100,
          "y": 100
        },
        "move1": {
          "opcode": "motion_movesteps",
          "next": null,
          "parent": "hat1",
          "inputs": {
            "STEPS": [1, [4, "10"]]
          },
          "fields": {},
          "shadow": false,
          "topLevel": false
        }
      },
      "comments": {},
      "currentCostume": 0,
      "costumes": [{
        "assetId": "b7853f557e4426412e64bb3da6531a99",
        "name": "costume1",
        "md5ext": "b7853f557e4426412e64bb3da6531a99.svg",
        "dataFormat": "svg",
        "rotationCenterX": 48, "rotationCenterY": 50
      }],
      "sounds": [],
      "volume": 100, "layerOrder": 1,
      "visible": true,
      "x": 0, "y": 0,
      "size": 100, "direction": 90,
      "draggable": false,
      "rotationStyle": "all around"
    }
  ],
  "monitors": [],
  "extensions": [],
  "meta": {
    "semver": "3.0.0",
    "vm": "0.2.0",
    "agent": "vs-code-sb3-author"
  }
}
```

---

## COMMON MISTAKES TO AVOID

| Mistake | Fix |
|---------|-----|
| Putting assets in subdirectories inside the ZIP | All files must be at ZIP root |
| Forgetting `topLevel: true` on hat blocks | Hat/orphan blocks need `topLevel: true` + `x`/`y` |
| Using `topLevel: true` on non-root blocks | Only the first block in a script stack is top-level |
| Omitting `x`/`y` on top-level blocks | Required or block will appear at 0,0 |
| Adding `x`/`y` to non-top-level blocks | Remove them; only top-level blocks have coordinates |
| `mutation.argumentids` as an array instead of a JSON string | It must be a string: `"[\"id1\",\"id2\"]"` |
| `stage.isStage` not being the first element in `targets` | Stage must be `targets[0]` |
| Duplicate block IDs | All block IDs must be unique within the project |
| Wrong input shadow code | `1`=shadow only, `2`=no shadow, `3`=obscured shadow |
| Asset `md5ext` not matching the actual file's MD5 | Always recompute the MD5 when changing asset content |
| Missing required `"meta"` keys | `semver`, `vm`, and `agent` are all required |
| Using `"name"` other than `"Stage"` for the stage target | Stage name must be `"Stage"` exactly |

---

## ASSET MD5 COMPUTATION

When adding new assets, compute the MD5 of the file content:

```javascript
// Node.js
const crypto = require('crypto');
const fs     = require('fs');
function getAssetId(filePath) {
  const buf = fs.readFileSync(filePath);
  return crypto.createHash('md5').update(buf).digest('hex');
}
const id  = getAssetId('./assets/my-sprite.svg');
const ext = 'svg';
console.log({ assetId: id, md5ext: `${id}.${ext}` });
```

```python
# Python
import hashlib
def get_asset_id(path):
    return hashlib.md5(open(path,'rb').read()).hexdigest()
```

---

## VALIDATION SCRIPT (`validate.js`)

Quick structural check before building:

```javascript
const fs      = require('fs');
const project = JSON.parse(fs.readFileSync('project.json', 'utf8'));
const errors  = [];

// Top-level keys
for (const k of ['targets','monitors','extensions','meta']) {
  if (!(k in project)) errors.push(`Missing "${k}"`);
}

// Stage
if (project.targets?.[0]?.isStage !== true)
  errors.push('targets[0] must have isStage: true');

// meta
if (project.meta?.semver !== '3.0.0')
  errors.push('meta.semver must be "3.0.0"');

// Block cross-references
for (const target of project.targets || []) {
  const blockIds = new Set(Object.keys(target.blocks || {}));
  for (const [id, block] of Object.entries(target.blocks || {})) {
    if (block.next && !blockIds.has(block.next))
      errors.push(`Block "${id}".next → unknown ID "${block.next}"`);
    if (block.parent && !blockIds.has(block.parent))
      errors.push(`Block "${id}".parent → unknown ID "${block.parent}"`);
  }
  // costumes required
  if (!target.costumes || target.costumes.length === 0)
    errors.push(`Target "${target.name}" has no costumes`);
}

if (errors.length) {
  console.error('Validation FAILED:');
  errors.forEach(e => console.error(' •', e));
  process.exit(1);
} else {
  console.log('Validation PASSED ✓');
}
```

---

## HOW TO LOAD IN SCRATCH

1. Zip `project.json` + all asset files (**flat root, no subfolders**) into `output.zip`.
2. Rename to `output.sb3` (or keep `.zip` and use "Load from computer → All Files" in Scratch).
3. Open [scratch.mit.edu](https://scratch.mit.edu), click **File → Load from your computer**, select the `.sb3`.
4. Alternatively use **TurboWarp** (`turbowarp.org`) for faster loading and testing.

---

## NOTES FOR THE AGENT

- Always generate complete, valid JSON — never truncate or use placeholders like `// ...` inside the JSON itself.
- When the user asks for a Scratch project or block, produce the full `project.json` JSON structure, not pseudocode.
- Default to the minimal valid template and add only what is needed.
- When unsure of a block's opcode, consult R6.
- When adding a custom block (My Blocks), always generate: the `procedures_definition` hat, a `procedures_prototype` shadow block, and the corresponding `procedures_call` blocks — all with correct mutations.
- Always include the `build.js` / `build.py` packaging script when the user wants a `.sb3` file output.
- Never generate an SB3 by embedding binary data in the JSON — assets are always separate files in the ZIP.
