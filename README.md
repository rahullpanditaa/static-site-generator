# Static Site Generator

A static site generator built from scratch in Python. It parses Markdown into an intermediate node tree, converts it to HTML, applies templates, copies static assets, and recursively generates complete websites.

## Features

* Parses inline Markdown syntax:

  * Bold (`**text**`)
  * Italic (`_text_`)
  * Inline code (`` `code` ``)
  * Links (`[text](url)`)
  * Images (`![alt](image.png)`)
* Parses block-level Markdown:

  * Headings
  * Paragraphs
  * Ordered lists
  * Unordered lists
  * Blockquotes
  * Code blocks
* Converts Markdown into a tree of HTML nodes
* Applies an HTML template
* Extracts page titles from `# H1` headings
* Copies CSS and image assets
* Recursively processes nested directories
* Supports configurable base paths for GitHub Pages deployment
* Includes shell scripts for local development, testing, and deployment builds
* Fully unit tested

## Example

### Input Markdown

```markdown
# My Blog

Welcome to **my website**.

- Post 1
- Post 2
```

### Generated HTML

```html
<h1>My Blog</h1>
<p>Welcome to <strong>my website</strong>.</p>
<ul>
  <li>Post 1</li>
  <li>Post 2</li>
</ul>
```

## Architecture

### TextNode

Represents parsed inline text and its semantic type.

### HTMLNode

Base class for all HTML elements.

### LeafNode

Represents HTML elements without children (e.g. `<strong>`, `<code>`, `<img>`).

### ParentNode

Represents HTML elements containing child nodes.

### Markdown Parser

Converts raw Markdown into:

1. Blocks
2. Inline text nodes
3. HTML nodes

### Site Generator

* Walks the `content/` directory recursively
* Converts `.md` files to `.html`
* Applies the HTML template
* Copies static assets
* Preserves directory structure

## Project Structure

```text
.
├── build.sh        # Build site for GitHub Pages
├── content/        # Markdown source files
├── docs/           # Generated website output
├── main.sh         # Local build + development server
├── README.md
├── src/            # Python source code and tests
├── static/         # CSS, images, and other assets
├── template.html   # HTML template
└── test.sh         # Run unit tests
```

## Usage

### Run Locally

Build the site and start a local server on port `8888`:

```bash
./main.sh
```

Open `http://localhost:8888` in your browser.

### Run Tests

```bash
./test.sh
```

### Build for GitHub Pages

```bash
./build.sh
```

This command passes the repository base path (`/static-site-generator/`) so links and assets work correctly when deployed to GitHub Pages.

## Shell Scripts

### `main.sh`

```bash
python3 src/main.py
cd docs && python3 -m http.server 8888
```

Builds the site and serves the generated output locally.

### `build.sh`

```bash
python3 src/main.py "/static-site-generator/"
```

Builds the site using the GitHub Pages base path.

### `test.sh`

```bash
python3 -m unittest discover -s src
```

Runs all unit tests.

## Output

The generated site is written to the `docs/` directory, which is configured for GitHub Pages deployment.
