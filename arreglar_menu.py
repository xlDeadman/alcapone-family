import os

css = """
  /* ── USER MENU ── */
  .user-menu { position: relative; }
  .user-btn { display: flex; align-items: center; gap: 0.5rem; background: rgba(201,168,76,0.08); border: 1px solid rgba(201,168,76,0.25); color: rgba(201,168,76,0.8); font-family: 'Cinzel', serif; font-size: 0.65rem; letter-spacing: 0.2em; text-transform: uppercase; padding: 0.5rem 1rem; cursor: pointer; transition: all 0.3s; }
  .user-btn:hover { background: rgba(201,168,76,0.15); color: #c9a84c; border-color: #c9a84c; }
  .user-btn-arrow { font-size: 0.5rem; transition: transform 0.3s; }
  .user-menu.open .user-btn-arrow { transform: rotate(180deg); }
  .user-dropdown { position: absolute; top: calc(100% + 0.5rem); right: 0; background: rgba(12,10,5,0.98); border: 1px solid rgba(201,168,76,0.2); min-width: 180px; display: none; flex-direction: column; z-index: 200; }
  .user-dropdown::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, transparent, #c9a84c, transparent); }
  .user-menu.open .user-dropdown { display: flex; }
  .user-dropdown a { display: flex; align-items: center; gap: 0.7rem; padding: 0.8rem 1.2rem; font-family: 'Cinzel', serif; font-size: 0.6rem; letter-spacing: 0.2em; text-transform: uppercase; color: rgba(245,234,208,0.5); text-decoration: none; transition: all 0.3s; border-bottom: 1px solid rgba(201,168,76,0.05); }
  .user-dropdown a:last-child { border-bottom: none; }
  .user-dropdown a:hover { background: rgba(201,168,76,0.06); color: #c9a84c; }
  .user-dropdown a.danger { color: rgba(192,57,43,0.6); }
  .user-dropdown a.danger:hover { background: rgba(192,57,43,0.06); color: #c0392b; }
"""

js = """
  function toggleUserMenu() {
    document.getElementById('userMenu').classList.toggle('open');
  }
  document.addEventListener('click', (e) => {
    const menu = document.getElementById('userMenu');
    if (menu && !menu.contains(e.target)) menu.classList.remove('open');
  });
"""

carpeta = 'templates'
for root, dirs, files in os.walk(carpeta):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                contenido = file.read()

            # Saltar index.html y panel
            if 'index.html' in path or 'panel' in path:
                continue

            # Agregar CSS si no lo tiene
            if 'user-menu' not in contenido and '</style>' in contenido:
                contenido = contenido.replace('</style>', css + '</style>', 1)

            # Agregar JS si no lo tiene
            if 'toggleUserMenu' not in contenido and '</script>' in contenido:
                contenido = contenido.replace('</script>', js + '</script>', 1)
            elif 'toggleUserMenu' not in contenido and '</body>' in contenido:
                contenido = contenido.replace('</body>', f'<script>{js}</script>\n</body>', 1)

            with open(path, 'w', encoding='utf-8') as file:
                file.write(contenido)
            print(f'Actualizado: {path}')

print('Listo!')