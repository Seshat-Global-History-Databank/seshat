from pathlib import Path

################################################################
# Get file lists                                               #
################################################################

python_files = Path("../seshat").glob("**/*.py")
html_files = Path("../seshat").glob("**/*.html")

################################################################
# Process all python files looking for template references     #
################################################################

potential_lines = []
for python_file in python_files:
    if python_file.stem.startswith("00"):
        continue  # Skip files starting with "00"

    lines = python_file.read_text().splitlines()
    for ix, line in enumerate(lines):
        if line.strip().startswith("#") or line.strip().startswith('"""'):
            continue  # skip comments

        if (
            "django.template.context_processors" in line
            or "BACKEND" in line
            or "DIRS" in line
        ):
            continue

        if "function is used" in line:
            continue

        if "import" in line:
            continue

        if "template.Library" in line:
            continue

        add = None
        if "template" in line and not line.endswith("("):
            add = line.strip()
        elif "template" in line and line.endswith("("):
            add = lines[ix + 1].strip()

        if not add:
            if "html" in line and "render" in line:
                add = line.strip()
                add = add.split('"')[1].split('"')[0]
                potential_lines += [add]

                continue
            elif "render" in line and line.strip().endswith("("):
                test_val = lines[ix + 1].strip().strip('request, "').split('"')[0]
                if test_val:
                    potential_lines += [test_val]
                else:
                    test_val = lines[ix + 2].split('"')[1]
                    potential_lines += [test_val]

        if add:
            add = add.split("#")[0]
            add = add.strip("template_name").strip()
            add = add.strip("=").strip()
            add = add.strip('"').strip()

            if "core/seshatcomments/your_template.html" in add:
                add = add.split('"')[1].split('"')[0]

            potential_lines += [add]

template_files_in_code = sorted(list(set(potential_lines)))
print(len(template_files_in_code), "templates found referenced in code")
print()

################################################################
# Get template files in templates directories                  #
################################################################

existing_templates = []
for html_file in html_files:
    existing_templates += [str(html_file.absolute()).split("templates/")[1]]

existing_templates = sorted(list(set(existing_templates)))

print(len(existing_templates), "templates found in templates directories")
print()

################################################################
# Output results to terminal                                   #
################################################################

# These files are in the templates directory but not referenced in the code
files_not_in_code = set(existing_templates) - set(template_files_in_code)

# These files are referenced in the code but not in the templates directory
missing_files = set(template_files_in_code) - set(existing_templates)

# remove manually some weird leftover
missing_files = [
    x
    for x in missing_files
    if x
    not in [
        "return render(request, template_name, context)",
    ]
]

print(len(files_not_in_code), "files not referenced in the code")
print(len(missing_files), "files missing from the templates directory")
print()

################################################################
# Output results to files                                      #
################################################################

Path("output").mkdir(exist_ok=True)
Path("output/missing_files.txt").write_text("\n".join(missing_files))
Path("output/files_not_in_code.txt").write_text("\n".join(files_not_in_code))

print("####################################################################")
print()
print("2 files written with results in the root directory of this script:")
print("- missing_files.txt contains files referenced in the code but missing")
print("  from the templates directory")
print("- files_not_in_code.txt contains files in the templates directory but")
print("  not referenced in the code")
