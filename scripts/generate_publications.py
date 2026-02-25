import json
from pathlib import Path
from slugify import slugify
from typing import Any
import hashlib
import re
import calendar

# ---------------- CONFIG ----------------

INPUT = Path("publications.json")   # CSL‑JSON
OUTPUT_DIR_PUBS = Path("content/publications")
OUTPUT_DIR_PRESENTATIONS = Path("content/conferences")
SEARCH_DIR = Path("static/search")
TAG_RE = re.compile(r"</?\s*(em|i)\b[^>]*>", flags=re.IGNORECASE)

TYPE_MAP = {
    "article-journal": "journal article",
    "paper-conference": "conference paper",
    "chapter": "chapter",
    "thesis": "thesis",
    "book": "book",
    "speech": "conference presentation"
}

ALLOWED_TYPES_PUBS = {
    "journal article",
    "conference paper",
    "chapter",
    "thesis",
    "book"
}

ALLOWED_TYPES_PRESENTATIONS = {
    "conference presentation",
    "extended abstract presentation",
    "keynote",
    "panel presentation",
    "seminar presentation",
    "workshop"
}

# ---------------- UTILITIES ----------------

def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def format_authors(author_list):
    return [f"{a['family']}, {a['given']}" for a in author_list]

def format_editors(editor_list):
    return [f"{a['family']}, {a['given']} (Eds.)," for a in author_list]

def format_full_name(person):
    return f"{person['given']} {person['family']}"

def format_initial_name(person):
    initials = " ".join(f"{n[0]}." for n in person["given"].split())
    return f"{person['family']}, {initials}"

def join_names(names):
    if not names:
        return ""
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]}, & {names[1]}"
    return ", ".join(names[:-1]) + f", & {names[-1]}"

def join_full_names(names):
    if not names:
        return ""
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return ", ".join(names[:-1]) + f" and {names[-1]}"

def extract_date(issued):
    parts = issued["date-parts"][0]
    year = parts[0]
    month = parts[1] if len(parts) > 1 else 1
    day = parts[2] if len(parts) > 2 else 1
    return year, f"{year}-{month:02d}-{day:02d}"

def format_apa_date_from_issued(issued: Any) -> str:
    """
    Accepts: - dict like {"date-parts": [[2025, 5, 28]]} - dict like {"date-parts": [["2025","5","28"]]} - a string like "2025-05-28" or "2025/05" - a bare year int or str Returns: - "2025" or "2025, May" or "2025, May 28" or "n.d." when no usable date
    """

    if not issued: return "n.d." # If it's a dict with date-parts
    if isinstance(issued, dict):
        parts = issued.get("date-parts") or []
        if parts and parts[0]:
            dp = parts[0]
            try:
                year = int(dp[0])
            except Exception:
                return "n.d."
            if len(dp) == 1:
                return str(year)
            try:
                month = int(dp[1])
                month_name = calendar.month_name[month] if 1 <= month <= 12 else None
            except Exception:
                month_name = None
            if len(dp) == 2:
                return f"{year}, {month_name}" if month_name else str(year) 
            try:
                day = int(dp[2])
            except Exception:
                return f"{year}, {month_name}" if month_name else str(year) 
            return f"{year}, {month_name} {day}" if month_name else str(year)
    
    # If it's a plain list like [2025,5,28] 
    if isinstance(issued, (list, tuple)) and issued:
        dp = issued
        try:
            year = int(dp[0])
        except Exception:
            return "n.d."
        if len(dp) == 1:
            return str(year)
        try:
            month = int(dp[1])
            month_name = calendar.month_name[month] if 1 <= month <= 12 else None
        except Exception:
            month_name = None
        if len(dp) == 2:
            return f"{year}, {month_name}" if month_name else str(year) 
        try:
            day = int(dp[2])
        except Exception:
            return f"{year}, {month_name}" if month_name else str(year)
        return f"{year}, {month_name} {day}" if month_name else str(year)
    
    # If it's a string like "2025-05-28" or "2025/05" 
    if isinstance(issued, str):
        m = re.match(r"^\s*(\d{4})(?:[-/](\d{1,2})(?:[-/](\d{1,2}))?)?\s*$", issued)
        if m:
            year = int(m.group(1))
            if not m.group(2):
                return str(year)
            month = int(m.group(2))
            month_name = calendar.month_name[month] if 1 <= month <= 12 else None
            if not m.group(3):
                return f"{year}, {month_name}" if month_name else str(year)
            day = int(m.group(3))
            return f"{year}, {month_name} {day}" if month_name else str(year)
    
    # If it's an int-like year
    try:
        year = int(issued)
        return str(year)
    except Exception:
        pass
    
    return "n.d."

