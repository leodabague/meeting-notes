import streamlit as st
import openai
import anthropic
from pathlib import Path
from datetime import datetime
import os

def load_template():
    """Carrega o template de ata de reunião"""
    template_path = Path("template/meeting.md")
    if template_path.exists():
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def create_prompt(template, transcription, context):
    """Cria o prompt para a IA baseado no template"""
    prompt = f"""
{template}

## CONTEXTO DA REUNIÃO:
{context}

## TRANSCRIÇÃO:
{transcription}

---

Por favor, analise a transcrição da reunião acima e crie uma ata profissional em markdown seguindo exatamente o formato de saída desejado especificado no template. Mantenha o tom profissional e organize as informações de forma clara e concisa.
"""
    return prompt

def call_openai_api(api_key, prompt):
    """Faz chamada para API da OpenAI"""
    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4.1-mini-2025-04-14",
            messages=[
                {"role": "system", "content": "Você é um assistente especializado em criar atas de reunião profissionais e bem estruturadas."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=4000,
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro na API da OpenAI: {str(e)}"

def call_anthropic_api(api_key, prompt):
    """Faz chamada para API da Anthropic"""
    try:
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-3-7-sonnet-latest",
            max_tokens=4000,
            temperature=0.3,
            system="Você é um assistente especializado em criar atas de reunião profissionais e bem estruturadas.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"Erro na API da Anthropic: {str(e)}"



def main():
    st.set_page_config(
        page_title="Gerador de Atas de Reunião",
        page_icon="📝",
        layout="wide"
    )
    
    st.title("📝 Gerador de Atas de Reunião")
    st.markdown("---")
    
    # Sidebar para configurações
    with st.sidebar:
        st.header("⚙️ Configurações")
        
        # Debug: Verificar se template foi carregado
        template = load_template()
        if template:
            st.success(f"✅ Template carregado ({len(template)} caracteres)")
        else:
            st.error("❌ Template não encontrado")
        
        # Botão para visualizar template
        if st.button("👁️ Ver Template"):
            st.session_state.show_template = True
        
        # Seleção do provedor de IA
        ai_provider = st.selectbox(
            "Provedor de IA:",
            ["OpenAI", "Anthropic"],
            help="Escolha o provedor de inteligência artificial"
        )
        
        # Campo para API Key
        api_key = st.text_input(
            f"Chave da API {ai_provider}:",
            type="password",
            help=f"Insira sua chave da API do {ai_provider}"
        )
        
        st.markdown("---")
        st.markdown("### 📋 Instruções")
        st.markdown("""
        1. **Upload da transcrição** (arquivo .txt)
        2. **Adicione o contexto** da reunião
        3. **Configure sua API Key**
        4. **Clique em Gerar Ata**
        5. **Baixe o resultado** em markdown
        """)
    
    # Mostrar template se solicitado
    if hasattr(st.session_state, 'show_template') and st.session_state.show_template:
        st.header("📋 Template da Ata")
        template = load_template()
        if template:
            st.markdown("### Conteúdo do Template:")
            st.code(template, language="markdown")
        else:
            st.error("❌ Não foi possível carregar o template")
        
        if st.button("🔒 Fechar Template"):
            st.session_state.show_template = False
            st.rerun()
        st.markdown("---")
    
    # Área principal
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📤 Upload da Transcrição")
        
        # Upload do arquivo
        uploaded_file = st.file_uploader(
            "Selecione o arquivo de transcrição:",
            type=['txt'],
            help="Arquivo .txt contendo a transcrição da reunião"
        )
        
        transcription_text = ""
        if uploaded_file is not None:
            try:
                transcription_text = uploaded_file.read().decode('utf-8')
                st.success(f"✅ Arquivo carregado: {uploaded_file.name}")
                
                # Preview da transcrição
                with st.expander("👁️ Visualizar transcrição"):
                    st.text_area(
                        "Conteúdo do arquivo:",
                        transcription_text,
                        height=200,
                        disabled=True
                    )
            except Exception as e:
                st.error(f"❌ Erro ao ler arquivo: {str(e)}")
    
    with col2:
        # Área de contexto
        st.header("📋 Contexto da Reunião")
        context_text = st.text_area(
            "Cole aqui as informações do Google Calendar ou adicione contexto relevante:",
            height=150,
            placeholder="Ex: Reunião de planejamento semanal\nData: 15/01/2025\nParticipantes: João, Maria, Pedro\nObjetivo: Revisar metas do trimestre..."
        )
        
    # Geração da Ata | centralizada para usar o container wide
    st.header("🤖 Geração da Ata")
    
    # Botão para gerar ata
    if st.button("🚀 Gerar Ata de Reunião", type="primary", use_container_width=False):
        if not transcription_text:
            st.error("❌ Por favor, faça upload da transcrição primeiro!")
        elif not context_text.strip():
            st.error("❌ Por favor, adicione o contexto da reunião!")
        elif not api_key:
            st.error(f"❌ Por favor, adicione sua chave da API do {ai_provider}!")
        else:
            with st.spinner(f"🔄 Gerando ata usando {ai_provider}..."):
                # Carrega template
                template = load_template()
                
                # Cria prompt
                prompt = create_prompt(template, transcription_text, context_text)
                
                # Chama API
                if ai_provider == "OpenAI":
                    result = call_openai_api(api_key, prompt)
                else:  # Anthropic
                    result = call_anthropic_api(api_key, prompt)
                
                # Armazena resultado na sessão
                st.session_state.generated_ata = result
                st.session_state.generation_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    
        # Exibe resultado se existir
    if hasattr(st.session_state, 'generated_ata'):
        st.header("📄 Ata Gerada")
        
        # Botões de ação
        col_preview, col_download = st.columns([1, 1])
        
        with col_preview:
            show_preview = st.button("👁️ Visualizar Ata", use_container_width=True)
        
        with col_download:
            filename = f"ata_reuniao_{st.session_state.generation_time}.md"
            st.download_button(
                label="📥 Baixar Ata em Markdown",
                data=st.session_state.generated_ata,
                file_name=filename,
                mime="text/markdown",
                use_container_width=True
            )
        
        # Preview da ata
        if show_preview or 'show_ata' in st.session_state:
            st.session_state.show_ata = True
            
            st.markdown("### 📋 Preview da Ata:")
            st.markdown("---")
            st.markdown(st.session_state.generated_ata)
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 10px;'>
            🚀 Gerador de Atas de Reunião | Powered by AI
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main() 