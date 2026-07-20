# Como rodar a aplicação

## PARTE A

### 1. Clone o repositório na sua máquina e entre no diretório da aplicação

Abra o terminal, navegue até a pasta em que deseja clonar o diretório e rode os comandos:

```shell
git clone https://github.com/Felipems999/roteiro-de-vendas
cd roteiro-de-vendas
```

### 2. Subir o backend em uma porta local

Para rodar o backend, é necessário ter instalado o interpratador da linguagem Python, versão 3.10.0 ou superior.
Ele pode ser obtido no site oficial da linguagem:

- [Python](https://www.python.org/downloads/);

Em seguida, basta rodar esse o comando em um terminal:

```shell
python3 backend.py
```
ou
```shell
python backend.py
```

### 3. Subir o frontend em uma porta local

Para rodar o frontend localmente, foi utilizado o pacote dlx, através do pnpm. Basta instalar o gerenciador
de pacotes pnpm, caso não o possua instalado, ou outro gerenciador de pacotes de Javascritp. As instruções
para instalar o pnpm estão no endereço abaixo:

- [Instalação do pnpm](https://pnpm.io/pt/installation);

Em seguida, em outro terminal, em que o backend não esteja sendo executado, execute o arquivo "backend.py" com
o comando:

```shell
pnpm dlx http-server -p 8080 -c-1
```

Isso fará com que a aplicação seja hospedada na porta 8080 do localhost. Basta acessar http://localhost:8080.

## PARTE B

- Problema:
  Caso o campo de público não seja preenchido, ocorrerá um erro ao chamar o método toLowerCase, pois ele será
  do tipo "undefined". Um erro também pode ocorrer caso "dodos.nomeOferta" ou "dados.resultado" também não
  sejam preenchidos.

- Solução:
  
```javascript
function gerarRoteiro(dados) {
  const publico = dados.publico ? dados.publico.toLowerCase() : "SEM PÚBLICO";
  const linhas = [
    "Oferta: " + (dados.nomeOferta ?? "SEM OFERTA"),
    "Para quem é: " + publico,
    "O que você promete: " + (dados.resultado ?? "SEM RESULTADO"),
  ];
  return linhas.join("\n");
}
```

Para evitar o erro caso "dados.publico" seja "undefined", acrescentei uma operação ternária na declaração da
variável publico que verifica se o dado existe. O mesmo foi feito na declaração dos items da lista "linhas",
para que o mesmo erro não ocorra caso "dodos.nomeOferta" ou "dados.resultado" também não sejam preenchidos.