def smart_quotes(text: str) -> str:
    # Double quotes
    text = re.sub(r'(^|[\s(\[{<])"', r'\1“', text)
    text = re.sub(r'"', '”', text)

    # Single quotes / apostrophes
    text = re.sub(r"(^|[\s(\[{<])'", r"\1‘", text)
    text = re.sub(r"'", "’", text)

    return text

def capitalise_subtitle(title: str) -> str:
    if ":" not in title:
        return title

    main, subtitle = title.split(":", 1)
    subtitle = subtitle.lstrip()

    if not subtitle:
        return title

    subtitle = subtitle[0].upper() + subtitle[1:]
    return f"{main}: {subtitle}"

def normalise_title(title: str) -> str:
    title = smart_quotes(title)
    title = capitalise_subtitle(title)
    return title

def generate_article_citation(pub):
    authors = join_names(
        [format_initial_name(a) for a in pub["authors"]]
    )
    year = pub["year"]
    title = pub["title"]
    journal = pub["venue"]

    volume = pub.get("volume")
    issue = pub.get("issue")
    pages = pub.get("pages")

    journal_bits = []

    if volume:
        vol = f"<em>{volume}</em>"
        if issue:
            vol += f"({issue})"
        journal_bits.append(vol)

    if pages:
        journal_bits.append(pages.replace("-", "–"))

    journal_part = ", ".join(journal_bits)

    citation = (
        f"{authors} ({year}). {title}. "
        f"<em>{journal}</em>"
    )

    if journal_part:
        citation += f", {journal_part}"

    citation += "."

    if pub.get("doi"):
        citation += f" <a href='https://doi.org/{pub['doi']}'>https://doi.org/{pub['doi']}</a>"
    elif pub.get("url"):
        citation += f" <a href='{pub['url']}'>{pub['url']}</a>"

    return citation

def generate_chapter_citation(pub):
    authors = join_names(
        [format_initial_name(a) for a in pub["authors"]]
    )
    year = pub["year"]
    title = pub["title"]
    editors = join_names(
        [format_initial_name(e) for e in pub["editors"]]
    )
    book_title = pub["venue"]
    pages = pub.get("pages", "").replace("-", "–")
    publisher = pub.get("publisher", "")

    citation = f"{authors} ({year}). {title}. "

    if editors:
        citation += f"In {editors} (Eds.), "

    citation += f"<em>{book_title}</em>"

    if pages:
        citation += f" (pp. {pages})"

    citation += f". {publisher}."

    if pub.get("doi"):
        citation += f" <a href='https://doi.org/{pub['doi']}'>https://doi.org/{pub['doi']}</a>"
    elif pub.get("url"):
        citation += f" <a href='{pub['url']}'>{pub['url']}</a>"

    return citation

def generate_thesis_citation(pub):
    authors = join_names(
        [format_initial_name(a) for a in pub["authors"]]
    )
    year = pub["year"]
    title = pub["title"]
    publisher = pub["publisher"]
    genre = pub["genre"]

    citation = f"{authors} ({year}). <em>{title}</em> [{genre}, {publisher}]."

    if pub.get("doi"):
        citation += f" <a href='https://doi.org/{pub['doi']}'>https://doi.org/{pub['doi']}</a>"
    elif pub.get("url"):
        citation += f" <a href='{pub['url']}'>{pub['url']}</a>"

    return citation

def generate_conference_paper_citation(pub):
    authors = join_names(
        [format_initial_name(a) for a in pub["authors"]]
    )
    year = pub["year"]
    title = pub["title"]
    editors = join_names(
        [format_initial_name(e) for e in pub["editors"]]
    )
    proceedings = pub["venue"]
    pages = pub.get("pages", "").replace("-", "–")
    publisher = pub.get("publisher", "")

    citation = f"{authors} ({year}). {title}. "

    if editors:
        citation += f"In {editors} (Eds.), "

    citation += f"<em>{proceedings}</em>."

    if publisher:
        citation += f" {publisher}."

    if pub.get("doi"):
        citation += f" <a href='https://doi.org/{pub['doi']}'>https://doi.org/{pub['doi']}</a>"
    elif pub.get("url"):
        citation += f" <a href='{pub['url']}'>{pub['url']}</a>"

    return citation

def generate_book_citation(pub):
    authors = join_names([format_initial_name(a) for a in pub["authors"]])
    year = pub["year"]
    title = pub["title"]
    editors = join_names([format_initial_name(e) for e in pub["editors"]])
    publisher = pub.get("publisher", "")

    citation = f"{authors} ({year}). <em>{title}</em>. {publisher}."

    if pub.get("doi"):
        citation += f" <a href='https://doi.org/{pub['doi']}'>https://doi.org/{pub['doi']}</a>"
    elif pub.get("url"):
        citation += f" <a href='{pub['url']}'>{pub['url']}</a>"

    return citation

