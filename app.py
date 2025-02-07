import streamlit as st
from fpdf import FPDF
import tempfile


# Função para gerar o arquivo .txt
def gerar_txt(resultados):
    with open("relatorio.txt", "w") as file:
        for key, value in resultados.items():
            file.write(f"{key}: {value}\n")
    return "relatorio.txt"

# Função para gerar o arquivo .pdf
def gerar_pdf(resultados, fotos):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Relatório de acessibilidade", ln=True, align='C')
    pdf.ln(10)
    
    for key, value in resultados.items():
        pdf.multi_cell(0, 10, f"{key}: {value}")
        pdf.ln(5)
        if key in fotos and fotos[key]:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                temp_file.write(fotos[key].getbuffer())
                temp_file_path = temp_file.name
            pdf.image(temp_file_path, x=10, w=100)
            pdf.ln(5)
    
    pdf_file = "relatorio.pdf"
    pdf.output(pdf_file)
    return pdf_file

# Função para criar as perguntas e salvar as respostas
def perguntas():
    resultados = {}
    fotos = {}

    # Tópico 0: Passeio circundante ao lote
    with st.expander("## **0.0 Passeio circundante ao lote**"):
        # Pergunta 0.1
        projeto_arquitetonico = st.checkbox("O projeto arquitetônico e/ou o croqui do laudo topográfico não apresentam as cotas da calçada. (Lei n.º 6.138/2018, art. 40 e Decreto n.º 43.056/2022, art. 4, inciso V, b)", 
                                        key="0projeto_arquitetonico")
        if projeto_arquitetonico:
            resultados["0.1 Projeto Arquitetônico"] = "O projeto arquitetônico e/ou o croqui do laudo topográfico não apresentam as cotas da calçada. (Lei n.º 6.138/2018, art. 40 e Decreto n.º 43.056/2022, art. 4, inciso V, b)"
            fotos["0.1 Projeto Arquitetônico"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_projeto_arquitetonico")

        # Pergunta 0.2
        largura_calcada = st.checkbox("Em caso de calçadas com lagura mmaior que 2m. A largura da calçada é inferior a 2,00m, não sendo possível executar a faixa de serviço com largura mínima de 0,70m e o passeio com largura mínima de 1,20m (ABNT NBR 9050:2020 - item 6.12.3)", 
                                    key="0largura_calcada")
        if largura_calcada:
            resultados["0.2 Largura da Calçada"] = "A largura da calçada é inferior a 2,00m, não sendo possível executar a faixa de serviço com largura mínima de 0,70m e o passeio com largura mínima de 1,20m (ABNT NBR 9050:2020 - item 6.12.3)"
            fotos["0.2 Largura da Calçada"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_largura_calcada")

        # Pergunta 0.3
        largura_minima_passeio = st.checkbox("O passeio não foi executado com a largura mínima de 1,20m (ABNT NBR 9050:2020 - item 6.12.3)", 
                                            key="0largura_minima_passeio")
        if largura_minima_passeio:
            resultados["0.3 Largura Mínima do Passeio"] = "O passeio não foi executado com a largura mínima de 1,20m (ABNT NBR 9050:2020 - item 6.12.3)"
            fotos["0.3 Largura Mínima do Passeio"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_largura_minima_passeio")

        # Pergunta 0.4
        falta_passeio = st.checkbox("Falta executar o passeio circundante ao lote, ou trecho dele (Lei nº 6.758/2020)", 
                                    key="0falta_passeio")
        if falta_passeio:
            resultados["0.4 Falta Passeio Circundante"] = "Falta executar o passeio circundante ao lote, ou trecho dele (Lei nº 6.758/2020)"
            fotos["0.4 Falta Passeio Circundante"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_falta_passeio")

        # Pergunta 0.5
        inclinacao_transversal = st.checkbox("A inclinação transversal do passeio está acima de 3% (ABNT NBR 9050:2020 - item 6.12.1)", 
                                            key="0inclinacao_transversal")
        if inclinacao_transversal:
            resultados["0.5 Inclinação Transversal do Passeio"] = "A inclinação transversal do passeio está acima de 3% (ABNT NBR 9050:2020 - item 6.12.1)"
            fotos["0.5 Inclinação Transversal do Passeio"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_inclinacao_transversal")

        # Pergunta 0.6
        passeio_declividade = st.checkbox("O passeio não acompanha a declividade da via, no sentido longitudinal e não está no nível do meio-fio (ABNT NBR 9050:2020 - item 6.12.1)", 
                                        key="0passeio_declividade")
        if passeio_declividade:
            resultados["0.6 Passeio e Declividade"] = "O passeio não acompanha a declividade da via, no sentido longitudinal e não está no nível do meio-fio (ABNT NBR 9050:2020 - item 6.12.1)"
            fotos["0.6 Passeio e Declividade"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_passeio_declividade")

        # Pergunta 0.7
        passeio_superficie_irregular = st.checkbox("O passeio possui superfície irregular e/ou com desnível e/ou trepidante para dispositivos com rodas (ABNT NBR 9050:2020 - itens 6.3.2 e 6.3.4.1)", 
                                                key="0passeio_superficie_irregular")
        if passeio_superficie_irregular:
            resultados["0.7 Superfície Irregular do Passeio"] = "O passeio possui superfície irregular e/ou com desnível e/ou trepidante para dispositivos com rodas (ABNT NBR 9050:2020 - itens 6.3.2 e 6.3.4.1)"
            fotos["0.7 Superfície Irregular do Passeio"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_passeio_superficie_irregular")

        # Pergunta 0.8
        passeio_superficie_derrapante = st.checkbox("O passeio possui superfície derrapante (ABNT NBR 9050:2020 - item 6.3.2)", 
                                                    key="0passeio_superficie_derrapante")
        if passeio_superficie_derrapante:
            resultados["0.8 Superfície Derrapante do Passeio"] = "O passeio possui superfície derrapante (ABNT NBR 9050:2020 - item 6.3.2)"
            fotos["0.8 Superfície Derrapante do Passeio"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_passeio_superficie_derrapante")

        # Pergunta 0.9
        dimensao_vaos_grelhas = st.checkbox("Os vãos das grelhas no passeio estão com dimensão superior a 1,5 cm e/ou a grelha não está nivelada com o piso e/ou não está firme ou estável (ABNT NBR 9050:2020 - item 6.3.5)", 
                                            key="0dimensao_vaos_grelhas")
        if dimensao_vaos_grelhas:
            resultados["0.9 Dimensão dos Vãos das Grelhas"] = "Os vãos das grelhas no passeio estão com dimensão superior a 1,5 cm e/ou a grelha não está nivelada com o piso e/ou não está firme ou estável (ABNT NBR 9050:2020 - item 6.3.5)"
            fotos["0.9 Dimensão dos Vãos das Grelhas"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_dimensao_vaos_grelhas")

        # Pergunta 0.10
        tampas_caixa_inspecao = st.checkbox("As tampas de caixa de inspeção ou de visita não estão niveladas com o piso e/ou suas frestas estão com dimensão maior de 1,50cm e/ou não estão firmes ou estáveis (ABNT NBR 9050:2020 - item 6.3.6)", 
                                            key="0tampas_caixa_inspecao")
        if tampas_caixa_inspecao:
            resultados["0.10 Tampas de Caixa de Inspeção"] = "As tampas de caixa de inspeção ou de visita não estão niveladas com o piso e/ou suas frestas estão com dimensão maior de 1,50cm e/ou não estão firmes ou estáveis (ABNT NBR 9050:2020 - item 6.3.6)"
            fotos["0.10 Tampas de Caixa de Inspeção"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_tampas_caixa_inspecao")

        # Pergunta 0.11
        desnivel_espaco_0_18 = st.checkbox("Em trechos do passeio junto a desníveis de altura igual ou acima de 0,18 m falta espaço com no mínimo 0,60 m de largura entre a faixa de circulação de pedestres e o desnível ou falta mureta de proteção contra a queda, com altura mínima de 0,15 m e com a cor contrastante com a cor do caminho (ABNT NBR 9050:2020 - itens 4.3.7.1 e 4.3.7.2)", 
                                        key="0desnivel_espaco_0_18")
        if desnivel_espaco_0_18:
            resultados["0.11 Desnível e Mureta de Proteção"] = "Em trechos do passeio junto a desníveis de altura igual ou acima de 0,18 m falta espaço com no mínimo 0,60 m de largura entre a faixa de circulação de pedestres e o desnível ou falta mureta de proteção contra a queda, com altura mínima de 0,15 m e com a cor contrastante com a cor do caminho (ABNT NBR 9050:2020 - itens 4.3.7.1 e 4.3.7.2)"
            fotos["0.11 Desnível e Mureta de Proteção"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_desnivel_espaco_0_18")

        # Pergunta 0.12
        desnivel_espaco_0_60 = st.checkbox("Em trechos do passeio junto a desníveis de altura superior a 0,60 m, falta guarda-corpo com altura de 1,05 m ao longo da circulação de pedestres (ABNT NBR 9050:2020 - item 4.3.7.3)", 
                                        key="0desnivel_espaco_0_60")
        if desnivel_espaco_0_60:
            resultados["0.12 Desnível e Guarda-Corpo"] = "Em trechos do passeio junto a desníveis de altura superior a 0,60 m, falta guarda-corpo com altura de 1,10 m ao longo da circulação de pedestres (ABNT NBR 9050:2020 - item 4.3.7.3)"
            fotos["0.12 Desnível e Guarda-Corpo"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_desnivel_espaco_0_60")

        # Pergunta 0.13
        obstaculo_pontual = st.checkbox("O passeio possui obstáculo pontual implantado pelo proprietário sem garantir uma largura livre mínima de 0,90 m (ABNT NBR 9050:2020 - item 4.3.2)", 
                                        key="0obstaculo_pontual")
        if obstaculo_pontual:
            resultados["0.13 Obstáculo Pontual no Passeio"] = "O passeio possui obstáculo pontual implantado pelo proprietário sem garantir uma largura livre mínima de 0,90 m (ABNT NBR 9050:2020 - item 4.3.2)"
            fotos["0.13 Obstáculo Pontual no Passeio"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_obstaculo_pontual")

        # Pergunta 0.14
        elementos_interferindo_passeio = st.checkbox("Existem elementos interferindo no passeio com altura inferior a 2,10 m (toldos, placas informativas, galhos de árvore, etc) (ABNT NBR 9050:2020 - item 6.12.3)", 
                                                    key="0elementos_interferindo_passeio")
        if elementos_interferindo_passeio:
            resultados["0.14 Elementos Interferindo no Passeio"] = "Existem elementos interferindo no passeio com altura inferior a 2,10 m (toldos, placas informativas, galhos de árvore, etc) (ABNT NBR 9050:2020 - item 6.12.3)"
            fotos["0.14 Elementos Interferindo no Passeio"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_elementos_interferindo_passeio")

        # Pergunta 0.15
        interrupcao_passeio_acesso_veiculo = st.checkbox("Nos locais de acesso de veículo ao lote, existe interrupção do passeio ou desnível. (O passeio não pode ter rebaixamento e nem elevado para acesso de veículo e deve acompanhar a declividade da via no sentido longitudinal) (ABNT NBR 9050:2020 - item 6.12.4)", 
                                                        key="0interrupcao_passeio_acesso_veiculo")
        if interrupcao_passeio_acesso_veiculo:
            resultados["0.15 Interrupção do Passeio para Acesso de Veículo"] = "Nos locais de acesso de veículo ao lote, existe interrupção do passeio ou desnível. (O passeio não pode ter rebaixamento e nem elevado para acesso de veículo e deve acompanhar a declividade da via no sentido longitudinal) (ABNT NBR 9050:2020 - item 6.12.4)"
            fotos["0.15 Interrupção do Passeio para Acesso de Veículo"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_interrupcao_passeio_acesso_veiculo")

        # Pergunta 0.16
        largura_minima_acesso_veiculo = st.checkbox("Nos locais de acesso de veículo ao lote, o passeio não possui largura mínima de 1,20m (ABNT NBR 9050:2020 - item 6.12.4)", 
                                                    key="0largura_minima_acesso_veiculo")
        if largura_minima_acesso_veiculo:
            resultados["0.16 Largura Mínima de Acesso de Veículo"] = "Nos locais de acesso de veículo ao lote, o passeio não possui largura mínima de 1,20m (ABNT NBR 9050:2020 - item 6.12.4)"
            fotos["0.16 Largura Mínima de Acesso de Veículo"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_largura_minima_acesso_veiculo")

        # Pergunta 0.17
        inclinacao_transversal_acesso_veiculo = st.checkbox("Nos locais de acesso de veículo ao lote, o passeio tem inclinação transversal superior a 3% (ABNT NBR 9050:2020 - item 6.12.4)", 
                                                        key="0inclinacao_transversal_acesso_veiculo")
        if inclinacao_transversal_acesso_veiculo:
            resultados["0.17 Inclinação Transversal de Acesso de Veículo"] = "Nos locais de acesso de veículo ao lote, o passeio tem inclinação transversal superior a 3% (ABNT NBR 9050:2020 - item 6.12.4)"
            fotos["0.17 Inclinação Transversal de Acesso de Veículo"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_inclinacao_transversal_acesso_veiculo")

        # Pergunta 0.18
        portao_abre_sobre_passeio = st.checkbox("O portão de acesso à garagem abre sobre a faixa livre de circulação de pedestre (ABNT NBR 9050:2020 - item 6.15)", 
                                            key="0portao_abre_sobre_passeio")
        if portao_abre_sobre_passeio:
            resultados["0.18 Portão de Acesso à Garagem"] = "O portão de acesso à garagem abre sobre a faixa livre de circulação de pedestre (ABNT NBR 9050:2020 - item 6.15)"
            fotos["0.18 Portão de Acesso à Garagem"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_portao_abre_sobre_passeio")

        # Pergunta 0.19
        alarme_saida_garagem = st.checkbox("Falta instalar o alarme de saída de garagem de edificação de uso público ou coletivo (ABNT NBR 9050:2020 - item 5.6.4.2)", 
                                        key="0alarme_saida_garagem")
        if alarme_saida_garagem:
            resultados["0.19 Alarme de Saída de Garagem"] = "Falta instalar o alarme de saída de garagem de edificação de uso público ou coletivo (ABNT NBR 9050:2020 - item 5.6.4.2)"
            fotos["0.19 Alarme de Saída de Garagem"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_alarme_saida_garagem")

        # Pergunta 0.20
        rampa_acesso_nao_atende_legislacao = st.checkbox("A rampa de pedestre, localizada em área pública, para acesso a edificação não atende a legislação de acessibilidade (edificação de uso público ou coletivo) (ABNT NBR 9050:2020 - item 6.6)", 
                                                        key="0rampa_acesso_nao_atende_legislacao")
        if rampa_acesso_nao_atende_legislacao:
            resultados["0.20 Rampa de Acesso de Pedestre"] = "A rampa de pedestre, localizada em área pública, para acesso a edificação não atende a legislação de acessibilidade (edificação de uso público ou coletivo) (ABNT NBR 9050:2020 - item 6.6)"
            fotos["0.20 Rampa de Acesso de Pedestre"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_rampa_acesso_nao_atende_legislacao")

        # Pergunta 0.21
        escada_nao_atende_legislacao = st.checkbox("A escada, localizada em área pública, para acesso a edificação não atende a legislação de acessibilidade (edificação de uso público ou coletivo) (ABNT NBR 9050:2020 - item 6.7)", 
                                                key="0escada_nao_atende_legislacao")
        if escada_nao_atende_legislacao:
            resultados["0.21 Escada de Acesso"] = "A escada, localizada em área pública, para acesso a edificação não atende a legislação de acessibilidade (edificação de uso público ou coletivo) (ABNT NBR 9050:2020 - item 6.7)"
            fotos["0.21 Escada de Acesso"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_escada_nao_atende_legislacao")

        # Pergunta 0.22
        abertura_janelas_faixa_circulacao = st.checkbox("Abertura de janelas, com altura inferior a 2,10m, incidindo sobre a faixa de circulação (ABNT NBR 9050:2020 - item 6.2.3)", 
                                                        key="0abertura_janelas_faixa_circulacao")
        if abertura_janelas_faixa_circulacao:
            resultados["0.22 Abertura de Janelas"] = "Abertura de janelas, com altura inferior a 2,10m, incidindo sobre a faixa de circulação (ABNT NBR 9050:2020 - item 6.2.3)"
            fotos["0.22 Abertura de Janelas"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_abertura_janelas_faixa_circulacao")

        # Pergunta 0.23
        rampa_acesso_veiculo_nao_deve_avancar = st.checkbox("A rampa para acesso de veículos não pode avançar sobre a área de circulação de veículos (asfalto). A rampa deve ser feita na faixa de serviço da calçada com largura de até 0,70m. Retirar cunha (rampa) construída na caixa da via (Decreto 38.047/2017 - artigo 10, inciso VI)", 
                                                            key="0rampa_acesso_veiculo_nao_deve_avancar")
        if rampa_acesso_veiculo_nao_deve_avancar:
            resultados["0.23 Rampa de Acesso de Veículo"] = "A rampa para acesso de veículos não pode avançar sobre a área de circulação de veículos (asfalto). A rampa deve ser feita na faixa de serviço da calçada com largura de até 0,70m. Retirar cunha (rampa) construída na caixa da via (Decreto 38.047/2017 - artigo 10, inciso VI)"
            fotos["0.23 Rampa de Acesso de Veículo"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_rampa_acesso_veiculo_nao_deve_avancar")

        # Pergunta 0.24
        dois_portoes_acesso_veiculo = st.checkbox("Existem dois ou mais portões de acesso de veículos ao lote (Decreto 38.047/2017 - artigo 10, inciso I)", 
                                                key="0dois_portoes_acesso_veiculo")
        if dois_portoes_acesso_veiculo:
            resultados["0.24 Dois Portões de Acesso de Veículo"] = "Existem dois ou mais portões de acesso de veículos ao lote (Decreto 38.047/2017 - artigo 10, inciso I)"
            fotos["0.24 Dois Portões de Acesso de Veículo"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_dois_portoes_acesso_veiculo")

        # Pergunta 0.25
        pisotatil_alerta_nao_conforme = st.checkbox("O piso tátil de alerta não tem relevo contrastante e/ou contraste de luminância em relação ao piso adjacente, para ser percebida por pessoas com baixa visão (ABNT NBR 16537:2024 - item 6.2)", 
                                                    key="0pisotatil_alerta_nao_conforme")
        if pisotatil_alerta_nao_conforme:
            resultados["0.25 Piso Tátil de Alerta"] = "O piso tátil de alerta não tem relevo contrastante e/ou contraste de luminância em relação ao piso adjacente, para ser percebida por pessoas com baixa visão (ABNT NBR 16537:2024 - item 6.2)"
            fotos["0.25 Piso Tátil de Alerta"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="0foto_pisotatil_alerta_nao_conforme")




    # Tópico 1: Condições gerais de acesso e circulação - Rota acessível
    with st.expander("## **1.0 Condições gerais de acesso e circulação - Rota acessível**"):
        # Pergunta 1
        calçada = st.checkbox("Não existe calçada com, no mínimo, 1.20m de largura interligando as edificações dentro do lote (ABNT NBR 9050:2020 - itens 6.1.1.1 e 6.1.1.2)",
                              key="calçada")
        if calçada:
            resultados["1.1 Calçada"] = "Não existe calçada com, no mínimo, 1.20m de largura interligando as edificações dentro do lote (ABNT NBR 9050:2020 - itens 6.1.1.1 e 6.1.1.2)"
            fotos["1. Calçada"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_calçada")

        # Pergunta 2
        inclinacao_externa = st.checkbox("A inclinação transversal do piso externo está acima de 3% (ABNT NBR 9050:2020 - item 6.3.3)",
                                        key="inclinacao_externa")
        if inclinacao_externa:
            resultados["1.2 Inclinação Externa"] = "A inclinação transversal do piso externo está acima de 3% (ABNT NBR 9050:2020 - item 6.3.3)"
            fotos["2. Inclinação Externa"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_inclinacao_externa")

        # Pergunta 3
        inclinacao_interna = st.checkbox("A inclinação transversal do piso interno está acima de 3% (ABNT NBR 9050:2020 - item 6.3.3)",
                                        key="inclinacao_interna")
        if inclinacao_interna:
            resultados["1.3 Inclinação Interna"] = "A inclinação transversal do piso interno está acima de 3% (ABNT NBR 9050:2020 - item 6.3.3)"
            fotos["3. Inclinação Interna"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_inclinacao_interna")
        
        # Pergunta 4
        inclinacao_longitudinal = st.checkbox("A inclinação longitudinal do piso é igual ou superior a 5% e não está acessível (rampa)? (ABNT NBR 9050:2020 - item 6.6.1)",
                                            key="inclinacao_longitudinal")
        if inclinacao_longitudinal:
            resultados["1.4 Inclinação Longitudinal"] = "A inclinação longitudinal do piso é igual ou superior a 5% e não está acessível (rampa) (ABNT NBR 9050:2020 - item 6.6.1)."
            fotos["1. Inclinação Longitudinal"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_inclinacao_longitudinal")

        # Pergunta 5
        superficie_irregular = st.checkbox("A calçada, no interior do lote, possui superfície irregular e/ou com desnível e/ou trepidante para dispositivos com rodas? (ABNT NBR 9050:2020 - itens 6.3.2 e 6.3.4.1)",
                                        key="superficie_irregular")
        if superficie_irregular:
            resultados["1.5 Superfície Irregular"] = "A calçada, no interior do lote, possui superfície irregular e/ou com desnível e/ou trepidante para dispositivos com rodas? (ABNT NBR 9050:2020 - itens 6.3.2 e 6.3.4.1)"
            fotos["2. Superfície Irregular"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_superficie_irregular")

        # Pergunta 6
        superficie_derrapante = st.checkbox("A calçada, no interior do lote, possui superfície derrapante? (ABNT NBR 9050:2020 - item 6.3.2)",
                                        key="superficie_derrapante")
        if superficie_derrapante:
            resultados["1.6 Superfície Derrapante"] = "A calçada, no interior do lote, possui superfície derrapante? (ABNT NBR 9050:2020 - item 6.3.2)"
            fotos["3. Superfície Derrapante"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_superficie_derrapante")

        # Pergunta 7
        piso_tatil_alerta = st.checkbox("O piso tátil de alerta não tem relevo contrastante e/ou contraste de luminância em relação ao piso adjacente, para ser percebido por pessoas com baixa visão? (ABNT NBR 16537:2024 - item 6.2)",
                                    key="piso_tatil_alerta")
        if piso_tatil_alerta:
            resultados["1.7 Piso Tátil de Alerta"] = "O piso tátil de alerta não tem relevo contrastante e/ou contraste de luminância em relação ao piso adjacente, para ser percebido por pessoas com baixa visão? (ABNT NBR 16537:2024 - item 6.2)"
            fotos["4. Piso Tátil de Alerta"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_piso_tatil_alerta")

        # Pergunta 8
        abertura_janelas = st.checkbox("Abertura de janelas, com altura inferior a 2,10m, incidindo sobre a faixa de circulação? (ABNT NBR 9050:2020 - item 6.2.3)",
                                    key="abertura_janelas")
        if abertura_janelas:
            resultados["1.8 Abertura de Janelas"] = "Abertura de janelas, com altura inferior a 2,10m, incidindo sobre a faixa de circulação? (ABNT NBR 9050:2020 - item 6.2.3)"
            fotos["5. Abertura de Janelas"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_abertura_janelas")

        # Pergunta 9
        dispositivos_segurança = st.checkbox("Dispositivos de segurança e para controle de acesso (catraca, cancela, portas ou outros) não é acessível e/ou não prevê manobra de cadeira de rodas? (ABNT NBR 9050:2020 - itens 6.2.5, 6.2.6 e 9.4.1)",
                                            key="dispositivos_segurança")
        if dispositivos_segurança:
            resultados["1.9 Dispositivos de Segurança"] = "Dispositivos de segurança e para controle de acesso (catraca, cancela, portas ou outros) não é acessível e/ou não prevê manobra de cadeira de rodas? (ABNT NBR 9050:2020 - itens 6.2.5, 6.2.6 e 9.4.1)"
            fotos["6. Dispositivos de Segurança"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_dispositivos_segurança")

        # Pergunta 10
        desnivel_piso = st.checkbox("Há desníveis no piso da circulação ou nas soleiras entre 0,5 cm e 2,0 cm que não possuem acabamento chanfrado na proporção de 1:2? (ABNT NBR 9050:2020 - item 6.3.4)",
                                key="desnivel_piso")
        if desnivel_piso:
            resultados["1.10 Desnível Piso"] = "Há desníveis no piso da circulação ou nas soleiras entre 0,5 cm e 2,0 cm que não possuem acabamento chanfrado na proporção de 1:2. (ABNT NBR 9050:2020 - item 6.3.4)"
            fotos["7. Desnível Piso"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_desnivel_piso")

        # Pergunta 11
        desnivel_superior = st.checkbox("Há desnível superior a 2,0 cm não associado à rampa? (Desnível superior a 2,0 cm é considerado degrau isolado) (ABNT NBR 9050:2020 - item 6.3.4)",
                                    key="desnivel_superior")
        if desnivel_superior:
            resultados["1.11 Desnível Superior"] = "Há desnível superior a 2,0 cm não associado à rampa. (Desnível superior a 2,0 cm é considerado degrau isolado) (ABNT NBR 9050:2020 - item 6.3.4)"
            fotos["8. Desnível Superior"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_desnivel_superior")

        # Pergunta 12
        circulacao_chuva = st.checkbox("Circulação, sujeita a chuva, não tem piso antiderrapante? (ABNT NBR 9050:2020 - item 6.3.2)",
                                    key="circulacao_chuva")
        if circulacao_chuva:
            resultados["1.12 Circulação Chuva"] = "Circulação, sujeita a chuva, não tem piso antiderrapante. (ABNT NBR 9050:2020 - item 6.3.2)"
            fotos["9. Circulação Chuva"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_circulacao_chuva")

        # Pergunta 13
        grellas_passeio = st.checkbox("Os vãos das grelhas no passeio estão com dimensão superior a 1,5 cm e/ou a grelha não está nivelada com o piso e/ou não está firme ou estável? (ABNT NBR 9050:2020 - item 6.3.5)",
                                    key="grellas_passeio")
        if grellas_passeio:
            resultados["1.13 Grelhas Passeio"] = "Os vãos das grelhas no passeio estão com dimensão superior a 1,5 cm e/ou a grelha não está nivelada com o piso e/ou não está firme ou estável? (ABNT NBR 9050:2020 - item 6.3.5)"
            fotos["10. Grelhas Passeio"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_grellas_passeio")

        # Pergunta 14
        tampas_caixa = st.checkbox("As tampas de caixa de inspeção ou de visita não estão niveladas com o piso e/ou suas frestas estão com dimensão maior de 1,50m e/ou não estão firmes ou estáveis? (ABNT NBR 9050:2020 - item 6.3.6)",
                                key="tampas_caixa")
        if tampas_caixa:
            resultados["1.14 Tampas Caixa"] = "As tampas de caixa de inspeção ou de visita não estão niveladas com o piso e/ou suas frestas estão com dimensão maior de 1,50m e/ou não estão firmes ou estáveis? (ABNT NBR 9050:2020 - item 6.3.6)"
            fotos["11. Tampas Caixa"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_tampas_caixa")

        # Pergunta 15
        capachos_fixados = st.checkbox("Os capachos não estão firmemente fixados ao piso e/ou embutidos ou sobrepostos e nivelados de maneira que eventual desnível exceda 5 mm? (ABNT NBR 9050:2020 - item 6.3.7)",
                                    key="capachos_fixados")
        if capachos_fixados:
            resultados["1.15 Capachos Fixados"] = "Os capachos não estão firmemente fixados ao piso e/ou embutidos ou sobrepostos e nivelados de maneira que eventual desnível exceda 5 mm. (ABNT NBR 9050:2020 - item 6.3.7)"
            fotos["12. Capachos Fixados"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_capachos_fixados")
        
        # Verificação de elementos suspensos ou fixados
        elementos_suspendidos = st.checkbox("Existem elementos suspensos ou fixados em parede/teto/piso (extintores, toldos, vigas, luminárias, arandelas, etc.) com altura entre 0,60m a 2,10m, em áreas de circulação (ABNT NBR 9050:2020 - item 4.3.3 e ABNT NBR 16537:2024 - item 6.8)", key="elementos_suspendidos")
        if elementos_suspendidos:
            resultados["1.16 Elementos Suspensos"] = "Existem elementos suspensos ou fixados em parede/teto/piso (extintores, toldos, vigas, luminárias, arandelas, etc.) com altura entre 0,60m a 2,10m, em áreas de circulação (ABNT NBR 9050:2020 - item 4.3.3 e ABNT NBR 16537:2024 - item 6.8)"
            fotos["13. Elementos Suspensos"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_elementos_suspendidos")

        # Verificação de portas com vão livre inadequado
        portas_vão_inadequado = st.checkbox("As portas não possuem vão livre mínimo de 0,80m de largura e 2,10m de altura (ABNT NBR 9050:2020 - item 6.11.2.4)", key="portas_vão_inadequado")
        if portas_vão_inadequado:
            resultados["1.17 Portas com Vão Livre Inadequado"] = "As portas não possuem vão livre mínimo de 0,80m de largura e 2,10m de altura (ABNT NBR 9050:2020 - item 6.11.2.4)"
            fotos["14. Portas com Vão Livre Inadequado"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_portas_vão_inadequado")

        # Verificação de maçanetas de portas
        macanetas_inadequadas = st.checkbox("Maçanetas de portas não são do tipo alavanca, com pelo menos 100 mm de comprimento e acabamento sem arestas e recurvado na extremidade, e/ou não estão instaladas a uma altura entre 0,80 m e 1,10 m (ABNT NBR 9050:2020 - itens 4.6.6.1 e 6.11.2.6)", key="macanetas_inadequadas")
        if macanetas_inadequadas:
            resultados["1.18 Maçanetas de Portas Inadequadas"] = "Maçanetas de portas não são do tipo alavanca, com pelo menos 100 mm de comprimento e acabamento sem arestas e recurvado na extremidade, e/ou não estão instaladas a uma altura entre 0,80 m e 1,10 m (ABNT NBR 9050:2020 - itens 4.6.6.1 e 6.11.2.6)"
            fotos["15. Maçanetas de Portas Inadequadas"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_macanetas_inadequadas")

        # Verificação de puxador vertical inadequado
        puxador_vertical_inadequado = st.checkbox("Puxador vertical de portas não tem no mínimo 0,30m de comprimento e/ou não está instalado à altura entre 0,80m e 1,10m do piso e/ou não está afastado 0,10 m do batente (ABNT NBR 9050:2020 - item 4.6.6.2)", key="puxador_vertical_inadequado")
        if puxador_vertical_inadequado:
            resultados["1.19 Puxador Vertical Inadequado"] = "Puxador vertical de portas não tem no mínimo 0,30m de comprimento e/ou não está instalado à altura entre 0,80m e 1,10m do piso e/ou não está afastado 0,10 m do batente (ABNT NBR 9050:2020 - item 4.6.6.2)"
            fotos["16. Puxador Vertical Inadequado"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_puxador_vertical_inadequado")

        # Verificação de puxador horizontal inadequado
        puxador_horizontal_inadequado = st.checkbox("Puxador horizontal de portas não tem no mínimo 0,40 m de comprimento e/ou não está instalado na altura da maçaneta e/ou não está afastado 0,10 m do batente (do lado das dobradiças) (ABNT NBR 9050:2020 - item 4.6.6.3)", key="puxador_horizontal_inadequado")
        if puxador_horizontal_inadequado:
            resultados["1.20 Puxador Horizontal Inadequado"] = "Puxador horizontal de portas não tem no mínimo 0,40 m de comprimento e/ou não está instalado na altura da maçaneta e/ou não está afastado 0,10 m do batente (do lado das dobradiças) (ABNT NBR 9050:2020 - item 4.6.6.3)"
            fotos["17. Puxador Horizontal Inadequado"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_puxador_horizontal_inadequado")

        # Verificação de rota acessível com obstáculo
        rota_com_obstaculo = st.checkbox("A rota acessível possui obstáculo isolado, sem garantir uma largura livre mínima de 0,90 m (ABNT NBR 9050:2020 - item 4.3.2)", key="rota_com_obstaculo")
        if rota_com_obstaculo:
            resultados["1.21 Rota Acessível com Obstáculo"] = "A rota acessível possui obstáculo isolado, sem garantir uma largura livre mínima de 0,90 m (ABNT NBR 9050:2020 - item 4.3.2)"
            fotos["18. Rota Acessível com Obstáculo"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_rota_com_obstaculo")

        # Verificação de trilho ou guia inferior da porta de correr
        trilho_ou_guia_inadequado = st.checkbox("Trilho ou guia inferior da porta de correr não está nivelado com a superfície do piso ou a fresta resultante da guia inferior possui largura superior a 15 mm (ABNT NBR 9050:2020 - item 6.11.2.11)", key="trilho_ou_guia_inadequado")
        if trilho_ou_guia_inadequado:
            resultados["1.22 Trilho ou Guia Inadequado"] = "Trilho ou guia inferior da porta de correr não está nivelado com a superfície do piso ou a fresta resultante da guia inferior possui largura superior a 15 mm (ABNT NBR 9050:2020 - item 6.11.2.11)"
            fotos["19. Trilho ou Guia Inadequado"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_trilho_ou_guia_inadequado")

        # Verificação de balcão de atendimento inadequado
        balcao_inadequado = st.checkbox("Balcão de atendimento não possui largura mínima de 0,90 m e/ou altura entre 0,75 m e 0,85 m do piso acabado (ABNT NBR 9050:2020 - item 9.2.1.4)", key="balcao_inadequado")
        if balcao_inadequado:
            resultados["21.3 Balcão de Atendimento Inadequado"] = "Balcão de atendimento não possui largura mínima de 0,90 m e/ou altura entre 0,75 m e 0,85 m do piso acabado (ABNT NBR 9050:2020 - item 9.2.1.4)"
            fotos["20. Balcão de Atendimento Inadequado"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_balcao_inadequado")

        # Verificação de escoamento de águas pluviais
        escoamento_inadequado = st.checkbox("Escoamento de águas pluviais de coberturas diretamente para área pública ou para lotes e projeções vizinhas (Lei 6.138/2018 - artigo 97)", key="escoamento_inadequado")
        if escoamento_inadequado:
            resultados["21. Escoamento de Águas Pluviais Inadequado"] = "Escoamento de águas pluviais de coberturas diretamente para área pública ou para lotes e projeções vizinhas (Lei 6.138/2018 - artigo 97)"
            fotos["21. Escoamento de Águas Pluviais Inadequado"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_escoamento_inadequado")



    # Tópico 2: Sinalização visual, tátil e tátil de alerta
    with st.expander("## **2.0 Sinalização visual, tátil e tátil de alerta**"):
        # Pergunta 1
        faixas_horizontais = st.checkbox("Faltam faixas horizontais (sinalização visual) nas portas e paredes de vidro (ABNT NBR 9050:2020 - item 6.11.2.13)",
                                        key="faixas_horizontais")
        if faixas_horizontais:
            resultados["2.1 Faixas Horizontais"] = "Faltam faixas horizontais (sinalização visual) nas portas e paredes de vidro (ABNT NBR 9050:2020 - item 6.11.2.13)"
            fotos["1. Faixas Horizontais"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_faixas_horizontais")

        # Pergunta 2
        sinalizacao_alerta = st.checkbox("Falta sinalização visual e tátil de alerta no piso, na projeção dos obstáculos fixados/suspensos entre 0,60m e 2,10m de altura do piso acabado e/ou não está sinalizada corretamente (embaixo de vigas inclinadas, de rampas, de escadas, etc) (ABNT NBR 16537:2024 - item 6.8)",
                                        key="sinalizacao_alerta")
        if sinalizacao_alerta:
            resultados["2.2 Sinalização de Alerta"] = "Falta sinalização visual e tátil de alerta no piso, na projeção dos obstáculos fixados/suspensos entre 0,60m e 2,10m de altura do piso acabado e/ou não está sinalizada corretamente (embaixo de vigas inclinadas, de rampas, de escadas, etc) (ABNT NBR 16537:2024 - item 6.8)"
            fotos["2. Sinalização de Alerta"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_sinalizacao_alerta")

        # Pergunta 3
        sinalizacao_suspensa = st.checkbox("A sinalização visual suspensa está instalada abaixo de 2,10m de altura, em áreas de circulação (ABNT NBR 16537:2024 - item 6.8)",
                                          key="sinalizacao_suspensa")
        if sinalizacao_suspensa:
            resultados["2.3 Sinalização Suspensa"] = "A sinalização visual suspensa está instalada abaixo de 2,10m de altura, em áreas de circulação (ABNT NBR 16537:2024 - item 6.8)"
            fotos["3. Sinalização Suspensa"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_sinalizacao_suspensa")

        # Verificação de sinalização visual das portas
        sinalizacao_visual_portas = st.checkbox("A sinalização visual das portas (sanitários, banheiros, vestiários, acessos verticais e horizontais, números de pavimentos) não está localizada entre 1,20 m e 1,60 m e/ou não está centralizada (ABNT NBR 9050:2020 - item 5.4.1)", key="sinalizacao_visual_portas")
        if sinalizacao_visual_portas:
            resultados["2.4 Sinalização Visual das Portas"] = "A sinalização visual das portas (sanitários, banheiros, vestiários, acessos verticais e horizontais, números de pavimentos) não está localizada entre 1,20 m e 1,60 m e/ou não está centralizada (ABNT NBR 9050:2020 - item 5.4.1)"
            fotos["22. Sinalização Visual das Portas"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_sinalizacao_visual_portas")

        # Verificação de sinalização visual e tátil ao lado das portas
        sinalizacao_visual_tatil = st.checkbox("A sinalização visual e tátil ao lado das portas (sanitários, banheiros, vestiários, acessos verticais e horizontais, números de pavimentos) não está localizada entre 1,20 m e 1,60 m e/ou não contém informações em relevo e em braile (ABNT NBR 9050:2020 - itens 5.4.1 e 5.2.8.1.3)", key="sinalizacao_visual_tatil")
        if sinalizacao_visual_tatil:
            resultados["2.5 Sinalização Visual e Tátil"] = "A sinalização visual e tátil ao lado das portas (sanitários, banheiros, vestiários, acessos verticais e horizontais, números de pavimentos) não está localizada entre 1,20 m e 1,60 m e/ou não contém informações em relevo e em braile (ABNT NBR 9050:2020 - itens 5.4.1 e 5.2.8.1.3)"
            fotos["23. Sinalização Visual e Tátil"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_sinalizacao_visual_tatil")

        # Verificação de percurso tátil direcional no piso
        percurso_tatil_direcional = st.checkbox("O percurso tátil direcional no piso instalado não atende os parâmetros técnicos da ABNT NBR 16537:2024", key="percurso_tatil_direcional")
        if percurso_tatil_direcional:
            resultados["2.6 Percurso Tátil Direcional"] = "O percurso tátil direcional no piso instalado não atende os parâmetros técnicos da ABNT NBR 16537:2024"
            fotos["24. Percurso Tátil Direcional"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_percurso_tatil_direcional")

        # Verificação de falta de contraste visual na sinalização tátil do piso
        falta_contraste_visual = st.checkbox("Falta contraste visual (cor) na sinalização tátil do piso (ABNT NBR 16537:2024 - item 7.2)", key="falta_contraste_visual")
        if falta_contraste_visual:
            resultados["2.7 Falta de Contraste Visual"] = "Falta contraste visual (cor) na sinalização tátil do piso (ABNT NBR 16537:2024 - item 7.2)"
            fotos["25. Falta de Contraste Visual"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_falta_contraste_visual")

        # Verificação de falta de sinalização tátil e visual informando o número do pavimento
        falta_sinalizacao_pavimento = st.checkbox("Falta sinalização tátil e visual informando o número do pavimento, junto à porta corta-fogo, do lado de dentro da caixa da escada (ABNT NBR 9050:2020 - item 5.5.1.3)", key="falta_sinalizacao_pavimento")
        if falta_sinalizacao_pavimento:
            resultados["2.8 Falta de Sinalização de Pavimento"] = "Falta sinalização tátil e visual informando o número do pavimento, junto à porta corta-fogo, do lado de dentro da caixa da escada (ABNT NBR 9050:2020 - item 5.5.1.3)"
            fotos["26. Falta de Sinalização de Pavimento"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_falta_sinalizacao_pavimento")

        # Verificação de faixas laterais ao piso tátil direcional
        faixas_laterais_inadequadas = st.checkbox("As faixas laterais ao piso tátil direcional não possuem a largura mínima de 0,60m (ABNT NBR 16537:2024 - item 7.3.8)", key="faixas_laterais_inadequadas")
        if faixas_laterais_inadequadas:
            resultados["2.9 Faixas Laterais Inadequadas"] = "As faixas laterais ao piso tátil direcional não possuem a largura mínima de 0,60m (ABNT NBR 16537:2024 - item 7.3.8)"
            fotos["27. Faixas Laterais Inadequadas"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="foto_faixas_laterais_inadequadas")
        

        # Tópico 3: Garagem e/ou estacionamento interno ao lote
    with st.expander("## **3.0 Garagem e/ou estacionamento interno ao lote**"):
        # Pergunta 3.1
        rota_acessivel_piso = st.checkbox("Rota acessível com piso irregular e/ou que trepida e/ou derrapante e/ou com desnível, no percurso entre o estacionamento ou garagem e a entrada principal. (ABNT NBR 9050:2020 - item 6.14.2)", 
                                        key="3rota_acessivel_piso")
        if rota_acessivel_piso:
            resultados["3.1 Rota Acessível"] = "Rota acessível com piso irregular e/ou que trepida e/ou derrapante e/ou com desnível, no percurso entre o estacionamento ou garagem e a entrada principal. (ABNT NBR 9050:2020 - item 6.14.2)"
            fotos["3.1 Rota Acessível"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="3foto_rota_acessivel_piso")

        # Pergunta 3.2
        vaga_deficiencia_nao_demarcada = st.checkbox("Não há vaga demarcada para pessoa com deficiência conforme o projeto aprovado (ABNT NBR 9050:2020 - item 6.14)", 
                                                    key="3vaga_deficiencia_nao_demarcada")
        if vaga_deficiencia_nao_demarcada:
            resultados["3.2 Vaga para Deficiência"] = "Não há vaga demarcada para pessoa com deficiência conforme o projeto aprovado. (ABNT NBR 9050:2020 - item 6.14)"
            fotos["3.2 Vaga para Deficiência"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="3foto_vaga_deficiencia_nao_demarcada")

        # Pergunta 3.3
        vaga_idoso_nao_demarcada = st.checkbox("Não há vaga demarcada para idoso conforme o projeto aprovado (ABNT NBR 9050:2020 - item 6.14)", 
                                            key="3vaga_idoso_nao_demarcada")
        if vaga_idoso_nao_demarcada:
            resultados["3.3 Vaga para Idoso"] = "Não há vaga demarcada para idoso conforme o projeto aprovado (ABNT NBR 9050:2020 - item 6.14)."
            fotos["3.3 Vaga para Idoso"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="f3oto_vaga_idoso_nao_demarcada")

        # Pergunta 3.4
        espaco_demarcado_deficiencia = st.checkbox("Falta junto à vaga para pessoa com deficiência um espaço demarcado de 1,20m de largura (ABNT NBR 9050:2020 - item 6.14.1.2.b)", 
                                                key="4espaco_demarcado_deficiencia")
        if espaco_demarcado_deficiencia:
            resultados["3.4 Espaço Demarcado Deficiência"] = "Falta junto à vaga para pessoa com deficiência um espaço demarcado de 1,20m de largura (ABNT NBR 9050:2020 - item 6.14.1.2.b)."
            fotos["3.4 Espaço Demarcado Deficiência"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="f4oto_espaco_demarcado_deficiencia")

        # Pergunta 3.5
        sinalizacao_deficiencia_falta = st.checkbox("Falta sinalização horizontal (no piso) e/ou vertical nas vagas para pessoa com deficiência (ABNT NBR 9050:2020 - item 5.5.2)", 
                                                    key="3sinalizacao_deficiencia_falta")
        if sinalizacao_deficiencia_falta:
            resultados["3.5 Sinalização Deficiência"] = "Falta sinalização horizontal (no piso) e/ou vertical nas vagas para pessoa com deficiência (ABNT NBR 9050:2020 - item 5.5.2)."
            fotos["3.5 Sinalização Deficiência"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="3foto_sinalizacao_deficiencia_falta")

        # Pergunta 3.6
        sinalizacao_idoso_falta = st.checkbox("Falta sinalização horizontal (no piso) e/ou vertical nas vagas para idoso (ABNT NBR 9050:2020 - item 5.5.2)", 
                                            key="3sinalizacao_idoso_falta")
        if sinalizacao_idoso_falta:
            resultados["3.6 Sinalização Idoso"] = "Falta sinalização horizontal (no piso) e/ou vertical nas vagas para idoso. (ABNT NBR 9050:2020 - item 5.5.2)"
            fotos["3.6 Sinalização Idoso"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="3foto_sinalizacao_idoso_falta")

        # Pergunta 3.7
        borda_plaque_sinalizacao = st.checkbox("A borda inferior da placa de sinalização vertical de vaga, em áreas de circulação tem altura inferior a 2,10m (ABNT NBR 9050:2020 - item 5.2.8.2.3)", 
                                            key="3borda_plaque_sinalizacao")
        if borda_plaque_sinalizacao:
            resultados["3.7 Borda Placa Sinalização"] = "A borda inferior da placa de sinalização vertical de vaga, em áreas de circulação tem altura inferior a 2,10m (ABNT NBR 9050:2020 - item 5.2.8.2.3)."
            fotos["3.7 Borda Placa Sinalização"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="3foto_borda_plaque_sinalizacao")

        # Pergunta 3.8
        falta_grelha_canaleneta = st.checkbox("Falta grelha na canaleta do piso e/ou os vãos da grelha estão com dimensão superior a 1,5 cm e/ou a grelha não está nivelada com o piso e/ou não está firme ou estável (ABNT NBR 9050:2020 - item 6.3.5)", 
                                            key="3falta_grelha_canaleneta")
        if falta_grelha_canaleneta:
            resultados["3.8 Grelha Canaleta Piso"] = "Falta grelha na canaleta do piso e/ou os vãos da grelha estão com dimensão superior a 1,5 cm e/ou a grelha não está nivelada com o piso e/ou não está firme ou estável (ABNT NBR 9050:2020 - item 6.3.5)."
            fotos["3.8 Grelha Canaleta Piso"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="3foto_falta_grelha_canaleneta")

        # Tópico 4: Rampas internas e rampas para acesso à edificação
    with st.expander("## **4.0 Rampas internas e rampas para acesso à edificação**"):
        # Tópico 4
        sinalizacao_identificacao_pavimentos = st.checkbox("Falta sinalização de identificação de pavimentos (andares), visual, em relevo e em Braille, nas duas alturas dos corrimãos e nos dois lados (a sinalização visual e em relevo pode ser aplicada na parede, a sinalização em Braille deve estar obrigatoriamente posicionada na geratriz superior do prolongamento do corrimão) (ABNT NBR 9050:2020 - item 5.4.3)",
                                                        key="sinalizacao_identificacao_pavimentos")
        if sinalizacao_identificacao_pavimentos:
            resultados["4.1 Sinalização Identificação de Pavimentos"] = "Falta sinalização de identificação de pavimentos (andares), visual, em relevo e em Braille, nas duas alturas dos corrimãos e nos dois lados (a sinalização visual e em relevo pode ser aplicada na parede, a sinalização em Braille deve estar obrigatoriamente posicionada na geratriz superior do prolongamento do corrimão) (ABNT NBR 9050:2020 - item 5.4.3)"
            fotos["4.1 Sinalização Identificação de Pavimentos"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_sinalizacao_identificacao_pavimentos")

        sinalizacao_tatil_alerta_rampa = st.checkbox("Falta sinalização tátil de alerta no início e no final da rampa (ABNT NBR 16537:2024 - item 6.4.4)", key="4sinalizacao_tatil_alerta_rampa")
        if sinalizacao_tatil_alerta_rampa:
            resultados["4.2 Sinalização Tátil Alerta Rampa"] = "Falta sinalização tátil de alerta no início e no final da rampa (ABNT NBR 16537:2024 - item 6.4.4)"
            fotos["4.2 Sinalização Tátil Alerta Rampa"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_sinalizacao_tatil_alerta_rampa")

        retirar_sinalizacao_tatil_alerta_patamar = st.checkbox("Retirar sinalização tátil de alerta situado nos patamares das rampas (ABNT NBR 16537:2024 - item 6.5.1) - Só se aplica no caso de patamar com comprimento maior que 2,10m", key="4retirar_sinalizacao_tatil_alerta_patamar")
        if retirar_sinalizacao_tatil_alerta_patamar:
            resultados["4.3 Retirar Sinalização Tátil Alerta Patamar"] = "Retirar sinalização tátil de alerta situado nos patamares das rampas (ABNT NBR 16537:2024 - item 6.5.1) - Só se aplica no caso de patamar com comprimento maior que 2,10m"
            fotos["4.3 Retirar Sinalização Tátil Alerta Patamar"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_retirar_sinalizacao_tatil_alerta_patamar")

        rampa_com_inclinacao_maior_833 = st.checkbox("Rampa com inclinação longitudinal superior a 8,33% (ABNT NBR 9050:2020 - item 6.6.2.1)", key="4rampa_com_inclinacao_maior_833")
        if rampa_com_inclinacao_maior_833:
            resultados["4.4 Rampa com Inclinação Maior que 8,33%"] = "Rampa com inclinação longitudinal superior a 8,33% (ABNT NBR 9050:2020 - item 6.6.2.1)"
            fotos["4.4 Rampa com Inclinação Maior que 8,33%"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_rampa_com_inclinacao_maior_833")

        rampa_com_largura_inferior_120m = st.checkbox("Rampa com largura livre inferior a 1,20 m (ABNT NBR 9050:2020 - item 6.6.2.5)", key="4rampa_com_largura_inferior_120m")
        if rampa_com_largura_inferior_120m:
            resultados["4.5 Rampa com Largura Inferior a 1,20m"] = "Rampa com largura livre inferior a 1,20 m (ABNT NBR 9050:2020 - item 6.6.2.5)"
            fotos["4.5 Rampa com Largura Inferior a 1,20m"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_rampa_com_largura_inferior_120m")

        inclinacao_transversal_superior = st.checkbox("A inclinação transversal é superior a 2 % (rampa interna) ou superior a 3 % (rampa externa) (ABNT NBR 9050:2020 - item 6.6.2.4)", key="4inclinacao_transversal_superior")
        if inclinacao_transversal_superior:
            resultados["4.6 Inclinação Transversal Superior"] = "A inclinação transversal é superior a 2 % (rampa interna) ou superior a 3 % (rampa externa) (ABNT NBR 9050:2020 - item 6.6.2.4)"
            fotos["4.6 Inclinação Transversal Superior"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_inclinacao_transversal_superior")

        rampa_nao_antiderrapante = st.checkbox("Piso da rampa não é antiderrapante (ABNT NBR 9050:2020 - item 6.3.2)", key="4rampa_nao_antiderrapante")
        if rampa_nao_antiderrapante:
            resultados["4.7 Piso da Rampa Não Antiderrapante"] = "Piso da rampa não é antiderrapante (ABNT NBR 9050:2020 - item 6.3.2)"
            fotos["4.7 Piso da Rampa Não Antiderrapante"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_rampa_nao_antiderrapante")

        faltam_corrimaos_rampa = st.checkbox("Faltam corrimãos instalados em ambos os lados da rampa (ABNT NBR 9050:2020 - item 6.6.2.6)", key="4faltam_corrimaos_rampa")
        if faltam_corrimaos_rampa:
            resultados["4.8 Faltam Corrimãos Instalados em Ambos os Lados da Rampa"] = "Faltam corrimãos instalados em ambos os lados da rampa (ABNT NBR 9050:2020 - item 6.6.2.6)"
            fotos["4.8 Faltam Corrimãos Instalados em Ambos os Lados da Rampa"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_faltam_corrimaos_rampa")
        # Tópico 4 - Corrimãos e Acessibilidade

        corrimao_duas_alturas = st.checkbox("Os corrimãos não possuem duas alturas (0,70m e 0,92m medidos da face superior ao piso do patamar) (ABNT NBR 9050:2020 - item 6.9.3.2)", key="4corrimao_duas_alturas")
        if corrimao_duas_alturas:
            resultados["4.9 Corrimãos Duas Alturas"] = "Os corrimãos não possuem duas alturas (0,70m e 0,92m medidos da face superior ao piso do patamar) (ABNT NBR 9050:2020 - item 6.9.3.2)"
            fotos["4.9 Corrimãos Duas Alturas"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_corrimao_duas_alturas")

        corrimao_prolongamentos = st.checkbox("Os corrimãos não possuem prolongamentos de 0,30m nas extremidades (ABNT NBR 9050:2020 - item 6.9.3.2)", key="4corrimao_prolongamentos")
        if corrimao_prolongamentos:
            resultados["4.10 Corrimãos Prolongamentos"] = "Os corrimãos não possuem prolongamentos de 0,30m nas extremidades (ABNT NBR 9050:2020 - item 6.9.3.2)"
            fotos["4.10 Corrimãos Prolongamentos"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_corrimao_prolongamentos")

        corrimao_firma_fixa = st.checkbox("Corrimãos não estão firmemente fixados às paredes ou barras de suporte (ABNT NBR 9050:2020 - item 6.9.1)", key="4corrimao_firma_fixa")
        if corrimao_firma_fixa:
            resultados["4.11 Corrimãos Firma Fixa"] = "Corrimãos não estão firmemente fixados às paredes ou barras de suporte (ABNT NBR 9050:2020 - item 6.9.1)"
            fotos["4.11 Corrimãos Firma Fixa"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_corrimao_firma_fixa")

        corrimao_passagem_continua = st.checkbox("O corrimão não permite passagem contínua da mão (ABNT NBR 9050:2020 - item 6.9.3.3)", key="corrimao_passagem_continua")
        if corrimao_passagem_continua:
            resultados["4.12 Corrimão Passagem Contínua"] = "O corrimão não permite passagem contínua da mão (ABNT NBR 9050:2020 - item 6.9.3.3)"
            fotos["4.12 Corrimão Passagem Contínua"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_corrimao_passagem_continua")

        corrimao_prolongamento_interfere = st.checkbox("O prolongamento do corrimão no início/final da rampa interfere na circulação (ABNT NBR 9050:2020 - item 6.9.3.3)", key="c4orrimao_prolongamento_interfere")
        if corrimao_prolongamento_interfere:
            resultados["4.13 Prolongamento Corrimão Interfere"] = "O prolongamento do corrimão no início/final da rampa interfere na circulação (ABNT NBR 9050:2020 - item 6.9.3.3)"
            fotos["4.13 Prolongamento Corrimão Interfere"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_corrimao_prolongamento_interfere")

        corrimao_acabamento_recurvado = st.checkbox("Os corrimãos não possuem acabamento recurvado nas extremidades (ABNT NBR 9050:2020 - item 6.9.3.4)", key="4corrimao_acabamento_recurvado")
        if corrimao_acabamento_recurvado:
            resultados["4.14 Corrimãos Acabamento Recurvado"] = "Os corrimãos não possuem acabamento recurvado nas extremidades (ABNT NBR 9050:2020 - item 6.9.3.4)"
            fotos["4.14 Corrimãos Acabamento Recurvado"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_corrimao_acabamento_recurvado")

        corrimao_secao_circular = st.checkbox("Os corrimãos não têm seção circular com diâmetro entre 3,0cm e 4,5cm (ABNT NBR 9050:2020 - item 4.6.5)", key="4corrimao_secao_circular")
        if corrimao_secao_circular:
            resultados["4.15 Corrimãos Seção Circular"] = "Os corrimãos não têm seção circular com diâmetro entre 3,0cm e 4,5cm (ABNT NBR 9050:2020 - item 4.6.5)"
            fotos["4.15 Corrimãos Seção Circular"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_corrimao_secao_circular")

        guias_balizamento_piso = st.checkbox("Faltam guias de balizamento no piso (ABNT NBR 9050:2020 - item 6.6.3)", key="4guias_balizamento_piso")
        if guias_balizamento_piso:
            resultados["4.16 Guias de Balizamento no Piso"] = "Faltam guias de balizamento no piso (ABNT NBR 9050:2020 - item 6.6.3)"
            fotos["4.16 Guias de Balizamento no Piso"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_guias_balizamento_piso")

        corrimao_sem_guarda_corpo = st.checkbox("Corrimão sem paredes laterais e sem guarda-corpo (ABNT NBR 9050:2020 - item 6.6.2.8)", key="4corrimao_sem_guarda_corpo")
        if corrimao_sem_guarda_corpo:
            resultados["4.17 Corrimão Sem Paredes Laterais e Guarda-Corpo"] = "Corrimão sem paredes laterais e sem guarda-corpo (ABNT NBR 9050:2020 - item 6.6.2.8)"
            fotos["4.17 Corrimão Sem Paredes Laterais e Guarda-Corpo"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="4foto_corrimao_sem_guarda_corpo")
        
    # Tópico 5: Degraus isolados (até dois degraus)
    with st.expander("## **5.0 Degraus isolados (até dois degraus)**"):
        # Pergunta 1
        sinalizacao_visual = st.checkbox("Falta sinalização visual, no piso e no espelho, em toda a extensão do degrau com uma faixa de no mínimo 3 cm de largura, contrastante com o piso adjacente (ABNT NBR 9050:2020 - item 5.4.4.1)",
                                        key="5sinalizacao_visual")
        if sinalizacao_visual:
            resultados["5.1 Sinalização Visual no Degrau"] = "Falta sinalização visual, no piso e no espelho, em toda a extensão do degrau com uma faixa de no mínimo 3 cm de largura, contrastante com o piso adjacente (ABNT NBR 9050:2020 - item 5.4.4.1)"
            fotos["5.1 Sinalização Visual no Degrau"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="5foto_sinalizacao_visual")

        # Pergunta 2
        sinalizacao_tatil_alerta = st.checkbox("Falta sinalização tátil de alerta embaixo e em cima do degrau (ABNT NBR 16537:2024 - item 6.4.3)",
                                              key="5sinalizacao_tatil_alerta")
        if sinalizacao_tatil_alerta:
            resultados["5.2 Sinalização Tátil de Alerta"] = "Falta sinalização tátil de alerta embaixo e em cima do degrau (ABNT NBR 16537:2024 - item 6.4.3)"
            fotos["5.2 Sinalização Tátil de Alerta"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="5foto_sinalizacao_tatil_alerta")

        # Pergunta 3
        corrimao_extremidade = st.checkbox("Falta corrimão em uma das extremidades do degrau com no mínimo 0,30 m de comprimento, posicionado a 0,75 m de altura (somente para degrau isolado, com um único degrau) (ABNT NBR 9050:2020 - item 6.9.4.1)",
                                           key="5corrimao_extremidade")
        if corrimao_extremidade:
            resultados["5.3 Corrimão na Extremidade do Degrau"] = "Falta corrimão em uma das extremidades do degrau com no mínimo 0,30 m de comprimento, posicionado a 0,75 m de altura (somente para degrau isolado, com um único degrau) (ABNT NBR 9050:2020 - item 6.9.4.1)"
            fotos["5.3 Corrimão na Extremidade do Degrau"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="5foto_corrimao_extremidade")

        # Pergunta 4
        corrimao_duas_alturas = st.checkbox("Faltam corrimãos instalados a 0,92 m e a 0,70 m de altura do piso. Se o vão for maior do que 2,40 m pode ser adotado um só corrimão intermediário. (para degrau isolado, com dois degraus) (ABNT NBR 9050:2020 - itens 6.9.3 e 6.9.4.1)",
                                            key="5corrimao_duas_alturas")
        if corrimao_duas_alturas:
            resultados["5.4 Corrimão com Duas Alturas"] = "Faltam corrimãos instalados a 0,92 m e a 0,70 m de altura do piso. Se o vão for maior do que 2,40 m pode ser adotado um só corrimão intermediário. (para degrau isolado, com dois degraus) (ABNT NBR 9050:2020 - itens 6.9.3 e 6.9.4.1)"
            fotos["5.4 Corrimão com Duas Alturas"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="5foto_corrimao_duas_alturas")

        # Pergunta 5
        secao_corrimao = st.checkbox("Os corrimãos não têm seção circular com diâmetro entre 3,0cm e 4,5cm (ABNT NBR 9050:2020 - item 4.6.5)",
                                     key="5secao_corrimao")
        if secao_corrimao:
            resultados["5.5 Seção do Corrimão"] = "Os corrimãos não têm seção circular com diâmetro entre 3,0cm e 4,5cm (ABNT NBR 9050:2020 - item 4.6.5)"
            fotos["5.5 Seção do Corrimão"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="5foto_secao_corrimao")

        # Pergunta 6
        fixacao_corrimao = st.checkbox("Corrimãos não estão firmemente fixados às paredes ou barras de suporte (ABNT NBR 9050:2020 - item 6.9.1)",
                                      key="5fixacao_corrimao")
        if fixacao_corrimao:
            resultados["5.6 Fixação do Corrimão"] = "Corrimãos não estão firmemente fixados às paredes ou barras de suporte (ABNT NBR 9050:2020 - item 6.9.1)"
            fotos["5.6 Fixação do Corrimão"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="5foto_fixacao_corrimao")

        # Pergunta 7
        dimensoes_piso_espelho = st.checkbox("As dimensões dos pisos e espelhos não são constantes (piso entre 0,28 m e 0,32 m e, espelho entre 0,16 m e 0,18 m) (ABNT NBR 9050:2020 - item 6.8.2)",
                                             key="5dimensoes_piso_espelho")
        if dimensoes_piso_espelho:
            resultados["5.7 Dimensões do Piso e Espelho"] = "As dimensões dos pisos e espelhos não são constantes (piso entre 0,28 m e 0,32 m e, espelho entre 0,16 m e 0,18 m) (ABNT NBR 9050:2020 - item 6.8.2)"
            fotos["5.7 Dimensões do Piso e Espelho"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="5foto_dimensoes_piso_espelho")

        # Pergunta 8
        piso_antiderrapante = st.checkbox("Piso do degrau não é antiderrapante (ABNT NBR 9050:2020 - item 6.3.2)",
                                          key="5piso_antiderrapante")
        if piso_antiderrapante:
            resultados["5.8 Piso Antiderrapante"] = "Piso do degrau não é antiderrapante (ABNT NBR 9050:2020 - item 6.3.2)"
            fotos["5.8 Piso Antiderrapante"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="5foto_piso_antiderrapante")

        # Pergunta 9
        degrau_isolado = st.checkbox("Degrau isolado não está associado à rampa ou a equipamento de transporte vertical (ABNT NBR 9050:2020 - item 6.7)",
                                     key="5degrau_isolado")
        if degrau_isolado:
            resultados["5.9 Degrau Isolado"] = "Degrau isolado não está associado à rampa ou a equipamento de transporte vertical (ABNT NBR 9050:2020 - item 6.7)"
            fotos["5.9 Degrau Isolado"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="5foto_degrau_isolado")
            
    # Tópico 6: Escadas (não se aplica em escadas de acesso à áreas técnicas e de uso privativo)
    with st.expander("## **6.0 Escadas (não se aplica em escadas de acesso à áreas técnicas e de uso privativo)**"):
        # Pergunta 1
        sinalizacao_identificacao_pavimentos = st.checkbox("Falta sinalização de identificação de pavimentos (andares), visual, em relevo e em Braille, nas duas alturas dos corrimãos e nos dois lados (a sinalização visual e em relevo pode ser aplicada na parede, a sinalização em Braille deve estar obrigatoriamente posicionada na geratriz superior do prolongamento do corrimão) (ABNT NBR 9050:2020 - item 5.4.3)",
                                                        key="6sinalizacao_identificacao_pavimentos")
        if sinalizacao_identificacao_pavimentos:
            resultados["6.1 Sinalização de Identificação de Pavimentos"] = "Falta sinalização de identificação de pavimentos (andares), visual, em relevo e em Braille, nas duas alturas dos corrimãos e nos dois lados (a sinalização visual e em relevo pode ser aplicada na parede, a sinalização em Braille deve estar obrigatoriamente posicionada na geratriz superior do prolongamento do corrimão) (ABNT NBR 9050:2020 - item 5.4.3)"
            fotos["6.1 Sinalização de Identificação de Pavimentos"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_sinalizacao_identificacao_pavimentos")

        # Pergunta 2
        sinalizacao_tatil_alerta_inicio_fim = st.checkbox("Falta sinalização tátil de alerta no início e no final da escada (ABNT NBR 16537:2024 - item 6.4.1)",
                                                        key="6sinalizacao_tatil_alerta_inicio_fim")
        if sinalizacao_tatil_alerta_inicio_fim:
            resultados["6.2 Sinalização Tátil de Alerta Início e Fim"] = "Falta sinalização tátil de alerta no início e no final da escada (ABNT NBR 16537:2024 - item 6.4.1)"
            fotos["6.2 Sinalização Tátil de Alerta Início e Fim"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_sinalizacao_tatil_alerta_inicio_fim")
        # Pergunta 3
        sinalizacao_tatil_alerta_patarma = st.checkbox("Retirar sinalização tátil de alerta situado nos patamares das escadas (ABNT NBR 16537:2024 - item 6.5.1)",
                                                    key="6sinalizacao_tatil_alerta_patarma")
        if sinalizacao_tatil_alerta_patarma:
            resultados["6.3 Sinalização Tátil de Alerta nos Patamares"] = "Retirar sinalização tátil de alerta situado nos patamares das escadas (ABNT NBR 16537:2024 - item 6.5.1)"
            fotos["6.3 Sinalização Tátil de Alerta nos Patamares"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_sinalizacao_tatil_alerta_patarma")

        # Pergunta 4
        sinalizacao_tatil_alerta_projecao = st.checkbox("Falta sinalização tátil de alerta na projeção da escada (ABNT NBR 16537:2024 - item 6.8)",
                                                    key="6sinalizacao_tatil_alerta_projecao")
        if sinalizacao_tatil_alerta_projecao:
            resultados["6.4 Sinalização Tátil de Alerta na Projeção"] = "Falta sinalização tátil de alerta na projeção da escada (ABNT NBR 16537:2024 - item 6.8)"
            fotos["6.4 Sinalização Tátil de Alerta na Projeção"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_sinalizacao_tatil_alerta_projecao")

        # Pergunta 5
        sinalizacao_visual_degrau = st.checkbox("Falta sinalização visual na borda do piso e do espelho do degrau e/ou a sinalização não tem cor contrastante com o piso e/ou não mede 3 cm de largura. (Uma faixa em toda a extensão do degrau ou restrita à projeção dos corrimãos, com no mínimo 7,0 cm de extensão) (ABNT NBR 9050:2020 item 5.4.4.2)",
                                            key="6sinalizacao_visual_degrau")
        if sinalizacao_visual_degrau:
            resultados["6.5 Sinalização Visual no Degrau"] = "Falta sinalização visual na borda do piso e do espelho do degrau e/ou a sinalização não tem cor contrastante com o piso e/ou não mede 3 cm de largura. (Uma faixa em toda a extensão do degrau ou restrita à projeção dos corrimãos, com no mínimo 7,0 cm de extensão) (ABNT NBR 9050:2020 item 5.4.4.2)"
            fotos["6.5 Sinalização Visual no Degrau"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_sinalizacao_visual_degrau")

        # Pergunta 6
        piso_antiderrapante = st.checkbox("O piso dos degraus da escada não é antiderrapante ou falta faixa de proteção antiderrapante ao longo do seu bordo (ABNT NBR 9050:2020 - item 6.3.2)",
                                        key="6piso_antiderrapante")
        if piso_antiderrapante:
            resultados["6.6 Piso Antiderrapante nos Degraus"] = "O piso dos degraus da escada não é antiderrapante ou falta faixa de proteção antiderrapante ao longo do seu bordo (ABNT NBR 9050:2020 - item 6.3.2)"
            fotos["6.6 Piso Antiderrapante nos Degraus"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_piso_antiderrapante")

        # Pergunta 7
        escada_com_espelho_vazado = st.checkbox("Escada em rota acessível com espelho vazado (ABNT NBR 9050:2020 item 6.7.1)",
                                            key="6escada_com_espelho_vazado")
        if escada_com_espelho_vazado:
            resultados["6.7 Escada com Espelho Vazado"] = "Escada em rota acessível com espelho vazado (ABNT NBR 9050:2020 item 6.7.1)"
            fotos["6.7 Escada com Espelho Vazado"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_escada_com_espelho_vazado")

        # Pergunta 8
        escada_sem_associacao_rampa = st.checkbox("Escada não está associada à rampa ou a equipamento de transporte vertical (somente válido para edificações com mais de 4 pavimentos) (ABNT NBR 9050:2020 - item 6.7)",
                                                key="6escada_sem_associacao_rampa")
        if escada_sem_associacao_rampa:
            resultados["6.8 Escada sem Associação a Rampa"] = "Escada não está associada à rampa ou a equipamento de transporte vertical (somente válido para edificações com mais de 4 pavimentos) (ABNT NBR 9050:2020 - item 6.7)"
            fotos["6.8 Escada sem Associação a Rampa"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_escada_sem_associacao_rampa")

        # Pergunta 9
        dimensoes_piso_espelho_variadas = st.checkbox("As dimensões dos pisos e espelhos não são constantes em toda a escada (piso entre 0,28 m e 0,32 m e, espelho entre 0,16 m e 0,18 m) (ABNT NBR 9050:2020 - item 6.8.2)",
                                                    key="6dimensoes_piso_espelho_variadas")
        if dimensoes_piso_espelho_variadas:
            resultados["6.9 Dimensões Variadas no Piso e Espelho"] = "As dimensões dos pisos e espelhos não são constantes em toda a escada (piso entre 0,28 m e 0,32 m e, espelho entre 0,16 m e 0,18 m) (ABNT NBR 9050:2020 - item 6.8.2)"
            fotos["6.9 Dimensões Variadas no Piso e Espelho"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_dimensoes_piso_espelho_variadas")

        # Pergunta 10
        escada_com_largura_inferior = st.checkbox("Escada com largura inferior a 1,20 m (ABNT NBR 9050:2020 - item 6.8.3)",
                                                key="6escada_com_largura_inferior")
        if escada_com_largura_inferior:
            resultados["6.10 Escada com Largura Inferior a 1,20m"] = "Escada com largura inferior a 1,20 m (ABNT NBR 9050:2020 - item 6.8.3)"
            fotos["6.10 Escada com Largura Inferior a 1,20m"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_escada_com_largura_inferior")

        # Pergunta 11
        escada_sem_guia_balizamento = st.checkbox("Escada sem guia de balizamento (ABNT NBR 9050:2020 - item 6.8.3)",
                                                key="6escada_sem_guia_balizamento")
        if escada_sem_guia_balizamento:
            resultados["6.11 Escada sem Guia de Balizamento"] = "Escada sem guia de balizamento (ABNT NBR 9050:2020 - item 6.8.3)"
            fotos["6.11 Escada sem Guia de Balizamento"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_escada_sem_guia_balizamento")

        # Pergunta 12
        inclinacao_transversal_deg_pat = st.checkbox("Inclinação transversal dos degraus ou dos patamares, superior a 1 % (escada interna) ou 2 % (escada externa) (ABNT NBR 9050:2020 - itens 6.8.5 e 6.8.9)",
                                                    key="6inclinacao_transversal_deg_pat")
        if inclinacao_transversal_deg_pat:
            resultados["6.12 Inclinação Transversal dos Degraus ou Patamares"] = "Inclinação transversal dos degraus ou dos patamares, superior a 1 % (escada interna) ou 2 % (escada externa) (ABNT NBR 9050:2020 - itens 6.8.5 e 6.8.9)"
            fotos["6.12 Inclinação Transversal dos Degraus ou Patamares"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_inclinacao_transversal_deg_pat")

        # Pergunta 13
        escada_com_lances_curvos = st.checkbox("Escada com lances curvos com distância inferior a 0,55 m da borda interna da escada (ABNT NBR 9050:2020 - item 6.8.6)",
                                            key="6escada_com_lances_curvos")
        if escada_com_lances_curvos:
            resultados["6.13 Escada com Lances Curvos"] = "Escada com lances curvos com distância inferior a 0,55 m da borda interna da escada (ABNT NBR 9050:2020 - item 6.8.6)"
            fotos["6.13 Escada com Lances Curvos"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_escada_com_lances_curvos")

        # Pergunta 10
        corrimao_instalacao = st.checkbox("Falta instalar os corrimãos em ambos os lados da escada e/ou não estão instalados com alturas de 0,70m e de 0,92m, medidas da borda do degrau até a face superior do corrimão (ABNT NBR 9050:2020 - item 6.9.3.2)",
                                         key="6corrimao_instalacao")
        if corrimao_instalacao:
            resultados["6.14 Corrimãos Instalados"] = "Falta instalar os corrimãos em ambos os lados da escada e/ou não estão instalados com alturas de 0,70m e de 0,92m, medidas da borda do degrau até a face superior do corrimão (ABNT NBR 9050:2020 - item 6.9.3.2)"
            fotos["6.3 Corrimãos Instalados"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_corrimao_instalacao")
        
        # Pergunta 11
        corrimao_firme = st.checkbox("Corrimãos não estão firmemente fixados às paredes ou barras de suporte (ABNT NBR 9050:2020 - item 6.9.1)",
                                     key="6corrimao_firme")
        if corrimao_firme:
            resultados["6.15 Corrimãos Firmes"] = "Corrimãos não estão firmemente fixados às paredes ou barras de suporte (ABNT NBR 9050:2020 - item 6.9.1)"
            fotos["6.4 Corrimãos Firmes"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_corrimao_firme")
        
        # Pergunta 12
        corrimao_prolongamento = st.checkbox("Os corrimãos da escada não possuem prolongamento de 30cm nas extremidades, inclusive no patamar intermediário. (se o prolongamento interferir com a circulação, este pode ser feito ao longo da área de circulação ou fixado na parede adjacente) (ABNT NBR 9050:2020 - item 6.9.3.2)",
                                             key="6corrimao_prolongamento")
        if corrimao_prolongamento:
            resultados["6.16 Prolongamento Corrimãos"] = "Os corrimãos da escada não possuem prolongamento de 30cm nas extremidades, inclusive no patamar intermediário. (se o prolongamento interferir com a circulação, este pode ser feito ao longo da área de circulação ou fixado na parede adjacente) (ABNT NBR 9050:2020 - item 6.9.3.2)"
            fotos["6.5 Prolongamento Corrimãos"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_corrimao_prolongamento")
        
        # Pergunta 13
        corrimao_continuo = st.checkbox("Corrimãos laterais não são contínuos e/ou estão interrompidos nos patamares e/ou interferem com as áreas de circulação (ABNT NBR 9050:2020 - item 6.9.3.3)",
                                       key="6corrimao_continuo")
        if corrimao_continuo:
            resultados["6.17 Corrimãos Contínuos"] = "Corrimãos laterais não são contínuos e/ou estão interrompidos nos patamares e/ou interferem com as áreas de circulação (ABNT NBR 9050:2020 - item 6.9.3.3)"
            fotos["6.6 Corrimãos Contínuos"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_corrimao_continuo")
        
        # Pergunta 14
        corrimao_acabamento = st.checkbox("Corrimãos não tem acabamento recurvado nas extremidades e/ou não permite passagem contínua da mão (ABNT NBR 9050:2020 - item 6.9.3.4)",
                                          key="6corrimao_acabamento")
        if corrimao_acabamento:
            resultados["6.18 Acabamento Corrimãos"] = "Corrimãos não tem acabamento recurvado nas extremidades e/ou não permite passagem contínua da mão (ABNT NBR 9050:2020 - item 6.9.3.4)"
            fotos["6.7 Acabamento Corrimãos"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_corrimao_acabamento")
        
        # Pergunta 15
        corrimao_seccao = st.checkbox("Os corrimãos não têm seção circular com diâmetro entre 3,0cm e 4,5cm (ABNT NBR 9050:2020 - item 4.6.5)",
                                      key="6corrimao_seccao")
        if corrimao_seccao:
            resultados["6.19 Seção Corrimãos"] = "Os corrimãos não têm seção circular com diâmetro entre 3,0cm e 4,5cm (ABNT NBR 9050:2020 - item 4.6.5)"
            fotos["6.8 Seção Corrimãos"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_corrimao_seccao")
        
        # Pergunta 16
        escada_largura_corrimao = st.checkbox("Escada com largura maior ou igual a 2,40m sem corrimão intermediário (ABNT NBR 9050:2020 - item 6.9.3.5)",
                                             key="6escada_largura_corrimao")
        if escada_largura_corrimao:
            resultados["6.20 Largura Escada com Corrimão"] = "Escada com largura maior ou igual a 2,40m sem corrimão intermediário (ABNT NBR 9050:2020 - item 6.9.3.5)"
            fotos["6.9 Largura Escada com Corrimão"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_escada_largura_corrimao")
        
        # Pergunta 17
        guarda_corpo_altura = st.checkbox("Falta guarda-corpo nas bordas livres da escada e/ou o guarda-corpo não está a altura mínima de 1,05m (ABNT NBR 14718:2019 - item 4.4.2.2)",
                                         key="6guarda_corpo_altura")
        if guarda_corpo_altura:
            resultados["6.21 Guarda-corpo Altura"] = "Falta guarda-corpo nas bordas livres da escada e/ou o guarda-corpo não está a altura mínima de 1,05m (ABNT NBR 14718:2019 - item 4.4.2.2)"
            fotos["6.10 Guarda-corpo Altura"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_guarda_corpo_altura")
        
        # Pergunta 18
        guarda_corpo_escala = st.checkbox("Existem no guarda-corpo componentes que propiciam escalada ou elementos verticais com espaçamento superior a 11cm (ABNT NBR 14718:2019 - item 4.4.2.2)",
                                          key="6guarda_corpo_escala")
        if guarda_corpo_escala:
            resultados["6.22 Guarda-corpo Escalada"] = "Existem no guarda-corpo componentes que propiciam escalada ou elementos verticais com espaçamento superior a 11cm (ABNT NBR 14718:2019 - item 4.4.2.2)"
            fotos["6.11 Guarda-corpo Escalada"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="6foto_guarda_corpo_escala")

    # Tópico 7: Sanitários, banheiros e vestiários acessíveis
    with st.expander("## **7.0 Sanitários, banheiros e vestiários acessíveis**"):
        # Pergunta 1
        sanitario_acessivel = st.checkbox("A edificação não possui sanitário acessível ou o sanitário disponível não possui dimensão suficiente para permitir um giro de 360º com diâmetro de 1,50 m. (A área de giro pode utilizar no máximo 0,10 m sob a bacia sanitária e 0,30 m sob o lavatório) (ABNT NBR 9050:2020 - itens 7.4.3.1 e 7.5.c)", 
                                        key="7sanitario_acessivel")
        if sanitario_acessivel:
            resultados["7.1 Sanitário Acessível"] = "A edificação não possui sanitário acessível ou o sanitário disponível não possui dimensão suficiente para permitir um giro de 360º com diâmetro de 1,50 m. (A área de giro pode utilizar no máximo 0,10 m sob a bacia sanitária e 0,30 m sob o lavatório) (ABNT NBR 9050:2020 - itens 7.4.3.1 e 7.5.c)"
            fotos["7.0 Sanitário Acessível"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_sanitario_acessivel")

        # Pergunta 20
        sanitario_pavimento = st.checkbox("Não há sanitário acessível em cada pavimento onde há sanitário comum, com entrada independente e dimensões mínimas para permitir o giro de 360 graus, área para manobra e área de transferência para a bacia sanitária por uma pessoa em cadeira de rodas; com sinalização visual e tátil; com bacia sanitária acessível com altura entre 43cm e 45cm e sem abertura frontal, lavatório acessível com altura entre 78cm e 80cm sem coluna ou com meia coluna, torneira com acionamento facilitado, acessórios sanitários, espelho e barras de apoio adequadas; porta abrindo para fora, com largura mínima de 0,80m e com puxador horizontal de 0,40m no lado interno; e com alarme de emergência. (ABNT NBR 9050 itens 7.1 e 7.5)", 
                                            key="7sanitario_pavimento")
        if sanitario_pavimento:
            resultados["7.2 Sanitário por Pavimento"] = "Não há sanitário acessível em cada pavimento onde há sanitário comum, com entrada independente e dimensões mínimas para permitir o giro de 360 graus, área para manobra e área de transferência para a bacia sanitária por uma pessoa em cadeira de rodas; com sinalização visual e tátil; com bacia sanitária acessível com altura entre 43cm e 45cm e sem abertura frontal, lavatório acessível com altura entre 78cm e 80cm sem coluna ou com meia coluna, torneira com acionamento facilitado, acessórios sanitários, espelho e barras de apoio adequadas; porta abrindo para fora, com largura mínima de 0,80m e com puxador horizontal de 0,40m no lado interno; e com alarme de emergência. (ABNT NBR 9050 itens 7.1 e 7.5)"
            fotos["7.1 Sanitário por Pavimento"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_sanitario_pavimento")

        # Pergunta 21
        espaco_transferencia = st.checkbox("Falta espaço de 0,80m x 1,20m para fazer a transferência lateral e/ou perpendicular e/ou diagonal para a bacia sanitária (ABNT NBR 9050:2020 - item 7.7.1)", 
                                        key="7espaco_transferencia")
        if espaco_transferencia:
            resultados["7.3 Espaço para Transferência"] = "Falta espaço de 0,80m x 1,20m para fazer a transferência lateral e/ou perpendicular e/ou diagonal para a bacia sanitária (ABNT NBR 9050:2020 - item 7.7.1)"
            fotos["7.2 Espaço para Transferência"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_espaco_transferencia")

        # Pergunta 22
        sinalizacao_visual = st.checkbox("A sinalização visual (símbolo representativo) da(s) porta(s) (sanitários, banheiros ou vestiários acessíveis) não está localizada entre 1,20 m e 1,60 m e/ou não está centralizada (ABNT NBR 9050:2020 - item 5.4.1)", 
                                        key="7sinalizacao_visual")
        if sinalizacao_visual:
            resultados["7.4 Sinalização Visual"] = "A sinalização visual (símbolo representativo) da(s) porta(s) (sanitários, banheiros ou vestiários acessíveis) não está localizada entre 1,20 m e 1,60 m e/ou não está centralizada (ABNT NBR 9050:2020 - item 5.4.1)"
            fotos["7.4 Sinalização Visual"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_sinalizacao_visual")

        # Pergunta 23
        sinalizacao_tatil = st.checkbox("Falta instalar a sinalização visual e tátil ao lado da porta do sanitário acessível. Deve estar localizada entre 1,20 m e 1,60 m, contendo informações em relevo e em braile (Sanitários, banheiros ou vestiários acessíveis - ABNT NBR 9050:2020 - item 5.4.1 e 5.2.8.1.3)", 
                                        key="7sinalizacao_tatil")
        if sinalizacao_tatil:
            resultados["7.5 Sinalização Tátil"] = "Falta instalar a sinalização visual e tátil ao lado da porta do sanitário acessível. Deve estar localizada entre 1,20 m e 1,60 m, contendo informações em relevo e em braile (Sanitários, banheiros ou vestiários acessíveis - ABNT NBR 9050:2020 - item 5.4.1 e 5.2.8.1.3)"
            fotos["7.5 Sinalização Tátil"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_sinalizacao_tatil")

        # Pergunta 24
        porta_externa = st.checkbox("A porta do sanitário não abre para o lado externo (ABNT NBR 9050:2020 - item 7.5.f)", 
                                    key="7porta_externa")
        if porta_externa:
            resultados["7.6 Abertura da Porta"] = "A porta do sanitário não abre para o lado externo (ABNT NBR 9050:2020 - item 7.5.f)."
            fotos["7.6 Abertura da Porta"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_porta_externa")

        # Pergunta 25
        puxador_horizontal = st.checkbox("A porta não tem puxador horizontal associado à maçaneta ou não está instalado do lado interno do ambiente e/ou o puxador horizontal não tem comprimento de 40 cm e/ou não está localizado a uma distância de 10 cm da face onde se encontra a dobradiça (ABNT NBR 9050:2020 - itens 4.6.6.3, 6.11.2.7, 7.5.f e 7.11.5)", 
                                        key="7puxador_horizontal")
        if puxador_horizontal:
            resultados["7.7 Puxador Horizontal"] = "A porta não tem puxador horizontal associado à maçaneta ou não está instalado do lado interno do ambiente e/ou o puxador horizontal não tem comprimento de 40 cm e/ou não está localizado a uma distância de 10 cm da face onde se encontra a dobradiça (ABNT NBR 9050:2020 - itens 4.6.6.3, 6.11.2.7, 7.5.f e 7.11.5)"
            fotos["7.7 Puxador Horizontal"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_puxador_horizontal")

        # Pergunta 26
        vao_livre = st.checkbox("A porta de acesso ao sanitário não tem vão livre mínimo de 80cm e 2,10 m de altura (válido para todos os tipos de portas: de abrir, de correr e sanfonadas) (ABNT NBR 9050:2020 - itens 6.11.2.4 e 7.5.g)", 
                                key="7vao_livre")
        if vao_livre:
            resultados["7.8 Vão Livre da Porta"] = "A porta de acesso ao sanitário não tem vão livre mínimo de 80cm e 2,10 m de altura (válido para todos os tipos de portas: de abrir, de correr e sanfonadas) (ABNT NBR 9050:2020 - itens 6.11.2.4 e 7.5.g)"
            fotos["7.8 Vão Livre da Porta"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_vao_livre")

        # Pergunta 27
        macaneta_alavanca = st.checkbox("Maçanetas de portas não são do tipo alavanca, com pelo menos 100 mm de comprimento e acabamento sem arestas e recurvado na extremidade, e/ou não estão instaladas a uma altura entre 0,80 m e 1,10 m (ABNT NBR 9050:2020 - itens 4.6.6.1 e 6.11.2.6)", 
                                        key="7macaneta_alavanca")
        if macaneta_alavanca:
            resultados["7.9 Maçaneta Tipo Alavanca"] = "Maçanetas de portas não são do tipo alavanca, com pelo menos 100 mm de comprimento e acabamento sem arestas e recurvado na extremidade, e/ou não estão instaladas a uma altura entre 0,80 m e 1,10 m (ABNT NBR 9050:2020 - itens 4.6.6.1 e 6.11.2.6)"
            fotos["7.9 Maçaneta Tipo Alavanca"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_macaneta_alavanca")

        # Pergunta 28
        puxador_vertical = st.checkbox("Puxador vertical de portas não tem no mínimo 0,30m de comprimento e/ou não está instalado à altura entre 0,80m e 1,10m do piso e/ou não está afastado 0,10 m do batente (ABNT NBR 9050:2020 - item 4.6.6.2)", 
                                    key="7puxador_vertical")
        if puxador_vertical:
            resultados["7.10 Puxador Vertical"] = "Puxador vertical de portas não tem no mínimo 0,30m de comprimento e/ou não está instalado à altura entre 0,80m e 1,10m do piso e/ou não está afastado 0,10 m do batente (ABNT NBR 9050:2020 - item 4.6.6.2)"
            fotos["7.10 Puxador Vertical"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_puxador_vertical")

        # Pergunta 29
        bacia_abertura_frontal = st.checkbox("Bacia sanitária com abertura frontal. (O vaso sanitário com abertura frontal pode ser usado apenas em estabelecimentos de saúde) (ABNT NBR 9050:2020 - item 7.7.2.1)", 
                                            key="7bacia_abertura_frontal")
        if bacia_abertura_frontal:
            resultados["7.11 Bacia Sanitária com Abertura Frontal"] = "Bacia sanitária com abertura frontal. (O vaso sanitário com abertura frontal pode ser usado apenas em estabelecimentos de saúde) (ABNT NBR 9050:2020 - item 7.7.2.1)"
            fotos["7.11 Bacia Sanitária com Abertura Frontal"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_bacia_abertura_frontal")

        # Pergunta 30
        altura_bacia = st.checkbox("A altura da bacia sanitária (vaso) não está a 46cm, com assento, ou entre 43cm e 45cm, sem assento (ABNT NBR 9050:2020 - item 7.7.2.1)", 
                                key="7altura_bacia")
        if altura_bacia:
            resultados["7.12 Altura da Bacia Sanitária"] = "A altura da bacia sanitária (vaso) não está a 46cm, com assento, ou entre 43cm e 45cm, sem assento (ABNT NBR 9050:2020 - item 7.7.2.1)"
            fotos["7.12 Altura da Bacia Sanitária"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_altura_bacia")

        # Pergunta 31
        barras_convencional = st.checkbox("As barras de apoio (bacia convencional com parede lateral) não foram instaladas e/ou não estão corretamente instaladas (ABNT NBR 9050:2020: item 7.7.2.3.1)", 
                                        key="7barras_convencional")
        if barras_convencional:
            resultados["7.13 Barras de Apoio - Bacia Convencional"] = "As barras de apoio (bacia convencional com parede lateral) não foram instaladas e/ou não estão corretamente instaladas (ABNT NBR 9050:2020: item 7.7.2.3.1)"
            fotos["7.13 Barras de Apoio - Bacia Convencional"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_barras_convencional")

        # Pergunta 32
        barras_suspensa = st.checkbox("As barras de apoio (bacia suspensa com parede lateral) não foram instaladas e/ou não estão corretamente instaladas (ABNT NBR 9050:2020: item 7.7.2.3.2)", 
                                    key="7barras_suspensa")
        if barras_suspensa:
            resultados["7.14 Barras de Apoio - Bacia Suspensa"] = "As barras de apoio (bacia suspensa com parede lateral) não foram instaladas e/ou não estão corretamente instaladas (ABNT NBR 9050:2020: item 7.7.2.3.2)"
            fotos["7.14 Barras de Apoio - Bacia Suspensa"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_barras_suspensa")

        # Pergunta 33
        barras_acoplada = st.checkbox("As barras de apoio (bacia com caixa acoplada com parede lateral) não foram instaladas e/ou não estão corretamente instaladas (ABNT NBR 9050:2020: item 7.7.2.3.3)", 
                                    key="7barras_acoplada")
        if barras_acoplada:
            resultados["7.15 Barras de Apoio - Bacia com Caixa Acoplada"] = "As barras de apoio (bacia com caixa acoplada com parede lateral) não foram instaladas e/ou não estão corretamente instaladas (ABNT NBR 9050:2020: item 7.7.2.3.3)"
            fotos["7.15 Barras de Apoio - Bacia com Caixa Acoplada"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_barras_acoplada")

        # Pergunta 34
        barras_reta_fixa = st.checkbox("As barras de apoio (bacia convencional ou suspensa, com barra de apoio reta e barra lateral fixa) não foram instaladas e/ou não estão corretamente instaladas (ABNT NBR 9050:2020: item 7.7.2.4.1)", 
                                    key="7barras_reta_fixa")
        if barras_reta_fixa:
            resultados["7.16 Barras de Apoio - Bacia Convencional/Suspensa com Barra Reta e Fixa"] = "As barras de apoio (bacia convencional ou suspensa, com barra de apoio reta e barra lateral fixa) não foram instaladas e/ou não estão corretamente instaladas (ABNT NBR 9050:2020: item 7.7.2.4.1)"
            fotos["7.16 Barras de Apoio - Bacia Convencional/Suspensa com Barra Reta e Fixa"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_barras_reta_fixa")

        # Pergunta 35
        barras_acoplada_reta_fixa = st.checkbox("As barras de apoio (bacia com caixa acoplada com barra de apoio reta e barra lateral fixa) não foram instaladas e/ou não estão corretamente instaladas (ABNT NBR 9050:2020: item 7.7.2.4.2)", 
                                                key="7barras_acoplada_reta_fixa")
        if barras_acoplada_reta_fixa:
            resultados["7.17 Barras de Apoio - Bacia com Caixa Acoplada com Barra Reta e Fixa"] = "As barras de apoio (bacia com caixa acoplada com barra de apoio reta e barra lateral fixa) não foram instaladas e/ou não estão corretamente instaladas (ABNT NBR 9050:2020: item 7.7.2.4.2)"
            fotos["7.17 Barras de Apoio - Bacia com Caixa Acoplada com Barra Reta e Fixa"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_barras_acoplada_reta_fixa")

        # Pergunta 36
        barras_acoplada_articulada = st.checkbox("As barras de apoio (bacia com caixa acoplada, com barras lateral articulada e fixa) não foram instaladas e/ou não estão corretamente instaladas (ABNT NBR 9050:2020: item 7.7.2.4.3)", 
                                                key="7barras_acoplada_articulada")
        if barras_acoplada_articulada:
            resultados["7.18 Barras de Apoio - Bacia com Caixa Acoplada com Barra Articulada"] = "As barras de apoio (bacia com caixa acoplada, com barras lateral articulada e fixa) não foram instaladas e/ou não estão corretamente instaladas (ABNT NBR 9050:2020: item 7.7.2.4.3)"
            fotos["7.18 Barras de Apoio - Bacia com Caixa Acoplada com Barra Articulada"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_barras_acoplada_articulada")

        # Pergunta 7.19
        valvula_descarga = st.checkbox("A válvula de descarga está com altura acima de 1,00m e/ou não tem acionamento facilitado (ABNT NBR 9050:2020: item 7.7.3)", 
                                        key="7valvula_descarga")
        if valvula_descarga:
            resultados["7.19 Válvula de Descarga"] = "A válvula de descarga está com altura acima de 1,00m e/ou não tem acionamento facilitado (ABNT NBR 9050:2020: item 7.7.3)"
            fotos["7.19 Válvula de Descarga"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_valvula_descarga")
        
        # Pergunta 7.20
        tampo_lavatorio = st.checkbox("O tampo para lavatório não possui altura entre 0,78m e 0,80m, e livre inferior de 0,73 m (ABNT NBR 9050:2020: itens 7.5.e e 7.8)", 
                                        key="7tampo_lavatorio")
        if tampo_lavatorio:
            resultados["7.20 Tampo para Lavatório"] = "O tampo para lavatório não possui altura entre 0,78m e 0,80m, e livre inferior de 0,73 m (ABNT NBR 9050:2020: itens 7.5.e e 7.8)"
            fotos["7.20 Tampo para Lavatório"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_tampo_lavatorio")
        
        # Pergunta 7.21
        barra_apoio_lavatorio = st.checkbox("Falta barra de apoio no lavatório e/ou não está devidamente instalada (ABNT NBR 9050:2020: item 7.8.1)", 
                                        key="7barra_apoio_lavatorio")
        if barra_apoio_lavatorio:
            resultados["7.21 Barra de Apoio no Lavatório"] = "Falta barra de apoio no lavatório e/ou não está devidamente instalada (ABNT NBR 9050:2020: item 7.8.1)"
            fotos["7.21 Barra de Apoio no Lavatório"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_barra_apoio_lavatorio")
        
        # Pergunta 7.22
        torneira_lavatorio = st.checkbox("A torneira do lavatório não é acionada por alavanca, sensor eletrônico ou dispositivo equivalente (ABNT NBR 9050:2020: item 7.8.2)", 
                                        key="7torneira_lavatorio")
        if torneira_lavatorio:
            resultados["7.22 Torneira do Lavatório"] = "A torneira do lavatório não é acionada por alavanca, sensor eletrônico ou dispositivo equivalente (ABNT NBR 9050:2020: item 7.8.2)"
            fotos["7.22 Torneira do Lavatório"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_torneira_lavatorio")
        
        # Pergunta 7.23
        manuseio_acessorios = st.checkbox("O ponto de manuseio dos acessórios (porta-objeto, cabides, saboneteiras e toalheiro) do sanitário não está entre 0,80m e 1,20m de altura (ABNT NBR 9050:2020: itens 7.11)", 
                                        key="7manuseio_acessorios")
        if manuseio_acessorios:
            resultados["7.23 Manuseio de Acessórios"] = "O ponto de manuseio dos acessórios (porta-objeto, cabides, saboneteiras e toalheiro) do sanitário não está entre 0,80m e 1,20m de altura (ABNT NBR 9050:2020: itens 7.11)"
            fotos["7.23 Manuseio de Acessórios"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_manuseio_acessorios")
        
        # Pergunta 7.24
        espelho_altura = st.checkbox("O espelho não está instalado a uma altura de 0,90 m quando atrás da bancada e/ou entre 0,50 m e 1,80 m quando instalado na parede (ABNT NBR 9050:2020 - item 7.11.1)", key="7espelho_altura")
        if espelho_altura:
            resultados["7.24 Espelho Altura"] = "O espelho não está instalado a uma altura de 0,90 m quando atrás da bancada e/ou entre 0,50 m e 1,80 m quando instalado na parede (ABNT NBR 9050:2020 - item 7.11.1)"
            fotos["7.24 Espelho Altura"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_espelho_altura")
        
        # Pergunta 7.25
        box_chuveiro_dimensoes = st.checkbox("O box de chuveiro não tem dimensões mínimas de 0,90m x 0,95m (ABNT NBR 9050:2020 - item 7.12.1.2)", key="7box_chuveiro_dimensoes")
        if box_chuveiro_dimensoes:
            resultados["7.25 Box Chuveiro Dimensões"] = "O box de chuveiro não tem dimensões mínimas de 0,90m x 0,95m (ABNT NBR 9050:2020 - item 7.12.1.2)"
            fotos["7.25 Box Chuveiro Dimensões"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_box_chuveiro_dimensoes")
        
        # Pergunta 7.26
        registro_pressao_chuveiro = st.checkbox("O registro de pressão (acionamento do chuveiro) não está instalado a 1,00 m de altura e/ou não é acionado por alavanca (ABNT NBR 9050:2020 - item 7.12.2)", key="7registro_pressao_chuveiro")
        if registro_pressao_chuveiro:
            resultados["7.26 Registro Pressão Chuveiro"] = "O registro de pressão (acionamento do chuveiro) não está instalado a 1,00 m de altura e/ou não é acionado por alavanca (ABNT NBR 9050:2020 - item 7.12.2)"
            fotos["7.26 Registro Pressão Chuveiro"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_registro_pressao_chuveiro")
        
        # Pergunta 7.27
        desnivel_piso_box = st.checkbox("Há desnível no piso do box do chuveiro. Deve estar em nível com o piso adjacente e ser antiderrapante (ABNT NBR 9050:2020 - item 7.12.4)", key="7desnivel_piso_box")
        if desnivel_piso_box:
            resultados["7.27 Desnível Piso Box"] = "Há desnível no piso do box do chuveiro. Deve estar em nível com o piso adjacente e ser antiderrapante (ABNT NBR 9050:2020 - item 7.12.4)"
            fotos["7.27 Desnível Piso Box"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_desnivel_piso_box")

        # Pergunta 7.28
        banco_chuveiro = st.checkbox("Falta banco articulado ou removível no box para chuveiro e/ou não é antiderrapante e/ou tem profundidade menor que 45cm e/ou tem comprimento menor que 70cm e/ou não tem 46cm de altura. (ABNT NBR 9050:2020 - item 7.12.3)", 
                                      key="7banco_chuveiro")
        if banco_chuveiro:
            resultados["7.28 Banco no Box do Chuveiro"] = "Falta banco articulado ou removível no box para chuveiro e/ou não é antiderrapante e/ou tem profundidade menor que 45cm e/ou tem comprimento menor que 70cm e/ou não tem 46cm de altura. (ABNT NBR 9050:2020 - item 7.12.3)"
            fotos["7.28 Banco no Box do Chuveiro"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_banco_chuveiro")

        # Pergunta 7.29
        ducha_manual = st.checkbox("O chuveiro não está equipado com desviador para ducha manual e/ou a ducha não está a 30cm afastada da parede onde está fixado o banco (ABNT NBR 9050:2020 - item 7.12.2)", 
                                   key="7ducha_manual")
        if ducha_manual:
            resultados["7.29 Ducha Manual"] = "O chuveiro não está equipado com desviador para ducha manual e/ou a ducha não está a 30cm afastada da parede onde está fixado o banco (ABNT NBR 9050:2020 - item 7.12.2)"
            fotos["7.29 Ducha Manual"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_ducha_manual")

        # Pergunta 7.30
        barras_apoio_chuveiro = st.checkbox("Faltam barras de apoio junto ao chuveiro ou não estão devidamente instaladas (ABNT NBR 9050:2020 - item 7.12.3)", 
                                            key="7barras_apoio_chuveiro")
        if barras_apoio_chuveiro:
            resultados["7.30 Barras de Apoio no Chuveiro"] = "Faltam barras de apoio junto ao chuveiro ou não estão devidamente instaladas (ABNT NBR 9050:2020 - item 7.12.3)"
            fotos["7.30 Barras de Apoio no Chuveiro"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_barras_apoio_chuveiro")

        # Pergunta 7.31
        dispositivo_alarme = st.checkbox("Falta dispositivo de alarme próximo à bacia sanitária ou ao lavatório e/ou não está instalado a 40cm do piso (ABNT NBR 9050:2020 - item 5.6.4.1)", 
                                        key="7dispositivo_alarme")
        if dispositivo_alarme:
            resultados["7.31 Dispositivo de Alarme"] = "Falta dispositivo de alarme próximo à bacia sanitária ou ao lavatório e/ou não está instalado a 40cm do piso (ABNT NBR 9050:2020 - item 5.6.4.1)"
            fotos["7.31 Dispositivo de Alarme"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="7foto_dispositivo_alarme")

    # Tópico 8: Box para pessoas com deficiência no sanitário coletivo
    with st.expander("## **8.0 Box para pessoas com deficiência no sanitário coletivo**"):
        
        boxe_giro = st.checkbox("Não há dimensões mínimas do boxe para permitir o giro de 360 graus, área para manobra e área de transferência para a bacia sanitária por uma pessoa em cadeira de rodas. (NBR 9050 item 7.5 e 7.7.1)", key="8boxe_giro")
        
        if boxe_giro:
            resultados["8.1 Boxe - Giro 360 graus e manobra"] = "Não há dimensões mínimas do boxe para permitir o giro de 360 graus, área para manobra e área de transferência para a bacia sanitária por uma pessoa em cadeira de rodas. (NBR 9050 item 7.5 e 7.7.1)"
            fotos["8.1 Boxe - Giro 360 graus e manobra"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9foto_boxe_giro")
        
        porta_boxe_externo = st.checkbox("A porta do boxe não abre para o lado externo (ABNT NBR 9050:2020 - item 7.5.f)", key="8porta_boxe_externo")

        if porta_boxe_externo:
            resultados["8.2 Porta Boxe - Lado Externo"] = "A porta do boxe não abre para o lado externo (ABNT NBR 9050:2020 - item 7.5.f)"
            fotos["8.2 Porta Boxe - Lado Externo"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9foto_porta_boxe_externo")
        
        puxador_porta_boxe = st.checkbox("A porta do boxe não tem puxador horizontal, instalado do lado interno do ambiente, com comprimento mínimo de 0,40m e localizado a 0,10m da dobradiça e com altura de 0,90m. (NBR 9050 item 6.11.2.7)", key="8puxador_porta_boxe")
        
        if puxador_porta_boxe:
            resultados["8.3 Puxador Porta Boxe"] = "A porta do boxe não tem puxador horizontal, instalado do lado interno do ambiente, com comprimento mínimo de 0,40m e localizado a 0,10m da dobradiça e com altura de 0,90m. (NBR 9050 item 6.11.2.7)"
            fotos["8.3 Puxador Porta Boxe"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9foto_puxador_porta_boxe")

        dispositivo_alarme = st.checkbox("Falta dispositivo de alarme instalado a 40cm do piso. (NBR 9050 item 7.4.2.2)", key="8dispositivo_alarme")

        if dispositivo_alarme:
            resultados["8.4 Dispositivo de Alarme"] = "Falta dispositivo de alarme instalado a 40cm do piso. (NBR 9050 item 7.4.2.2)"
            fotos["8.4 Dispositivo de Alarme"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9foto_dispositivo_alarme")

        puxador_vertical_boxe = st.checkbox("Falta puxador vertical no lado externo da porta do boxe com no mínimo 0,30m de comprimento e instalado à altura entre 0,80m e 1,10m. (ABNT NBR 9050:2020 - item 4.6.6.2)", key="8puxador_vertical_boxe")
        
        if puxador_vertical_boxe:
            resultados["8.5 Puxador Vertical Boxe"] = "Falta puxador vertical no lado externo da porta do boxe com no mínimo 0,30m de comprimento e instalado à altura entre 0,80m e 1,10m. (ABNT NBR 9050:2020 - item 4.6.6.2)"
            fotos["8.5 Puxador Vertical Boxe"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9foto_puxador_vertical_boxe")


        altura_bacia_sanitária = st.checkbox("A bacia sanitária não tem altura entre 43cm e 45cm. (NBR 9050 item 7.7.2.1)", key="8altura_bacia_sanitária")

        if altura_bacia_sanitária:
            resultados["8.6 Altura Bacia Sanitária"] = "A bacia sanitária não tem altura entre 43cm e 45cm. (NBR 9050 item 7.7.2.1)"
            fotos["8.6 Altura Bacia Sanitária"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9foto_altura_bacia_sanitária")


        barra_apoio_lateral_bacia = st.checkbox("A barra de apoio horizontal, fixada na parede lateral da bacia sanitária, não está instalada a uma altura de 0,75m do piso. (NBR 9050 item 7.7.2.2.1)", key="8barra_apoio_lateral_bacia")

        if barra_apoio_lateral_bacia:
            resultados["8.7 Barra Apoio Lateral Bacia"] = "A barra de apoio horizontal, fixada na parede lateral da bacia sanitária, não está instalada a uma altura de 0,75m do piso. (NBR 9050 item 7.7.2.2.1)"
            fotos["8.7 Barra Apoio Lateral Bacia"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9foto_barra_apoio_lateral_bacia")

        
        barra_apoio_fundo_bacia = st.checkbox("Falta barra de apoio horizontal, fixada na parede do fundo da bacia sanitária, com comprimento mínimo de 0,80m e instalada a uma altura de 0,75m do piso. (NBR 9050 item 7.7.2.2.1)", key="8barra_apoio_fundo_bacia")
        
        if barra_apoio_fundo_bacia:
            resultados["8.8 Barra Apoio Fundo Bacia"] = "Falta barra de apoio horizontal, fixada na parede do fundo da bacia sanitária, com comprimento mínimo de 0,80m e instalada a uma altura de 0,75m do piso. (NBR 9050 item 7.7.2.2.1)"
            fotos["8.8 Barra Apoio Fundo Bacia"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9foto_barra_apoio_fundo_bacia")
        
        
        barra_apoio_vertical_bacia = st.checkbox("Falta barra de apoio vertical, fixada na parede lateral da bacia sanitária, com comprimento de 0,70m e posicionada a 0,10m acima da barra horizontal e a 0,30m da borda frontal da bacia sanitária. (NBR 9050 item 7.7.2.2.1)", key="8barra_apoio_vertical_bacia")
        
        if barra_apoio_vertical_bacia:
            resultados["8.9 Barra Apoio Vertical Bacia"] = "Falta barra de apoio vertical, fixada na parede lateral da bacia sanitária, com comprimento de 0,70m e posicionada a 0,10m acima da barra horizontal e a 0,30m da borda frontal da bacia sanitária. (NBR 9050 item 7.7.2.2.1)"
            fotos["8.9 Barra Apoio Vertical Bacia"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9foto_barra_apoio_vertical_bacia")

        
        lavatório_no_boxe = st.checkbox("Falta lavatório dentro do boxe que deve ser instalado com altura entre 0,78m e 0,80m e com barras de apoio. (NBR 9050 item 7.5d)", key="8lavatório_no_boxe")
        
        if lavatório_no_boxe:
            resultados["8.10 Lavatório no Boxe"] = "Falta lavatório dentro do boxe que deve ser instalado com altura entre 0,78m e 0,80m e com barras de apoio. (NBR 9050 item 7.5d)"
            fotos["8.10 Lavatório no Boxe"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9foto_lavatório_no_boxe")

    # Tópico 9: Piscina
    with st.expander("## **9.0 Piscina**"):
        # Pergunta 9
        rampa_ou_equipamento = st.checkbox("Falta rampa, ou equipamento de acesso, ou banco de transferência ou escada para acesso à água (ABNT NBR 9050:2020 - item 10.2.2)", 
                                            key="9rampa_ou_equipamento")
        if rampa_ou_equipamento:
            resultados["9.1 Falta Rampa ou Equipamento de Acesso"] = "Falta rampa, ou equipamento de acesso, ou banco de transferência ou escada para acesso à água (ABNT NBR 9050:2020 - item 10.2.2)"
            fotos["9 Falta Rampa ou Equipamento de Acesso"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9foto_rampa_ou_equipamento")

        # Pergunta 9.1
        banco_transferencia_agua = st.checkbox("O banco de transferência para acesso à água não tem altura entre 0,40 e 0,48m e/ou não tem extensão de no mínimo 1,20m por 0,45m de profundidade e/ou não possui barras entre 1,00 m e 1,10 m (ABNT NBR 9050:2020 - item 10.12.2.1)", 
                                            key="9.1banco_transferencia_agua")
        if banco_transferencia_agua:
            resultados["9.2 Banco de Transferência para Acesso à Água"] = "O banco de transferência para acesso à água não tem altura entre 0,40 e 0,48m e/ou não tem extensão de no mínimo 1,20m por 0,45m de profundidade e/ou não possui barras entre 1,00 m e 1,10 m (ABNT NBR 9050:2020 - item 10.12.2.1)"
            fotos["9.1 Banco de Transferência para Acesso à Água"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9.1foto_banco_transferencia_agua")

        # Pergunta 9.2
        escada_acesso_agua = st.checkbox("A escada para acesso à água não possui largura entre 0,80 m e 1,00 m e/ou os degraus não possuem piso entre 0,35 m e 0,46 m e/ou o espelho não possui no máximo 0,20 m (ABNT NBR 9050:2020 - item 10.12.2.2)", 
                                        key="9.2escada_acesso_agua")
        if escada_acesso_agua:
            resultados["9.3 Escada para Acesso à Água"] = "A escada para acesso à água não possui largura entre 0,80 m e 1,00 m e/ou os degraus não possuem piso entre 0,35 m e 0,46 m e/ou o espelho não possui no máximo 0,20 m (ABNT NBR 9050:2020 - item 10.12.2.2)"
            fotos["9.2 Escada para Acesso à Água"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9.2foto_escada_acesso_agua")

        # Pergunta 9.3
        corrimao_escada = st.checkbox("A escada para acesso à água não possui corrimão dos dois lados em três alturas (0,45 m, 0,70 m e 0,92 m) (ABNT NBR 9050:2020 - item 10.12.2.2)", 
                                    key="9.3corrimao_escada")
        if corrimao_escada:
            resultados["9.4 Corrimão na Escada para Acesso à Água"] = "A escada para acesso à água não possui corrimão dos dois lados em três alturas (0,45 m, 0,70 m e 0,92 m) (ABNT NBR 9050:2020 - item 10.12.2.2)"
            fotos["9.3 Corrimão na Escada para Acesso à Água"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9.3foto_corrimao_escada")

        # Pergunta 9.4
        rampa_inclinacao = st.checkbox("A rampa para acesso à água possui inclinação superior a 8,33% e/ou não possui corrimão dos dois lados, a 0,70 m do piso (ABNT NBR 9050:2020 - item 10.12.2.3)", 
                                    key="9.4rampa_inclinacao")
        if rampa_inclinacao:
            resultados["9.5 Rampa para Acesso à Água"] = "A rampa para acesso à água possui inclinação superior a 8,33% e/ou não possui corrimão dos dois lados, a 0,70 m do piso (ABNT NBR 9050:2020 - item 10.12.2.3)"
            fotos["9.4 Rampa para Acesso à Água"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9.4foto_rampa_inclinacao")

        # Pergunta 9.5
        acesso_ducha = st.checkbox("Não há acesso à pessoa em cadeira de rodas a pelo menos uma das duchas (ABNT NBR 9050:2020 - item 10.12.2.3)", 
                                key="9.5acesso_ducha")
        if acesso_ducha:
            resultados["9.6 Acesso à Pessoa em Cadeira de Rodas à Ducha"] = "Não há acesso à pessoa em cadeira de rodas a pelo menos uma das duchas (ABNT NBR 9050:2020 - item 10.12.2.3)"
            fotos["9.5 Acesso à Pessoa em Cadeira de Rodas à Ducha"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="9.5foto_acesso_ducha")

        #
        # Tópico 10: Elevador acessível (pelo menos um elevador por prumada deve atender os requisitos de acessibilidade)
    with st.expander("## **10.0 Elevador acessível (pelo menos um elevador por prumada deve atender os requisitos de acessibilidade)**"):
        # Pergunta 10.1

        sinalizacao_batente = st.checkbox("Falta sinalização tátil indicando o pavimento com caracteres em relevo e em Braille nos dois lados do batente da porta do elevador. Deverão estar instalados a uma altura entre 1,20 m e 1,60 m (ABNT NBR 9050:2020 -item 5.4.5.2)", 
                                        key="10sinalizacao_batente")
        if sinalizacao_batente:
            resultados["10.1 Sinalização Tátil Batente"] = "Falta sinalização tátil indicando o pavimento com caracteres em relevo e em Braille nos dois lados do batente da porta do elevador. Deverão estar instalados a uma altura entre 1,20 m e 1,60 m (ABNT NBR 9050:2020 -item 5.4.5.2)"
            fotos["10.1 Sinalização Tátil Batente"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="10foto_sinalizacao_batente")

        # Pergunta 10.2
        sinalizacao_alerta = st.checkbox("Falta sinalização tátil de alerta no piso em frente à porta do elevador (ABNT NBR 16537:2024 - item 6.9.1)", 
                                        key="10sinalizacao_alerta")
        if sinalizacao_alerta:
            resultados["10.2 Sinalização Tátil de Alerta"] = "Falta sinalização tátil de alerta no piso em frente à porta do elevador (ABNT NBR 16537:2024 - item 6.9.1)"
            fotos["10.2 Sinalização Tátil de Alerta"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="10foto_sinalizacao_alerta")

        # Pergunta 10.3
        corrimao_elevador = st.checkbox("Não há corrimãos nos três lados da cabine do elevador (NM 313/2007 - item 5.3.2.1)", 
                                        key="10corrimao_elevador")
        if corrimao_elevador:
            resultados["10.3 Corrimãos na Cabine"] = "Não há corrimãos nos três lados da cabine do elevador (NM 313/2007 - item 5.3.2.1)"
            fotos["10.3 Corrimãos na Cabine"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="10foto_corrimao_elevador")

        # Pergunta 10.4
        espelho_cabine = st.checkbox("O elevador não tem espelho na face oposta à porta ou outro dispositivo que permita ao usuário de cadeira de rodas observar obstáculos quando mover-se para trás ao sair do elevador (NM 313/2007 - item 5.3.2.3)", 
                                    key="10espelho_cabine")
        if espelho_cabine:
            resultados["10.4 Espelho ou Dispositivo"] = "O elevador não tem espelho na face oposta à porta ou outro dispositivo que permita ao usuário de cadeira de rodas observar obstáculos quando mover-se para trás ao sair do elevador (NM 313/2007 - item 5.3.2.3)"
            fotos["10.4 Espelho ou Dispositivo"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="10foto_espelho_cabine")

        # Pergunta 10.5
        revestimento_piso = st.checkbox("O revestimento do piso da cabina não possui superfície dura e/ou antiderrapante e/ou as cores do piso não são contrastantes com as do piso do pavimento (NM 313/2007 - item E 6.3)", 
                                    key="10revestimento_piso")
        if revestimento_piso:
            resultados["10.5 Revestimento de Piso"] = "O revestimento do piso da cabina não possui superfície dura e/ou antiderrapante e/ou as cores do piso não são contrastantes com as do piso do pavimento (NM 313/2007 - item E 6.3)"
            fotos["10.5 Revestimento de Piso"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="10foto_revestimento_piso")
    
        # Tópico 11: Sanitário coletivo
    with st.expander("## **11 Sanitário coletivo**"):
        # Pergunta 11.1
        porta_acesso_sanitario = st.checkbox("A porta de acesso ao sanitário não tem vão livre mínimo de 80cm e 2,10 m de altura (válido para todos os tipos de portas: de abrir, de correr e sanfonadas) (ABNT NBR 9050:2020 - item 6.11.2.4)", 
                                            key="11porta_acesso_sanitario")
        if porta_acesso_sanitario:
            resultados["11.1 Porta de Acesso ao Sanitário"] = "A porta de acesso ao sanitário não tem vão livre mínimo de 80cm e 2,10 m de altura (válido para todos os tipos de portas: de abrir, de correr e sanfonadas) (ABNT NBR 9050:2020 - item 6.11.2.4)"
            fotos["11.1 Porta de Acesso ao Sanitário"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="11foto_porta_acesso_sanitario")

        # Pergunta 11.2
        macaneta_tipo_alavanca = st.checkbox("Maçanetas de portas não são do tipo alavanca, com pelo menos 100 mm de comprimento e acabamento sem arestas e recurvado na extremidade. Deverão estar instaladas a uma altura entre 0,80 m e 1,10 m (ABNT NBR 9050:2020 - itens 4.6.6.1 e 6.11.2.6)", 
                                            key="11macaneta_tipo_alavanca")
        if macaneta_tipo_alavanca:
            resultados["11.2 Maçaneta Tipo Alavanca"] = "Maçanetas de portas não são do tipo alavanca, com pelo menos 100 mm de comprimento e acabamento sem arestas e recurvado na extremidade. Deverão estar instaladas a uma altura entre 0,80 m e 1,10 m (ABNT NBR 9050:2020 - itens 4.6.6.1 e 6.11.2.6)"
            fotos["11.2 Maçaneta Tipo Alavanca"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="11foto_macaneta_tipo_alavanca")

        # Pergunta 11.3
        puxador_vertical = st.checkbox("Puxador vertical de portas não tem no mínimo 0,30m de comprimento. Deverá estar instalado à altura entre 0,80m e 1,10m do piso e, afastado 0,10 m do batente (ABNT NBR 9050:2020 - item 4.6.6.2)", 
                                    key="11puxador_vertical")
        if puxador_vertical:
            resultados["11.3 Puxador Vertical"] = "Puxador vertical de portas não tem no mínimo 0,30m de comprimento. Deverá estar instalado à altura entre 0,80m e 1,10m do piso e, afastado 0,10 m do batente (ABNT NBR 9050:2020 - item 4.6.6.2)"
            fotos["11.3 Puxador Vertical"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="11foto_puxador_vertical")

        # Pergunta 11.4
        sinalizacao_visual_porta = st.checkbox("A sinalização visual da(s) porta(s) não está localizada entre 1,20 m e 1,60 m e/ou não está centralizada (ABNT NBR 9050:2020 - item 5.4.1)", 
                                            key="11sinalizacao_visual_porta")
        if sinalizacao_visual_porta:
            resultados["11.4 Sinalização Visual da Porta"] = "A sinalização visual da(s) porta(s) não está localizada entre 1,20 m e 1,60 m e/ou não está centralizada (ABNT NBR 9050:2020 - item 5.4.1)"
            fotos["11.4 Sinalização Visual da Porta"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="11foto_sinalizacao_visual_porta")

        # Pergunta 11.5
        sinalizacao_visual_tatil = st.checkbox("A sinalização visual e tátil ao lado da(s) porta(s) não está localizada entre 1,20 m e 1,60 e/ou não contém informações em relevo e em braile (ABNT NBR 9050:2020 - itens 5.4.1 e 5.2.8.1.3)", 
                                            key="11sinalizacao_visual_tatil")
        if sinalizacao_visual_tatil:
            resultados["11.5 Sinalização Visual e Tátil"] = "A sinalização visual e tátil ao lado da(s) porta(s) não está localizada entre 1,20 m e 1,60 e/ou não contém informações em relevo e em braile (ABNT NBR 9050:2020 - itens 5.4.1 e 5.2.8.1.3)"
            fotos["11.5 Sinalização Visual e Tátil"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="11foto_sinalizacao_visual_tatil")

        # Pergunta 11.6
        porta_acesso_boxes = st.checkbox("A porta de acesso aos boxes não possui largura mínima de 60 cm (edificações antigas) ou 80 cm (edificações novas) (ABNT NBR 9050:2020 - item 7.10.1)", 
                                        key="11porta_acesso_boxes")
        if porta_acesso_boxes:
            resultados["11.6 Porta de Acesso aos Boxes"] = "A porta de acesso aos boxes não possui largura mínima de 60 cm (edificações antigas) ou 80 cm (edificações novas) (ABNT NBR 9050:2020 - item 7.10.1)"
            fotos["11.6 Porta de Acesso aos Boxes"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="11foto_porta_acesso_boxes")

        # Pergunta 11.7
        tampo_lavatórios = st.checkbox("O tampo para lavatórios não possui no mínimo uma cuba com superfície superior entre 0,78 m e 0,80 m, e livre inferior de 0,73 m. Esta cuba deverá estar dotada de barra de apoio e equipada com torneira acionada por alavancas, sensores eletrônicos ou dispositivos equivalentes (ABNT NBR 9050:2020 - itens 7.8.1, 7.8.2 e 7.10.3)", 
                                    key="11tampo_lavatorios")
        if tampo_lavatórios:
            resultados["11.7 Tampo para Lavatórios"] = "O tampo para lavatórios não possui no mínimo uma cuba com superfície superior entre 0,78 m e 0,80 m, e livre inferior de 0,73 m. Esta cuba deverá estar dotada de barra de apoio e equipada com torneira acionada por alavancas, sensores eletrônicos ou dispositivos equivalentes (ABNT NBR 9050:2020 - itens 7.8.1, 7.8.2 e 7.10.3)"
            fotos["11.7 Tampo para Lavatórios"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="11foto_tampo_lavatorios")

        # Pergunta 11.8
        barras_apoio_mictorio = st.checkbox("Falta instalar barras de apoio em pelo menos um dos mictórios. As barras de apoio do mictório devem possuir 70cm de comprimento, estar a 75cm do piso e a 30cm do eixo do mictório (ABNT NBR 9050:2020 - item 7.10.4.3)", 
                                        key="11barras_apoio_mictorio")
        if barras_apoio_mictorio:
            resultados["11.8 Barras de Apoio em Mictório"] = "Falta instalar barras de apoio em pelo menos um dos mictórios. As barras de apoio do mictório devem possuir 70cm de comprimento, estar a 75cm do piso e a 30cm do eixo do mictório (ABNT NBR 9050:2020 - item 7.10.4.3)"
            fotos["11.8 Barras de Apoio em Mictório"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="11foto_barras_apoio_mictorio")

        # Pergunta 11.9
        borda_mictorio = st.checkbox("A borda do mictório não está entre 60cm e 65cm do piso (ABNT NBR 9050:2020 - item 7.10.4.3)", 
                                    key="11borda_mictorio")
        if borda_mictorio:
            resultados["11.9 Borda do Mictório"] = "A borda do mictório não está entre 60cm e 65cm do piso (ABNT NBR 9050:2020 - item 7.10.4.3)"
            fotos["11.9 Borda do Mictório"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="11foto_borda_mictorio")

        # Pergunta 11.10
        ponto_acionamento_valvula = st.checkbox("O ponto de acionamento da válvula de descarga do mictório não está a 1,00m de altura do piso (ABNT NBR 9050:2020 - item 7.10.4.2)", 
                                            key="11ponto_acionamento_valvula")
        if ponto_acionamento_valvula:
            resultados["11.10 Ponto de Acionamento da Válvula de Descarga"] = "O ponto de acionamento da válvula de descarga do mictório não está a 1,00m de altura do piso (ABNT NBR 9050:2020 - item 7.10.4.2)"
            fotos["11.10 Ponto de Acionamento da Válvula de Descarga"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="11foto_ponto_acionamento_valvula")

        # Pergunta 11.11
        ponto_manuseio_acessorios = st.checkbox("O ponto de manuseio dos acessórios (porta-objeto, cabides, saboneteiras e toalheiro) do sanitário não está entre 0,80m e 1,20m de altura (ABNT NBR 9050:2020: item 7.11)", 
                                                key="11ponto_manuseio_acessorios")
        if ponto_manuseio_acessorios:
            resultados["11.11 Ponto de Manuseio dos Acessórios"] = "O ponto de manuseio dos acessórios (porta-objeto, cabides, saboneteiras e toalheiro) do sanitário não está entre 0,80m e 1,20m de altura (ABNT NBR 9050:2020: item 7.11)"
            fotos["11.11 Ponto de Manuseio dos Acessórios"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="11foto_ponto_manuseio_acessorios")

        # Pergunta 11.12
        espelho_instalacao_altura = st.checkbox("O espelho não está instalado a uma altura de 0,90 m quando atrás da bancada e/ou entre 0,50m e 1,80m quando instalado na parede (ABNT NBR 9050:2020 - item 7.11.1)", 
                                            key="11espelho_instalacao_altura")
        if espelho_instalacao_altura:
            resultados["11.12 Espelho Instalação Altura"] = "O espelho não está instalado a uma altura de 0,90 m quando atrás da bancada e/ou entre 0,50m e 1,80m quando instalado na parede (ABNT NBR 9050:2020 - item 7.11.1)"
            fotos["11.12 Espelho Instalação Altura"] = st.file_uploader("Envie uma foto", type=["png", "jpg", "jpeg"], key="11foto_espelho_instalacao_altura")

    # Caixa de observações
    st.subheader("Observações:")
    observacoes = st.text_area("Escreva suas observações aqui:", key="observacoes")
    if observacoes:
        resultados["Observações"] = observacoes

    return resultados, fotos

# Função principal
def main():
    st.title("Relatório de acessibilidade")
    
    resultados, fotos = perguntas()

    # Exibe o resumo das respostas
    st.subheader("Resumo das Respostas:")
    for key, value in resultados.items():
        st.write(f"{key}: {value}")
    
    # Botão para gerar o arquivo .txt e .pdf
    if st.button("Confirmar relatório"):
        file_txt = gerar_txt(resultados)
        file_pdf = gerar_pdf(resultados, fotos)
        
        # Fornece os arquivos para download
        with open(file_txt, "r") as file:
            st.download_button(
                label="Baixar TXT",
                data=file,
                file_name=file_txt,
                mime="text/plain"
            )
        
        with open(file_pdf, "rb") as file:
            st.download_button(
                label="Baixar PDF",
                data=file,
                file_name=file_pdf,
                mime="application/pdf"
            )

if __name__ == "__main__":
    main()
