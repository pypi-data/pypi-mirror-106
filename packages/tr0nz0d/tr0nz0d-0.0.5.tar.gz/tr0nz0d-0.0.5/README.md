<h1>TR0NZ0D Lib</h1>
<hr>

<h3>O que é?</h3>
<p>TR0NZ0D Lib é uma biblioteca criada em python para facilitar a utilização de algumas ferramentas. O projeto ainda está em fase de desenvolvimento, aprimoramentos e novas funcionalidades serão adicionados.</p>

<h3>Breve Documentação</h3>

<h4>Introdução</h4>
<p>A Instalação da biblioteca pode ser feita executando o comando <code>pip install tr0nz0d</code> em um terminal que possua Python [3.8.x] instalado.</p>

<h4>Métodos</h4>
<h5><code>tr0nz0d.tools</code></h5>

- CPF
<small>Ferramentas para gerar, formatar e validar um cpf.</small>
    * <small>``cpf.gerar()`` - Gera um cpf matemáticamente válido.<br>**Retorna**
        - O cpf sem formatação.</small>
    * <small>``cpf.formatar(cpf: str)`` - Formata o cpf com as divisões.<br>**Retorna**
        - O cpf formatado.</small>
    * <small>``cpf.gerar_formatado()`` - Gera um cpf matemáticamente válido.<br>**Retorna**
        - O cpf formatado.</small>
    * <small>``cpf.validar()`` - Valida a autênticidade matemática do CPF.<br>**Retorna**
        - True [válido] ou False [inválido] </small>
- CNPJ
<small>Ferramentas para gerar, formatar e validar um cnpj.</small>
    * <small>``cnpj.gerar()`` - Gera um cnpj matemáticamente válido.<br>**Retorna**
        - O cnpj sem formatação.</small>
    * <small>``cnpj.formatar(cnpj: str)`` - Formata o cnpj com as divisões.<br>**Retorna**
        - O cnpj formatado.</small>
    * <small>``cnpj.gerar_formatado()`` - Gera um cnpj matemáticamente válido.<br>**Retorna**
        - O cnpj formatado.</small>
    * <small>``cnpj.validar()`` - Valida a autênticidade matemática do cnpj.<br>**Retorna**
        - True [válido] ou False [inválido] </small>
- TEXT
<small>Ferramentas para encapsular e imprimir um texto dentro de um conjunto de caracteres.</small>
    * <small>``text.line_print(texto: str, char_tl: str, char_md: str, char_tr: str, char_sides: str, char_bl: str, char_br: str)`` - Encapsula um texto de uma única linha dentro dos caracteres especificados e realiza um print na tela.</small>
    * <small>``text.text_print(texto: str, char_tl: str, char_md: str, char_tr: str, char_sides: str, char_bl: str, char_br: str)`` - Encapsula um texto de multiplas linhas dentro dos caracteres especificados e realiza um print na tela.</small>

<h5><code>tr0nz0d.security</code></h5>

- CRIPTOGRAFIA
<small>Ferramentas para criptografar e descriptografar um texto.</small>
    * <small>``criptografia.criptografar(text: str)`` - Criptografa o texto passado.<br>**Retorna**
        - Lista contendo o texto encriptado e a chave.</small>
    * <small>``criptografia.descriptografar(text: bytes)`` - Descriptografa o texto passado.<br>**Retorna**
        - Texto literal descriptografado.</small>
    * <small>``criptografia.descriptografar_com_chave(text: bytes, custom_key: bytes)`` - Descriptografa o texto passado utilizando a chave específica.<br>**Retorna**
        - Texto literal descriptografado.</small>
    * <small>``criptografia.get_key()`` - Retorna a chave utilizada na criptografia do texto.<br>**Retorna**
        - Chave de criptografia.</small>
- PSWD
<small>Ferramentas para criar senhas e códigos complexos.</small>
    * <small>``pass.gerar(lenght: int)`` - Cria um código complexo de comprimento determinado.<br>**Retorna**
        - O código criado em texto literal.</small>


<hr>