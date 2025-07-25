# 📝 Gerador de Atas de Reunião

Uma aplicação Streamlit que utiliza inteligência artificial para gerar atas profissionais de reunião a partir de transcrições.

## 🚀 Funcionalidades

- **Upload de transcrições**: Carregue arquivos `.txt` com transcrições de reunião
- **Contexto personalizado**: Adicione informações do Google Calendar ou contexto relevante
- **Múltiplos provedores de IA**: Suporte para OpenAI (GPT-4) e Anthropic (Claude)
- **Template profissional**: Usa um template estruturado para gerar atas consistentes
- **Preview em tempo real**: Visualize a ata gerada diretamente na aplicação
- **Download em markdown**: Baixe a ata gerada em formato `.md`

## 🛠️ Instalação

1. **Clone ou baixe o projeto**
   ```bash
   git clone <repositorio>
   cd meeting-notes
   ```

2. **Instale as dependências**
   ```bash
   pip install -e .
   # ou
   uv sync
   ```

3. **Execute a aplicação**
   ```bash
   streamlit run main.py
   ```

## 📋 Como Usar

### 1. Configuração Inicial
- Abra a aplicação no navegador (geralmente `http://localhost:8501`)
- Na barra lateral, escolha o provedor de IA (OpenAI ou Anthropic)
- Insira sua chave de API correspondente

### 2. Upload da Transcrição
- Clique em "Browse files" na seção "Upload da Transcrição"
- Selecione um arquivo `.txt` contendo a transcrição da reunião
- Use o botão "Visualizar transcrição" para verificar o conteúdo

### 3. Adicionar Contexto
- Na seção "Contexto da Reunião", cole as informações do convite
- Inclua detalhes como:
  - Data e horário da reunião
  - Participantes
  - Objetivo da reunião
  - Agenda
  - Qualquer contexto relevante

### 4. Gerar Ata
- Clique no botão "🚀 Gerar Ata de Reunião"
- Aguarde o processamento pela IA
- Use "👁️ Visualizar Ata" para ver o resultado
- Clique em "📥 Baixar Ata em Markdown" para fazer download

## 🔑 Configuração de API Keys

### OpenAI
1. Acesse [platform.openai.com](https://platform.openai.com/)
2. Vá em "API Keys" no menu
3. Crie uma nova chave de API
4. Cole a chave na aplicação

### Anthropic
1. Acesse [console.anthropic.com](https://console.anthropic.com/)
2. Vá em "API Keys"
3. Crie uma nova chave de API
4. Cole a chave na aplicação

## 📄 Formato da Ata

A aplicação gera atas seguindo este formato estruturado:

- **Resumo Executivo**: Objetivo, tópicos principais, status e próxima reunião
- **Decisões Tomadas**: Tabela com decisões, responsáveis, contexto e impacto
- **Próximos Passos**: Lista de ações com responsáveis e prazos
- **Insights e Observações**: Oportunidades, riscos e métricas
- **Pontos em Aberto**: Questões pendentes com responsáveis
- **Datas Importantes**: Cronograma de eventos e prazos

## 📁 Estrutura do Projeto

```
meeting-notes/
├── main.py                    # Aplicação Streamlit principal
├── template/
│   └── meeting.md             # Template da ata de reunião
├── pyproject.toml             # Dependências do projeto
├── README.md                  # Este arquivo
└── uv.lock                    # Lock file das dependências
```

## 🔧 Requisitos Técnicos

- **Python**: ≥ 3.11
- **Streamlit**: ≥ 1.47.1
- **OpenAI**: ≥ 1.0.0 (opcional)
- **Anthropic**: ≥ 0.34.0 (opcional)

## 🚨 Importante

- **Chaves de API**: Nunca compartilhe suas chaves de API
- **Dados sensíveis**: Use com cuidado ao processar informações confidenciais
- **Custo**: Verifique os preços das APIs antes de usar extensivamente

## 📞 Suporte

Para problemas ou sugestões, verifique:
1. Se todas as dependências estão instaladas
2. Se a chave de API está correta
3. Se o arquivo de transcrição está no formato correto (.txt)

## 📜 Licença

MIT License - veja o arquivo `LICENSE` para detalhes.
