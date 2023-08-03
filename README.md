# Graphic-Calendar
Calendário gráfico simples utilizando Python, junto do framework Kivy.

## Classe GraphicCalendar

A classe `GraphicCalendar` representa o calendário gráfico.

## Atributos:

- `grid` (GraphicCalendarGrid): Grade do calendário.
- `month_label` (Label): Rótulo para exibir o nome do mês.
- `year_label` (Label): Rótulo para exibir o ano.
- `current_month` (tuple): Armazena o mês e o ano atualmente exibidos no calendário.

## Métodos:

### 1. __init__(self, month=1, year=2023, label_color='#000000', bg_color='#FFFFFF', bt_clean=True, **kwargs)

   Método construtor que inicializa o calendário gráfico.

   **Argumentos**:
   - `month` (int, opcional): Número do mês (1 a 12). O padrão é 1 (Janeiro).
   - `year` (int, opcional): Ano. O padrão é 2023.
   - `label_color` (str, opcional): Cor dos rótulos (mês e ano). Pode ser uma cor em formato hexadecimal ou um nome de cor suportado pelo Kivy. O padrão é preto (#000000).
   - `bg_color` (str, opcional): Cor de fundo do calendário. Pode ser uma cor em formato hexadecimal ou um nome de cor suportado pelo Kivy. O padrão é branco (#FFFFFF).
   - `bt_clean` (bool, opcional): Define se o fundo dos botões do calendário deve ser limpo (transparente). O padrão é True.
   - `**kwargs`: Argumentos adicionais para a classe BoxLayout.

### 2. set_month(self, month, year)

   Define o mês e o ano a serem exibidos no calendário.

   **Argumentos**:
   - `month` (int): Número do mês (1 a 12).
   - `year` (int): Ano.

### 3. current_monthrange(self)

   Retorna o número de dias do mês atualmente exibido no calendário.

   **Retorno**:
   - `int`: Número de dias do mês atualmente exibido.
  
