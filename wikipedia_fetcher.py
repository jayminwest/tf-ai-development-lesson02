import wikipediaapi
import sys
import os

def fetch_wikipedia_article(title):
    """Fetch a Wikipedia article and save it as markdown"""
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(title)
    
    if not page.exists():
        print(f"Error: Article '{title}' does not exist on Wikipedia")
        return False
        
    filename = f"{title.replace(' ', '_')}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(page.text)
    
    print(f"Successfully saved {filename}")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wikipedia_fetcher.py <article_title>")
        sys.exit(1)
        
    article_title = sys.argv[1]
    fetch_wikipedia_article(article_title)
