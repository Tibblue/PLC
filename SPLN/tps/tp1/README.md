# TP1 - A

### Grupo
* Francisco Oliveira - A78416
* Raul Vilas Boas - A79617

## Requisitos
Antes de correr o código é necessário instalar a package **termcolor**, atraves do *pip*:

`$pip3 install termcolor`

## Ficheiros

* Ficheiros de teste:
    * [example_input.txt](test/example_input.txt)
    * [example_output.txt](test/example_output.txt)
    * [teste_input.txt](test/teste_input.txt)
    * [teste_output.txt](test/teste_output.txt)

* [numeros.py](numeros.py)
    * Este ficheiro contem o nosso dicionário com os números e seu equivalente em texto e vice-versa

* [**tp1.py**](tp1.py)
    * Este ficheiro converte números inteiros, usando espaço como separador de milhares, para texto na forma que concluimos ser a mais correta em Português.

* [**tp1aLaEnunciado.py**](tp1aLaEnunciado.py)
    * Este ficheiro converte números inteiros, usando virgula como separador dos milhares, e anos, para texto de forma a ficar igual ao output que nos foi dado pelos professores.
    * Adicionalmente, tambem faz o processo inverso. Tambem converte de texto de volta para números, de forma a podermos obter o ficheiro original de input.

## Execução

* [**tp1.py**](tp1.py)
    * Basta apenas executar o ficheiro, e depois introduzir o valor a converter:
        ``` bash
        $ python3 tp1.py
        2 345
        dois mil trezentos e quarenta e cinco
        ```

* [**tp1aLaEnunciado.py**](tp1aLaEnunciado.py)
    * Basta apenas executar o ficheiro:
        ``` bash
        $ python3 tp1aLaEnunciado.py
        ```
    * Por default, estamos a converter o example_input.txt para texto e o example_output para digitos.