def generate_edited_collection_citation(pub):
    authors = join_names([format_initial_name(a) for a in pub["editors"]])
    year = pub["year"]
    title = pub["title"]
    publisher = pub.get("publisher", "")

    citation = f"{authors} (Eds.). ({year}). <em>{title}</em>. {publisher}."

    if pub.get("doi"):
        citation += f" <a href='https://doi.org/{pub['doi']}'>https://doi.org/{pub['doi']}</a>"
    elif pub.get("url"):
        citation += f" <a href='{pub['url']}'>{pub['url']}</a>"

    return citation

def generate_presentation_citation(pub):
    authors = join_names([format_initial_name(a) for a in pub.get("authors", [])])
    date = format_apa_date_from_issued(pub.get("issued", {}))
    title = pub.get("title", "")
    genre = pub.get("genre", "")
    conference = pub.get("event-title", "")
    place = pub.get("event-place", "")

    citation = f"{authors} ({date}). <em>{title}</em> [{genre}]. {conference}, {place}."

    if pub.get("doi"):
        citation += f" <a href='https://doi.org/{pub['doi']}'>https://doi.org/{pub['doi']}</a>"
    elif pub.get("url"):
        citation += f" <a href='{pub['url']}'>{pub['url']}</a>"

    return citation

def toml_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')

def clean_title(title: str) -> str:
    return TAG_RE.sub("", title).strip()

# ---------------- NORMALIZATION ----------------

def normalize_entry(entry):
    year, date = extract_date(entry.get("issued", {}))
    title = normalise_title(entry.get("title", ""))
    entry_type = None

    entry_type_field = entry.get("type", "")
    genre = entry.get("genre", "")
    container = entry.get("container-title", "")

    # Normalize container-title to a single lowercase string for matching
    if isinstance(container, list):
        container_text = " ".join(str(x) for x in container).lower()
    else:
        container_text = str(container).lower()

    # Handle conference / speech types
    if entry_type_field in ("paper-conference", "conference paper", "speech"):
        if genre == "Extended abstract":
            entry_type = "extended abstract presentation"
        elif "abstract" in container_text:
            entry_type = "extended abstract presentation"
            genre = "Extended abstract"
        elif genre == "Keynote":
            entry_type = "keynote"
        elif genre == "Panel presentation":
            entry_type = "panel presentation"
        elif genre == "Seminar presentation":
            entry_type = "seminar presentation"
        elif genre == "Workshop":
            entry_type = "workshop"

    # Fallback to TYPE_MAP or misc
    if not entry_type:
        entry_type = TYPE_MAP.get(entry_type_field, "misc")

    return {
        "id": entry.get("id", ""),
        "type": entry_type,
        "title": title,
        "title_html": title,
        "title-short": entry.get("title-short", ""),
        "authors": entry.get("author", []),
        "editors": entry.get("editor", []),
        "year": year,
        "date": date,
        "issued": entry.get("issued", {}),
        "venue": entry.get("container-title", ""),
        "volume": entry.get("volume", ""),
        "issue": entry.get("issue", ""),
        "pages": entry.get("page", ""),
        "publisher": entry.get("publisher", ""),
        "genre": genre,
        "event-title": entry.get("event-title", ""),
        "event-place": entry.get("event-place", ""),
        "genre": genre,
        "doi": entry.get("DOI", ""),
        "url": entry.get("URL", ""),
        "abstract": entry.get("abstract", ""),
    }

# ---------------- RENDERING ----------------

def render_markdown_pubs(pub):

    authors_list = [format_full_name(a) for a in pub["authors"]]
    editors_list = [format_full_name(e) for e in pub["editors"]]
    authors_toml = ", ".join(f'"{toml_escape(a)}"' for a in authors_list)
    editors_toml = ", ".join(f'"{toml_escape(e)}"' for e in editors_list)
    all_authors = join_full_names(authors_list)
    all_editors = f'{join_full_names(editors_list)} (editors)'
    lines = [
        "+++",
        f'title = "{toml_escape(pub["title"])}"',
        f"date = {pub['date']}",
        f"authors = [{authors_toml}]",
        "",
        "[extra]",
        f'type = "{pub["type"]}"',
        f'editors = "{pub["editors"]}"',
        f'all_editors = "{all_editors}"',
        f'all_authors = "{all_authors}"',
        "title_html = '''",
        pub["title_html"],
        "'''",
        f'venue = "{toml_escape(pub["venue"])}"',
        f'url = "https://doi.org/{pub['doi']}"' if pub['doi'] else f'url = "{pub['url']}"'
    ]
    lines.append("authors_structured = [")
    for a in pub["authors"]:
        lines.append(
            f'  {{ family = "{toml_escape(a["family"])}", given = "{toml_escape(a["given"])}" }},'
        )
    lines.append("]")


    if pub["doi"]:
        lines.append(f'doi = "{pub["doi"]}"')

    if pub["type"] == "journal article":
        citation = generate_article_citation(pub)
    elif pub["type"] == "conference paper":
        citation = generate_conference_paper_citation(pub)
    elif pub["type"] == "chapter":
        citation = generate_chapter_citation(pub)
    elif pub["type"] == "thesis":
        citation = generate_thesis_citation(pub)
    elif pub["type"] == "book":
        if pub["authors"]:
            citation = generate_book_citation(pub)
        else:
            citation = generate_edited_collection_citation(pub)

    lines.append(f'citation = "{toml_escape(citation)}"')
    lines.append(f'taxonomies = {{ type = ["{pub["type"]}"] }}')
    lines.append("+++")
    lines.append("")
    lines.append(pub["abstract"])

    return "\n".join(lines)

