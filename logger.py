class RoundLogger:
    def __enter__(self):
        print("Начало раунда")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Конец раунда")
