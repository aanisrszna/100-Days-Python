import os

# Define the project structure
folders = [
    "allrecipes_scraper",
    "allrecipes_scraper/data",
    "allrecipes_scraper/scripts",
    "allrecipes_scraper/drivers"
]

files = {
    "allrecipes_scraper/scripts/scraper.py": "# TODO: Write scraper code here\n",
    "allrecipes_scraper/data/allrecipes_scraped.csv": "Title,Rating,Ingredients,Link\n",
    "allrecipes_scraper/requirements.txt": "selenium\npandas\n",
    "allrecipes_scraper/README.md": "# AllRecipes Web Scraper\n\n## Setup\n1. Install dependencies:\n   ```bash\n   pip install -r requirements.txt\n   ```\n2. Run the scraper:\n   ```bash\n   python scripts/scraper.py\n   ```\n3. Output file: `data/allrecipes_scraped.csv`\n",
    "allrecipes_scraper/.gitignore": "data/*.csv\n"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with default content
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("✅ Project setup complete!")
