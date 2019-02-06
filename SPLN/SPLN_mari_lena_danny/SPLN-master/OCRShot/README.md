# OCRShot

O OCRShot é um filtro Unix que permite o pós-processamento de um texto retirado de uma imagem.

## Usage
Como argumentos do programa, o OCRshot recorre às seguintes \textit{flags}:

- **-i <image>** Imagem à qual se pretende aplicar OCR e cujo texto se deseja ser pós-processado. Argumento opcional, caso não seja especificado, o OCRShot permite tirar um *screenshot* a uma área livre no ecrã e usar essa imagem.
- **-p <type>** Tipo de pré-processamento a aplicar à imagem. O OCRshot permite dois tipos de pré-processamento: *thresh* para criar uma imagem binária a partir da original ou *blur* para a remoção de ruído. Argumento opcional, caso não seja especificado, nenhum pré-processamento será feito à imagem.
- **-l <language>** Linguagem do texto na imagem. Argumento opcional, por defeito assume que o texto da imagem se encontra em português. Os códigos a usar para a linguagem devem ser iguais aos usados pelo *pytesseract*.

## Authors

* [Daniel Fernandes](https://github.com/danielsf97)
* [Helena Poleri](https://github.com/helenapoleri)
* [Mariana Miranda](https://github.com/mmm97)