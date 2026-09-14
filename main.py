import gold_api
import time
from database import insert_gold_price
from market_status import is_market_open

def run_monitor():
    print("\n-- INICIANDO MONITOR DE MERCADO AURIFERO...")
    print("\n-- Presione Ctrl+C para detener el proceso.\n")

    while True:
        if not is_market_open():
            print(f"[SISTEMA] Mercado Forex cerrado en fin de semana. Pausando monitor por 1 hora...")
            time.sleep(900)
            continue

        api_data = gold_api.make_gold_api_request()

        if api_data is not None:
            timestamp, price = api_data
            insert_gold_price(timestamp, price)
            print(f"[{timestamp}] - Precio registrado exitosamente: ${price}.") 
        else:
            print(f"[SISTEMA] Fallo en la extracción. Reintentado...")
    
        time.sleep(300)

if __name__ == "__main__":
    try:
        run_monitor()
    except KeyboardInterrupt:
        print("\n[SALIDA] Monitor detenido manualmente. Cerrando sistema de forma segura...")