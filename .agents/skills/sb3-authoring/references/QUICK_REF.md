# SB3 Quick-Reference Card

## Block Chain Pattern
```
[hat block]  → topLevel:true, parent:null, next:"block2", x:N, y:N
[block2]     → topLevel:false, parent:"hat", next:"block3"
[block3]     → topLevel:false, parent:"block2", next:null
```

## Input Encodings (most common)
```jsonc
// Literal number 10 (shadow-only)
"STEPS": [1, [4, "10"]]

// Variable reporter replacing a number
"STEPS": [3, "varBlockId", [4, "10"]]

// Another block with no shadow
"CONDITION": [2, "boolBlockId"]

// String literal
"MESSAGE": [1, [10, "Hello!"]]

// Color literal
"COLOR": [1, [9, "#ff0000"]]
```

## Field Encodings (most common)
```jsonc
// Simple string field (key press, rotation style, etc.)
"KEY_OPTION": ["space"]

// Variable/List/Broadcast fields carry an ID
"VARIABLE":   ["score", "variableId123"]
"LIST":       ["myList", "listId456"]
```

## Common Hat Blocks
```jsonc
// Green flag
{"opcode":"event_whenflagclicked","inputs":{},"fields":{}}

// Key pressed
{"opcode":"event_whenkeypressed","inputs":{},"fields":{"KEY_OPTION":["space"]}}

// Clone start
{"opcode":"control_start_as_clone","inputs":{},"fields":{}}

// Receive broadcast
{"opcode":"event_whenbroadcastreceived","inputs":{},"fields":{"MESSAGE":["go","broadcastId"]}}
```

## C-Block (if/repeat) Pattern
```jsonc
// control_if — condition + body
{
  "opcode": "control_if",
  "inputs": {
    "CONDITION": [2, "boolBlock"],
    "SUBSTACK":  [2, "firstBodyBlock"]
  }
}
// firstBodyBlock.parent = "ifBlockId"
```

## Custom Block (My Block)
Three blocks always needed together:
1. `procedures_definition` (hat) → input: reference to prototype
2. `procedures_prototype` (shadow inside definition's CUSTOM_BLOCK input)
3. `procedures_call` (where you call the custom block)

## Extensions in Opcodes
`pen_clear`, `pen_stamp`, `pen_penDown`, `pen_penUp`
`music_playDrumForBeats`, `music_playNoteForBeats`
`text2speech_speakAndWait`, `text2speech_setLanguage`
`translate_getTranslate`, `translate_language`
`videoSensing_videoOn`, `videoSensing_videoToggle`
