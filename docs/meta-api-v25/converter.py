#!/usr/bin/env python3
"""
Converte HTML salvo da docs da Meta em Markdown limpo.
Usa BeautifulSoup para parsing robusto.
Uso: python3 converter.py [arquivo.html | --all]
"""
import sys
import re
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

# Mapa de classes CSS sprite do Meta para simbolos unicode
_SPRITE_MAP = {
    'sx_d4b184': '✓',   # check verde
    'sx_4132bf': '✗',   # X vermelho
    'sx_a3284c': '●',   # bullet/dot
    'sx_331aa4': '○',   # circle
    'sx_70ec3d': '◆',   # diamond
}


def tag_to_md(tag, depth=0) -> str:
    """Converte recursivamente uma tag HTML em markdown."""
    if isinstance(tag, NavigableString):
        text = str(tag)
        if not text.strip():
            return ' '
        return text

    if not isinstance(tag, Tag):
        return ''

    name = tag.name

    # Skip
    if name in ('script', 'style', 'noscript', 'svg', 'path', 'meta', 'link', 'img'):
        return ''

    # Inline content
    children_md = ''.join(tag_to_md(c, depth) for c in tag.children)

    if name in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        level = int(name[1])
        title = re.sub(r'\s+', ' ', children_md).strip()
        if title:
            return f'\n\n{"#" * level} {title}\n\n'
        return ''

    if name == 'p':
        text = re.sub(r'\s+', ' ', children_md).strip()
        if text:
            return f'\n\n{text}\n'
        return ''

    if name == 'br':
        return '\n'

    if name in ('strong', 'b'):
        inner = re.sub(r'\s+', ' ', children_md).strip()
        return f'**{inner}**' if inner else ''

    if name == 'i':
        # Detectar icones sprite do Meta (check/cross em tabelas)
        classes = tag.get('class', [])
        for cls in classes:
            if cls in _SPRITE_MAP:
                return _SPRITE_MAP[cls]
        # Se tem classes de sprite (img sp_) mas nao mapeado, retornar vazio
        if any('img' in c or 'sp_' in c for c in classes):
            return ''
        # i normal = italico
        inner = re.sub(r'\s+', ' ', children_md).strip()
        return f'*{inner}*' if inner else ''

    if name == 'em':
        inner = re.sub(r'\s+', ' ', children_md).strip()
        return f'*{inner}*' if inner else ''

    if name == 'code':
        # Se esta dentro de um <pre>, nao adicionar backticks
        if tag.parent and tag.parent.name == 'pre':
            return tag.get_text()
        inner = tag.get_text()
        return f'`{inner}`'

    if name == 'pre':
        # Pegar todo o texto, incluindo spans do prettyprint
        code = tag.get_text()
        return f'\n```\n{code.strip()}\n```\n'

    # Skip tab navigation buttons (HTTP, PHP SDK, cURL, etc.)
    if name == 'button':
        return ''

    if name == 'a':
        href = tag.get('href', '')
        text = re.sub(r'\s+', ' ', children_md).strip()
        if href and text:
            return f'[{text}]({href})'
        return text

    if name == 'li':
        text = re.sub(r'\s+', ' ', children_md).strip()
        return f'\n- {text}'

    if name in ('ul', 'ol'):
        return f'\n{children_md}\n'

    if name == 'table':
        return convert_table(tag)

    if name in ('div', 'span', 'section', 'article', 'main', 'td', 'th',
                 'tr', 'thead', 'tbody', 'tfoot', 'header', 'footer',
                 'nav', 'aside', 'figure', 'figcaption', 'blockquote',
                 'dl', 'dt', 'dd', 'label', 'form', 'input', 'button',
                 'select', 'option', 'textarea'):
        return children_md

    return children_md


def _extract_sprite_icon(tag) -> str:
    """Detecta icone sprite do Meta em uma tag ou seus filhos."""
    if not isinstance(tag, Tag):
        return ''
    # Checar a propria tag
    if tag.name == 'i':
        for cls in tag.get('class', []):
            if cls in _SPRITE_MAP:
                return _SPRITE_MAP[cls]
    # Checar filhos recursivamente
    for child in tag.find_all('i', class_=True):
        for cls in child.get('class', []):
            if cls in _SPRITE_MAP:
                return _SPRITE_MAP[cls]
    return ''


