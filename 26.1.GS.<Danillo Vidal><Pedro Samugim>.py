# -*- coding: utf-8 -*-
qtdEventos = int(input("Insira a quantidade de eventos: "))

lista_eventos = []
for i in range(qtdEventos):
    while True:
        print(f"\n--- Evento {i + 1} ---")
        while True:
            tipo_evento = input("Tipo:  ").strip()
            if tipo_evento.replace(" ", "").isalpha():
                break
            print("Invalido, Digite apenas letras! ")

        while True:
            pais = input("País: ").strip()
            if pais.replace(" ", "").isalpha():
                break
            print("Invalido, Digite apenas letras! ")

        while True:
            regiao = input("Região: ").strip()
            if regiao.replace(" ", "").isalpha():
                break
            print("Inválido, Digite apenas letras! ")

        while True:
            cidade = input("Cidade:  ").strip()
            if cidade.replace(" ", "").isalpha():
                break
            print("Inválido, Digite apenas letras! ")

        while True:
            a_afetada = float(input("Área: "))
            if a_afetada > 0:
                break
            print("Entrada inválida! Digite um número maior que zero")

        while True:
            intensidade = int(input("Intensidade: "))
            if 1 <= intensidade <= 10:
                break
            print("Entrada inválida! Digite um número dentro do intervalo de 1 a 10")

        n_ocorrencias = int(input("Ocorrências: "))

        
        print(f"\n--- Resumo do Evento {i + 1} ---")
        print(f"Tipo de evento: {tipo_evento}")
        print(f"País: {pais}")
        print(f"Região: {regiao}")
        print(f"Cidade: {cidade}")
        print(f"Área afetada: {a_afetada:.2f} km²")
        print(f"Intensidade: {intensidade}/10")
        print(f"Ocorrências: {n_ocorrencias}")

        confirma = input("\nOs dados estão corretos? (s/n): ").strip().lower()
        if confirma == "s":
            break
        print("\nVoltando ao cadastro do evento...")

    
    dados_evento = [tipo_evento, pais, regiao, cidade, a_afetada, intensidade, n_ocorrencias]

    
    lista_eventos.append(dados_evento)


total_area = sum(dados_evento[4] for dados_evento in lista_eventos)

media_intensidade = sum(dados_evento[5] for dados_evento in lista_eventos) / len(lista_eventos)


maior_ocorrencia = 0
regiao_mais_ocorrencias = ""
for dados_evento in lista_eventos:
    if dados_evento[6] > maior_ocorrencia:
        maior_ocorrencia = dados_evento[6]
        regiao_mais_ocorrencias = dados_evento[2]


cont_acima_media = 0
for dados_evento in lista_eventos:
    if dados_evento[5] > media_intensidade:
        cont_acima_media += 1


densidade_media = sum(dados_evento[6] for dados_evento in lista_eventos) / total_area


idx_critico = 0
for i in range(len(lista_eventos)):
    if lista_eventos[i][5] > lista_eventos[idx_critico][5]:
        idx_critico = i


print("\n" + "=" * 40)
print("        RELATÓRIO DE ANÁLISE")
print("=" * 40)
print(f"Total de eventos registrados: {len(lista_eventos)}")
print()
print("-" * 40)
print("Resumo Geral")
print("-" * 40)
print(f"Área total afetada: {total_area:.2f} km²")
print(f"Média de intensidade: {media_intensidade:.1f}")
print("-" * 40)
print()
print("-" * 40)
print("Análises")
print("-" * 40)
print(f"Região com maior número de ocorrências: {regiao_mais_ocorrencias}")
print(f"Quantidade de eventos acima da média: {cont_acima_media}")
print(f"Densidade média de ocorrências: {densidade_media:.2f} ocorr/km²")
print()
print("-" * 40)
print("Evento Mais Crítico")
print("-" * 40)
print(f"Tipo: {lista_eventos[idx_critico][0]}")
print(f"Local: {lista_eventos[idx_critico][3]}, {lista_eventos[idx_critico][2]}, {lista_eventos[idx_critico][1]}")
print(f"Intensidade: {lista_eventos[idx_critico][5]}/10")
print(f"Área: {lista_eventos[idx_critico][4]:.2f} km²")
print("=" * 40)
print(f"Total de desastres registrados: {len(lista_eventos)}")
