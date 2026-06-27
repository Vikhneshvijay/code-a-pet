import json, zipfile, os, sys

PROJECT_JSON = "project.json"
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

def main():
    if not os.path.exists(PROJECT_JSON):
        print(f"[ERROR] {PROJECT_JSON} not found. Please create it first.")
        sys.exit(1)

    with open(PROJECT_JSON, encoding="utf-8") as f:
        project = json.load(f)

    validate(project)
    required = collect_assets(project)

    with zipfile.ZipFile(OUTPUT_SB3, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("project.json", json.dumps(project, separators=(",", ":")))
        for filename in required:
            # Look in the root first, then in the assets/ directory
            fp = filename
            if not os.path.isfile(fp):
                fp = os.path.join("assets", filename)
                
            if os.path.isfile(fp):
                zf.write(fp, filename)
            else:
                print(f"[WARN] Asset not found: {filename} — creating empty placeholder")
                zf.writestr(filename, b"")

    print(f"[OK] Compiled: {OUTPUT_SB3}")

if __name__ == "__main__":
    main()