def convert_table(table_tag) -> str:
    """Converte <table> em markdown table."""
    rows = []
    for tr in table_tag.find_all('tr'):
        # Detectar sub-campos e profundidade
        # row_3 = top-level, row_3-0 = sub (depth 1), row_3-0-1 = sub-sub (depth 2)
        tr_classes = tr.get('class', [])
        depth = 0
        for c in tr_classes:
            m = re.match(r'row_[\d]+(-[\d]+)+', c)
            if m:
                depth = c.count('-')
                break
        cells = []
        for cell in tr.find_all(['td', 'th']):
            # Pegar texto preservando code inline e icones sprite
            parts = []
            for child in cell.children:
                if isinstance(child, NavigableString):
                    parts.append(str(child).strip())
                elif isinstance(child, Tag):
                    # Verificar icones sprite (podem estar em qualquer nivel)
                    icon = _extract_sprite_icon(child)
                    if icon:
                        parts.append(icon)
                    elif child.name == 'code':
                        parts.append(f'`{child.get_text()}`')
                    elif child.name == 'a':
                        text = child.get_text(strip=True)
                        href = child.get('href', '')
                        parts.append(f'[{text}]({href})' if href else text)
                    elif child.name in ('ul', 'ol'):
                        items = [li.get_text(' ', strip=True) for li in child.find_all('li')]
                        parts.append('; '.join(items))
                    else:
                        parts.append(child.get_text(' ', strip=True))
            cell_text = ' '.join(p for p in parts if p)
            cell_text = re.sub(r'\s+', ' ', cell_text).strip()
            cell_text = cell_text.replace('|', '\\|')  # escape pipes
            # Escapar < > que nao estao dentro de backticks (senao somem no markdown)
            # Preservar os que ja estao em code inline (`...`)
            parts_final = cell_text.split('`')
            for idx in range(len(parts_final)):
                if idx % 2 == 0:  # fora de backticks
                    parts_final[idx] = parts_final[idx].replace('<', '\\<').replace('>', '\\>')
            cell_text = '`'.join(parts_final)
            cells.append(cell_text)
        if cells:
            # Prefixar primeiro campo com → pra indicar profundidade
            if depth > 0 and cells:
                prefix = '→ ' * depth
                cells[0] = prefix + cells[0]
            rows.append(cells)

    if not rows:
        return ''

    ncols = max(len(r) for r in rows)
    for r in rows:
        while len(r) < ncols:
            r.append('')

    md = '\n\n'
    md += '| ' + ' | '.join(rows[0]) + ' |\n'
    md += '| ' + ' | '.join(['---'] * ncols) + ' |\n'
    for row in rows[1:]:
        md += '| ' + ' | '.join(row) + ' |\n'
    md += '\n'
    return md


def convert_file(html_path: Path) -> str:
    """Converte um arquivo HTML completo em markdown."""
    html = html_path.read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    # Remover elementos indesejados
    for tag in soup(['script', 'style', 'noscript', 'svg']):
        tag.decompose()

    # Tentar encontrar o conteudo principal
    main = soup.find('div', {'role': 'main'})
    if not main:
        main = soup.find('div', class_=re.compile(r'content|article|doc'))
    if not main:
        # Fallback: pegar tudo do body
        main = soup.find('body') or soup

    md = tag_to_md(main)

    # Limpar
    # Cortar navegacao do topo - encontrar primeiro H1
    lines = md.split('\n')
    cut = 0
    for i, ln in enumerate(lines):
        if ln.strip().startswith('# ') and len(ln.strip()) > 8:
            cut = i
            break
    md = '\n'.join(lines[cut:])

    # Remover "Nesta Pagina" sidebar
    md = re.sub(r'Nesta Página.*?(?=\n## |\n# )', '', md, count=1, flags=re.DOTALL)

    # Limpar whitespace excessivo
    md = re.sub(r'\n{4,}', '\n\n\n', md)
    md = re.sub(r'[ \t]+$', '', md, flags=re.MULTILINE)

    # Extrair URL original do HTML
    url_match = re.search(r'saved from url=\(\d+\)(https?://[^\s"]+)', html)
    url = url_match.group(1) if url_match else 'N/A'

    header = f'<!-- Fonte: {html_path.name} -->\n'
    header += f'<!-- URL: {url} -->\n'
    header += f'<!-- API: v25.0 | Data: 2026-03-30 -->\n\n'

    return header + md.strip()


def main():
    docs = Path(__file__).parent
    if len(sys.argv) > 1 and sys.argv[1] != '--all':
        files = [Path(sys.argv[1])]
    else:
        files = sorted(docs.glob('*.html'))

    if not files:
        print("Nenhum arquivo HTML encontrado.")
        return

    for f in files:
        print(f"Convertendo: {f.name}")
        md = convert_file(f)
        out = docs / (f.stem.lower().replace(' ', '-') + '.md')
        out.write_text(md, encoding='utf-8')
        lines = md.count('\n')
        tables = md.count('| ---')
        print(f"  -> {out.name} ({len(md):,} chars, {lines} linhas, {tables} tabelas)")

    print(f"\n{len(files)} arquivo(s) convertido(s).")


if __name__ == '__main__':
    main()
