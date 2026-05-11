import os

viejo = """    {% if user.is_authenticated %}
    <a href="/panel/" class="btn-login" style="background:rgba(201,168,76,0.1);">⚙ Panel</a>
    <a href="/logout/" class="btn-login">Cerrar Sesión</a>
    {% else %}
    <a href="/login/" class="btn-login">Iniciar Sesión</a>
    {% endif %}"""

nuevo = """    {% if user.is_authenticated %}
    <div class="user-menu" id="userMenu">
      <button class="user-btn" onclick="toggleUserMenu()">
        ✦ {{ user.username }}
        <span class="user-btn-arrow">▼</span>
      </button>
      <div class="user-dropdown">
        <a href="/panel/">⚙ Panel</a>
        <a href="/perfil/">👤 Perfil</a>
        <a href="/cambiar-contrasena/">🔑 Cambiar Contraseña</a>
        <a href="/logout/" class="danger">← Cerrar Sesión</a>
      </div>
    </div>
    {% else %}
    <a href="/login/" class="btn-login">Iniciar Sesión</a>
    {% endif %}"""

carpeta = 'templates'
for root, dirs, files in os.walk(carpeta):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                contenido = file.read()
            if viejo in contenido:
                contenido = contenido.replace(viejo, nuevo)
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(contenido)
                print(f'Actualizado: {path}')

print('Listo!')