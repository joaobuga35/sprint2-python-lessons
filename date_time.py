from datetime import datetime, timedelta
STR_FORMATACAO = "Data de realização do exame:"
exame_realizado_em = datetime.now()
date_exame_str = exame_realizado_em.strftime("%d/%m/%y %H:%M:%S")
previsao_resultado = exame_realizado_em + timedelta(days=2)
previsao_str = previsao_resultado.strftime("%d/%m/%y %H:%M:%S")
TEMPO_RESULTADO_EXAME = "Previsão de entrega do resultado:"
print(STR_FORMATACAO + date_exame_str)
print()
print(TEMPO_RESULTADO_EXAME + previsao_str)