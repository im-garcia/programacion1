# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 60 # Lo dejo así y no en 61 porque mi variable mes arranca en 0.
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if mes >= pago_extra_mes_comienzo and mes < pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
    else: 
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    print(f'{mes} {total_pagado:0.2f} {saldo:0.2f}' )
print(f'Total pagado:  {total_pagado:0.2f}')
print(f'Meses: {mes}')