#!/usr/bin/python3
import re

texto = """ As mulheres estiveram em destaque nos prémios norte-americanos de música Grammy ao vencerem no domingo, em Los Angeles, nas categorias de Melhor Álbum do Ano e de Melhor Jovem Artista, enquanto o "rap" conquistou importantes troféus.

"Golden Hour", de Kacey Musgraves, venceu o Melhor Álbum do Ano e Dua Lipa ganhou o prémio de Melhor Jovem Artista.

Childish Gambino foi o grande vencedor da noite, recebendo quatro prémios, incluindo Melhor Videoclip e Melhor Desempenho Rap/Cantado."""

def cleanText(texto):
    texto = texto.lower()
    texto = re.sub(r"[ãâáà]",r"a",texto)
    texto = re.sub(r"[ç]",r"c",texto)
    texto = re.sub(r"[ú]",r"u",texto)
    texto = re.sub(r"(\w+)([,.!?])",r"\1 \2",texto)
    return texto

print(cleanText(texto))