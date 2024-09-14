## Подготовка окружения

1. Установить homebrew <br>
   ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```
2. Установить зависимостей <br> 
   ```brew install pyenv poetry readline xz sqlite docker-compose```
3. Выполнить команды <br>
   ```echo 'export PATH="/opt/homebrew/opt/sqlite/bin:$PATH"' >> ~/.zshrc``` <br>
   ```export LDFLAGS="-L/opt/homebrew/opt/sqlite/lib"``` <br>
   ```export CPPFLAGS="-I/opt/homebrew/opt/sqlite/include"``` <br>
   ```export PKG_CONFIG_PATH="/opt/homebrew/opt/sqlite/lib/pkgconfig"``` <br>
