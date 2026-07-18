# Como rodar a aplicação

### 1. Clone o repositório na sua máquina e entre no diretório da aplicação

Abra o terminal, navegue até a pasta em que deseja clonar o diretório e rode os comandos:

```shell
git clone https://github.com/Felipems999/roteiro-de-vendas
cd roteiro-de-vendas
```

### 2. Subir o frontend em uma porta local

Para rodar o frontend localmente, foi utilizado o pacote dlx, através do pnpm. Basta instalar o gerenciador
de pacotes pnpm, caso não o possua instalado, ou outro gerenciador de pacotes de Javascritp. As instruções
para instalar o pnpm estão no endereço abaixo:

- [Instalação do pnpm](https://pnpm.io/pt/installation);

Em seguida, basta rodar o comando em um terminal:

```shell
pnpm dlx http-server -p 8080 -c-1
```

Isso fará com que a aplicação seja hospedada na porta 8080 do localhost. Basta acessar http://localhost:8080.

### 3. Subir o backend em uma porta local

Para rodar o backend, é necessário ter instalado o interpratador da linguagem Python, versão 3.10.0 ou superior.
Ele pode ser obtido no site oficial da linguagem:

- [Python](https://www.python.org/downloads/);

Em seguida, em outro terminal, em que o frontend não esteja sendo executado, execute o arquivo "backend.py" com
o comando:

```shell
python3 backend.py
```
ou
```shell
python backend.py
```
