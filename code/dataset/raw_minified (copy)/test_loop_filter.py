from jinja2 import Environment as A
B=A().from_string('<ul>\n{%- for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if item % 2 == 0 %}\n    <li>{{ loop.index }} / {{ loop.length }}: {{ item }}</li>\n{%- endfor %}\n</ul>\nif condition: {{ 1 if foo else 0 }}\n')
print(B.render(foo=True))