"""Check Jekyll output for missing pages, local links and assets."""

from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urljoin, urlsplit


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("href", "src") and value:
                self.urls.append(value)


def check(root):
    required = ["index.html", "404.html", "downloads/index.html",
                "meetup/index.html", "supporters/index.html", "news/index.html",
                "acknowledgements/index.html", "get-involved/index.html",
                "users/index.html", "team/index.html", "assets/js/search-data.json"]
    errors = [f"Missing output: {name}" for name in required
              if not (root / name).is_file()]
    home = root / "index.html"
    if not home.exists():
        return errors
    parser = Links()
    parser.feed(home.read_text())
    # The theme emits the stylesheet through relative_url. Infer the deployed
    # project prefix so this check also supports custom domains and local builds.
    styles = [urlsplit(u).path for u in parser.urls
              if urlsplit(u).path.endswith("/assets/css/just-the-docs-default.css")]
    if not styles:
        errors.append("Just the Docs stylesheet missing")
        return errors
    prefix = styles[0].removesuffix("/assets/css/just-the-docs-default.css")
    for page in root.rglob("*.html"):
        parser = Links()
        content = page.read_text()
        if "{{" in content or "{%" in content:
            errors.append(f"Unrendered Liquid in {page.relative_to(root)}")
        parser.feed(content)
        page_url = prefix + "/" + page.relative_to(root).as_posix()
        for value in parser.urls:
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc or value.startswith("#"):
                continue
            path = unquote(urlsplit(urljoin(page_url, value)).path)
            if prefix and not path.startswith(prefix + "/"):
                errors.append(f"Link escapes project path in {page.name}: {value}")
                continue
            local = root / path[len(prefix):].lstrip("/")
            if local.is_dir():
                local = local / "index.html"
            if not local.is_file():
                errors.append(f"Missing target in {page.relative_to(root)}: {value}")
    return sorted(set(errors))


if __name__ == "__main__":
    failures = check(Path(sys.argv[1] if len(sys.argv) > 1 else "_site"))
    if failures:
        print("\n".join(failures))
        sys.exit(1)
    print("Site pages, theme, local links and assets verified.")
