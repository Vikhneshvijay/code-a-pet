import json
import sys
import os

PROJECT_JSON = 'project.json'
if not os.path.exists(PROJECT_JSON):
    print(f"Error: {PROJECT_JSON} not found.")
    sys.exit(1)

with open(PROJECT_JSON, 'r', encoding='utf-8') as f:
    try:
        project = json.load(f)
    except Exception as e:
        print(f"JSON Parse Error: {e}")
        sys.exit(1)

errors = []

# Top-level keys
for k in ['targets', 'monitors', 'extensions', 'meta']:
    if k not in project:
        errors.append(f'Missing "{k}"')

# Stage
targets = project.get('targets', [])
if not targets or not targets[0].get('isStage'):
    errors.append('targets[0] must have isStage: true')

# meta
meta = project.get('meta', {})
if meta.get('semver') != '3.0.0':
    errors.append('meta.semver must be "3.0.0"')

# Block cross-references
for target in targets:
    blocks = target.get('blocks', {})
    block_ids = set(blocks.keys())
    for id, block in blocks.items():
        if isinstance(block, dict):
            next_id = block.get('next')
            if next_id and next_id not in block_ids:
                errors.append(f'Block "{id}".next -> unknown ID "{next_id}"')
            parent_id = block.get('parent')
            if parent_id and parent_id not in block_ids:
                errors.append(f'Block "{id}".parent -> unknown ID "{parent_id}"')
    
    # costumes required
    costumes = target.get('costumes', [])
    if not costumes:
        errors.append(f'Target "{target.get("name")}" has no costumes')

if errors:
    print('Validation FAILED:')
    for e in errors:
        print(' •', e)
    sys.exit(1)
else:
    print('Validation PASSED ✓')