def render_markdown_presentation(pub):
    authors_list = [format_full_name(a) for a in pub.get("authors", [])]
    authors_toml = ", ".join(f'"{toml_escape(a)}"' for a in authors_list)
    all_authors = join_full_names(authors_list)

    # Safely read fields that may be missing
    event_title = pub.get("event-title", "")
    event_place = pub.get("event-place", "")
    venue = pub.get("venue", "")
    doi = pub.get("doi", "")
    url = pub.get("url", "")

    lines = [
        "+++",
        f'title = "{toml_escape(pub.get("title", ""))}"',
        f"date = {pub.get('date', '1970-01-01')}",
        f"authors = [{authors_toml}]",
        "",
        "[extra]",
        f'type = "{toml_escape(pub.get("type", ""))}"',
        f'conference = "{toml_escape(event_title)}"',
        f'place = "{toml_escape(event_place)}"',
        f'all_authors = "{toml_escape(all_authors)}"',
        "title_html = '''",
        pub.get("title_html", ""),
        "'''",
        f'venue = "{toml_escape(venue)}"',
        f'url = "https://doi.org/{doi}"' if doi else f'url = "{toml_escape(url)}"'
    ]

    lines.append("authors_structured = [")
    for a in pub.get("authors", []):
        lines.append(
            f'  {{ family = "{toml_escape(a.get("family",""))}", given = "{toml_escape(a.get("given",""))}" }},'
        )
    lines.append("]")

    if doi:
        lines.append(f'doi = "{toml_escape(doi)}"')

    citation = ""
    if pub.get("type") in ALLOWED_TYPES_PRESENTATIONS:
        citation = generate_presentation_citation(pub)

    lines.append(f'citation = "{toml_escape(citation)}"')
    lines.append(f'taxonomies = {{ type = ["{toml_escape(pub.get("type",""))}"] }}')
    lines.append("+++")
    lines.append("")
    lines.append(pub.get("abstract", ""))

    return "\n".join(lines)

# ---------------- MAIN ----------------

def main():
    OUTPUT_DIR_PUBS.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR_PRESENTATIONS.mkdir(parents=True, exist_ok=True)
    SEARCH_DIR.mkdir(parents=True, exist_ok=True)

    with open(INPUT, encoding="utf-8") as f:
        entries = json.load(f)

    search_index = []

    for raw_pub in entries:
        pub = normalize_entry(raw_pub)

        # Decide whether this is a publication or a presentation
        if pub["type"] in ALLOWED_TYPES_PUBS:
            out_dir = OUTPUT_DIR_PUBS
            render_fn = render_markdown_pubs
        elif pub["type"] in ALLOWED_TYPES_PRESENTATIONS:
            out_dir = OUTPUT_DIR_PRESENTATIONS
            render_fn = render_markdown_presentation
        else:
            # Skip types we don't handle
            continue

        slug_source = pub.get("title-short") or pub.get("title", "")
        slug = f"{pub['year']}-{slugify(slug_source)[:60]}"
        path = out_dir / f"{slug}.md"

        content = render_fn(pub)
        new_hash = hash_text(content)

        # If file exists and content unchanged, skip writing
        if path.exists() and hash_text(path.read_text(encoding="utf-8")) == new_hash:
            continue

        path.write_text(content, encoding="utf-8")
        print(f"Updated: {path}")


        search_index.append({
            "title": pub["title"],
            "title_html": pub["title_html"],
            "authors": pub["authors"],
            "year": pub["year"],
            "venue": pub["venue"],
            "doi": pub["doi"],
            "slug": slug,
            "url": f"/publications/{slug}/",
        })

    with open(SEARCH_DIR / "publications.json", "w", encoding="utf-8") as f:
        json.dump(search_index, f, indent=2, ensure_ascii=False)

    print("Search index updated.")

if __name__ == "__main__":
    main()
