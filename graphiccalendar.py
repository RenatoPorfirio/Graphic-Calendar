import calendar
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.utils import get_color_from_hex as color
from kivy.graphics import Color, Rectangle

calendar.setfirstweekday(6)

def month_map(month):
    """
    Retorna o nome do mês com base no número do mês (1 a 12).

    Argumentos:
        month (int): Número do mês (1 a 12).

    Retorna:
        str: Nome do mês correspondente.
    """
    __map_of_months = [
            '',
            'Janeiro',
            'Fevereiro',
            'Março',
            'Abril',
            'Maio',
            'Junho',
            'Julho',
            'Agosto',
            'Setembro',
            'Outubro',
            'Novembro',
            'Dezembro'
            ]
    try:
        return __map_of_months[month]
    except:
        return __map_of_months[0]
    
def day_map(day):
    """
    Retorna o valor do mapa de dias com base no número do dia da semana.

    Argumentos:
        day (int): Número do dia da semana (0 a 6, sendo 0 Domingo).

    Retorna:
        int: Valor do mapa de dias correspondente.
    """
    __map_of_days = [1, 2, 3, 4, 5, 6, 0]
    try:
        return __map_of_days[day]
    except:
        return __map_of_days[0]

class GraphicCalendarGrid(GridLayout):
    """
    Classe que representa a grade do calendário.

    Atributos:
        selected (ToggleButton): Armazena o botão selecionado atualmente.
        buttons (list): Lista de botões na grade do calendário.
    """

    def __init__(self, label_color='#000000', bg_color='#FFFFFF', bg_clean=True, **kwargs):
        """
        Inicializa a grade do calendário.

        Argumentos:
            label_color (str, opcional): Cor dos rótulos (dias da semana e números). 
                Pode ser uma cor em formato hexadecimal ou um nome de cor suportado pelo Kivy. 
                O padrão é preto (#000000).
            bg_color (str, opcional): Cor de fundo dos botões do calendário. 
                Pode ser uma cor em formato hexadecimal ou um nome de cor suportado pelo Kivy. 
                O padrão é branco (#FFFFFF).
            bg_clean (bool, opcional): Define se o fundo dos botões deve ser limpo (transparente). 
                O padrão é True.
            **kwargs: Argumentos adicionais para a classe GridLayout.
        """
        super(GraphicCalendarGrid, self).__init__(**kwargs)
        self.selected = None
        self.cols = 7
        week = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']
        for day in week:
            self.add_widget(Label(text=day, color=color(label_color)))
        self.buttons = []
        for j in range(0, 42):
            button = ToggleButton(color=color(label_color), background_color=bg_color)
            if bg_clean:
                button.background_normal = ''
            button.bind(on_release=lambda button=button: self.onclick(button))
            self.buttons.append(button)
            self.add_widget(button)
    
    def onclick(self, button):
        """
        Método chamado quando um botão do calendário é clicado.

        Argumentos:
            button (ToggleButton): O botão que foi clicado.
        """
        if button.state == 'down':
            if self.selected:
                self.selected.state = 'normal'
            self.selected = button
        else:
            self.selected = None

class GraphicCalendar(BoxLayout):
    """
    Classe que representa o calendário gráfico.

    Atributos:
        grid (GraphicCalendarGrid): Grade do calendário.
        month_label (Label): Rótulo para exibir o nome do mês.
        year_label (Label): Rótulo para exibir o ano.
        current_month (tuple): Armazena o mês e o ano atualmente exibidos no calendário.
    """

    def __init__(self, month=1, year=2023, label_color='#000000', bg_color='#FFFFFF', bt_clean=True, **kwargs):
        """
        Inicializa o calendário gráfico.

        Argumentos:
            month (int, opcional): Número do mês (1 a 12). O padrão é 1 (Janeiro).
            year (int, opcional): Ano. O padrão é 2023.
            label_color (str, opcional): Cor dos rótulos (mês e ano). 
                Pode ser uma cor em formato hexadecimal ou um nome de cor suportado pelo Kivy. 
                O padrão é preto (#000000).
            bg_color (str, opcional): Cor de fundo do calendário. 
                Pode ser uma cor em formato hexadecimal ou um nome de cor suportado pelo Kivy. 
                O padrão é branco (#FFFFFF).
            bt_clean (bool, opcional): Define se o fundo dos botões do calendário deve ser limpo (transparente). 
                O padrão é True.
            **kwargs: Argumentos adicionais para a classe BoxLayout.
        """
        super(GraphicCalendar, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.grid = GraphicCalendarGrid(label_color=label_color, bg_color=bg_color, bg_clean=bt_clean)
        self.month_label = Label(color=color(label_color))
        self.month_label.size_hint_y = .13
        self.year_label = Label(color=color(label_color))
        self.year_label.size_hint_y = .13
        self.add_widget(self.year_label)
        self.add_widget(self.month_label)
        self.add_widget(self.grid)

        with self.canvas.before:
            Color().rgba = color(bg_color)
            self.background_shape = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.set_shape, pos=self.set_shape)
        self.set_month(month, year)

    def set_month(self, month, year):
        """
        Define o mês e o ano a serem exibidos no calendário.

        Argumentos:
            month (int): Número do mês (1 a 12).
            year (int): Ano.
        """
        self.month_label.text = month_map(month)
        self.year_label.text = str(year)
        init, length = calendar.monthrange(year, month)
        init = day_map(init)
        setlist = ['']*init
        for value in range(1, length + 1):
            setlist.append(str(value))
        i = 0
        for value in setlist:
            self.grid.buttons[i].text = value
            if value:
                self.grid.buttons[i].disabled = False
            else:
                self.grid.buttons[i].disabled = True
            i += 1
        while i < 42:
            self.grid.buttons[i].text = ''
            self.grid.buttons[i].disabled = True
            i += 1
        self.current_month = (month, year)
        return self
    
    def set_shape(self, shape, value):
        """
        Define a forma (tamanho e posição) do calendário.

        Argumentos:
            shape (tuple): Tupla contendo o tamanho (width, height) do calendário.
            value: Valor associado à forma (posição, no caso) do calendário.
        """
        self.background_shape.size = shape.size
        self.background_shape.pos = shape.pos

    def current_monthrange(self):
        """
        Retorna o número de dias do mês atualmente exibido no calendário.

        Retorna:
            int: Número de dias do mês atualmente exibido.
        """
        month, year = self.current_month
        _, length = calendar.monthrange(year, month)
        return length
