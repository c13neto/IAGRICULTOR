# IAGRICULTOR
### Escopo do projeto:
<dl>
  <dt> O IAgricultor é uma inteligência artificial (IA) focada no conhecimento da área de agricultura, com o objetivo de auxiliar fazendeiros no plantio e cultivo na região semiárida da Bahia. O agente será capaz de fazer recomendações, explicar técnicas, identificar problemas e melhorar o desempenho das plantações</dt>
</dl>

***
### O modelo foi:
- Treinado com Biblioteca da Embrapa
- Utilizado técnicas de fine-tuning e engenharia de prompt
- Uso de RAG para aumento do repertório

***

### Utilização:
1. Utilize o [Colab Google](https://colab.research.google.com/) como máquina virtual para conseguir perfomance aceitavel.
2. Em seguida copie o seguinte código dentro do primeiro bloco:

```
!pip install colab-xterm pyexcel_ods
%load_ext colabxterm
%xterm
!curl -fsSL https://ollama.com/install.sh | sh
!nohup ollama serve &
```